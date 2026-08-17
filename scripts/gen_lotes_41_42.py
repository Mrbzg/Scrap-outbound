#!/usr/bin/env python3
"""Generate seeds for lotes 41-42 (scoops/sorpresas, artículos para adultos).
ONLY real companies — tiendas, mayoristas y marcas con presencia MX verificada."""
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


# ============================================================
# LOTE 41 — Regalos / Scoops / sorpresas
# ============================================================
SCOOPS = [
    L("Scoops Sorpresas Mx", "https://www.tiktok.com/@scoopssorpresasmx", "", "6142442232", "Chihuahua", "Chihuahua", "Ejemplo original", "Ejemplo del cliente — scoop orders por TikTok; WhatsApp 614 244 2232; envíos nacionales", "ejemplo_cliente"),
    L("Deiker Scoops", "https://deikerscoops.com/", "", "", "México", "México", "Ecom", "Scoops sorpresa con productos seleccionados; Luxe Clásica $899; video personalizado", "research"),
    L("Cool Scoops MX", "https://www.tiktok.com/@cool.scoops.mx", "", "5534286710", "México", "México", "Ecom", "Mystery scoop orders con envíos a todo México; WhatsApp 55 3428 6710", "research"),
    L("Maneki Lucky Scoop MX", "https://www.instagram.com/manekiluckyscoopmx/", "", "", "CDMX", "CDMX", "Ecom", "Scoop order kawaii y Sanrio desde CDMX; envíos nacionales", "research"),
    L("Scoup Mewss", "", "", "", "Torreón", "Coahuila", "Ecom", "Pionera de scoops en La Laguna: mini (7-12 artículos) y premium (12-20) con video ASMR", "research"),
    L("FLOR DE NEÓN | scoops", "https://www.tiktok.com/@flordeneon.scoops", "", "", "México", "México", "Ecom", "Scoop orders con envíos a toda la República; papelería kawaii y Sanrio", "research"),
    L("Bubble Scoops", "https://www.tiktok.com/@bubble.scoops", "", "", "México", "México", "Ecom", "Pedidos kawaii con ASMR; fidgets, squishy y papelería", "research"),
    L("Küssy Scoop", "https://www.tiktok.com/@kussyscoop", "", "", "México", "México", "Ecom", "Maxi y sweet scoop orders kawaii; empaque ASMR; scoopmexico", "research"),
    L("Puchi Scoop", "https://www.tiktok.com/@puchi.scoop", "", "", "México", "México", "Ecom", "Mystery scoop shop: maquillaje y papelería", "research"),
    L("Kawaii Devil Shop", "https://www.tiktok.com/@kawaiidevilshop", "", "", "México", "México", "Ecom", "Mystery scoop box con charms, pins y stickers; mini scoop gratis por orden", "research"),
    L("Hammy Scoops MX", "https://www.tiktok.com/@sweethamscoops", "", "", "México", "México", "Ecom", "Scoop orders Sanrio/papelería kawaii; TikTok Shop; envíos MX", "research"),
    L("Shoppink", "https://www.tiktok.com/@shoppinkk0", "", "", "México", "México", "Ecom", "Mystery scoop de 20 cápsulas con productos de belleza y regalos", "research"),
    L("Bookscoop MX", "https://www.tiktok.com/@bookscoopmx", "", "", "México", "México", "Ecom", "Caja sorpresa 20 scoops temática booktok/libros", "research"),
    L("CUTIENINI Boutique", "https://www.tiktok.com/@cutienini_boutique", "", "", "México", "México", "Ecom", "Sanrio mix box y mystery scoop ASMR", "research"),
    L("Crystaira Mystery Scoop", "https://www.tiktok.com/@crystaira_mystery", "", "", "México", "México", "Ecom", "Sanrio cards + scoops; packing orders", "research"),
    L("Favorite Scoops", "https://www.tiktok.com/@favorite.scoops", "", "", "México", "México", "Ecom", "Mini scoops temáticas Sanrio/Hello Kitty", "research"),
    L("Tienda Komet", "https://tiendakomet.com/", "", "", "México", "México", "Ecom", "Cajas sorpresa de electrónica (Apple/iPhone) con 20% off hot sale", "research"),
    L("LiquiMart México", "https://www.tiktok.com/@liquimartmexico", "", "", "México", "México", "Ecom", "Cajas sorpresa de electrónica y liquidación", "research"),
    L("Regalos y Canastas", "https://www.regalosycanastas.mx/", "", "", "Mérida", "Yucatán", "Regalos", "Caja sorpresa con flores, chocolates y frase personalizada (Mérida)", "research"),
    L("Mystery Box Caja Sorpresa ML", "https://listado.mercadolibre.com.mx/caja-sorpresa", "", "", "México", "México", "Marketplace", "Sellers de cajas sorpresa/misteriosas de electrónica en ML", "research"),
    L("Sanrio", "https://www.sanrio.com.mx/", "", "", "", "", "Marca", "Licencias Hello Kitty y personajes kawaii que se revenden en scoops", "brand"),
    L("Squishmallows MX", "", "", "", "", "", "Marca", "Squishy y peluches que se incluyen en scoops", "brand"),
    L("TikTok Shop México", "https://shop.tiktok.com/", "", "", "", "", "Marketplace", "Plataforma donde operan la mayoría de tiendas scoop MX", "research"),
    L("Etsy — sellers scoop", "https://www.etsy.com/mx/market/kawaii_stationery_scoop", "", "", "", "", "Marketplace", "Vendedores de mystery scoops y lucky dips", "research"),
    L("Chíkidi", "https://chikidi.com.mx/", "", "", "México", "México", "Papelería kawaii", "Tienda MX de papelería kawaii y stickers Sanrio; insumo para scoops", "research"),
    L("Papecute", "https://www.instagram.com/papecuteoficial/", "", "5550326851", "México", "México", "Papelería kawaii", "Papelería boutique MX especializada en accesorios kawaii y Sanrio; catálogo WhatsApp", "research"),
    L("PANGEA Un Mundo de Diversión", "", "", "", "México", "México", "Distribuidor", "Stickers Hello Kitty 500 pzas; seller de ML", "research"),
    L("Lola Tienda", "", "", "", "México", "México", "Distribuidor", "Lapiceras y papelería Sanrio; seller de ML", "research"),
    L("Kawaii Box Kuromi (ML)", "https://listado.mercadolibre.com.mx/sanrio-papeleria", "", "", "México", "México", "Marketplace", "Kits de papelería Sanrio en caja de regalo kawaii", "research"),
]


