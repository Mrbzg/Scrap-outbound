#!/usr/bin/env python3
"""Generate seeds for lote 52 (skincare coreano / K-beauty MX).
ONLY real companies — tiendas y distribuidores K-beauty con nombre verificable."""
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


KBEAUTY = [
    L("Halo Skin (ejemplo)", "https://haloskin.mx/", "", "", "México", "México", "Ejemplo original", "Ejemplo del cliente — skincare coreano D2C", "ejemplo_cliente"),
    L("Piel Coreana", "https://www.pielcoreana.com/", "", "", "México", "México", "Mayoreo", "8+ años con marcas coreanas; mayoreo K-beauty con factura y envíos express 1-2 días", "research"),
    L("Celiz", "https://www.celiz.com.mx/", "", "", "México", "México", "Mayoreo", "Proveedor de skincare coreano al mayoreo; 50% desc al invertir $30k", "research"),
    L("Kkul", "", "", "", "México", "México", "Mayoreo", "Skincare coreano a precio de mayoreo desde 1 pieza; envíos MX y USA", "research"),
    L("Laly Skin", "https://www.lalyskin.com/", "", "", "México", "México", "Mayoreo", "Mayoreo de skincare coreano en línea", "research"),
    L("Yoon Lab", "https://yoonlab.mx/", "contacto@yoonlab.mx", "5520041035", "CDMX", "CDMX", "Ecom", "Juan Salvador Agraz 73; skincare coreano auténtico", "research"),
    L("Klara Beauty", "https://klarabeauty.com.mx/", "hola@klarabeauty.com.mx", "4776121896", "León", "Guanajuato", "Ecom", "Muralista Latino 204; marcas coreanas originales", "research"),
    L("Youngmi", "https://youngmi.mx/", "", "", "México", "México", "Ecom", "+800 productos COSRX, Anua, Medicube", "research"),
    L("KBeauty MX", "https://kbeautymx.com/", "contacto.kbeautymx@gmail.com", "", "México", "México", "Ecom", "Skin1004, Tocobo, Medicube; L-V 9-18", "research"),
    L("Mayoreo K-Beauty", "https://mayoreokbeauty.com.mx/", "info@mayoreokbeauty.com.mx", "", "México", "México", "Mayoreo", "From Seoul to Tokyo; etiquetado COFEPRIS", "research"),
    L("MakeupMX Distribuidora", "https://makeupmx.com/", "contacto@makeupmxdistribuidora.com", "4424673394", "Querétaro", "Querétaro", "Mayoreo", "K-beauty y cosmética originales; Campo Real 1402 local 4", "research"),
    L("Nahima Korean Beauty", "https://nahima.mx/", "", "", "Mexicali", "BC", "Ecom", "K-beauty en frontera", "research"),
    L("COSRX", "", "", "", "Corea", "", "Marca", "Skincare coreano, retail MX vía Youngmi y otros", "brand"),
    L("Anua", "", "", "", "Corea", "", "Marca", "Skincare coreano, retail MX", "brand"),
    L("Medicube", "", "", "", "Corea", "", "Marca", "Skincare coreano, retail MX", "brand"),
    L("Skin1004", "", "", "", "Corea", "", "Marca", "Centella asiática, retail MX", "brand"),
    L("Tocobo", "", "", "", "Corea", "", "Marca", "Skincare coreano, retail MX", "brand"),
    L("Purito", "", "", "", "Corea", "", "Marca", "Skincare coreano, venta MX vía K-beauty shops", "brand"),
    L("Beauty of Joseon", "", "", "", "Corea", "", "Marca", "Skincare coreano viral, venta MX", "brand"),
    L("Laneige", "", "", "", "Corea", "", "Marca", "Skincare coreano, retail departamental MX", "brand"),
    L("Innisfree", "", "", "", "Corea", "", "Marca", "Skincare coreano, retail MX", "brand"),
    L("Etude House", "", "", "", "Corea", "", "Marca", "K-beauty, retail MX", "brand"),
    L("Missha", "", "", "", "Corea", "", "Marca", "K-beauty, venta MX", "brand"),
    L("Amazon MX K-beauty", "https://www.amazon.com.mx/s?k=skincare+coreano", "", "", "México", "México", "Marketplace", "Sellers de skincare coreano", "research"),
    L("Mercado Libre K-beauty", "https://listado.mercadolibre.com.mx/skincare-coreano", "", "", "México", "México", "Marketplace", "Tiendas de skincare coreano en ML", "research"),
    L("Sephora México K-beauty", "https://www.sephora.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Vende marcas coreanas (Laneige, Innisfree)", "brand"),
    L("Liverpool belleza coreana", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Sección de K-beauty", "brand"),
    L("TikTok Shop K-beauty", "https://shop.tiktok.com/", "", "", "México", "México", "Marketplace", "Venta D2C de K-beauty", "research"),
]


def main():
    print("Generating lote 52 (skincare coreano)…")
    dump("52", "skincare_coreano", "Skincare Coreano MX", KBEAUTY)
    print(f"counts: 52={len(KBEAUTY)}")


if __name__ == "__main__":
    main()
