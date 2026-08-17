"""Source-specific HTML parsers."""

from __future__ import annotations

import re
from html import unescape
from typing import Iterable
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .models import Lead, clean_text, normalize_phone, normalize_url

EMAIL_RE = re.compile(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", re.I)
PHONE_RE = re.compile(
    r"(?:\+52\s*)?(?:\(?\d{2,3}\)?[\s\-]*)?\d{3,4}[\s\-]?\d{4}"
)
URL_RE = re.compile(
    r"(?:https?://|www\.)[^\s<>\"']+",
    re.I,
)


def _extract_emails(text: str) -> list[str]:
    emails = EMAIL_RE.findall(text or "")
    out = []
    for e in emails:
        e = e.lower().strip(".,);")
        if any(x in e for x in ("dirind.com", "example.com", "sentry", "wixpress")):
            continue
        out.append(e)
    return list(dict.fromkeys(out))


def _extract_phones(text: str) -> list[str]:
    phones = [normalize_phone(p) for p in PHONE_RE.findall(text or "")]
    return [p for p in phones if len(re.sub(r"\D", "", p)) >= 8]


def _extract_urls(text: str, base: str = "") -> list[str]:
    found = []
    for m in URL_RE.findall(text or ""):
        u = m.rstrip(".,);")
        if any(x in u.lower() for x in ("dirind.com", "facebook.com/sharer", "google.com/maps")):
            continue
        if u.startswith("www."):
            u = "https://" + u
        if base and u.startswith("/"):
            u = urljoin(base, u)
        found.append(normalize_url(u))
    return list(dict.fromkeys([u for u in found if u]))


def parse_dirind(html: str, fuente: str = "dirind") -> list[Lead]:
    """
    Parse Dirind category pages.
    Structure: company blocks separated by ALTA: YYYY-MM-DD
    """
    # Work on a simplified text-ish version but keep mailto/href via soup first
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Prefer splitting raw HTML by ALTA markers (stable on Dirind)
    raw = str(soup)
    blocks = re.split(r"ALTA:\s*\d{4}-\d{2}-\d{2}", raw, flags=re.I)
    leads: list[Lead] = []

    for block in blocks:
        text = clean_text(BeautifulSoup(block, "lxml").get_text(" ", strip=True))
        if len(text) < 40:
            continue

        # Company name: first long ALL-CAPS-ish token sequence
        name = ""
        # From HTML headings / strong early strings
        bsoup = BeautifulSoup(block, "lxml")
        candidates = []
        for el in bsoup.find_all(["b", "strong", "h1", "h2", "h3", "h4"]):
            t = clean_text(el.get_text(" ", strip=True))
            if 4 <= len(t) <= 90:
                candidates.append(t)
        # Also lines that look like company titles
        for part in re.split(r"[\n\r]+", bsoup.get_text("\n", strip=True)):
            p = clean_text(part)
            if not p:
                continue
            if re.match(r"^[A-ZÁÉÍÓÚÑ0-9][A-ZÁÉÍÓÚÑ0-9\s\.,&'/\-]{4,80}$", p):
                if not p.startswith("COL ") and "ACTUALIZ" not in p and "FILTRAR" not in p:
                    candidates.append(p)
        for c in candidates:
            if any(x in c.upper() for x in ("COTIZAR", "CONSULTAR", "FILTRAR", "HOME", "ÍNDICE", "INDICE")):
                continue
            name = c
            break
        if not name:
            # fallback: first 5-60 chars before Tel/email
            m = re.search(r"^(.{5,70}?)(?:Tel|email|WhatsApp|web)", text, re.I)
            if m:
                name = clean_text(m.group(1))
        if not name or len(name) < 4:
            continue

        emails = _extract_emails(block + " " + text)
        # Prefer mailto
        for a in bsoup.select('a[href^="mailto:"]'):
            href = a.get("href", "")
            em = href.replace("mailto:", "").split("?")[0].strip()
            if em:
                emails.insert(0, em.lower())
        emails = list(dict.fromkeys(emails))

        urls = []
        for a in bsoup.select("a[href]"):
            href = a.get("href", "")
            label = clean_text(a.get_text(" ", strip=True)).lower()
            if "dirind.com" in href:
                # Dirind cloaked links — use anchor text if it looks like a domain
                if re.search(r"\.(com\.mx|mx|com|coffee|cafe)\b", label):
                    urls.append(normalize_url(label))
                continue
            if href.startswith("mailto:"):
                continue
            if href.startswith("http") or href.startswith("www"):
                urls.append(normalize_url(href))
        # Visible "web:" patterns
        for m in re.finditer(r"web(?:\s*\d*)?:\s*([^\s<]+)", text, re.I):
            urls.append(normalize_url(m.group(1)))
        urls = [u for u in urls if u and "dirind.com" not in u]
        urls = list(dict.fromkeys(urls))

        phones = []
        for m in re.finditer(r"(?:Tel(?:éfono|\.\s*celular|\.)?|WhatsApp|LADA[^:]*)\s*:\s*([^|]+?)(?=email|web|Tel|WhatsApp|ALTA|$)", text, re.I):
            phones.extend(_extract_phones(m.group(1)))
        if not phones:
            phones = _extract_phones(text)

        ciudad, estado = "", ""
        cm = re.search(
            r"(\d{5})\s+([A-Za-zÁÉÍÓÚáéíóúñÑ\.\s]+?),\s*([A-Za-zÁÉÍÓÚáéíóúñÑ\.\s]{2,40})",
            text,
        )
        if cm:
            ciudad = clean_text(cm.group(2))
            estado = clean_text(cm.group(3))[:40]

        notes = text[:180]
        leads.append(
            Lead(
                empresa=name,
                url=urls[0] if urls else "",
                email=emails[0] if emails else "",
                telefono=phones[0] if phones else "",
                ciudad=ciudad,
                estado=estado,
                tipo="Directorio industrial",
                notas=notes,
                fuente=fuente,
            )
        )
    return leads


def parse_quiminet(html: str, fuente: str = "quiminet") -> list[Lead]:
    """Parse QuimiNet supplier listing pages (best-effort)."""
    soup = BeautifulSoup(html, "lxml")
    leads: list[Lead] = []

    # Company cards often contain logo alt / headings and nearby phone
    text = soup.get_text("\n", strip=True)
    # Split around "Logo de la empresa" or repeated phone patterns
    chunks = re.split(r"Logo de la empresa\s*", text)
    if len(chunks) < 2:
        chunks = re.split(r"\n(?=[A-ZÁÉÍÓÚÑ][^\n]{4,80}\n)", text)

    for chunk in chunks:
        chunk = clean_text(chunk)
        if len(chunk) < 30:
            continue
        # First sentence-like company name
        name_m = re.match(r"([A-ZÁÉÍÓÚÑa-záéíóúñ0-9][^\n\.]{3,80})", chunk)
        if not name_m:
            continue
        name = clean_text(name_m.group(1))
        # Trim trailing descriptors
        name = re.split(r":|Vendemos|Ofrecemos|Somos|Nos dedicamos", name)[0].strip()
        if len(name) < 4 or name.lower().startswith("actualizado"):
            continue
        emails = _extract_emails(chunk)
        phones = _extract_phones(chunk)
        urls = _extract_urls(chunk)
        # Location heuristics
        ciudad = ""
        for c in (
            "CDMX",
            "Guadalajara",
            "Monterrey",
            "León",
            "Puebla",
            "Zapopan",
            "Tlalnepantla",
            "Metepec",
            "Querétaro",
            "Ecatepec",
        ):
            if c.lower() in chunk.lower():
                ciudad = c
                break
        leads.append(
            Lead(
                empresa=name[:90],
                url=urls[0] if urls else "",
                email=emails[0] if emails else "",
                telefono=phones[0] if phones else "",
                ciudad=ciudad,
                tipo="Proveedor B2B",
                notas=chunk[:160],
                fuente=fuente,
            )
        )
    return leads


def parse_digimon_stores(html: str, fuente: str = "digimon_stores") -> list[Lead]:
    """Parse official Digimon MX store list."""
    soup = BeautifulSoup(html, "lxml")
    leads: list[Lead] = []
    text = soup.get_text("\n", strip=True)

    # Pattern: **Store Name** then ADDRESS: ...
    parts = re.split(r"\n\s*[-•]?\s*", text)
    current_name = ""
    current_addr = ""
    for part in parts:
        part = clean_text(part)
        if not part:
            continue
        if part.startswith("ADDRESS") or part.lower().startswith("address"):
            current_addr = clean_text(re.sub(r"(?i)address\s*:\s*", "", part))
            if current_name:
                ciudad, estado = _guess_mx_city_state(current_addr)
                leads.append(
                    Lead(
                        empresa=current_name,
                        ciudad=ciudad,
                        estado=estado,
                        tipo="Tienda TCG autorizada",
                        notas=current_addr[:200],
                        fuente=fuente,
                    )
                )
                current_name, current_addr = "", ""
            continue
        # Likely store name lines
        if 3 <= len(part) <= 80 and not part.lower().startswith("mexico") and "list of" not in part.lower():
            # Avoid pure addresses
            if not re.search(r"\d{4,}", part) and "col." not in part.lower():
                current_name = part.strip("*- ")

    # Secondary: strong/bold tags
    for el in soup.find_all(["strong", "b", "h3", "h4"]):
        name = clean_text(el.get_text(" ", strip=True))
        if 3 <= len(name) <= 80:
            # look at next siblings for address
            nxt = clean_text(el.parent.get_text(" ", strip=True) if el.parent else "")
            ciudad, estado = _guess_mx_city_state(nxt)
            leads.append(
                Lead(
                    empresa=name,
                    ciudad=ciudad,
                    estado=estado,
                    tipo="Tienda TCG autorizada",
                    notas=nxt[:180],
                    fuente=fuente,
                )
            )
    return leads


def parse_generic_companies(html: str, fuente: str = "generic") -> list[Lead]:
    """
    Best-effort generic extractor: names near phones/emails/domains.
    Useful for trade-show pages and simple directories.
    """
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    leads: list[Lead] = []

    # 1) Explicit external websites with nearby text
    for a in soup.select("a[href]"):
        href = a.get("href", "")
        if not href.startswith("http"):
            continue
        if any(
            x in href
            for x in (
                "facebook.com",
                "instagram.com",
                "twitter.com",
                "linkedin.com",
                "youtube.com",
                "wa.me",
                "google.com",
                "schema.org",
            )
        ):
            # keep wa.me as phone later
            if "wa.me" in href:
                phone = re.sub(r"\D", "", href.split("wa.me/")[-1])
                parent_text = clean_text(a.parent.get_text(" ", strip=True) if a.parent else "")
                name = clean_text(a.get_text(" ", strip=True)) or parent_text[:60]
                if name and phone:
                    leads.append(
                        Lead(
                            empresa=name[:80],
                            telefono=phone,
                            tipo="Listado web",
                            fuente=fuente,
                            notas=parent_text[:160],
                        )
                    )
            continue
        name = clean_text(a.get_text(" ", strip=True))
        parent_text = clean_text(a.parent.get_text(" ", strip=True) if a.parent else "")
        if not name or len(name) < 3:
            # domain as name fallback
            name = re.sub(r"^https?://(www\.)?", "", href).split("/")[0]
        emails = _extract_emails(parent_text)
        phones = _extract_phones(parent_text)
        leads.append(
            Lead(
                empresa=name[:90],
                url=normalize_url(href),
                email=emails[0] if emails else "",
                telefono=phones[0] if phones else "",
                tipo="Listado web",
                notas=parent_text[:160],
                fuente=fuente,
            )
        )

    # 2) Headings as company names
    for h in soup.find_all(["h2", "h3", "h4"]):
        name = clean_text(h.get_text(" ", strip=True))
        if not (4 <= len(name) <= 80):
            continue
        block = clean_text(h.parent.get_text(" ", strip=True) if h.parent else name)
        emails = _extract_emails(block)
        phones = _extract_phones(block)
        urls = _extract_urls(block)
        if emails or phones or urls:
            leads.append(
                Lead(
                    empresa=name,
                    url=urls[0] if urls else "",
                    email=emails[0] if emails else "",
                    telefono=phones[0] if phones else "",
                    tipo="Listado web",
                    notas=block[:160],
                    fuente=fuente,
                )
            )
    return leads


def load_seeds(path: str, fuente: str = "seeds") -> list[Lead]:
    """Load manual seed JSON list of lead dicts."""
    import json
    from pathlib import Path

    p = Path(path)
    if not p.exists():
        return []
    data = json.loads(p.read_text(encoding="utf-8"))
    if isinstance(data, dict) and "leads" in data:
        data = data["leads"]
    leads = []
    for item in data:
        lead = Lead.from_dict(item)
        if not lead.fuente:
            lead.fuente = fuente
        leads.append(lead)
    return leads


def _guess_mx_city_state(text: str) -> tuple[str, str]:
    text_l = (text or "").lower()
    mapping = [
        ("monterrey", "Monterrey", "Nuevo León"),
        ("san pedro", "San Pedro Garza García", "Nuevo León"),
        ("guadalajara", "Guadalajara", "Jalisco"),
        ("zapopan", "Zapopan", "Jalisco"),
        ("cdmx", "CDMX", "CDMX"),
        ("ciudad de méxico", "CDMX", "CDMX"),
        ("ciudad de mexico", "CDMX", "CDMX"),
        ("cuauhtémoc", "CDMX", "CDMX"),
        ("tijuana", "Tijuana", "Baja California"),
        ("méxico", "CDMX", "CDMX"),
        ("merida", "Mérida", "Yucatán"),
        ("mérida", "Mérida", "Yucatán"),
        ("puebla", "Puebla", "Puebla"),
        ("querétaro", "Querétaro", "Querétaro"),
        ("queretaro", "Querétaro", "Querétaro"),
        ("león", "León", "Guanajuato"),
        ("leon", "León", "Guanajuato"),
        ("celaya", "Celaya", "Guanajuato"),
        ("acapulco", "Acapulco", "Guerrero"),
        ("coatzacoalcos", "Coatzacoalcos", "Veracruz"),
        ("juárez", "Cd. Juárez", "Chihuahua"),
        ("juarez", "Cd. Juárez", "Chihuahua"),
        ("torreón", "Torreón", "Coahuila"),
        ("hermosillo", "Hermosillo", "Sonora"),
        ("cancún", "Cancún", "Quintana Roo"),
        ("cancun", "Cancún", "Quintana Roo"),
    ]
    for needle, city, state in mapping:
        if needle in text_l:
            return city, state
    return "", ""


PARSERS = {
    "dirind": parse_dirind,
    "quiminet": parse_quiminet,
    "digimon_stores": parse_digimon_stores,
    "generic_list": parse_generic_companies,
    "generic": parse_generic_companies,
}
