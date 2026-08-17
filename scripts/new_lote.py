#!/usr/bin/env python3
"""
Scaffold a new lote from nichos.json / manual args.

  python scripts/new_lote.py --from-nichos 5
  python scripts/new_lote.py --id 06 --slug disfraces --giro Ropa --nicho Disfraces --ejemplo https://mykidsmx.com/
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def slugify(text: str) -> str:
    text = text.lower().strip()
    repl = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ñ": "n",
        "ü": "u",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")[:40]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--from-nichos", type=int, help="1-based index in leads/nichos.json")
    parser.add_argument("--id", help="Lote id e.g. 06")
    parser.add_argument("--slug")
    parser.add_argument("--giro")
    parser.add_argument("--nicho")
    parser.add_argument("--ejemplo", default="")
    parser.add_argument("--dirind-url", action="append", default=[], help="Optional Dirind category URL")
    args = parser.parse_args()

    if args.from_nichos:
        nichos = json.loads((ROOT / "leads" / "nichos.json").read_text(encoding="utf-8"))
        idx = args.from_nichos - 1
        if idx < 0 or idx >= len(nichos):
            raise SystemExit(f"Index fuera de rango 1..{len(nichos)}")
        item = nichos[idx]
        lote_id = args.id or f"{args.from_nichos:02d}"
        giro = item["giro"]
        nicho = item["nicho"]
        ejemplo = item.get("ejemplo", "")
        slug = args.slug or slugify(nicho)
    else:
        if not all([args.id, args.slug or args.nicho, args.giro, args.nicho]):
            parser.error("Proporciona --from-nichos N  o  --id/--giro/--nicho")
        lote_id = args.id.zfill(2) if args.id.isdigit() else args.id
        giro = args.giro
        nicho = args.nicho
        ejemplo = args.ejemplo
        slug = args.slug or slugify(nicho)

    cfg_path = ROOT / "config" / "sources.yaml"
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    lotes = cfg.setdefault("lotes", {})
    if lote_id in lotes:
        print(f"[!] Lote {lote_id} ya existe en sources.yaml — no se sobrescribe config")
    else:
        sources = []
        if args.dirind_url:
            sources.append(
                {
                    "id": f"dirind_{slug}",
                    "kind": "dirind",
                    "urls": args.dirind_url,
                }
            )
        sources.append(
            {
                "id": "seed_manual",
                "kind": "seeds",
                "file": f"config/seeds/{lote_id}_{slug}.json",
            }
        )
        lotes[lote_id] = {
            "slug": slug,
            "giro": giro,
            "nicho": nicho,
            "ejemplo": ejemplo,
            "sources": sources,
            "search_queries": [
                f"{nicho} México tienda online .mx",
                f"{nicho} mayoreo México",
                f"{nicho} distribuidor México",
            ],
        }
        cfg_path.write_text(
            yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
        print(f"Added lote {lote_id} to config/sources.yaml")

    seed_path = ROOT / "config" / "seeds" / f"{lote_id}_{slug}.json"
    if not seed_path.exists():
        seed = {
            "lote": lote_id,
            "slug": slug,
            "description": f"Semillas para {giro} / {nicho}",
            "leads": [],
        }
        if ejemplo:
            seed["leads"].append(
                {
                    "empresa": f"{nicho} (ejemplo)",
                    "url": ejemplo,
                    "tipo": "Ejemplo original",
                    "fuente": "ejemplo_cliente",
                }
            )
        seed_path.write_text(json.dumps(seed, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Created {seed_path}")
    else:
        print(f"Seed already exists: {seed_path}")

    print(
        f"\nNext:\n  1) Edita seeds: {seed_path}\n"
        f"  2) Agrega URLs Dirind/QuimiNet en config/sources.yaml si aplica\n"
        f"  3) python scripts/run_lote.py --lote {lote_id}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
