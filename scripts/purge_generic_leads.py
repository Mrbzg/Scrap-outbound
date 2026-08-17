#!/usr/bin/env python3
"""Purge generic/filler leads from seeds and exports.

Drops leads that are NOT real companies:
  1. tipo == "Regional"                 (city-padding used by gen_lotes_*)
  2. empresa endswith " extra"          (research annotations / dup rows)
  3. no url/email/tel AND empresa ends with a known MX city  ("Prefix + City")
  4. no url/email/tel AND tipo in segment types (Canal B2B, Cluster, Temporada,
     Adyacente, Uso, SKU, Canal digital, Independiente, Sellers, Import, Canal)

Keeps everything else (real companies/brands with or without contact).

Usage:
  python scripts/purge_generic_leads.py            # dry-run
  python scripts/purge_generic_leads.py --apply    # rewrite files
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Same city lists used by gen_lotes_27_28 / 29_32 / 33_36 (names only).
CITIES = [
    "Aguascalientes", "Tijuana", "Mexicali", "La Paz", "Campeche", "Tuxtla Gutiérrez",
    "Chihuahua", "Cd. Juárez", "Juárez", "Juarez", "Saltillo", "Torreón", "Torreon",
    "Colima", "Durango", "León", "Leon", "Irapuato", "Acapulco", "Pachuca", "Toluca",
    "Cuernavaca", "Tepic", "Monterrey", "Oaxaca", "Puebla", "Querétaro", "Queretaro",
    "Cancún", "Cancun", "San Luis Potosí", "San Luis Potosi", "Culiacán", "Culiacan",
    "Hermosillo", "Villahermosa", "Tampico", "Tlaxcala", "Xalapa", "Veracruz",
    "Zacatecas", "Mérida", "Merida", "Guadalajara", "Zapopan", "Celaya", "Salamanca",
    "San Juan del Río", "Cuautla", "Jiutepec", "Córdoba", "Cordoba", "Orizaba",
    "Poza Rica", "Coatzacoalcos", "Tapachula", "Comitán", "Los Mochis",
    "Ciudad Obregón", "Nogales", "Ensenada", "Playa del Carmen", "Chetumal",
    "Reynosa", "Matamoros", "Nuevo Laredo", "Gómez Palacio", "Fresnillo", "Uruapan",
    "Zamora", "Morelia", "Tehuacán", "Apizaco", "Tulancingo", "Ixtapa", "Naucalpan",
    "Ecatepec", "Nezahualcóyotl", "Tlalnepantla", "Cuautitlán Izcalli",
    "Puerto Vallarta", "Mazatlán", "Los Cabos", "San Miguel de Allende",
    "Chilpancingo", "Minatitlán", "Ciudad Victoria", "Piedras Negras", "Monclova",
    "Ocotlán", "Xalostoc", "Nextlalpan", "Cholula", "Mineral de la Reforma",
    "Cuautitlán", "Empalme", "Santa Ana Nextlalpan",
]

SEGMENT_TIPOS = {
    "Canal B2B", "Cluster", "Temporada", "Adyacente", "Uso", "SKU",
    "Canal digital", "Independiente", "Sellers", "Import", "Canal",
    "Hub", "Grupo",
}


def has_contact(lead: dict) -> bool:
    return bool(lead.get("url") or lead.get("email") or lead.get("telefono"))


def is_generic(lead: dict) -> tuple[bool, str]:
    tipo = (lead.get("tipo") or "").strip()
    empresa = (lead.get("empresa") or "").strip()

    if tipo == "Regional":
        return True, "tipo Regional"
    if empresa.endswith(" extra"):
        return True, "sufijo 'extra'"
    if not has_contact(lead):
        for c in sorted(CITIES, key=len, reverse=True):
            if empresa.endswith(" " + c):
                return True, f"genérico '{c}'"
        if tipo in SEGMENT_TIPOS:
            return True, f"segmento {tipo}"
    return False, ""


def purge_leads(leads: list[dict]) -> tuple[list[dict], list[str]]:
    kept, dropped = [], []
    for lead in leads:
        is_gen, why = is_generic(lead)
        if is_gen:
            dropped.append(f"{lead.get('empresa','?')}  [{why}]")
        else:
            kept.append(lead)
    return kept, dropped


def purge_file(path: Path, apply: bool) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and "leads" in data:
        leads, dropped = purge_leads(data["leads"])
        if dropped and apply:
            data["leads"] = leads
            path.write_text(
                json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        print(f"  {path.name}: {len(leads)} kept / {len(dropped)} dropped")
        for d in dropped[:6]:
            print(f"      - {d}")
        if len(dropped) > 6:
            print(f"      ... y {len(dropped)-6} más")
    elif isinstance(data, list):
        leads, dropped = purge_leads(data)
        if dropped and apply:
            path.write_text(
                json.dumps(leads, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        print(f"  {path.name}: {len(leads)} kept / {len(dropped)} dropped")
        for d in dropped[:6]:
            print(f"      - {d}")
        if len(dropped) > 6:
            print(f"      ... y {len(dropped)-6} más")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Rewrite files (default: dry-run)")
    args = ap.parse_args()

    print("== Seeds ==")
    for f in sorted((ROOT / "config" / "seeds").glob("*_*.json")):
        if "_TEMPLATE" in f.name:
            continue
        purge_file(f, args.apply)

    print("\n== Exports (leads/por_nicho) ==")
    for f in sorted((ROOT / "leads" / "por_nicho").glob("*.json")):
        if f.name.endswith(".run.json"):
            continue
        purge_file(f, args.apply)

    print("\n(dry-run: sin --apply no se modifica nada)" if not args.apply else "\nAplicado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
