#!/usr/bin/env python3
"""Generate seeds for lote 51 (jabones y shampoos MX).
ONLY real companies — jabonerías artesanales y marcas con nombre verificable."""
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


JABONES = [
    L("Rizos Mexicanos (ejemplo)", "https://www.rizosmexicanos.com/", "", "5514718602", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — shampoos y jabones", "ejemplo_cliente"),
    L("Mar Amoli", "https://www.amoli.mx/", "", "", "México", "México", "Fabricante", "Jabones artesanales, shampoo y acondicionador sólidos, cremas y bálsamos; catálogo mayoreo con envíos nacionales", "research"),
    L("Productos Möe", "https://www.productosmoe.com/", "", "3330365447", "Zapopan", "Jalisco", "Fabricante", "Jabones, shampoo sólido y velas de soja; maquila y mayoreo con marca personal; Río Tuxpan 1049", "research"),
    L("Bam Boo! Lifestyle", "https://www.bamboolifestyle.com.mx/", "onnearrss@gmail.com", "5579388337", "CDMX", "CDMX", "Marca", "Jabones artesanales 100g con carbón activado, chocomenta, miel y avena; packs de mayoreo", "research"),
    L("Onneageld (distribuidor Bam Boo)", "https://onneageld.com.mx/", "", "", "México", "México", "Distribuidor", "Distribuidor de Bam Boo! Lifestyle: 20 pack mix jabones mayoreo", "research"),
    L("Jabones Artesanales BioAlei", "https://www.jabonesartesanales.com.mx/", "", "5526486262", "CDMX", "CDMX", "Fabricante", "Jabones decorativos y aromaterapia; tiendas CDMX, Mérida, Puebla, Chiapas y GDL; amenidades para hoteles", "research"),
    L("BioAlei Mérida", "https://www.jabonesartesanales.com.mx/", "", "9991950922", "Mérida", "Yucatán", "Sucursal", "Tienda BioAlei Montejo, Mérida", "research"),
    L("BioAlei Guadalajara", "https://www.jabonesartesanales.com.mx/", "", "36596819", "Guadalajara", "Jalisco", "Sucursal", "BioAlei GDL; WhatsApp 331 539 8154", "research"),
    L("BioAlei Puebla", "https://www.jabonesartesanales.com.mx/", "", "", "Puebla", "Puebla", "Sucursal", "Rosendo Márquez 2501 local B", "research"),
    L("Jabones Artesanales Puebla", "https://jabonesartesanalespuebla.com.mx/", "", "", "Puebla", "Puebla", "Fabricante", "Jabones 100% naturales; Cam. al Batán 44, Villa Satélite Calera", "research"),
    L("Jabones Ordaz", "https://www.jabonesartesanalesordaz.net/", "ventas@jabonesartesanalesordaz.net", "5536169938", "CDMX", "CDMX", "Fabricante", "Fabricante de jabones artesanales; Avena 161, Granjas Esmeralda, Iztapalapa", "research"),
    L("Moldemanía", "https://www.moldemania.com/", "", "", "CDMX", "CDMX", "Insumos", "Tienda de moldes e insumos para velas, jabones y repostería; Mesones 75 y 138D, CDMX", "research"),
    L("Bianni Revolution", "", "", "5573661570", "CDMX", "CDMX", "Marca", "Jabones artesanales mayoreo; Carmen 24 y Correo Mayor 12 local 102, Centro CDMX", "research"),
    L("Jabones Artesanales Eclipse", "https://jabones-artesanales-eclipse.ueniweb.com/", "", "", "CDMX", "CDMX", "Tienda", "Jabones artesanales; Revolución Social 48, Iztapalapa; cobertura CDMX y Texmelucan", "research"),
    L("Jabón de Zorro D'Avi", "https://www.jabondezorro.com/", "", "", "México", "México", "Fabricante", "Champú sólido ecológico y jabones artesanales; venta por mayor y menor", "research"),
    L("Laguna Cyprien", "https://lagunacyprien.mx/", "", "", "México", "México", "Marca", "Shampoo sólido y jabones sin sulfatos ni plásticos, hechos en México", "research"),
    L("Raíces Co", "", "", "", "México", "México", "Marca", "Shampoo sólido anti-canas de nogal", "brand"),
    L("Avellana Beauty Eco Boutique", "", "", "", "México", "México", "Marca", "Shampoo sólido anti-canas", "brand"),
    L("Lu'um Nuestra Tierra", "", "", "", "México", "México", "Marca", "Shampoo matizante de canas sólido", "brand"),
    L("Kaisasa", "", "", "", "México", "México", "Marca", "Shampoo con tinte cubre canas, 4.7★ vía ML", "brand"),
    L("OnlyShop México", "https://www.onlyshop.com.mx/", "", "", "México", "México", "Ecom", "Shampoo tinte cubre canas jengibre 500ml", "research"),
    L("MEIDU México", "https://www.meidu.com.mx/", "", "5511336665", "CDMX", "CDMX", "Marca", "Shampoo con tinte y cuidado capilar", "research"),
    L("Amazon MX jabones artesanales", "https://www.amazon.com.mx/s?k=jabones+artesanales", "", "", "México", "México", "Marketplace", "Sellers de jabones artesanales", "research"),
    L("Mercado Libre jabones mayoreo", "https://listado.mercadolibre.com.mx/jabones-artesanales-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de jabones artesanales", "research"),
    L("Etsy México jabones", "https://www.etsy.com/mx/market/jabones_artesanales", "", "", "México", "México", "Marketplace", "Vendedores de jabones artesanales MX", "research"),
    L("Walmart México jabones", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Vende jabones de tocador y shampoo", "brand"),
    L("Tienda Naturista El Mundo Natural", "https://www.elmundonatural.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Tienda naturista con jabones y shampoo natural", "brand"),
    L("Gran Naturista", "", "", "", "CDMX", "CDMX", "Retail", "Cadena de tiendas naturistas", "brand"),
]


def main():
    print("Generating lote 51 (jabones y shampoos)…")
    dump("51", "jabones_shampoos", "Jabones y shampoos MX", JABONES)
    print(f"counts: 51={len(JABONES)}")


if __name__ == "__main__":
    main()
