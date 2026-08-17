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
| 13 | Juguetes sensoriales / TEA | `13_juguetes_sensoriales.*` |
| 14 | Miniaturas / modelismo escala | `14_articulos_miniatura.*` |
| 15 | Insumos para tatuar | `15_insumos_para_tatuar.*` |
| 16 | Invitaciones físicas | `16_invitaciones_fisicas.*` |
| 17 | Miel afrodisíaca / Royal Honey | `17_miel_afrodisiaca.*` |
| 18 | Tijeras con patrón al corte | `18_tijeras_patron_al_corte.*` |
| 19 | Charms / dijes plata 925 | `19_charms.*` |
| 20 | Pupilentes de color | `20_pupilentes.*` |
| 21 | Insumos para uñas / press on | `21_insumos_unas_press_on.*` |
| 22 | Tarot, lociones y velas esotéricas | `22_tarot_velas_esotericas.*` |
| 23 | Shampoo artesanal / con tinte | `23_shampoo_artesanal_tinte.*` |
| 24 | Hilos y estambre | `24_hilos_y_estambre.*` |
| 25 | Bolsas de regalo | `25_bolsas_de_regalo.*` |
| 26 | Tenis, botas y playeras | `26_tenis_botas_playeras.*` |
| 27 | Skincare / cosméticos | `27_skincare_cosmeticos.*` |
| 28 | Esmaltes, pegamentos y piedritas | `28_productos_unas_esmaltes.*` |
| 29 | Utensilios de cocina, tuppers | `29_utensilios_cocina_tuppers.*` |
| 30 | Audífonos bluetooth, cargadores, fundas | `30_audifonos_bluetooth_cargadores.*` |
| 31 | Fundas personalizadas y soporte para celular | `31_fundas_personalizadas_celular.*` |
| 32 | Aromatizantes para autos | `32_aromatizantes_para_autos.*` |
| 33 | Mochilas y útiles escolares | `33_mochilas_utiles_escolares.*` |
| 34 | Skincare y maquillaje | `34_skincare_maquillaje.*` |
| 35 | Refacciones automotrices | `35_refacciones_automotrices.*` |
| 36 | Vitaminas para plantas y abono | `36_vitaminas_plantas_abono.*` |
| 37 | Gomitas de vitaminas | `37_gomitas_vitaminas.*` |
| 38 | Libros de colección | `38_libros_coleccion.*` |
| 39 | Artículos de limpieza | `39_articulos_limpieza.*` |
| 40 | Perfumes | `40_perfumes.*` |
| 41 | Scoops / sorpresas | `41_scoops_sorpresas.*` |
| 42 | Artículos para adultos | `42_articulos_para_adultos.*` |
| 43 | Vitaminas y suplementos | `43_vitaminas_suplementos.*` |
| 44 | Productos para el cabello (keratina, cremas, ampolletas) | `44_productos_cabello_keratina.*` |
| 45 | Extensiones de pelo para salón | `45_extensiones_de_pelo.*` |
| 46 | Cortinas | `46_cortinas.*` |
| 47 | Juguetes sensoriales mayoreo | `47_juguetes_sensoriales_mayoreo.*` |
| 48 | Botellas y tapas personalizados | `48_botellas_tapas_personalizados.*` |
| 49 | Accesorios para autos (luces y refacciones pequeñas) | `49_accesorios_para_autos.*` |
| 50 | Pelucas de colores | `50_pelucas_de_colores.*` |

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
