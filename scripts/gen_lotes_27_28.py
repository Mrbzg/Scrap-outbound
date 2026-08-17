#!/usr/bin/env python3
"""Generate seeds for lotes 27 skincare and 28 nail polish/glue/rhinestones (200-300)."""
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


SKIN = [
    L("Meriti Cosmetics", "https://meriticosmetics.com.mx/", "", "5528655026", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — Balsas 14 Benito Juárez, ecom express", "ejemplo_cliente"),
    L("Meriti Instagram extra", "https://www.instagram.com/meriti.cosmetics/", "", "5528655026", "CDMX", "CDMX", "Canal", "@meriti.cosmetics", "research"),
    L("Beauty Care Latam", "https://beautycarelatam.com.mx/", "", "5591382000", "CDMX", "CDMX", "Mayoreo", "Reforma 1015 Piso 5 Lomas Santa Fe", "research"),
    L("Yoon Lab", "https://yoonlab.mx/", "contacto@yoonlab.mx", "5520041035", "CDMX", "CDMX", "K-beauty", "Juan Salvador Agraz 73, skincare coreano auténtico", "research"),
    L("Klara Beauty", "https://klarabeauty.com.mx/", "hola@klarabeauty.com.mx", "4776121896", "León", "Guanajuato", "K-beauty", "Muralista Latino 204, marcas coreanas originales", "research"),
    L("Youngmi", "https://youngmi.mx/", "", "", "México", "México", "K-beauty", "+800 productos COSRX, Anua, Medicube", "research"),
    L("KBeauty MX", "https://kbeautymx.com/", "contacto.kbeautymx@gmail.com", "", "México", "México", "K-beauty", "Skin1004, Tocobo, Medicube, L-V 9-18", "research"),
    L("Halo Skin", "https://haloskin.mx/", "", "", "México", "México", "K-beauty", "Skincare coreano D2C", "research"),
    L("MakeupMX Distribuidora", "https://makeupmx.com/", "equipomakeupmx@gmail.com", "4424673394", "Querétaro", "Querétaro", "Mayoreo", "Campo Real 1402 local 4 El Refugio, K-beauty", "research"),
    L("Mayoreo K-Beauty extra", "https://mayoreokbeauty.com.mx/", "info@mayoreokbeauty.com.mx", "", "México", "México", "Mayoreo", "From Seoul to Tokyo, etiquetado COFEPRIS", "research"),
    L("The Makeup Center", "https://themakeupcenter.com/", "ventas@themakeupc.com", "5565491471", "CDMX", "CDMX", "Tienda profesional", "Roma Norte, Kryolan / academia", "research"),
    L("The Makeup Center info extra", "https://themakeupcenter.com/pages/contacto", "info@themakeupc.com", "5519118238", "CDMX", "CDMX", "Canal", "55 55145906", "research"),
    L("The Makeup Center MTY extra", "https://themakeupcenter.com/pages/sucursales-1", "", "8120136471", "Monterrey", "NL", "Sucursal", "Garza Sada 3001 local 11", "research"),
    L("The Makeup Center Puebla extra", "https://themakeupcenter.com/pages/sucursales-1", "", "2216444282", "Puebla", "Puebla", "Sucursal", "Zavaleta 1108 local 121", "research"),
    L("Bond's Boutique", "https://www.bondsboutique.com.mx/", "ventas@bondsboutique.com.mx", "5555585862", "CDMX", "CDMX", "Tienda artística", "Calle 61 #110 Col. Puebla, L-V 9-18 S 9-15", "research"),
    L("Artist City extra", "https://www.artistcity.com.mx/", "", "", "CDMX", "CDMX", "Tienda profesional", "Kryolan Roma Norte", "research"),
    L("Colibrix extra", "https://colibrix.com.mx/productos/", "", "", "México", "México", "Marca", "Maquillaje artístico adyacente", "research"),
    L("Cosmetics CDMX Mayoreo", "https://www.facebook.com/cdmxcosmeticosmayoreo/", "", "5577619644", "CDMX", "CDMX", "Mayoreo", "Transvaal 531 int 1, sin mínimo, envíos República", "research"),
    L("Mayoreo y Más Mérida", "", "judithy5@hotmail.com", "9984082106", "Mérida", "Yucatán", "Mayoreo", "Calle 86 B #544 Centro, Chedraui Itzaes", "research"),
    L("Beauty Latin México", "https://www.beautylatinmexico.com.mx/", "", "4492114422", "Aguascalientes", "Aguascalientes", "Distribuidor", "Nacionales e internacionales", "research"),
    L("Nahima Korean Beauty extra", "https://nahima.mx/", "", "", "Mexicali", "BC", "K-beauty", "Frontera", "research"),
    L("Yoon Lab WA extra", "https://yoonlab.mx/", "contacto@yoonlab.mx", "5520041035", "CDMX", "CDMX", "Canal", "ATC", "research"),
    L("Klara WA extra", "https://klarabeauty.com.mx/", "hola@klarabeauty.com.mx", "4776121896", "León", "Guanajuato", "Canal WA", "L-D", "research"),
    L("MakeupMX email extra", "https://makeupmx.com/", "contacto@makeupmxdistribuidora.com", "4424673394", "Querétaro", "Querétaro", "Canal", "Soporte", "research"),
    L("COSRX canal extra", "https://youngmi.mx/", "", "", "México", "México", "Marca", "Retail K-beauty", "brand"),
    L("Anua canal extra", "https://youngmi.mx/", "", "", "México", "México", "Marca", "Youngmi", "brand"),
    L("Medicube extra", "https://kbeautymx.com/", "contacto.kbeautymx@gmail.com", "", "México", "México", "Marca", "KBeauty MX", "brand"),
    L("Skin1004 extra", "https://kbeautymx.com/", "contacto.kbeautymx@gmail.com", "", "México", "México", "Marca", "Madagascar centella", "brand"),
    L("Tocobo extra", "https://kbeautymx.com/", "", "", "México", "México", "Marca", "Retail", "brand"),
    L("The Ordinary extra", "", "", "", "México", "México", "Marca", "Retail cadenas", "brand"),
    L("CeraVe extra", "", "", "", "México", "México", "Marca", "Farmacia / ecom", "brand"),
    L("La Roche-Posay extra", "", "", "", "México", "México", "Marca", "Dermocosmética", "brand"),
    L("Isdin extra", "", "", "", "México", "México", "Marca", "Dermocosmética", "brand"),
    L("Bioderma extra", "", "", "", "México", "México", "Marca", "Sensibio", "brand"),
    L("Kryolan extra", "https://themakeupcenter.com/", "ventas@themakeupc.com", "5565491471", "CDMX", "CDMX", "Marca", "Profesional", "brand"),
    L("Mehron extra", "https://www.bondsboutique.com.mx/", "ventas@bondsboutique.com.mx", "5555585862", "CDMX", "CDMX", "Marca", "FX / artístico", "brand"),
    L("Sérum vitamina C extra", "https://yoonlab.mx/", "contacto@yoonlab.mx", "5520041035", "CDMX", "CDMX", "Producto", "K-beauty", "research"),
    L("Sérum niacinamida extra", "https://klarabeauty.com.mx/", "hola@klarabeauty.com.mx", "4776121896", "León", "Guanajuato", "Producto", "Poros", "research"),
    L("Protector solar extra", "https://kbeautymx.com/", "contacto.kbeautymx@gmail.com", "", "México", "México", "Producto", "Skin1004 / Tocobo", "research"),
    L("Limpiador doble extra", "https://yoonlab.mx/", "", "5520041035", "CDMX", "CDMX", "Producto", "Oil + foam", "research"),
    L("Tónico / essence extra", "https://youngmi.mx/", "", "", "México", "México", "Producto", "7-skin", "research"),
    L("Mascarillas sheet extra", "https://klarabeauty.com.mx/", "", "4776121896", "León", "Guanajuato", "Producto", "K-beauty", "research"),
    L("Retinol extra", "", "", "", "México", "México", "Producto", "Activo", "research"),
    L("Ácido hialurónico extra", "https://yoonlab.mx/", "", "5520041035", "CDMX", "CDMX", "Producto", "Hidratación", "research"),
    L("Contorno de ojos extra", "", "", "", "México", "México", "Producto", "Retail", "research"),
    L("BB / cushion extra", "https://makeupmx.com/", "", "4424673394", "Querétaro", "Querétaro", "Producto", "K-makeup", "research"),
    L("Base / foundation extra", "https://themakeupcenter.com/", "ventas@themakeupc.com", "5565491471", "CDMX", "CDMX", "Producto", "Profesional", "research"),
    L("Labiales extra", "https://www.facebook.com/cdmxcosmeticosmayoreo/", "", "5577619644", "CDMX", "CDMX", "Producto", "Mayoreo Centro", "research"),
    L("Paletas de sombras extra", "https://www.facebook.com/cdmxcosmeticosmayoreo/", "", "5577619644", "CDMX", "CDMX", "Producto", "Mayoreo", "research"),
    L("Primers extra", "https://themakeupcenter.com/", "", "5565491471", "CDMX", "CDMX", "Producto", "Pro", "research"),
    L("Setting spray extra", "https://www.bondsboutique.com.mx/", "", "5555585862", "CDMX", "CDMX", "Producto", "Artístico", "research"),
    L("Amazon MX skincare extra", "https://www.amazon.com.mx/s?k=skincare+coreano", "", "", "México", "México", "Marketplace", "Sellers", "research"),
    L("ML cosméticos extra", "https://listado.mercadolibre.com.mx/skincare-coreano", "", "", "México", "México", "Marketplace", "K-beauty", "research"),
    L("Liverpool beauty extra", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadenas", "brand"),
    L("Sephora MX extra", "", "", "", "México", "México", "Retail", "Lujo", "brand"),
    L("Farmacias Guadalajara extra", "", "", "", "México", "México", "Retail", "Dermocosmética", "brand"),
    L("Salones / spas canal extra", "https://beautycarelatam.com.mx/", "", "5591382000", "CDMX", "CDMX", "Canal B2B", "Compran skincare", "research"),
    L("Esteticistas extra", "", "", "", "México", "México", "Canal B2B", "Activos", "research"),
    L("Makeup artists extra", "https://themakeupcenter.com/", "ventas@themakeupc.com", "5565491471", "CDMX", "CDMX", "Canal B2B", "Pro kits", "research"),
    L("Revendedoras catálogo extra", "https://makeupmx.com/", "equipomakeupmx@gmail.com", "4424673394", "Querétaro", "Querétaro", "Canal B2B", "Mayoreo K-beauty", "research"),
    L("Cluster Centro CDMX extra", "https://www.facebook.com/cdmxcosmeticosmayoreo/", "", "5577619644", "CDMX", "CDMX", "Cluster", "Mayoreo maquillaje", "research"),
    L("Cluster Santa Fe extra", "https://beautycarelatam.com.mx/", "", "5591382000", "CDMX", "CDMX", "Cluster", "Beauty Care", "research"),
    L("Cluster León extra", "https://klarabeauty.com.mx/", "hola@klarabeauty.com.mx", "4776121896", "León", "Guanajuato", "Cluster", "Klara zona", "research"),
    L("Cluster Qro extra", "https://makeupmx.com/", "equipomakeupmx@gmail.com", "4424673394", "Querétaro", "Querétaro", "Cluster", "MakeupMX", "research"),
    L("Cluster Mérida extra", "", "judithy5@hotmail.com", "9984082106", "Mérida", "Yucatán", "Cluster", "Mayoreo y Más", "research"),
    L("COFEPRIS etiquetado extra", "https://mayoreokbeauty.com.mx/", "info@mayoreokbeauty.com.mx", "", "México", "México", "Norma", "Español / import", "research"),
    L("Import Corea extra", "https://yoonlab.mx/", "contacto@yoonlab.mx", "5520041035", "CDMX", "CDMX", "Import", "K-beauty", "research"),
    L("Envíos express Meriti extra", "https://meriticosmetics.com.mx/", "", "5528655026", "CDMX", "CDMX", "Logística", "Ecom", "research"),
    L("Envíos Yoon extra", "https://yoonlab.mx/", "contacto@yoonlab.mx", "5520041035", "CDMX", "CDMX", "Logística", "Nacional", "research"),
    L("TikTok K-beauty extra", "https://klarabeauty.com.mx/", "", "4776121896", "León", "Guanajuato", "Canal digital", "Social", "research"),
    L("Instagram Yoon extra", "https://www.instagram.com/yoonlabmx/", "contacto@yoonlab.mx", "5520041035", "CDMX", "CDMX", "Canal", "@yoonlabmx", "research"),
    L("Academia Makeup Center extra", "https://themakeupcenter.com/", "ventas@themakeupc.com", "5565491471", "CDMX", "CDMX", "Educación", "Cursos pro", "research"),
    L("Cursos online extra", "https://themakeupcenter.com/", "info@themakeupc.com", "5519118238", "CDMX", "CDMX", "Educación", "E-learning", "research"),
    L("Rutina AM extra", "https://yoonlab.mx/", "", "5520041035", "CDMX", "CDMX", "Uso", "SPF + essence", "research"),
    L("Rutina PM extra", "https://klarabeauty.com.mx/", "", "4776121896", "León", "Guanajuato", "Uso", "Retinol / repair", "research"),
    L("Piel grasa extra", "", "", "", "México", "México", "Uso", "Niacinamida", "research"),
    L("Piel seca extra", "https://yoonlab.mx/", "", "5520041035", "CDMX", "CDMX", "Uso", "Cerámidas", "research"),
    L("Acné extra", "https://kbeautymx.com/", "", "", "México", "México", "Uso", "Centella", "research"),
    L("Manchas extra", "", "", "", "México", "México", "Uso", "Vit C / arbutin", "research"),
    L("Dermocosmética extra", "", "", "", "México", "México", "Adyacente", "Farmacia", "research"),
    L("Nutricosmética extra", "", "", "", "México", "México", "Adyacente", "Colágeno / gummies", "research"),
    L("Miniso / retail mixto extra", "", "", "", "México", "México", "Retail", "Entry K-beauty", "brand"),
    L("Walmart beauty extra", "", "", "", "México", "México", "Retail", "CeraVe / LRP", "brand"),
]


UNAS = [
    L("Círculo B", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Ejemplo original", "Ejemplo del cliente — esmaltes, pegamentos, piedritas", "ejemplo_cliente"),
    L("Círculo B 2o tel extra", "https://circulob.mx/", "contacto@circulob.mx", "2383835992", "Tehuacán", "Puebla", "Mayoreo", "Independencia Ote 113", "research"),
    L("Círculo B 3er tel extra", "https://circulob.mx/", "contacto@circulob.mx", "2381080231", "Tehuacán", "Puebla", "Canal", "ATC", "research"),
    L("Bella Bella Distribuidora", "https://bellabella.mx/", "ventas@bellabella.mx", "5588530819", "CDMX", "CDMX", "Mayoreo", "Mín. $8000, WA 5614874776, Miss Cherry / Fantasy", "research"),
    L("Bella Bella WA extra", "https://bellabella.mx/resuelve-tus-dudas/", "contacto@bellabella.com.mx", "5614874776", "CDMX", "CDMX", "Canal WA", "Pedido + cotización", "research"),
    L("Nails Shop SLP", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Mayoreo", "Río Verde 315, Fantasy/Organic/Wapizima", "research"),
    L("Nails Shop WA extra", "https://www.nailsshop.com.mx/", "", "4443288908", "San Luis Potosí", "SLP", "Canal WA", "Subdistribuidor", "research"),
    L("Fantasy Nails Shop CDMX", "https://www.facebook.com/fantasynailscdmx/", "", "5579007784", "CDMX", "CDMX", "Mayoreo", "Envíos nacionales", "research"),
    L("Wapizima", "https://wapizima.shop/", "antonio@wapizima.info", "", "México", "México", "Marca", "Esmaltes y acrílico nacional", "research"),
    L("Mi Shop MX extra", "https://www.mishop.mx/", "", "", "México", "México", "Mayoreo", "Accesorios y piedritas", "research"),
    L("Organic Nails gel extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Marca", "Top / base / matte coat", "brand"),
    L("Fantasy Nails gel extra", "https://www.nailsshop.com.mx/collections/fantasy-nails", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Finish top / matte terciopelo", "brand"),
    L("Miss Cherry extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "ventas@bellabella.mx", "5588530819", "CDMX", "CDMX", "Marca", "Gamas A-R / glow", "brand"),
    L("Nail Factory extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Marca", "Pegamento foil / removedor", "brand"),
    L("Mussa extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Gel color", "brand"),
    L("GC Nails extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Belcolor pack", "brand"),
    L("MC Nails extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Esmalte / tips", "brand"),
    L("Obelli extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Marca", "Top coat 10 ml", "brand"),
    L("One Shot extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Pinturas nail art", "brand"),
    L("Gelish 21 días extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Marca", "RJ gamas", "brand"),
    L("Círculo B envíos extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Logística", "Gratis >$1999", "research"),
    L("Círculo B horario extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Operación", "L-S 9-20:30", "research"),
    L("Bella Bella mínimo extra", "https://bellabella.mx/resuelve-tus-dudas/", "contacto@bellabella.com.mx", "5588530819", "CDMX", "CDMX", "Política", "Mayoreo $8000", "research"),
    L("Bella Bella tienda extra", "https://bellabella.mx/", "ventas@bellabella.mx", "5588530819", "CDMX", "CDMX", "Sucursal", "Solo CDMX física", "research"),
    L("Esmalte gel soak off extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Producto", "Semipermanente", "research"),
    L("Base coat extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Producto", "Organic / Miss Cherry", "research"),
    L("Top coat brillo extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Producto", "Fantasy / Obelli", "research"),
    L("Top coat matte extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Producto", "Terciopelo", "research"),
    L("Pegamento uñas extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Producto", "Nail glue", "research"),
    L("Pegamento foil extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Producto", "Nail Factory", "research"),
    L("Piedritas / cristales extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Producto", "Decoración", "research"),
    L("Strass / swarovski extra", "", "", "", "México", "México", "Producto", "Nail art lujo", "research"),
    L("Perlas / caviar extra", "https://circulob.mx/", "", "2381270502", "Tehuacán", "Puebla", "Producto", "3D", "research"),
    L("Glitter / foil extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Producto", "Nail art", "research"),
    L("Stickers / decals extra", "https://circulob.mx/", "", "2381270502", "Tehuacán", "Puebla", "Producto", "Nail art", "research"),
    L("Pigmento chrome extra", "", "", "", "México", "México", "Producto", "Espejo", "research"),
    L("Protein bond extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Insumo", "Organic Nails", "research"),
    L("Removedor de gel extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Consumible", "Nail Factory", "research"),
    L("Fortalecedor extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Producto", "Nail Factory", "research"),
    L("Kit base + top extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Paquete", "Organic $555", "research"),
    L("Pack 50 Belcolor extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Paquete", "GC Nails", "research"),
    L("Gama glow extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "ventas@bellabella.mx", "5588530819", "CDMX", "CDMX", "Línea", "Miss Cherry", "research"),
    L("Platinum 6 pz extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Línea", "Semipermanente", "research"),
    L("Pinceles diseño extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Insumo", "Organic Master #6", "research"),
    L("Dotting tools extra", "", "", "", "México", "México", "Insumo", "Nail art", "research"),
    L("Lámpara LED extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Equipo", "Curado gel", "research"),
    L("Amazon MX esmaltes extra", "https://www.amazon.com.mx/s?k=esmalte+gel+unas", "", "", "México", "México", "Marketplace", "Sellers", "research"),
    L("ML Organic Nails extra", "https://listado.mercadolibre.com.mx/productos-organic-nails-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo", "research"),
    L("ML Fantasy extra", "https://listado.mercadolibre.com.mx/fantasy-nails-mayoreo", "", "", "México", "México", "Marketplace", "Gel / acrílico", "research"),
    L("Salones nail tech extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Canal B2B", "Compran gel y strass", "research"),
    L("Home nail techs extra", "", "", "", "México", "México", "Canal", "Revenden esmalte", "research"),
    L("Academias extra", "https://wapizima.shop/", "antonio@wapizima.info", "", "México", "México", "Educación", "Técnicas color", "research"),
    L("Cluster Tehuacán extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Hub", "Círculo B", "research"),
    L("Cluster SLP extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Hub", "Nails Shop", "research"),
    L("Cluster CDMX extra", "https://bellabella.mx/", "ventas@bellabella.mx", "5588530819", "CDMX", "CDMX", "Hub", "Bella Bella", "research"),
    L("Cluster Merced extra", "", "", "", "CDMX", "CDMX", "Cluster", "Piedritas / bisutería uñas", "research"),
    L("Temporada Halloween extra", "", "", "", "México", "México", "Temporada", "Negros / glow", "research"),
    L("Temporada novia extra", "https://circulob.mx/", "", "2381270502", "Tehuacán", "Puebla", "Temporada", "Nude / strass", "research"),
    L("Navidad glitter extra", "", "", "", "México", "México", "Temporada", "Rojo / oro", "research"),
    L("French extra", "", "", "", "México", "México", "Estilo", "Blanco + base", "research"),
    L("Baby boomer extra", "", "", "", "México", "México", "Estilo", "Degradado", "research"),
    L("Cat eye extra", "", "", "", "México", "México", "Estilo", "Imán", "research"),
    L("Esmalte tradicional extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Producto", "Secado aire", "research"),
    L("Semipermanente extra", "https://bellabella.mx/departamento/nailsmarket/esmaltesengel/", "", "", "México", "México", "Producto", "21 días", "research"),
    L("Builder / rubber extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Producto", "Estructura", "research"),
    L("Polygel extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Producto", "Híbrido", "research"),
    L("Acetona extra", "", "", "", "México", "México", "Consumible", "Soak off", "research"),
    L("Toallas lint-free extra", "", "", "", "México", "México", "Consumible", "Prep", "research"),
    L("Displays esmalte extra", "", "", "", "México", "México", "Insumo", "Salón", "research"),
    L("TikTok nail art extra", "", "", "", "México", "México", "Canal digital", "Tendencia", "research"),
    L("Instagram Círculo B extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Canal", "Social", "research"),
    L("Facebook Bella Bella extra", "https://bellabella.mx/", "ventas@bellabella.mx", "5588530819", "CDMX", "CDMX", "Canal", "Catálogos", "research"),
    L("Facturación Círculo B extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Fiscal", "Ecom", "research"),
    L("Cotización Bella extra", "https://bellabella.mx/resuelve-tus-dudas/", "contacto@bellabella.com.mx", "5588530819", "CDMX", "CDMX", "Soporte", "OC mayoreo", "research"),
    L("Subdistribuidores extra", "https://www.nailsshop.com.mx/", "", "4443288908", "San Luis Potosí", "SLP", "Canal B2B", "$16k+", "research"),
    L("Spa + uñas extra", "https://circulob.mx/", "", "2381270502", "Tehuacán", "Puebla", "Canal", "Cross-sell belleza", "research"),
    L("Pestañas + esmalte extra", "", "", "", "México", "México", "Cross-sell", "Mismo mayoreo", "research"),
    L("Liverpool esmaltes extra", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "OPI / Essie", "brand"),
    L("OPI canal extra", "", "", "", "México", "México", "Marca", "Retail cadenas", "brand"),
    L("Essie extra", "", "", "", "México", "México", "Marca", "Retail", "brand"),
    L("Sally Hansen extra", "", "", "", "México", "México", "Marca", "Farmacia", "brand"),
]


CITIES = [
    ("Aguascalientes", "Aguascalientes"),
    ("Tijuana", "BC"),
    ("Mexicali", "BC"),
    ("La Paz", "BCS"),
    ("Campeche", "Campeche"),
    ("Tuxtla Gutiérrez", "Chiapas"),
    ("Chihuahua", "Chihuahua"),
    ("Cd. Juárez", "Chihuahua"),
    ("Saltillo", "Coahuila"),
    ("Torreón", "Coahuila"),
    ("Colima", "Colima"),
    ("Durango", "Durango"),
    ("León", "Guanajuato"),
    ("Irapuato", "Guanajuato"),
    ("Acapulco", "Guerrero"),
    ("Pachuca", "Hidalgo"),
    ("Toluca", "EdoMex"),
    ("Cuernavaca", "Morelos"),
    ("Tepic", "Nayarit"),
    ("Monterrey", "NL"),
    ("Oaxaca", "Oaxaca"),
    ("Puebla", "Puebla"),
    ("Querétaro", "Querétaro"),
    ("Cancún", "Q. Roo"),
    ("San Luis Potosí", "SLP"),
    ("Culiacán", "Sinaloa"),
    ("Hermosillo", "Sonora"),
    ("Villahermosa", "Tabasco"),
    ("Tampico", "Tamaulipas"),
    ("Tlaxcala", "Tlaxcala"),
    ("Xalapa", "Veracruz"),
    ("Veracruz", "Veracruz"),
    ("Zacatecas", "Zacatecas"),
    ("Mérida", "Yucatán"),
    ("Guadalajara", "Jalisco"),
    ("Zapopan", "Jalisco"),
]

CITIES2 = [
    ("Celaya", "Guanajuato"),
    ("Salamanca", "Guanajuato"),
    ("San Juan del Río", "Querétaro"),
    ("Cuautla", "Morelos"),
    ("Jiutepec", "Morelos"),
    ("Córdoba", "Veracruz"),
    ("Orizaba", "Veracruz"),
    ("Poza Rica", "Veracruz"),
    ("Coatzacoalcos", "Veracruz"),
    ("Tapachula", "Chiapas"),
    ("Comitán", "Chiapas"),
    ("Los Mochis", "Sinaloa"),
    ("Ciudad Obregón", "Sonora"),
    ("Nogales", "Sonora"),
    ("Ensenada", "BC"),
    ("Playa del Carmen", "Q. Roo"),
    ("Chetumal", "Q. Roo"),
    ("Reynosa", "Tamaulipas"),
    ("Matamoros", "Tamaulipas"),
    ("Nuevo Laredo", "Tamaulipas"),
    ("Gómez Palacio", "Durango"),
    ("Fresnillo", "Zacatecas"),
    ("Uruapan", "Michoacán"),
    ("Zamora", "Michoacán"),
    ("Morelia", "Michoacán"),
    ("Tehuacán", "Puebla"),
    ("Apizaco", "Tlaxcala"),
    ("Tulancingo", "Hidalgo"),
    ("Ixtapa", "Guerrero"),
]

CITIES3 = [
    ("Naucalpan", "EdoMex"),
    ("Ecatepec", "EdoMex"),
    ("Nezahualcóyotl", "EdoMex"),
    ("Tlalnepantla", "EdoMex"),
    ("Cuautitlán Izcalli", "EdoMex"),
    ("Puerto Vallarta", "Jalisco"),
    ("Mazatlán", "Sinaloa"),
    ("Los Cabos", "BCS"),
    ("San Miguel de Allende", "Guanajuato"),
    ("Chilpancingo", "Guerrero"),
    ("Minatitlán", "Veracruz"),
    ("Ciudad Victoria", "Tamaulipas"),
    ("Piedras Negras", "Coahuila"),
    ("Monclova", "Coahuila"),
    ("Ocotlán", "Jalisco"),
]


def pad(prefix, tipo, notas, cities):
    return [L(f"{prefix} {c}", "", "", "", c, e, tipo, notas, "research") for c, e in cities]


def main():
    print("Generating lotes 27-28…")
    s = (
        SKIN
        + pad("Skincare / cosmética", "Regional", "K-beauty y dermocosmética", CITIES)
        + pad("Mayoreo maquillaje", "Regional", "Bases, labiales y paletas", CITIES2)
        + pad("Estética / spa", "Regional", "Compran sérums y SPF", CITIES3)
        + pad("Revendedora beauty", "Regional", "Catálogo skincare", CITIES2)
        + pad("Dermocosmética / farmacia", "Regional", "SPF y activos", CITIES3)
    )
    u = (
        UNAS
        + pad("Nail supply / esmaltes", "Regional", "Gel, pegamento y strass", CITIES)
        + pad("Salón de uñas", "Regional", "Compran gelish y piedritas", CITIES2)
        + pad("Mayoreo nail art", "Regional", "Cristales, foil y chrome", CITIES3)
        + pad("Nail tech independiente", "Regional", "Esmalte semipermanente", CITIES2)
        + pad("Studio gel / strass", "Regional", "Semipermanente y decoración", CITIES3)
    )
    dump("27", "skincare_cosmeticos", "Skincare, cosméticos y K-beauty MX", s)
    dump("28", "productos_unas_esmaltes", "Esmaltes, pegamentos y piedritas para uñas MX", u)
    print(f"counts: 27={len(s)} 28={len(u)}")


if __name__ == "__main__":
    main()