# ============================================================
# LOTE 42 — Adultos / Artículos para adultos
# ============================================================
ADULTOS = [
    L("Tienda Venus", "https://www.tiendavenus.com/", "", "", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — sex shop en línea", "ejemplo_cliente"),
    L("Love & Toys CDMX", "https://loveandtoys.com.mx/", "", "5657538385", "CDMX", "CDMX", "Sex shop", "500+ productos; showroom con cita; Ignacio Ramos Praslow 171, Iztapalapa", "research"),
    L("ToLove Sex Shop", "https://tolove.mx/", "", "5564338669", "CDMX", "CDMX", "Sex shop", "Eje 5 Sur Ramos Millán 65, Benito Juárez; envíos nacionales", "research"),
    L("Mi Pasión SexShop", "https://www.mipasion.com.mx/", "", "3326467132", "Guadalajara", "Jalisco", "Sex shop", "Juguetes eróticos; venta mayoreo; envíos a todo México y USA", "research"),
    L("Boners Sex Shop", "https://boners.com.mx/", "", "", "Puebla", "Puebla", "Sex shop", "Especializada en juguetes para hombres gay; envío discreto nacional", "research"),
    L("Inttimus Sex Shop", "https://www.inttimus.com.mx/", "", "", "Mazatlán", "Sinaloa", "Sex shop", "Boutique erótica: vibradores, dildos, lubricantes, BDSM; envíos", "research"),
    L("Secreto Amor MX", "https://secretoamormx.com/", "", "", "México", "México", "Mayoreo", "Distribuidor mayorista líder; mín. $10,000; marcas reconocidas; envíos nacionales", "research"),
    L("Bunny Brand Love Toys", "https://www.sexshopmayoreo.mx/", "", "5610442123", "CDMX", "CDMX", "Mayoreo", "Mayorista para sex shops; Calz. Tlalpan 2905 of 100, Coyoacán", "research"),
    L("Varta Mayoreo", "https://vartamayoreo.mx/", "ventas@vartamayoreo.mx", "5525695800", "CDMX", "CDMX", "Mayoreo", "Distribuidora de artículos para adulto; marcas internacionales; envíos MX", "research"),
    L("La Manzana de Eva", "", "", "", "CDMX", "CDMX", "Cadena", "Cadena mexicana de sex shops con varias sucursales", "brand"),
    L("Satisfyer", "", "", "", "Alemania", "", "Marca", "Succionadores; distribución y venta en México", "brand"),
    L("LELO", "", "", "", "Suecia", "", "Marca", "Vibradores premium; se vende en MX", "brand"),
    L("We-Vibe", "", "", "", "Canadá", "", "Marca", "Juguetes en pareja con app; venta MX", "brand"),
    L("Womanizer", "", "", "", "Alemania", "", "Marca", "Tecnología Pleasure Air; venta MX", "brand"),
    L("Lovense", "", "", "", "China", "", "Marca", "Juguetes control remoto vía app; venta MX", "brand"),
    L("Doc Johnson", "", "", "", "USA", "", "Marca", "Juguetes clásicos; distribución MX", "brand"),
    L("Pipedream Products", "", "", "", "USA", "", "Marca", "Juguetes y novedades; distribución MX", "brand"),
    L("Jimmy Jane", "", "", "", "USA", "", "Marca", "Juguetes de diseño; venta MX", "brand"),
    L("Kamasutra", "", "", "", "México", "", "Marca", "Lubricantes y cosmética íntima mexicana", "brand"),
    L("JO Lubricants", "", "", "", "USA", "", "Marca", "Lubricantes; distribución MX", "brand"),
    L("ID Lubricants", "", "", "", "USA", "", "Marca", "Lubricantes; vía mayoristas MX", "brand"),
    L("Sliquid", "", "", "", "USA", "", "Marca", "Lubricantes naturales; venta MX", "brand"),
    L("Tenga", "", "", "", "Japón", "", "Marca", "Masturbadores desechables; venta MX", "brand"),
    L("Fleshlight", "", "", "", "USA", "", "Marca", "Masturbadores; venta MX", "brand"),
    L("Fun Factory", "", "", "", "Alemania", "", "Marca", "Juguetes de silicona; venta MX", "brand"),
    L("Magic Motion", "", "", "", "China", "", "Marca", "Juguetes con app; distribución Latam", "brand"),
    L("Svakom", "", "", "", "China", "", "Marca", "Juguetes premium; venta MX", "brand"),
    L("Kiiroo", "", "", "", "Holanda", "", "Marca", "Juguetes interactivos; distribución Latam", "brand"),
    L("OhMiBod", "", "", "", "USA", "", "Marca", "Juguetes con música/app; venta MX", "brand"),
    L("Nasstoys", "", "", "", "USA", "", "Marca", "Juguetes económicos; distribución MX", "brand"),
    L("Trojan", "", "", "", "USA", "", "Marca", "Condones y lubricantes; retail MX", "brand"),
    L("Durex", "", "", "", "UK", "", "Marca", "Condones y lubricantes; retail MX", "brand"),
    L("Sico", "", "", "", "México", "", "Marca", "Condones mexicanos; retail", "brand"),
    L("Prudence", "", "", "", "México", "", "Marca", "Condones mexicanos; retail", "brand"),
    L("Control", "", "", "", "México", "", "Marca", "Condones mexicanos; retail", "brand"),
    L("Lifestyles", "", "", "", "USA", "", "Marca", "Condones; retail MX", "brand"),
    L("Farmacias del Ahorro", "https://www.fahorro.com/", "", "", "CDMX", "CDMX", "Retail", "Vende condones y lubricantes", "brand"),
    L("Farmacias Guadalajara", "https://www.farmaciasguadalajara.com.mx/", "", "", "Guadalajara", "Jalisco", "Retail", "Vende condones y lubricantes", "brand"),
    L("Farmacias San Pablo", "https://farmaciasanpablo.mx/", "", "", "CDMX", "CDMX", "Retail", "Vende condones y lubricantes", "brand"),
    L("Farmacias Benavides", "https://www.benavides.com.mx/", "", "", "Monterrey", "Nuevo León", "Retail", "Vende condones y lubricantes", "brand"),
    L("Erotika Love Store", "https://www.erotikalovestore.mx/", "hola@erotikalovestore.mx", "5621690379", "CDMX", "CDMX", "Sex shop", "Hamburgo 105, Col. Juárez; juguetes, lubricantes y lencería; envíos", "research"),
    L("SexyShop CDMX", "https://sexyshop.mx/", "", "5592455592", "CDMX", "CDMX", "Sex shop", "Calz. Acoxpa 566 local 1B, Prados Coapa, Tlalpan; WA 55 3031 2857", "research"),
    L("Gold Dreams", "", "", "", "CDMX", "CDMX", "Sex shop", "Hamburgo 165, Zona Rosa; 15+ años; artículos de piel, arneses y dildos", "research"),
    L("Diversex Condonería", "", "", "", "CDMX", "CDMX", "Sex shop", "Regina 72, Centro; lubricantes, vibradores, arneses, talleres y asesorías", "research"),
    L("Vainilla Condonería", "", "", "", "CDMX", "CDMX", "Sex shop", "Belisario Domínguez 15, Coyoacán; enfoque divertido y saludable", "research"),
    L("BeHappy Sex Store", "", "", "", "CDMX", "CDMX", "Sex shop", "Sex shop discreta en CDMX; vibradores, dildos y lencería", "research"),
    L("Sex Capital", "", "", "", "CDMX", "CDMX", "Sex shop", "16 de Septiembre 11, Centro; juguetes y cabinas de cine", "research"),
    L("Cake Sex Shop", "https://cake.com.mx/", "", "", "CDMX", "CDMX", "Sex shop", "Más de 2,500 productos; blog de salud sexual", "research"),
    L("Fantasías Boutique Tijuana", "https://fantasiasboutique.com/", "info@fantasiasboutique.com", "6643825677", "Tijuana", "Baja California", "Sex shop", "Blvd. Gustavo Díaz Ordaz 13391, Plaza Bonita; envíos y recolección", "research"),
    L("Sex Shop Sin Filtros Mérida", "https://www.facebook.com/SinFiltrosmerida/", "sexshopsinfiltrosmerida@gmail.com", "9995323488", "Mérida", "Yucatán", "Sex shop", "Tienda ONLINE con entregas discretas a domicilio en Mérida", "research"),
    L("Walmart México", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Sección de condones y lubricantes", "brand"),
    L("Soriana", "https://www.soriana.com/", "", "", "CDMX", "CDMX", "Retail", "Sección de condones y lubricantes", "brand"),
    L("Amazon MX juguetes eróticos", "https://www.amazon.com.mx/s?k=juguetes+eroticos", "", "", "México", "México", "Marketplace", "Sellers de juguetes eróticos", "research"),
    L("Mercado Libre sex shop", "https://listado.mercadolibre.com.mx/sex-shop", "", "", "México", "México", "Marketplace", "Tiendas de artículos para adultos en ML", "research"),
]


def main():
    print("Generating lotes 41-42 (solo empresas reales)…")
    dump("41", "scoops_sorpresas", "Scoops / cajas sorpresa MX", SCOOPS)
    dump("42", "articulos_para_adultos", "Artículos para adultos MX", ADULTOS)
    print(f"counts: 41={len(SCOOPS)} 42={len(ADULTOS)}")


if __name__ == "__main__":
    main()
