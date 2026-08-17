#!/usr/bin/env python3
"""Generate seeds for lotes 44-46 (productos capilares/keratina, extensiones
de cabello, cortinas). ONLY real companies — marcas, fábricas, tiendas y
sellers con nombre comercial verificable."""
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
# LOTE 44 — Belleza / Productos para el cabello (keratina, cremas, ampolletas)
# ============================================================
CABELLO = [
    L("Don Juan Beauty Supply (ejemplo)", "https://donjuan.mx/", "contacto@donjuan.mx", "6621940726", "Hermosillo", "Sonora", "Ejemplo original", "Ejemplo del cliente — productos capilares y keratina", "ejemplo_cliente"),
    # --- Marcas mexicanas de cuidado capilar ---
    L("Sedal (Unilever)", "https://www.unilever.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Línea de shampoo y keratina, retail MX", "brand"),
    L("Savile", "", "", "", "México", "México", "Marca", "Shampoo biotina y cuidado capilar, marca MX", "brand"),
    L("Moco de Gorila", "", "", "", "México", "México", "Marca", "Gel y productos capilares mexicanos", "brand"),
    L("Caprice", "", "", "", "México", "México", "Marca", "Productos capilares mexicanos", "brand"),
    L("Jockey Club", "", "", "", "México", "México", "Marca", "Gel fijador y cuidado capilar MX", "brand"),
    L("Pantene (P&G)", "https://www.pantene.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Línea keratina y ampolletas, retail MX", "brand"),
    L("TRESemmé", "https://www.tresemme.com/", "", "", "CDMX", "CDMX", "Marca", "Profesional accesible, retail MX", "brand"),
    L("Hair Genics", "", "", "", "México", "México", "Marca", "Cuidado capilar, venta MX", "brand"),
    L("Natura (línea capilar)", "", "", "", "México", "México", "Marca", "Productos naturales para cabello", "brand"),
    # --- Keratinas / tratamientos profesionales ---
    L("Nagama Keratina y Botox", "https://www.nagamakeratinaybotox.com/", "", "", "México", "México", "Fabricante", "Empresa mexicana de keratina, botox capilar y shampoo post-tratamiento; distribución por estados", "research"),
    L("Salerm Cosmetics", "", "", "", "España", "", "Marca", "Keratina y ampolletas profesionales, distribuido en MX", "brand"),
    L("Loquay", "", "", "", "México", "México", "Marca", "Primer aminokeratina y ampolletas, vía ML", "brand"),
    L("Liss-Factory", "", "", "", "México", "México", "Marca", "Keratin Repair 2.0, alaciados sin formol, vía ML", "brand"),
    L("KeratinShot True Professional", "", "", "", "México", "México", "Marca", "Keratina alaciado japonés/brasileño mayoreo, vía ML", "brand"),
    L("Nutriliss", "", "", "", "México", "México", "Marca", "Keratina por litro, vía ML", "brand"),
    L("Vittale", "", "", "", "México", "México", "Marca", "Keratina reestructurante 320ml, vía ML", "brand"),
    L("Fábrica de Keratinas", "", "", "", "México", "México", "Fabricante", "Keratina japonesa 19L, post-keratina y alaciados, vía ML", "research"),
    L("More Keratinas", "", "", "", "México", "México", "Marca", "Keratina Ultra 19L cubeta, vía ML", "brand"),
    L("Bio Products Corps", "", "", "", "México", "México", "Marca", "Keratina brasileña galón, vía ML", "brand"),
    L("Bio Bellisima", "", "", "", "México", "México", "Marca", "Keratina galón, vía ML", "brand"),
    L("Keratin bio xai", "", "", "", "México", "México", "Marca", "Keratinas artesanales galón/20L, vía ML", "brand"),
    L("Ro Keratin", "", "", "", "México", "México", "Marca", "Keratina plastificado 1L, vía ML", "brand"),
    L("Volga", "", "", "", "México", "México", "Marca", "Kit 4L keratina, vía ML", "brand"),
    L("LACIO", "", "", "", "México", "México", "Marca", "Keratina japonesa galón 5L, vía ML", "brand"),
    L("Dlord", "", "", "", "México", "México", "Marca", "Keratina Gold litro, vía ML", "brand"),
    L("Firenze", "", "", "", "México", "México", "Marca", "Ampolletas keratina 12 pzs, vía ML", "brand"),
    L("Nutrapel Keractive", "", "", "", "México", "México", "Marca", "Ampolletas keratina, vía ML", "brand"),
    L("ZAIRE", "", "", "", "México", "México", "Marca", "Kerat-in alisado perfecto mayoreo, vía ML", "brand"),
    L("SELGRY", "", "", "", "México", "México", "Marca", "Mayoreo keratina capilar 10 pzs, vía ML", "brand"),
    L("Nancy Bruno Productos Capilares", "", "", "", "México", "México", "Distribuidor", "Tratamientos capilares por mayoreo, vía ML", "research"),
    L("STEFANIE", "", "", "", "México", "México", "Marca", "Ampolletas queratina y colágeno, vía ML", "brand"),
    # --- Distribuidores / mayoreo ---
    L("Cosmética AKCARE", "https://akcare.mx/", "", "", "México", "México", "Mayoreo", "Productos de salón por mayoreo: keratina, botox capilar, shampoo sin sal; etiqueta propia", "research"),
    L("Alev Natural", "https://alev-natural.ueniweb.com/", "", "", "CDMX", "CDMX", "Mayoreo", "Keratina 100% brasileña al mayoreo, CDMX", "research"),
    L("Sally Beauty México", "https://www.sallymexico.com/", "", "", "CDMX", "CDMX", "Retail", "Cadena de productos de belleza profesional", "brand"),
    L("Beauty Art", "https://shop.beautyart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Tienda de productos de belleza profesional", "research"),
    L("Rizos Mexicanos", "https://www.rizosmexicanos.com/", "", "5514718602", "CDMX", "CDMX", "Ecom", "Productos para cabello rizado MX", "research"),
    L("MexMax", "https://mexmax.com/", "", "", "USA", "", "Mayoreo", "Mayorista de productos capilares mexicanos (compra a fabricantes MX)", "research"),
    # --- Retail ---
    L("Walmart México", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Vende Pantene, Sedal, TRESemmé, ampolletas", "brand"),
    L("Soriana", "https://www.soriana.com/", "", "", "CDMX", "CDMX", "Retail", "Vende línea capilar masiva", "brand"),
    L("HEB México", "https://www.heb.com.mx/", "", "", "Monterrey", "Nuevo León", "Retail", "Vende línea capilar", "brand"),
    L("Chedraui", "https://www.chedraui.com.mx/", "", "", "Xalapa", "Veracruz", "Retail", "Vende línea capilar", "brand"),
    L("Farmacias del Ahorro", "https://www.fahorro.com/", "", "", "CDMX", "CDMX", "Retail", "Vende ampolletas y tratamientos capilares", "brand"),
    L("Farmacias Guadalajara", "https://www.farmaciasguadalajara.com.mx/", "", "", "Guadalajara", "Jalisco", "Retail", "Vende línea capilar", "brand"),
    L("Coppel", "https://www.coppel.com/", "", "", "CDMX", "CDMX", "Retail", "Vende línea capilar", "brand"),
    L("Amazon MX keratina", "https://www.amazon.com.mx/s?k=keratina+para+cabello", "", "", "México", "México", "Marketplace", "Sellers de keratina y productos capilares", "research"),
    L("Mercado Libre keratina", "https://listado.mercadolibre.com.mx/keratina-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de keratina y tratamientos capilares", "research"),
    L("ARKARA CO", "", "", "", "México", "México", "Distribuidor", "Distribuye Salerm en ML", "research"),
    L("TO BEAUTYSHOP", "", "", "", "México", "México", "Distribuidor", "Vende Salerm ampolletas en ML", "research"),
    L("Kativa", "", "", "", "Colombia", "", "Marca", "Keratina y cuidado capilar, distribuido en MX", "brand"),
    L("Sally and Beauty GDL", "", "", "", "Guadalajara", "Jalisco", "Tienda", "Tienda de cosméticos y belleza, 4.6★ en GDL", "research"),
    L("Mel Bros Co.", "", "", "", "Guadalajara", "Jalisco", "Tienda", "Cosmetics & beauty supply en GDL", "research"),
    L("Novedades Santy", "", "", "", "Guadalajara", "Jalisco", "Tienda", "Cosmetics & beauty supply en GDL", "research"),
    L("Sofía Distribuidora", "", "", "", "Guadalajara", "Jalisco", "Distribuidor", "Distribuidora de belleza en GDL", "research"),
    L("G&K Cosmetics", "", "", "", "Guadalajara", "Jalisco", "Tienda", "Cosmetics & beauty supply en Jalisco", "research"),
    L("Distribuidora Alhóndiga", "", "", "", "CDMX", "CDMX", "Distribuidor", "Distribuidora de productos de belleza, Col. Juárez", "research"),
    L("Distribuidora de belleza Alejandri", "", "", "", "CDMX", "CDMX", "Distribuidor", "Distribuidora de productos de belleza CDMX", "research"),
    L("Biutik", "", "", "", "Coyoacán", "CDMX", "Tienda", "Cosmetics & beauty supply en Coyoacán", "research"),
    L("Casa Barba", "", "", "", "CDMX", "CDMX", "Tienda", "Cosmetics & beauty supply en CDMX", "research"),
    L("Betsary Real Beauty Supply", "https://betsary.com/", "", "", "CDMX", "CDMX", "Distribuidor", "Distribuidora de productos de belleza con envíos a todo México", "research"),
    L("Asepxia (Genomma)", "https://www.genommalab.com/", "", "", "CDMX", "CDMX", "Marca", "Cuidado capilar y facial, laboratorio MX", "brand"),
    L("L'Oréal Professionnel México", "https://www.lorealprofessionnel.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Tratamientos profesionales de keratina", "brand"),
    L("Kérastase", "https://www.kerastase.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Lujo capilar, retail MX", "brand"),
    L("Redken", "https://www.redken.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Cuidado capilar profesional, retail MX", "brand"),
    L("Wella Professionals", "https://www.wella.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Color y tratamiento profesional", "brand"),
    L("Schwarzkopf Professional", "https://www.schwarzkopf.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Color y cuidado capilar profesional", "brand"),
]


# ============================================================
# LOTE 45 — Belleza / Extensiones de pelo para salón
# ============================================================
EXTENSIONES = [
    L("Beauty Art (ejemplo)", "https://shop.beautyart.com.mx/", "", "", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — tienda de belleza con extensiones para salón", "ejemplo_cliente"),
    L("Rapunzel Extensiones Naturales", "https://www.facebook.com/RapunzelMX/", "", "5525005774", "CDMX", "CDMX", "Mayoreo", "Extensiones 100% natural, mayoreo y menudeo; Buenavista 227, Lindavista", "research"),
    L("Extensiones de Cabello CDMX", "https://extensiones-de-cabello-cdmx.negocio.site/", "", "5514406688", "CDMX", "CDMX", "Mayoreo", "Cabello 100% humano y virgen; Chupícuaro 15; envíos nacionales", "research"),
    L("MAYFE", "https://mayfe.com.mx/", "", "", "México", "México", "Ecom", "30+ años; extensiones de cabello 100% humano con garantía de color", "research"),
    L("Naked Hair", "https://www.sallymexico.com/", "", "", "México", "México", "Marca", "Extensiones Remy con clip, vía Sally Beauty MX", "brand"),
    L("LUV REMY", "", "", "", "México", "México", "Marca", "Extensiones Eve 22'' 100% natural, vía ML", "brand"),
    L("GALA Remy", "", "", "", "México", "México", "Marca", "Extensiones 100% natural 18'' básicos, vía ML", "brand"),
    L("XBWIG", "", "", "", "México", "México", "Marca", "Extensiones clip rectas 7 pzs, vía ML (4.6★ 1,015 reviews)", "brand"),
    L("JR Extensiones", "", "", "", "México", "México", "Marca", "Extensiones fibra natural con clips, mayoreo 6 pzs, vía ML", "brand"),
    L("MY STYLE", "", "", "", "México", "México", "Marca", "Coletas de listón mayoreo, vía ML", "brand"),
    L("INVISIBLE", "", "", "", "México", "México", "Marca", "Extensiones hilo invisible mayoreo 6 pzs, vía ML", "brand"),
    L("ANOGOL", "", "", "", "México", "México", "Marca", "Extensiones trenzadas de color, vía ML", "brand"),
    L("CHECKK", "", "", "", "México", "México", "Marca", "Coleta postiza cabello natural, vía ML", "brand"),
    L("GNN", "", "", "", "México", "México", "Marca", "Kit cortina de cabello 21 pzs, vía ML", "brand"),
    L("MU Extensiones", "", "", "", "México", "México", "Marca", "Extensiones clip de pelo natural 10 pzs, vía ML", "brand"),
    L("Sally Beauty México", "https://www.sallymexico.com/", "", "", "CDMX", "CDMX", "Retail", "Cadena con sección de extensiones y pelucas", "brand"),
    L("MV Hair Extensions", "", "", "", "CDMX", "CDMX", "Mayoreo", "Venta de cabello mayoreo/menudeo y colocaciones; Izazaga 89 piso 5 local 505, Centro", "research"),
    L("Novengasa / Star One", "", "", "5528468155", "CDMX", "CDMX", "Tienda", "Tienda de belleza con extensiones; Calle del Carmen 67, Centro", "research"),
    L("Michelle Sainz Extensiones", "", "", "5612964521", "Guadalajara", "Jalisco", "Mayoreo", "Sucursales GDL, CDMX y Vallarta; fibra premium (ACA Hair)", "research"),
    L("Don Moa Extensiones", "", "", "5559590050", "CDMX", "CDMX", "Mayoreo", "Emprende con pelucas; Correo Mayor 5, locales 9 y 10, CDMX", "research"),
    L("El 10 Pelucas & Extensiones", "", "", "5578602637", "CDMX", "CDMX", "Tienda", "Pelucas y extensiones en el Centro; Alhóndiga 29E; envíos", "research"),
    L("Crazy Hair", "https://www.crazyhair.com.mx/", "", "", "CDMX", "CDMX", "Mayoreo", "Pelucas y extensiones 100% humano, mix y sintético; ventas al mayoreo; sucursales CDMX y GDL", "research"),
    L("Cabello Natural", "https://www.cabellonatural.com.mx/", "extensionesdepelo16@gmail.com", "3338150221", "Zapopan", "Jalisco", "Ecom", "Extensiones y coletas de cabello natural; Plaza Picacho, Calz. Lázaro Cárdenas 3770 local 3A", "research"),
    L("Imperio Extensiones GDL", "https://www.instagram.com/imperio_extensionsgdl/", "", "3324941839", "Guadalajara", "Jalisco", "Mayoreo", "Extensiones 100% humano; envíos nacionales; mayoreo y menudeo", "research"),
    L("Amazon MX extensiones", "https://www.amazon.com.mx/s?k=extensiones+de+cabello", "", "", "México", "México", "Marketplace", "Sellers de extensiones", "research"),
    L("Mercado Libre extensiones", "https://listado.mercadolibre.com.mx/extensiones-de-cabello-a-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de extensiones", "research"),
]


# ============================================================
# LOTE 46 — Hogar / Cortinas
# ============================================================
CORTINAS = [
    L("Cortinas.com (ejemplo)", "https://cortinas.com/", "", "", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — cortinas", "ejemplo_cliente"),
    L("Grupo Cortilum", "https://www.cortilum.mx/", "", "3320022116", "Guadalajara", "Jalisco", "Fabricante", "15+ años; fábrica de cortinas enrollables, blackout, screen y toldos; sucursales PV y Cancún", "research"),
    L("Viva Persianas", "https://vivapersianas.com/", "contacto@vivapersianas.com", "8181900840", "Monterrey", "Nuevo León", "Fabricante", "13+ años y 50,000 clientes; persianas, cortinas y toldos a la medida; automatización Somfy", "research"),
    L("Viva Persianas GDL", "https://vivapersianas.com/", "guadalajara@vivapersianas.com", "3315962343", "Guadalajara", "Jalisco", "Sucursal", "Oficina Guadalajara", "research"),
    L("Persianas Casa Bonita", "https://www.persianascasabonita.com/", "", "", "Hermosillo", "Sonora", "Fabricante", "20 años; persianas y cortinas en 14 ciudades: MTY, GDL, Hermosillo, Mérida, Tampico, Saltillo…", "research"),
    L("Persianas Luxor", "https://www.persianasluxor.com.mx/", "ventas@persianasluxor.com.mx", "5585485672", "CDMX", "CDMX", "Fabricante", "Fabricantes directos desde 1996; persianas y cortinas a medida, eléctricas y blackout", "research"),
    L("Tecno Blinds Shop", "https://tecnoblindscdmx.shop/", "", "", "CDMX", "CDMX", "Fabricante", "Distribuidor oficial; persianas, cortinas y toldos con motorización; cobertura CDMX, Cuernavaca, Querétaro y Edomex", "research"),
    L("PersianasyCortinas.com", "https://persianasycortinas.com/", "", "8114973858", "México", "México", "Ecom", "Tienda en línea #1 de persianas y cortinas; envío gratis desde $3,499; medidas exactas garantizadas", "research"),
    L("Pisos y Muros LNA", "https://lna.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Persianas y cortinas blackout, enrollables y traslúcidas; sucursales", "research"),
    L("Meya Design", "https://www.meya-design.mx/", "", "", "Naucalpan", "EdoMex", "Fabricante", "Cortinas personalizadas fabricadas en planta Farz; showroom Ciudad Satélite; garantía hasta 3 años", "research"),
    L("Brancato", "https://www.brancato.com.mx/", "", "", "Monterrey", "Nuevo León", "Mayoreo", "Telas para cortinas de mayoreo: blackouts, sheers y decorativas; surte cortineros y tapiceros", "research"),
    L("Casa Osaka", "", "", "", "México", "México", "Marca", "Cortinas blackout 2 paneles, vía ML (4.9★ 179 reviews)", "brand"),
    L("Melocotton Hogar", "", "", "", "México", "México", "Marca", "Cortinas blackout microfibra, vía Walmart", "brand"),
    L("Zulema", "", "", "", "México", "México", "Marca", "Cortinas de encaje y cenefas, retail MX", "brand"),
    L("Nanwei", "", "", "", "China", "", "Marca", "Cortinas blackout, vía ML/import", "brand"),
    L("Lightdot", "", "", "", "México", "México", "Distribuidor", "Vende Nanwei en ML", "research"),
    L("Teker", "", "", "", "China", "", "Marca", "Cortinas blackout, vía ML (4.8★ 2,127 reviews)", "brand"),
    L("Home Trends (Walmart)", "", "", "", "México", "México", "Marca", "Cortinas blackout y de baño, marca de Walmart MX", "brand"),
    L("Home Creations", "", "", "", "México", "México", "Marca", "Cortinas de baño, marca retail MX", "brand"),
    L("Mainstays", "", "", "", "USA", "", "Marca", "Cortinas y cortineros, marca Walmart", "brand"),
    L("Way to Celebrate", "", "", "", "México", "México", "Marca", "Cortinas decorativas, vía Walmart", "brand"),
    L("Walmart México", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Sección de cortinas y persianas", "brand"),
    L("Amazon MX cortinas", "https://www.amazon.com.mx/s?k=cortinas+blackout", "", "", "México", "México", "Marketplace", "Sellers de cortinas", "research"),
    L("Mercado Libre cortinas", "https://listado.mercadolibre.com.mx/cortinas-black-out-por-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de cortinas blackout", "research"),
]


def main():
    print("Generating lotes 44-46 (solo empresas reales)…")
    dump("44", "productos_cabello_keratina", "Productos para el cabello / keratina MX", CABELLO)
    dump("45", "extensiones_de_pelo", "Extensiones de pelo para salón MX", EXTENSIONES)
    dump("46", "cortinas", "Cortinas MX", CORTINAS)
    print(f"counts: 44={len(CABELLO)} 45={len(EXTENSIONES)} 46={len(CORTINAS)}")


if __name__ == "__main__":
    main()
