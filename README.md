# Scrap-outbound

Prospección de leads outbound por giro/nicho (México).

## Archivos

| Archivo | Descripción |
|---|---|
| `leads/LEADS_REPORTE.md` | Reporte legible con tablas por nicho |
| `leads/leads_por_nicho.csv` | CSV listo para importar a CRM / Sheets |
| `leads/leads_por_nicho.json` | JSON estructurado |
| `leads/nichos.json` | Catálogo de giros/nichos/ejemplos del cliente |

## Resumen

- **149** registros totales
- **68** leads de **alta prioridad** (similares a tus ejemplos, ecom MX activos)
- **32** media prioridad
- **44** referencias (tus ejemplos originales)
- **5** baja prioridad (corporativos grandes)

## Lotes por nicho (`leads/por_nicho/`)

| Lote | Nicho | Leads | Archivos |
|---|---|---|---|
| 01 | Café / granos de café | 321 | `01_cafe_granos.*` |
| 02 | Colágeno hidrolizado | 324 | `02_colageno_hidrolizado.*` |

## Uso rápido

```bash
# Ver solo alta prioridad en CSV
awk -F',' '$7=="Alta"' leads/leads_por_nicho.csv
```

Abre `leads/LEADS_REPORTE.md` para navegar por nicho.
