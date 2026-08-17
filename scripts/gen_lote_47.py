#!/usr/bin/env python3
"""Generate seeds for lote 47 (juguetes sensoriales mayoreo MX).
ONLY real companies — fabricantes y mayoristas de juguetes con nombre verificable."""
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


JUGUETES = [
    L("Mayoreo Didáctico (ejemplo)", "https://www.mayoreodidactico.mx/", "monica@mayoreodidactico.mx", "8189891980", "Monterrey", "Nuevo León", "Ejemplo original", "Ejemplo del cliente — juguetes sensoriales, Montessori y didácticos por mayoreo", "ejemplo_cliente"),
    # --- Fabricantes / mayoristas MX de juguetes ---
    L("Toys 2 Teach", "https://www.toys2teach.mx/", "", "5565854337", "CDMX", "CDMX", "Fabricante", "30+ años; fabricante de mobiliario escolar y juguetes didácticos; 5 plantas; atiende mayoristas", "research"),
    L("Ideas Hands / Casa Didáctica", "https://www.ideashands.com.mx/", "ventas@casadidactica.com", "2222998488", "Puebla", "Puebla", "Fabricante", "Fabricante y distribuidor autorizado de juguetes educativos; mayoristas y distribuidores", "research"),
    L("D'Toys", "http://www.dtoys.com.mx/", "", "3318809509", "Guadalajara", "Jalisco", "Mayoreo", "Distribuidor mayorista de juguetes; C. José Fernando Abascal 157, San Juan de Dios; mín. $1,000", "research"),
    L("Toymark", "", "", "", "CDMX", "CDMX", "Fabricante", "Empresa mexicana de fabricación, importación y distribución de juguetes por mayoreo por caja", "research"),
    L("Promeyco", "", "", "", "México", "México", "Fabricante", "Fabrica y distribuye juguetes al mayoreo: patines, triciclos, carros montables y andaderas", "research"),
    L("Juguetería La Loba", "", "", "", "México", "México", "Mayoreo", "Mayoreo de juguetes: didácticos, educativos, montables, rompecabezas y juegos de mesa", "research"),
    L("Pepe Toys", "", "", "", "Guadalajara", "Jalisco", "Mayoreo", "Distribuidor mayorista GDL de juguetes y papelería; envíos nacionales; mín. $2,000", "research"),
    L("Mayoreo de Juguete", "", "", "", "México", "México", "Mayoreo", "Juguetes de marca al mayoreo directo de fábrica (Mattel, Hasbro, Spin Master)", "research"),
    L("B-Toys", "", "", "", "México", "México", "Mayoreo", "Juguetes de marca por mayoreo para bebés y preescolar", "research"),
    L("Educactivity", "https://educactivity.mx/", "", "", "México", "México", "Fabricante", "Red de distribuidores de juguetes educativos y material didáctico; mín. $3,000; márgenes 30-40%", "research"),
    L("JAVI TOYS", "https://javitoys.mx/", "", "", "México", "México", "Ecom", "Kits de fidget toys: squishy, oruga, pop tube, pelota antiestrés y slime", "research"),
    L("ELE-GATE", "https://www.ele-gate.com/", "", "", "CDMX", "CDMX", "Mayoreo", "Pop It fidget toys y accesorios al mayoreo; sección 'Mayoreo'", "research"),
    L("Coconini", "https://www.coconini.com.mx/", "", "", "México", "México", "Ecom", "Juguetes y estimulación temprana", "research"),
    L("XMajo Didácticos", "https://xmajodidacticos.com/", "info@xmajodidacticos.com", "8117537880", "Monterrey", "Nuevo León", "Ecom", "Material didáctico y sensorial; +1,000 productos; envíos MX", "research"),
    L("Toiki", "https://toiki.mx/", "", "", "Guadalajara", "Jalisco", "Mayoreo", "Juguetes y artículos por mayoreo en GDL", "research"),
    L("AIPAI Cositas", "https://aipaicositas.com/", "cositas.aipai@gmail.com", "5522657691", "CDMX", "CDMX", "Ecom", "Juguetes didácticos y sensoriales", "research"),
    L("Grupo Educar", "https://grupoeducar.com.mx/", "", "5514036115", "CDMX", "CDMX", "Fabricante", "Material didáctico y juguetes educativos", "research"),
    L("Teng Da Tepito", "", "", "", "CDMX", "CDMX", "Mayoreo", "Mayoreo de juguetes en Tepito, CDMX", "research"),
    L("BM Toys México", "", "", "", "México", "México", "Mayoreo", "Mayoreo de juguetes", "research"),
    L("Distribuidora Mesones", "", "", "5656770570", "CDMX", "CDMX", "Mayoreo", "Distribuidora de juguetes en Mesones, Centro CDMX", "research"),
    # --- Marcas de fidget/sensorial (venta en ML/Amazon MX) ---
    L("BOJA Sensory", "https://www.amazon.com.mx/", "", "", "México", "México", "Marca", "Kit 40 pzs fidget toys sensoriales vía Amazon MX", "brand"),
    L("Newpop", "https://www.amazon.com.mx/", "", "", "México", "México", "Marca", "Pop tubes 24 pzs vía Amazon MX", "brand"),
    L("TOYGON", "https://www.amazon.com.mx/", "", "", "México", "México", "Marca", "Kit 2 pzs pop it con llavero vía Amazon MX", "brand"),
    L("DAQI", "https://www.amazon.com.mx/", "", "", "México", "México", "Marca", "Fidget toys 64 pack vía Amazon MX", "brand"),
    L("ZHEYU / Kulome", "https://www.amazon.com.mx/", "", "", "México", "México", "Marca", "Pop It electrónico antiestrés vía Amazon MX", "brand"),
    L("XJZWHN", "https://www.amazon.com.mx/", "", "", "México", "México", "Marca", "Cubos de fidget antiestrés vía Amazon MX", "brand"),
    L("MNNHQ", "https://www.amazon.com.mx/", "", "", "México", "México", "Marca", "36 pack squishy mochi vía Amazon MX", "brand"),
    # --- Retail / marketplaces ---
    L("Amazon MX fidget mayoreo", "https://www.amazon.com.mx/fidget-toys-mayoreo/s?k=fidget+toys+mayoreo", "", "", "México", "México", "Marketplace", "Sellers de fidget toys por mayoreo", "research"),
    L("Mercado Libre fidget", "https://listado.mercadolibre.com.mx/fidget-toys-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de fidget y pop it", "research"),
    L("Walmart México juguetes", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Vende juguetes sensoriales y pop it", "brand"),
    L("Liverpool juguetes", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Vende juguetes didácticos", "brand"),
    L("Juguetron", "https://www.juguetron.com.mx/", "", "", "México", "México", "Retail", "Juguetería en línea", "brand"),
    L("Julio Cepeda Juguetes", "", "", "", "México", "México", "Retail", "Juguetería y distribuidor", "brand"),
]


def main():
    print("Generating lote 47 (juguetes sensoriales mayoreo)…")
    dump("47", "juguetes_sensoriales_mayoreo", "Juguetes sensoriales mayoreo MX", JUGUETES)
    print(f"counts: 47={len(JUGUETES)}")


if __name__ == "__main__":
    main()
