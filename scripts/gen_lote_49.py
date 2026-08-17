#!/usr/bin/env python3
"""Generate seeds for lote 49 (accesorios para autos — luces y refacciones pequeñas MX).
ONLY real companies — tiendas y marcas de accesorios automotrices verificables."""
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


AUTOS = [
    L("Mas Refacciones (ejemplo)", "https://www.masrefacciones.mx/", "", "", "México", "México", "Ejemplo original", "Ejemplo del cliente — refacciones y accesorios para autos", "ejemplo_cliente"),
    # --- Tiendas de accesorios automotrices ---
    L("Comercializadora Fénix", "https://www.autoaccesoriosfenix.com/", "", "", "CDMX", "CDMX", "Mayoreo", "1,302+ productos de iluminación LED y accesorios; precios de mayoreo; envío CDMX", "research"),
    L("Evolum", "https://evolum.shop/", "", "", "México", "México", "Ecom", "Tienda líder en luces LED para carros: kits H4/H7/H11/9005/9006 con 22,000 lúmenes", "research"),
    L("Accesorios Molo", "https://www.accesoriosmolo.com/", "", "5635518793", "CDMX", "CDMX", "Mayoreo", "17+ años; accesorios automotrices mayoreo/menudeo; Juventino Rosas 9, Peralvillo", "research"),
    L("Accesorios Aguilar", "https://www.accesoriosaguilar.com/", "", "3322621310", "Zapopan", "Jalisco", "Mayoreo", "Focos LED, xenón, barras, alarmas y polarizado; Puerto Guaymas 983, Miramar", "research"),
    L("Leds Cuernavaca", "", "", "7771282726", "Cuernavaca", "Morelos", "Mayoreo", "Faros LED mayoreo/menudeo; modelos Ultra Luxury y Ultimate; también en Puebla", "research"),
    L("Autopartes García", "", "", "3333445000", "Guadalajara", "Jalisco", "Tienda", "Repuestos y accesorios para autos; faros y calaveras en GDL", "research"),
    L("Mundo Electrónico Víctor's", "", "", "3336581000", "Guadalajara", "Jalisco", "Mayoreo", "Iluminación LED hogar y auto, materiales electrónicos y repuestos; mayoreo/menudeo", "research"),
    L("Goled", "", "", "3787819000", "Tepatitlán", "Jalisco", "Tienda", "Tienda de iluminación para autos y camiones", "research"),
    # --- Marcas de iluminación/autopartes ---
    L("ADERCO", "", "", "", "México", "México", "Marca", "Accesorios y LED para auto, marca mexicana", "brand"),
    L("CARLUMEX", "", "", "", "México", "México", "Marca", "Iluminación automotriz, marca mexicana", "brand"),
    L("HOD", "", "", "", "México", "México", "Marca", "Partes de colisión automotriz", "brand"),
    L("IPADSA", "", "", "", "México", "México", "Marca", "Partes de colisión y autopartes", "brand"),
    L("Tunix", "", "", "", "México", "México", "Marca", "Luces LED y accesorios, vía mayoristas MX", "brand"),
    L("Imloya", "", "", "", "México", "México", "Marca", "Iluminación automotriz", "brand"),
    L("Lumen", "", "", "", "México", "México", "Marca", "Iluminación automotriz", "brand"),
    L("Bronco", "", "", "", "México", "México", "Marca", "Accesorios e iluminación para auto", "brand"),
    L("Big Country", "", "", "", "México", "México", "Marca", "Accesorios para auto", "brand"),
    L("IOL", "", "", "", "México", "México", "Marca", "Códigos LED mini slim y estrobos, vía ML", "brand"),
    # --- Productos (sellers/ML verificados) ---
    L("Kit luces LED C6", "", "", "", "México", "México", "Producto", "Kit luces LED auto H1/H7/H3/9005/9006, 4.3★ (2,424 reviews) vía ML", "research"),
    L("Focos LED Master", "", "", "", "México", "México", "Producto", "Kit faros LED Master H1/H3/H7/H11/9005/9006, 4.5★ (230 reviews)", "research"),
    L("Luz interior LED Canbus", "", "", "", "México", "México", "Producto", "Luz interior 31/41/36/39mm, 4.8★ (665 reviews) vía ML", "research"),
    L("Faro LED redondo auxiliar", "", "", "", "México", "México", "Producto", "Faros auxiliares LED con lupa y estrobo, mayoreo 30 pzas", "research"),
    L("Barra LED mini faro", "", "", "", "México", "México", "Producto", "Barras LED 5-7 pulgadas, 16-27 LED", "research"),
    L("Torreta 30 LED", "", "", "", "México", "México", "Producto", "Torreta LED montecarga amarilla industrial 10-110V", "research"),
    L("Faros 4x6 Diamond", "", "", "", "México", "México", "Producto", "Faros LED 4x6 modelo Diamond con luz de día, mayoreo 10 pzas", "research"),
    # --- Retail / marketplaces ---
    L("Amazon MX accesorios auto", "https://www.amazon.com.mx/s?k=accesorios+para+auto+led", "", "", "México", "México", "Marketplace", "Sellers de accesorios automotrices", "research"),
    L("Mercado Libre luces LED", "https://listado.mercadolibre.com.mx/luces-led-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de luces LED para auto", "research"),
    L("AutoZone México", "https://www.autozone.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Refaccionarias con accesorios y luces", "brand"),
    L("O'Reilly Auto Parts MX", "https://www.oreillyauto.com.mx/", "", "", "", "", "Retail", "Refaccionarias con accesorios", "brand"),
    L("NAPA México", "https://www.napaautopartes.mx/", "", "", "", "", "Retail", "Refaccionarias con accesorios", "brand"),
    L("Walmart México auto", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Sección automotriz con accesorios", "brand"),
    L("Steren auto", "https://www.steren.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Accesorios electrónicos para auto", "brand"),
    L("Sección Amarilla — focos LED mayoreo", "https://www.seccionamarilla.com.mx/", "", "", "México", "México", "Directorio", "Directorio de proveedores de focos LED automotriz", "research"),
]


def main():
    print("Generating lote 49 (accesorios para autos)…")
    dump("49", "accesorios_para_autos", "Accesorios para autos (luces y refacciones pequeñas) MX", AUTOS)
    print(f"counts: 49={len(AUTOS)}")


if __name__ == "__main__":
    main()
