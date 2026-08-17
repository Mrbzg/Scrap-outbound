#!/usr/bin/env python3
"""
CLI principal del pipeline Scrap-outbound.

Ejemplos:
  python scripts/run_lote.py --list
  python scripts/run_lote.py --lote 01
  python scripts/run_lote.py --lote 01 --force-refresh
  python scripts/run_lote.py --lote 05 --seeds-only
  python scripts/run_lote.py --all-existing
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.lib.export import export_all
from scripts.lib.http_client import HttpClient
from scripts.lib.models import Lead, LeadBook
from scripts.lib.parsers import PARSERS, load_seeds


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def list_lotes(cfg: dict) -> None:
    lotes = cfg.get("lotes") or {}
    print(f"{'ID':<4} {'Slug':<28} {'Giro':<28} {'Nicho'}")
    print("-" * 100)
    for lid, meta in sorted(lotes.items(), key=lambda x: x[0]):
        print(
            f"{lid:<4} {meta.get('slug',''):<28} {meta.get('giro',''):<28} {meta.get('nicho','')}"
        )


def run_lote(
    cfg: dict,
    lote_id: str,
    force_refresh: bool = False,
    seeds_only: bool = False,
    min_leads: int | None = None,
) -> dict:
    lotes = cfg.get("lotes") or {}
    if lote_id not in lotes:
        raise SystemExit(
            f"Lote '{lote_id}' no está en config/sources.yaml. "
            f"Disponibles: {', '.join(sorted(lotes))}"
        )

    meta = lotes[lote_id]
    slug = meta["slug"]
    giro = meta.get("giro", "")
    nicho = meta.get("nicho", "")
    ejemplo = meta.get("ejemplo", "")
    out_dir = ROOT / (cfg.get("meta", {}).get("output_dir") or "leads/por_nicho")
    cache_dir = ROOT / (cfg.get("meta", {}).get("cache_dir") or "data/cache")
    raw_dir = ROOT / (cfg.get("meta", {}).get("raw_dir") or "data/raw") / f"{lote_id}_{slug}"
    raw_dir.mkdir(parents=True, exist_ok=True)

    book = LeadBook(giro=giro, nicho=nicho)
    client = HttpClient(cache_dir=cache_dir, use_cache=not force_refresh)

    # Always include ejemplo as reference lead
    if ejemplo:
        book.add(
            Lead(
                giro=giro,
                nicho=nicho,
                empresa=f"{nicho} (ejemplo original)",
                url=ejemplo,
                tipo="Ejemplo original",
                notas="Seed del cliente",
                fuente="ejemplo_cliente",
            )
        )

    stats = {"sources": [], "errors": []}

    for source in meta.get("sources") or []:
        kind = source.get("kind")
        sid = source.get("id", kind)
        src_stats = {"id": sid, "kind": kind, "leads": 0, "urls": []}

        if kind == "seeds" or seeds_only and kind != "seeds":
            if kind != "seeds":
                continue
            seed_file = ROOT / source.get("file", "")
            leads = load_seeds(seed_file, fuente=f"seeds:{sid}")
            # stamp giro/nicho
            for lead in leads:
                lead.giro = lead.giro or giro
                lead.nicho = lead.nicho or nicho
            book.extend(leads)
            src_stats["leads"] = len(leads)
            src_stats["file"] = str(seed_file)
            stats["sources"].append(src_stats)
            print(f"  [seeds] {sid}: {len(leads)} leads from {seed_file}")
            continue

        if seeds_only:
            continue

        parser = PARSERS.get(kind)
        if not parser:
            print(f"  [skip] unknown kind={kind} id={sid}")
            continue

        for url in source.get("urls") or []:
            src_stats["urls"].append(url)
            try:
                print(f"  [fetch] {url}")
                html = client.get_text(url, force=force_refresh)
                # persist raw snapshot
                safe = (
                    url.replace("https://", "")
                    .replace("http://", "")
                    .replace("/", "_")
                    .replace("?", "_")[:120]
                )
                (raw_dir / f"{safe}.html").write_text(html, encoding="utf-8")
                leads = parser(html, fuente=f"{kind}:{sid}")
                for lead in leads:
                    lead.giro = lead.giro or giro
                    lead.nicho = lead.nicho or nicho
                book.extend(leads)
                src_stats["leads"] += len(leads)
                print(f"         -> {len(leads)} leads")
            except Exception as exc:
                msg = f"{url}: {exc}"
                stats["errors"].append(msg)
                print(f"         !! ERROR {exc}")

        stats["sources"].append(src_stats)

    # Optional: merge previously exported lote if exists (enrich mode)
    existing_json = out_dir / f"{lote_id}_{slug}.json"
    if existing_json.exists() and not seeds_only:
        try:
            prev = json.loads(existing_json.read_text(encoding="utf-8"))
            book.extend(prev)
            print(f"  [merge] existing export: {len(prev)} rows")
        except Exception as exc:
            print(f"  [merge] skip existing ({exc})")

    final = book.finalize()
    paths = export_all(final, out_dir, slug=slug, lote_id=lote_id, ejemplo=ejemplo)

    # Write run report
    report = {
        "lote_id": lote_id,
        "slug": slug,
        "giro": giro,
        "nicho": nicho,
        "total": len(final),
        "alta": sum(1 for x in final if x.prioridad == "Alta"),
        "media": sum(1 for x in final if x.prioridad == "Media"),
        "baja": sum(1 for x in final if x.prioridad == "Baja"),
        "with_email": sum(1 for x in final if x.email),
        "with_phone": sum(1 for x in final if x.telefono),
        "with_url": sum(1 for x in final if x.url),
        "sources": stats["sources"],
        "errors": stats["errors"],
        "outputs": {k: str(v) for k, v in paths.items()},
    }
    report_path = out_dir / f"{lote_id}_{slug}.run.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    target_min = min_leads or cfg.get("meta", {}).get("default_min_leads", 100)
    print()
    print(f"=== Lote {lote_id} ({slug}) ===")
    print(f"Total: {report['total']} | Alta: {report['alta']} | Media: {report['media']} | Baja: {report['baja']}")
    print(f"Email: {report['with_email']} | Tel: {report['with_phone']} | URL: {report['with_url']}")
    for k, p in paths.items():
        print(f"  {k}: {p}")
    if report["total"] < target_min:
        print(
            f"\n[!] Solo {report['total']} leads (< {target_min}). "
            f"Agrega seeds en config/seeds/{lote_id}_{slug}.json o más URLs en sources.yaml"
        )
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Scrap-outbound lead pipeline")
    parser.add_argument("--config", default=str(ROOT / "config" / "sources.yaml"))
    parser.add_argument("--list", action="store_true", help="Listar lotes configurados")
    parser.add_argument("--lote", help="ID de lote, ej. 01")
    parser.add_argument("--all-existing", action="store_true", help="Correr todos los lotes en config")
    parser.add_argument("--force-refresh", action="store_true", help="Ignorar cache HTTP")
    parser.add_argument("--seeds-only", action="store_true", help="Solo seeds manuales")
    parser.add_argument("--min-leads", type=int, default=None)
    args = parser.parse_args(argv)

    cfg_path = Path(args.config)
    if not cfg_path.is_absolute():
        cfg_path = ROOT / cfg_path
    cfg = load_config(cfg_path)

    if args.list:
        list_lotes(cfg)
        return 0

    if args.all_existing:
        codes = []
        for lid in sorted((cfg.get("lotes") or {}).keys()):
            print(f"\n######## RUN {lid} ########")
            codes.append(
                run_lote(
                    cfg,
                    lid,
                    force_refresh=args.force_refresh,
                    seeds_only=args.seeds_only,
                    min_leads=args.min_leads,
                )
            )
        print(f"\nDone: {len(codes)} lotes")
        return 0

    if not args.lote:
        parser.print_help()
        print("\nUsa --list o --lote 01")
        return 1

    run_lote(
        cfg,
        args.lote.zfill(2) if args.lote.isdigit() else args.lote,
        force_refresh=args.force_refresh,
        seeds_only=args.seeds_only,
        min_leads=args.min_leads,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
