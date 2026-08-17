# Scrap-outbound

Pipeline reproducible de prospección de **leads outbound por giro/nicho (México)**.

Busca empresas similares a tus ejemplos (ecom, mayoreo, fabricantes), las unifica, scorea por calidad de contacto y exporta CSV / JSON / Markdown.

---

## Estructura

```text
Scrap-outbound/
├── config/
│   ├── sources.yaml          # lotes, URLs de directorios, queries
│   └── seeds/                # semillas manuales curadas por lote
├── scripts/
│   ├── run_lote.py           # CLI principal (fetch + parse + export)
│   ├── enrich_lote.py        # re-score/export sin re-fetch
│   ├── new_lote.py           # scaffold de un lote nuevo
│   └── lib/
│       ├── http_client.py    # HTTP + cache + retries (+ curl fallback)
│       ├── models.py         # Lead, dedupe, scoring
│       ├── parsers.py        # Dirind, QuimiNet, Digimon, generic
│       └── export.py         # CSV / JSON / MD
├── data/
│   ├── cache/                # HTML cache (gitignored)
│   └── raw/                  # snapshots por corrida (gitignored)
├── leads/
│   ├── nichos.json           # catálogo de 58 giros/nichos/ejemplos
│   ├── LEADS_REPORTE.md      # resumen multi-nicho inicial
│   ├── leads_por_nicho.*     # base inicial cruzada
│   └── por_nicho/            # salidas por lote (01, 02, ...)
├── requirements.txt
└── README.md
```

---

## Setup

```bash
cd Scrap-outbound
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Uso rápido

```bash
python scripts/run_lote.py --list
python scripts/run_lote.py --lote 01
python scripts/run_lote.py --lote 01 --seeds-only
python scripts/run_lote.py --lote 01 --force-refresh
python scripts/enrich_lote.py --lote 01
python scripts/new_lote.py --from-nichos 5
```

Salidas:

```text
leads/por_nicho/{ID}_{slug}.csv|.json|.md
```

---

## Lotes actuales

| Lote | Nicho | Archivos |
|---|---|---|
| 01 | Café / granos de café | `01_cafe_granos.*` |
| 02 | Colágeno hidrolizado | `02_colageno_hidrolizado.*` |
| 03 | Frutos secos | `03_frutos_secos.*` |
| 04 | Cartas coleccionables / TCG | `04_cartas_coleccionables.*` |
| 05 | Botanas y snacks mexicanos | `05_botanas_snacks.*` |
| 06 | Maquillaje artístico / FX | `06_maquillaje_artistico.*` |
| 07 | Disfraces | `07_disfraces.*` |
| 08 | Cestas de regalo / arcones | `08_cestas_de_regalo.*` |
| 09 | Almohadas y cobijas | `09_almohadas_cobijas.*` |
| 10 | Cargadores / porta laptop | `10_cargadores_porta_laptop.*` |
| 11 | Trajes típicos | `11_trajes_tipicos.*` |
| 12 | Zapatos para danza | `12_zapatos_para_danza.*` |

Catálogo: `leads/nichos.json` (58 nichos).

---

## Fuentes

| Fuente | Parser `kind` |
|---|---|
| Dirind | `dirind` |
| QuimiNet | `quiminet` |
| Digimon stores MX | `digimon_stores` |
| Páginas genéricas / expo | `generic_list` |
| Seeds JSON | `seeds` |

Config: `config/sources.yaml`

---

## Scoring

URL +2 · Email +3 · Tel +2 · Ciudad +1 · Tipo relevante +1 · Nombre genérico −1  
**Alta** ≥5 · **Media** ≥2 · **Baja** resto

---

## Nuevo nicho

```bash
python scripts/new_lote.py --from-nichos 6
# editar config/seeds/0N_*.json y sources.yaml
python scripts/run_lote.py --lote 0N
```

## Campos

```text
giro, nicho, empresa, url, email, telefono, ciudad, estado, pais,
tipo, prioridad, score_contacto, notas, fuente
```
