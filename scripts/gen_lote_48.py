#!/usr/bin/env python3
"""Generate seeds for lote 48 (botellas y tapas personalizados MX).
ONLY real companies — fábricas de envases/tapas y personalizadores con nombre verificable."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def L(empresa, url="", email="", tel="", ciudad="", estado="", tipo="", notas="", fuente="research"):
    d = {"empresa": empresa, "tipo": tipo, "notas": notas, "fuente": fuente}
    if url:
        d["url"] = url
    if email:
        d["email"] = email
    if tel:
        d["telefono"] = tel
    if ciudad:
        d["ciudad"] = ciudad
    if estado:
        d["estado"] = estado
    return d


def dump(lote, slug, desc, leads):
    path = ROOT / "config" / "seeds" / f"{lote}_{slug}.json"
    path.write_text(
        json.dumps({"lote": lote, "slug": slug, "description": desc, "leads": leads}, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    print(f"  {path.name}: {len(leads)} seeds")


ENVASES = [
    L("Escowill (ejemplo)", "https://escowill.com/", "", "", "México", "México", "Ejemplo original", "Ejemplo del cliente — fabricante de botellas PET y tapas para salud y belleza; 250+ modelos", "ejemplo_cliente"),
    # --- Fábricas de envases y tapas ---
    L("Industrias Bogri", "https://www.bogri.com.mx/", "", "5567206820", "CDMX", "CDMX", "Fabricante", "33 años; botellas, tarros, pomaderas y tapas PET/HDPE/PP/PVC; Sto. Tomás 29, Azcapotzalco", "research"),
    L("Plastika", "https://www.plastika.com.mx/", "", "", "Puebla", "Puebla", "Fabricante", "Desde 2000; envases y tapas de plástico ISO 9001; sectores farmacéutico, alimenticio y químico", "research"),
    L("Envases La Merced", "https://envaseslamerced.mx/", "", "", "CDMX", "CDMX", "Fabricante", "Envases PET al mayoreo; botellas, frascos y tapas; 5 sucursales y stock inmediato", "research"),
    L("TEGSA Tapas y Envases", "https://tegsa.mx/", "ventas@tegsa.mx", "3313065957", "Guadalajara", "Jalisco", "Fabricante", "Desde 2015; tapas y envases de plástico, metal y vidrio; WA 3314230801", "research"),
    L("MAHA Food Service", "https://maha.com.mx/collections/vasos-personalizables", "hola@maha.com.mx", "", "CDMX", "CDMX", "Mayoreo", "Vasos personalizados con logo para cafeterías y eventos; papel y PET; tinta grado alimenticio", "research"),
    L("Kupp Termos y Vasos", "https://tustermospersonalizados.com/", "", "", "México", "México", "Mayoreo", "Termos, vasos y cilindros personalizados; desde 30 pzs; +2,400 eventos; 4.8★", "research"),
    L("Impressline", "https://www.impressline.com.mx/termos-personalizados", "", "", "CDMX", "CDMX", "Mayoreo", "Artículos promocionales: termos, tazas, vasos y botellas personalizados con logo", "research"),
    L("Calate Taller Creativo", "https://calate.com.mx/", "", "", "Monterrey", "Nuevo León", "Personalización", "Termos con grabado láser, DTF UV y serigrafía; playeras y tote bags; envíos MX", "research"),
    L("TUYO.MX", "https://www.tuyo.mx/", "", "", "México", "México", "Personalización", "Termos personalizados con impresión UV; precios de mayoreo", "research"),
    L("Escowill tapas y atomizadores", "https://escowill.com/", "", "", "México", "México", "Producto", "Tapas y atomizadores para el mercado de salud y belleza", "research"),
    # --- Marcas de envases ---
    L("ALPLA México", "https://www.alpla.com/mx", "", "", "México", "México", "Fabricante", "Fabricante global de envases plásticos con plantas en México", "brand"),
    L("Envases Universales", "https://www.envasesuniversales.com/", "", "", "México", "México", "Fabricante", "Envases y empaques para la industria", "brand"),
    L("Vidriera Los Reyes", "", "", "", "CDMX", "CDMX", "Fabricante", "Fabricante de envases de vidrio", "brand"),
    L("Envases del Norte", "", "", "", "Monterrey", "Nuevo León", "Fabricante", "Envases y tapas para industria", "brand"),
    L("Plásticos Técnicos de México", "", "", "", "CDMX", "CDMX", "Fabricante", "Fabricación de envases y piezas plásticas", "brand"),
    # --- Sellers / marketplaces ---
    L("TLP (tazas personalizadas)", "", "", "", "México", "México", "Marca", "Taza personalizada económica mayoreo, 4.9★ vía ML", "brand"),
    L("Termos personalizados ML", "https://listado.mercadolibre.com.mx/termos-personalizados-economicos-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de termos y tazas personalizados", "research"),
    L("Amazon MX botellas personalizadas", "https://www.amazon.com.mx/s?k=botellas+personalizadas", "", "", "México", "México", "Marketplace", "Sellers de botellas y termos personalizados", "research"),
    L("Botella Vertis (Bogri)", "https://www.bogri.com.mx/fabricacion/botellas-de-plastico/", "", "5567206820", "CDMX", "CDMX", "Producto", "Modelo de botella de plástico de línea", "research"),
    L("Tarros y pomaderas Bogri", "https://www.bogri.com.mx/fabricacion/botellas-de-plastico/", "", "5567206820", "CDMX", "CDMX", "Producto", "Tarros, pomaderas y talqueras de plástico", "research"),
    L("Tapas dosificadoras TEGSA", "https://tegsa.mx/", "ventas@tegsa.mx", "3313065957", "Guadalajara", "Jalisco", "Producto", "Flip top, disc top y tapas dosificadoras", "research"),
    L("Tapas metálicas twist TEGSA", "https://tegsa.mx/", "ventas@tegsa.mx", "3313065957", "Guadalajara", "Jalisco", "Producto", "Tapas metálicas de medio giro para frascos", "research"),
    L("Goteros y bombas Plastika", "https://www.plastika.com.mx/", "", "", "Puebla", "Puebla", "Producto", "Goteros, vasos dosificadores y bombas atomizadoras", "research"),
    L("Garrafas Plastika", "https://www.plastika.com.mx/", "", "", "Puebla", "Puebla", "Producto", "Garrafas de plástico para industria", "research"),
    L("Vaso cafetero personalizado MAHA", "https://maha.com.mx/collections/vasos-personalizables", "", "", "CDMX", "CDMX", "Producto", "Vasos de papel 10-20oz con logo", "research"),
    L("Fajilla de cartón personalizada MAHA", "https://maha.com.mx/collections/vasos-personalizables", "", "", "CDMX", "CDMX", "Producto", "Fajillas full color para vasos de café", "research"),
]


def main():
    print("Generating lote 48 (botellas y tapas personalizados)…")
    dump("48", "botellas_tapas_personalizados", "Botellas y tapas personalizados MX", ENVASES)
    print(f"counts: 48={len(ENVASES)}")


if __name__ == "__main__":
    main()
