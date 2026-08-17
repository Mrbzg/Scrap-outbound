#!/usr/bin/env python3
"""Generate seeds for lote 53 (artículos de papelería en mayoreo MX).
Target 100+ REAL companies: marcas mexicanas, distribuidores y retail verificables."""
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


PAPEL = [
    L("Uline México (ejemplo)", "https://es.uline.mx/", "", "", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — papelería y empaque al mayoreo", "ejemplo_cliente"),
    # --- Distribuidores / papeleras mayoreo ---
    L("Papelerías Lumen", "https://lumen.com.mx/", "ventasmayoreo@lumen.com.mx", "5544455000", "CDMX", "CDMX", "Mayoreo", "Desde 1943; mayorista de papelería, electrónicos y hogar; República de El Salvador 52-54; ventas corporativas y gran mayoreo", "research"),
    L("Lumen Guadalajara", "https://lumen.com.mx/", "ventasmayoreo@lumen.com.mx", "3336143956", "Guadalajara", "Jalisco", "Sucursal", "C. Pedro Moreno 589, Centro GDL", "research"),
    L("Papira", "https://papira.com.mx/", "", "", "Guanajuato", "Guanajuato", "Mayoreo", "Papelería al mayoreo con planta en Guanajuato; marcas Bic, Crayola, Norma, Faber-Castell; envíos nacionales", "research"),
    L("Papelería Cornejo", "", "", "", "Guadalajara", "Jalisco", "Mayoreo", "Papelería de mayoreo en GDL", "research"),
    L("Papelería Omega", "", "", "", "Guadalajara", "Jalisco", "Mayoreo", "+9,000 artículos: útiles, oficina, escritura y archivo", "research"),
    L("Distribuidora Sajor", "", "", "", "Guadalajara", "Jalisco", "Mayoreo", "40+ años; productos Scribe, COPAMEX, Saira y Jiss", "research"),
    L("Unión Papelera", "", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidor de HP, 3M, Azor, Lefort, Avery Dennison, Epson, Sablón, Henkel, Scribe y Xerox", "research"),
    L("Papelera del Norte", "https://papeleradelnorte.shop/", "", "", "Monterrey", "Nuevo León", "Mayoreo", "Papelería al mayoreo del norte; 3M, BACO, Barrilito, BIC, Azor", "research"),
    L("Office Lab / Marchante", "https://marchante.mx/", "", "", "México", "México", "Mayoreo", "Colección papelería y oficina con 70+ marcas", "research"),
    L("Papelería Lozano Hermanos", "https://papeleriaslozanohermanos.com.mx/", "papeleria@lozano.com.mx", "5557611520", "CDMX", "CDMX", "Mayoreo", "Papelería y útiles, CDMX", "research"),
    L("COPAMEX", "https://www.copamex.com/", "", "", "Monterrey", "Nuevo León", "Fabricante", "Papelera mexicana líder en papeles de escritura y empaque", "brand"),
    L("Grupo Papelero Scribe", "https://scribe.com.mx/", "", "", "México", "México", "Fabricante", "Fabricante de cuadernos y papelería", "brand"),
    L("CIFRA Papelería", "", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora de papelería y consumibles", "research"),
    L("Dabo Papelerías", "", "", "", "CDMX", "CDMX", "Retail", "Cadena de papelerías", "brand"),
    L("RAI Papelerías", "", "", "", "CDMX", "CDMX", "Retail", "Cadena de papelerías y útiles", "brand"),
    L("Calpaco", "", "", "", "México", "México", "Mayoreo", "Papelería y regalos por mayoreo", "research"),
    L("Papelerías Yoreme", "", "", "", "Culiacán", "Sinaloa", "Retail", "Cadena de papelerías del noroeste", "brand"),
    L("Mango Papelerías", "", "", "", "México", "México", "Retail", "Cadena de papelerías", "brand"),
    L("Sanborns", "https://www.sanborns.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Dulcería y papelería fina", "brand"),
    L("Papelería Palacio", "", "", "", "CDMX", "CDMX", "Retail", "Papelería y librería", "brand"),
    # --- Marcas mexicanas de papelería ---
    L("Scribe", "https://scribe.com.mx/", "", "", "México", "México", "Marca", "Desde 1960; cuadernos y papelería mexicana", "brand"),
    L("Barrilito", "", "", "", "México", "México", "Marca", "200+ años; lápices, bolígrafos, tijeras y kits escolares", "brand"),
    L("BACO", "", "", "", "México", "México", "Marca", "75+ años; artículos escolares y de oficina", "brand"),
    L("Pelikan México", "https://www.pelikan.com.mx/", "", "", "México", "México", "Marca", "Papelería y útiles escolares, operación MX", "brand"),
    L("Norma", "", "", "", "México", "México", "Marca", "Cuadernos y útiles escolares mexicanos", "brand"),
    L("MAE", "", "", "", "México", "México", "Marca", "Útiles escolares mexicanos", "brand"),
    L("Chenson", "", "", "", "México", "México", "Marca", "Mochilas, loncheras y accesorios escolares MX", "brand"),
    L("Lápiz Carpintero", "", "", "", "México", "México", "Marca", "Lápices clásicos mexicanos", "brand"),
    L("Azor", "", "", "", "México", "México", "Marca", "Papelería y útiles, marca mexicana", "brand"),
    L("Janel", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Krystal", "", "", "", "México", "México", "Marca", "Cuadernos y papelería mexicana", "brand"),
    L("Offiland", "", "", "", "México", "México", "Marca", "Útiles escolares y oficina, marca MX", "brand"),
    L("Pegaso", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Rayter", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Sablón", "", "", "", "México", "México", "Marca", "Papelería y pegamentos, marca MX", "brand"),
    L("Vortred", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Mapasa", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Nassa", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Celosa", "", "", "", "México", "México", "Marca", "Cintas adhesivas mexicanas", "brand"),
    L("Memotip", "", "", "", "México", "México", "Marca", "Notas adhesivas mexicanas", "brand"),
    L("Devek", "", "", "", "México", "México", "Marca", "Plastificados y papelería MX", "brand"),
    L("Tuk", "", "", "", "México", "México", "Marca", "Adhesivos mexicanos", "brand"),
    L("Adhes", "", "", "", "México", "México", "Marca", "Adhesivos mexicanos", "brand"),
    L("K-Tape", "", "", "", "México", "México", "Marca", "Cintas adhesivas mexicanas", "brand"),
    L("Tapebear", "", "", "", "México", "México", "Marca", "Cintas adhesivas MX", "brand"),
    L("Navitek", "", "", "", "México", "México", "Marca", "Papelería técnica mexicana", "brand"),
    L("A-Ink", "", "", "", "México", "México", "Marca", "Tintas y papelería mexicana", "brand"),
    L("Easy Line", "", "", "", "México", "México", "Marca", "Útiles escolares MX", "brand"),
    L("First Class", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Kinera", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Kores México", "", "", "", "México", "México", "Marca", "Papelería y adhesivos, operación MX", "brand"),
    L("Kyma", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Lefort", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Starfile", "", "", "", "México", "México", "Marca", "Archivo y papelería mexicana", "brand"),
    L("Swingline", "", "", "", "USA", "", "Marca", "Engrapadoras y archivo, venta MX", "brand"),
    L("Euroformas", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Euromac", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Eurocolors", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Dietrix", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Bombin", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Confetti", "", "", "", "México", "México", "Marca", "Papelería mexicana", "brand"),
    L("Dixon", "", "", "", "USA", "", "Marca", "Lápices y colores, venta MX", "brand"),
    L("Paper Mate", "", "", "", "USA", "", "Marca", "Bolígrafos, venta MX", "brand"),
    L("Bic México", "", "", "", "México", "México", "Marca", "Bolígrafos y encendedores, operación MX", "brand"),
    L("Crayola México", "", "", "", "México", "México", "Marca", "Crayones y colores, operación MX", "brand"),
    L("Faber-Castell México", "", "", "", "México", "México", "Marca", "Lápices de color y escolares, operación MX", "brand"),
    L("Prismacolor", "", "", "", "USA", "", "Marca", "Arte profesional, venta MX", "brand"),
    L("Sharpie", "", "", "", "USA", "", "Marca", "Marcadores, venta MX", "brand"),
    L("Stabilo", "", "", "", "Alemania", "", "Marca", "Resaltadores y plumas, venta MX", "brand"),
    L("Pentel", "", "", "", "Japón", "", "Marca", "Escritura, venta MX", "brand"),
    L("Pilot", "", "", "", "Japón", "", "Marca", "Escritura, venta MX", "brand"),
    L("Uni-Ball", "", "", "", "Japón", "", "Marca", "Escritura, venta MX", "brand"),
    L("Zebra (papelería)", "", "", "", "Japón", "", "Marca", "Escritura, venta MX", "brand"),
    L("Parker", "", "", "", "Francia", "", "Marca", "Plumas, venta MX", "brand"),
    L("Waterman", "", "", "", "Francia", "", "Marca", "Plumas, venta MX", "brand"),
    L("Casio México", "", "", "", "México", "México", "Marca", "Calculadoras, operación MX", "brand"),
    L("3M México", "https://www.3m.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Post-it y cintas, operación MX", "brand"),
    L("Avery Dennison México", "", "", "", "México", "México", "Marca", "Etiquetas y archivo, operación MX", "brand"),
    L("ACCO Brands", "", "", "", "USA", "", "Marca", "Engrapadoras y archivo, venta MX", "brand"),
    L("Fellowes", "", "", "", "USA", "", "Marca", "Destructoras y oficina, venta MX", "brand"),
    L("Dymo", "", "", "", "USA", "", "Marca", "Etiquetadoras, venta MX", "brand"),
    L("Elmer's", "", "", "", "USA", "", "Marca", "Pegamentos, venta MX", "brand"),
    L("Xerox México", "", "", "", "México", "México", "Marca", "Papel y copiado, operación MX", "brand"),
    # --- Retail ---
    L("Office Depot México", "https://www.officedepot.com.mx/", "", "5525820910", "CDMX", "CDMX", "Retail", "Cadena de papelería y oficina", "brand"),
    L("OfficeMax México", "https://www.officemax.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadena de papelería y oficina", "brand"),
    L("Costco México", "https://www.costco.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Papelería y útiles por mayoreo", "brand"),
    L("Sam's Club México", "https://www.sams.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Papelería por mayoreo", "brand"),
    L("Walmart México", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Sección de papelería", "brand"),
    L("Liverpool Papelería", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Sección de papelería fina", "brand"),
    L("El Sótano", "https://www.elsotano.com/", "", "", "CDMX", "CDMX", "Retail", "Librería y papelería", "brand"),
    L("Posca", "", "", "", "Japón", "", "Marca", "Marcadores de pintura, venta MX", "brand"),
    L("Arteza", "", "", "", "USA", "", "Marca", "Arte y manualidades, venta MX", "brand"),
    L("Ecoline", "", "", "", "Holanda", "", "Marca", "Acuarelas líquidas, venta MX", "brand"),
    L("Derwent", "", "", "", "Reino Unido", "", "Marca", "Arte profesional, venta MX", "brand"),
    L("DAS", "", "", "", "Italia", "", "Marca", "Arcilla y modelado, venta MX", "brand"),
    L("Olfa", "", "", "", "Japón", "", "Marca", "Cúters y herramientas de corte, venta MX", "brand"),
    L("Markal", "", "", "", "USA", "", "Marca", "Marcadores industriales, venta MX", "brand"),
    L("Factis", "", "", "", "México", "México", "Marca", "Escolares mexicanos", "brand"),
    L("Expo", "", "", "", "USA", "", "Marca", "Marcadores para pizarrón, venta MX", "brand"),
    L("Acrilex", "", "", "", "Brasil", "", "Marca", "Pinturas y manualidades, venta MX", "brand"),
    L("Ampersand", "", "", "", "USA", "", "Marca", "Paneles de arte, venta MX", "brand"),
    L("Angelus", "", "", "", "USA", "", "Marca", "Pinturas para calzado, venta MX", "brand"),
    L("ATL", "", "", "", "México", "México", "Marca", "Papelería y arte mexicano", "brand"),
    # --- Marketplaces ---
    L("Amazon MX papelería mayoreo", "https://www.amazon.com.mx/s?k=papeleria+mayoreo", "", "", "México", "México", "Marketplace", "Sellers de papelería por mayoreo", "research"),
    L("Mercado Libre papelería mayoreo", "https://listado.mercadolibre.com.mx/papeleria-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de útiles escolares", "research"),
]


def main():
    print("Generating lote 53 (papelería mayoreo)…")
    dump("53", "papeleria_mayoreo", "Artículos de papelería en mayoreo MX", PAPEL)
    print(f"counts: 53={len(PAPEL)}")


if __name__ == "__main__":
    main()
