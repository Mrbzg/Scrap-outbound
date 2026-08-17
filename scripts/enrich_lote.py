#!/usr/bin/env python3
"""
Re-score and re-export an existing lote JSON without re-fetching web sources.

  python scripts/enrich_lote.py --lote 01
  python scripts/enrich_lote.py --input leads/por_nicho/01_cafe_granos.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.lib.export import export_all
from scripts.lib.models import Lead, LeadBook


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lote", help="ID lote, ej. 01")
    parser.add_argument("--input", help="Path a JSON de leads")
    parser.add_argument("--slug", help="Slug override")
    parser.add_argument("--out-dir", default=str(ROOT / "leads" / "por_nicho"))
    args = parser.parse_args()

    if args.input:
        path = Path(args.input)
        if not path.is_absolute():
            path = ROOT / path
        lote_id = args.lote or path.name.split("_")[0]
        slug = args.slug or "_".join(path.stem.split("_")[1:])
    elif args.lote:
        lote_id = args.lote.zfill(2) if args.lote.isdigit() else args.lote
        matches = list(Path(args.out_dir).glob(f"{lote_id}_*.json"))
        matches = [m for m in matches if not m.name.endswith(".run.json")]
        if not matches:
            raise SystemExit(f"No encontré JSON para lote {lote_id} en {args.out_dir}")
        path = matches[0]
        slug = args.slug or "_".join(path.stem.split("_")[1:])
    else:
        parser.error("Usa --lote o --input")

    rows = json.loads(path.read_text(encoding="utf-8"))
    book = LeadBook()
    book.extend(rows)
    final = book.finalize()
    giro = final[0].giro if final else ""
    nicho = final[0].nicho if final else ""
    paths = export_all(final, args.out_dir, slug=slug, lote_id=lote_id)
    print(f"Re-scored {len(final)} leads ({giro} / {nicho})")
    for k, p in paths.items():
        print(f"  {k}: {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
