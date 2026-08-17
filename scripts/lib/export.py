"""Export leads to CSV, JSON and Markdown."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable

from .models import Lead

FIELDS = [
    "giro",
    "nicho",
    "empresa",
    "url",
    "email",
    "telefono",
    "ciudad",
    "estado",
    "pais",
    "tipo",
    "prioridad",
    "score_contacto",
    "notas",
    "fuente",
]


def export_all(
    leads: Iterable[Lead],
    out_dir: str | Path,
    slug: str,
    lote_id: str,
    ejemplo: str = "",
) -> dict[str, Path]:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = [lead.to_dict() for lead in leads]
    prefix = f"{lote_id}_{slug}"

    csv_path = out_dir / f"{prefix}.csv"
    json_path = out_dir / f"{prefix}.json"
    md_path = out_dir / f"{prefix}.md"

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    md_path.write_text(_to_markdown(rows, lote_id, slug, ejemplo), encoding="utf-8")
    return {"csv": csv_path, "json": json_path, "md": md_path}


def _to_markdown(rows: list[dict], lote_id: str, slug: str, ejemplo: str) -> str:
    total = len(rows)
    alta = sum(1 for r in rows if r.get("prioridad") == "Alta")
    media = sum(1 for r in rows if r.get("prioridad") == "Media")
    baja = total - alta - media
    email_n = sum(1 for r in rows if r.get("email"))
    tel_n = sum(1 for r in rows if r.get("telefono"))
    url_n = sum(1 for r in rows if r.get("url"))

    giro = rows[0].get("giro", "") if rows else ""
    nicho = rows[0].get("nicho", "") if rows else ""

    lines = [
        f"# Lote {lote_id} — {giro} / {nicho}",
        "",
        f"**Slug:** `{slug}`  ",
        f"**Total leads:** {total}  ",
        f"**Alta:** {alta} · **Media:** {media} · **Baja:** {baja}  ",
        f"**Con email:** {email_n} · **Con teléfono:** {tel_n} · **Con URL:** {url_n}",
        "",
    ]
    if ejemplo:
        lines.append(f"Ejemplo original: {ejemplo}")
        lines.append("")

    lines += [
        "## Alta prioridad",
        "",
        "| Empresa | URL | Email | Tel | Ciudad | Tipo |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        if r.get("prioridad") != "Alta":
            continue
        lines.append(
            f"| {r.get('empresa','')} | {r.get('url','')} | {r.get('email','')} | "
            f"{r.get('telefono','')} | {r.get('ciudad','')} | {r.get('tipo','')} |"
        )

    lines += [
        "",
        "## Todos los leads",
        "",
        "| # | Empresa | URL | Email | Tel | Ciudad | Prioridad | Tipo |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(rows, 1):
        lines.append(
            f"| {i} | {r.get('empresa','')} | {r.get('url','')} | {r.get('email','')} | "
            f"{r.get('telefono','')} | {r.get('ciudad','')} | {r.get('prioridad','')} | {r.get('tipo','')} |"
        )
    lines.append("")
    return "\n".join(lines)
