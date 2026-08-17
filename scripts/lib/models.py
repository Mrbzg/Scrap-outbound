"""Lead model, scoring and dedupe helpers."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import Any, Iterable


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_key(name: str) -> str:
    name = clean_text(name).lower()
    name = re.sub(r"[^a-z0-9áéíóúüñ]", "", name)
    return name[:60]


def normalize_url(url: str) -> str:
    url = clean_text(url)
    if not url:
        return ""
    if url.startswith("//"):
        url = "https:" + url
    if url and not url.startswith("http"):
        url = "https://" + url.lstrip("/")
    return url


def normalize_phone(phone: str) -> str:
    phone = clean_text(phone)
    phone = re.sub(r"[^\d+\-() ]", "", phone)
    return phone.strip()


@dataclass
class Lead:
    giro: str = ""
    nicho: str = ""
    empresa: str = ""
    url: str = ""
    email: str = ""
    telefono: str = ""
    ciudad: str = ""
    estado: str = ""
    pais: str = "México"
    tipo: str = ""
    notas: str = ""
    fuente: str = ""
    prioridad: str = ""
    score_contacto: int = 0
    extra: dict = field(default_factory=dict)

    def key(self) -> str:
        return normalize_key(self.empresa)

    def merge(self, other: "Lead") -> None:
        for attr in (
            "url",
            "email",
            "telefono",
            "ciudad",
            "estado",
            "tipo",
            "giro",
            "nicho",
        ):
            cur = getattr(self, attr)
            new = getattr(other, attr)
            if new and not cur:
                setattr(self, attr, new)
        if other.notas:
            if not self.notas:
                self.notas = other.notas
            elif other.notas not in self.notas:
                self.notas = f"{self.notas}; {other.notas}"[:400]
        if other.fuente and other.fuente not in self.fuente:
            self.fuente = f"{self.fuente}|{other.fuente}".strip("|")

    def score(self) -> int:
        score = 0
        if self.url:
            score += 2
        if self.email:
            score += 3
        if self.telefono:
            score += 2
        if self.ciudad and self.ciudad not in ("México", "Norte", ""):
            score += 1
        tipo = (self.tipo or "").lower()
        if any(
            x in tipo
            for x in (
                "d2c",
                "ecom",
                "mayoreo",
                "fabricante",
                "productor",
                "b2b",
                "tienda tcg",
                "marca",
                "distribuidor",
            )
        ):
            score += 1
        el = (self.empresa or "").lower()
        # Generic seeds / clusters get lower priority
        if any(
            x in el
            for x in (
                " multi",
                "hub ",
                "grupo facebook",
                "organizador torneos",
                "independiente",
                "cluster",
                "sellers ",
                " shop b",
            )
        ):
            score = max(0, score - 1)
        self.score_contacto = score
        if score >= 5:
            self.prioridad = "Alta"
        elif score >= 2:
            self.prioridad = "Media"
        else:
            self.prioridad = "Baja"
        return score

    def to_dict(self) -> dict:
        d = asdict(self)
        d.pop("extra", None)
        return d

    @classmethod
    def from_dict(cls, data: dict) -> "Lead":
        known = {f.name for f in cls.__dataclass_fields__.values()}  # type: ignore
        payload = {k: clean_text(v) if k != "score_contacto" else v for k, v in data.items() if k in known}
        if "score_contacto" in payload:
            try:
                payload["score_contacto"] = int(payload["score_contacto"] or 0)
            except Exception:
                payload["score_contacto"] = 0
        lead = cls(**payload)
        lead.url = normalize_url(lead.url)
        lead.telefono = normalize_phone(lead.telefono)
        lead.email = clean_text(lead.email).lower()
        return lead


class LeadBook:
    def __init__(self, giro: str = "", nicho: str = ""):
        self.giro = giro
        self.nicho = nicho
        self._items: dict[str, Lead] = {}

    def add(self, lead: Lead | dict) -> None:
        if isinstance(lead, dict):
            lead = Lead.from_dict(lead)
        lead.empresa = clean_text(lead.empresa)
        if not lead.empresa or len(lead.empresa) < 3:
            return
        if not lead.giro:
            lead.giro = self.giro
        if not lead.nicho:
            lead.nicho = self.nicho
        if not lead.pais:
            lead.pais = "México"
        key = lead.key()
        if not key:
            return
        if key in self._items:
            self._items[key].merge(lead)
        else:
            self._items[key] = lead

    def extend(self, leads: Iterable[Lead | dict]) -> None:
        for lead in leads:
            self.add(lead)

    def finalize(self) -> list[Lead]:
        rows = list(self._items.values())
        for lead in rows:
            lead.score()
        order = {"Alta": 0, "Media": 1, "Baja": 2}
        rows.sort(key=lambda x: (order.get(x.prioridad, 9), x.empresa.lower()))
        return rows

    def __len__(self) -> int:
        return len(self._items)
