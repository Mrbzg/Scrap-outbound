#!/usr/bin/env python3
"""Generate seeds for lote 50 (pelucas de colores MX).
ONLY real companies — tiendas de pelucas y sellers con nombre verificable."""
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


PELUCAS = [
    L("El Famundi (ejemplo)", "https://www.elfamundi.com.mx/", "", "5555525294", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — pelucas de colores y disfraces", "ejemplo_cliente"),
    L("El Castillo de la Fantasía", "", "", "", "CDMX", "CDMX", "Mayoreo", "Imperio de pelucas en el Centro CDMX; pelucas de fantasía desde $100 y cabello natural hasta $5,500; mayoreo", "research"),
    L("Don Moa Extensiones", "", "", "5559590050", "CDMX", "CDMX", "Mayoreo", "Pelucas de colores fantasía 2x$500 y extensiones; Plaza Correo Mayor 5, locales 9 y 10", "research"),
    L("Pelucas Morris", "", "", "", "CDMX", "CDMX", "Tienda", "Tienda de pelucas en el Centro CDMX; drag y transformismo", "research"),
    L("SensHair MX", "", "", "", "CDMX", "CDMX", "Tienda", "Pelucas de cabello natural y sintético; cosplay, drag y uso diario", "research"),
    L("Supreme Wigs", "", "", "", "CDMX", "CDMX", "Ecom", "Tienda de pelucas con sucursales CDMX, Monterrey y Cancún; venta online", "research"),
    L("Misi Shop", "", "", "", "CDMX", "CDMX", "Tienda", "Tienda de pelucas en el Centro CDMX", "research"),
    L("Comercializadora de Novedades", "", "", "", "México", "México", "Mayoreo", "Pelucas largas de colores mayoreo desde 3 pzs; seller de ML (4.1★, 55 reviews)", "research"),
    L("Sombreros y Fiesta", "", "", "", "México", "México", "Mayoreo", "Pelucas lacias cortas colores fantasía mayoreo; seller de ML", "research"),
    L("Extensioneslibni", "", "", "", "México", "México", "Marca", "Pelucas de fantasía onduladas (rosa, plata, amarillo) vía ML", "brand"),
    L("KANEKALON", "", "", "", "México", "México", "Marca", "Pelucas con fleco largas cosplay y colores fantasía; 4.4★ vía ML", "brand"),
    L("Premium Wigs", "", "", "", "México", "México", "Marca", "Pelucas de gama premium vía ML", "brand"),
    L("Disfraces Luza Peluza", "", "", "", "México", "México", "Marca", "Pelucas de personajes (Aquaman) vía ML", "brand"),
    L("El 10 Pelucas & Extensiones", "", "", "5578602637", "CDMX", "CDMX", "Tienda", "Pelucas y extensiones en el Centro; Alhóndiga 29E; envíos", "research"),
    L("Crazy Hair", "https://www.crazyhair.com.mx/", "", "", "CDMX", "CDMX", "Mayoreo", "Pelucas de colores, lace front y full lace; ventas al mayoreo; CDMX y GDL", "research"),
    L("MV Hair Extensions", "", "", "", "CDMX", "CDMX", "Mayoreo", "Pelucas y cabello mayoreo/menudeo; Izazaga 89 piso 5 local 505", "research"),
    L("Funidelia México", "https://www.funidelia.mx/", "", "", "México", "México", "Ecom", "Pelucas de disfraz y accesorios de fiesta online", "research"),
    L("Amazon MX pelucas", "https://www.amazon.com.mx/s?k=pelucas+de+colores", "", "", "México", "México", "Marketplace", "Sellers de pelucas de colores", "research"),
    L("Mercado Libre pelucas", "https://listado.mercadolibre.com.mx/pelucas-de-colores", "", "", "México", "México", "Marketplace", "Mayoreo de pelucas de colores", "research"),
    L("Peluca larga rosa mayoreo", "https://listado.mercadolibre.com.mx/pelucas-de-colores", "", "", "México", "México", "Producto", "Peluca larga color disfraz cosplay, mayoreo", "research"),
    L("Peluca corta bob colores", "https://listado.mercadolibre.com.mx/pelucas-colores-fantasia", "", "", "México", "México", "Producto", "Peluca corta bob de colores fantasía/disfraz, 12 colores", "research"),
    L("Peluca afro rosa pastel", "https://listado.mercadolibre.com.mx/pelucas-fantasia", "", "", "México", "México", "Producto", "Peluca afro tono rosa pastel, vía ML", "research"),
    L("Paquete 7 pelucas colores", "https://listado.mercadolibre.com.mx/pelucas-de-colores", "", "", "México", "México", "Producto", "Paquete de 7 pelucas largas de colores, mayoreo", "research"),
]


def main():
    print("Generating lote 50 (pelucas de colores)…")
    dump("50", "pelucas_de_colores", "Pelucas de colores MX", PELUCAS)
    print(f"counts: 50={len(PELUCAS)}")


if __name__ == "__main__":
    main()
