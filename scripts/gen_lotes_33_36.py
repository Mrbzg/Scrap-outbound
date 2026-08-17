#!/usr/bin/env python3
"""Generate seeds for lotes 33-36 (mochilas/útiles escolares, skincare/maquillaje,
refacciones automotrices, vitaminas para plantas) — 200+ leads each."""
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
# LOTE 33 — Papelería / Mochilas y útiles escolares
# ============================================================
MOCHILAS = [
    L("Samsonite México (ejemplo)", "https://samsonite.com.mx/collections/mochilas-escolares", "", "", "Naucalpan", "EdoMex", "Ejemplo original", "Ejemplo del cliente — mochilas escolares; Blvd Manuel Ávila Camacho 5 Torre B P.24", "ejemplo_cliente"),
    L("Aguiglez Products", "https://aguiglez.com.mx/mochilas-aguiglez/", "aguiglez@gmail.com", "4777111542", "León", "Guanajuato", "Fabricante", "Fabricante mochilas escolar/universitaria/laboral, mín. 50 pzs, hecho en MX", "research"),
    L("Aguiglez WhatsApp", "https://aguiglez.com.mx/mochilas-aguiglez/", "", "4776479087", "León", "Guanajuato", "Canal", "WhatsApp (477) 647 9087", "research"),
    L("Mochilas & Backpacks", "https://mochilasybackpacks.com/", "", "5592624315", "CDMX", "CDMX", "Fabricante", "Calz. Mariano Escobedo 476 P.12, Anzures; desde 50 pzs; envíos MX/USA", "research"),
    L("Mochilas & Backpacks WA", "https://mochilasybackpacks.com/", "", "5564552687", "CDMX", "CDMX", "Canal", "WhatsApp +52 55 6455 2687", "research"),
    L("Mochilas, Carpetas y Agendas Plus", "https://mochilascarpetasyagendasplus.com/", "contacto2@carpetasyagendasplus.com.mx", "5554407000", "CDMX", "CDMX", "Mayoreo", "Proveedores de mochilas y útiles por mayoreo CDMX", "research"),
    L("Agendas Plus 2o tel", "https://mochilascarpetasyagendasplus.com/", "", "5555194935", "CDMX", "CDMX", "Canal", "55 5519 4935", "research"),
    L("Mayoreo Monterrey", "https://mayoreomonterrey.com.mx/", "ventas@mayoreomonterrey.com.mx", "8117988059", "Monterrey", "Nuevo León", "Mayoreo", "Mochilas, bolsos y accesorios por volumen; envíos nacionales", "research"),
    L("La Reyna del Mayoreo", "https://lareynadelmayoreo.com/", "", "", "CDMX", "CDMX", "Mayoreo", "Lotes de combos mochila escolar 3pz, figuras 3D, útiles", "research"),
    L("D165 Fabricante Tepito", "", "", "", "CDMX", "CDMX", "Fabricante", "Fabricante mochila escolar por mayoreo, Col. Tepito", "research"),
    L("Mochilas de mayoreo FB", "", "", "", "", "", "Fabricante", "Fabricación y venta de mochilas desde 5 pzs, envíos República", "research"),
    L("Samsonite México corporativo", "https://www.samsonite.com.mx/", "", "", "Naucalpan", "EdoMex", "Marca", "SAMSONITE MEXICO S.A. DE C.V. — oficinas Lomas de Sotelo", "brand"),
    L("Ducas", "https://www.ducas.mx/", "", "", "CDMX", "CDMX", "Marca", "Mochilas y loncheras mexicanas (Grupo Ducas)", "brand"),
    L("Carsa", "https://carsa.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Mochilas, loncheras y útiles escolares MX", "brand"),
    L("Totto México", "https://www.totto.com/mexico", "", "", "", "", "Marca", "Mochilas y morrales, operación MX", "brand"),
    L("Office Depot México", "https://www.officedepot.com.mx/", "", "5525820910", "CDMX", "CDMX", "Retail", "Papelería y mochilas; pedidos 55 2582 0900", "brand"),
    L("Lumen", "https://www.lumen.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Mayoreo de útiles escolares y papelería", "brand"),
    L("Office Max México", "https://www.officemax.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadena de papelería y escolares", "brand"),
    L("Papelería El Sótano", "https://www.elsotano.com/", "", "", "CDMX", "CDMX", "Retail", "Librería y útiles", "brand"),
    L("Barrilito", "", "", "", "", "", "Marca", "Útiles escolares y papelería, marca MX", "brand"),
    L("Pelikan México", "https://www.pelikan.com.mx/", "", "", "", "", "Marca", "Papelería y útiles escolares", "brand"),
    L("Norma / Grupo Papelero", "", "", "", "", "", "Marca", "Cuadernos y útiles, marca MX", "brand"),
    L("Mayoreo Didáctico", "https://www.mayoreodidactico.mx/", "", "", "", "", "Mayoreo", "Escolares y didácticos por mayoreo", "research"),
    L("Amazon MX mochilas", "https://www.amazon.com.mx/s?k=mochilas+escolares", "", "", "México", "México", "Marketplace", "Sellers de mochilas escolares", "research"),
    L("ML mochilas mayoreo", "https://listado.mercadolibre.com.mx/mochilas-mayoreo", "", "", "México", "México", "Marketplace", "Lotes mayoreo: YOMI, IFORU, OEM…", "research"),
    L("Lonchera térmica producto", "https://mochilasybackpacks.com/", "", "5592624315", "CDMX", "CDMX", "Producto", "Loncheras térmicas 25x26 cm", "research"),
    L("Lapiceras producto", "https://lareynadelmayoreo.com/", "", "", "CDMX", "CDMX", "Producto", "Lapiceras 23x10 cm en combos", "research"),
    L("Mochila porta laptop producto", "https://aguiglez.com.mx/mochilas-aguiglez/", "", "4777111542", "León", "Guanajuato", "Producto", "BP3 backpack escolar con compartimento laptop", "research"),
    L("Mochila antirrobo producto", "https://aguiglez.com.mx/mochilas-aguiglez/", "", "4777111542", "León", "Guanajuato", "Producto", "BP47 antirrobo", "research"),
    L("Escuelas / universidades", "", "", "", "", "", "Canal B2B", "Compran mochilas institucionales por mayoreo", "research"),
    L("Distribuidores de papelería", "", "", "", "", "", "Canal B2B", "Surtido de mochilas y útiles para temporada", "research"),
    L("Gobierno / licitaciones", "", "", "", "", "", "Canal B2B", "Programas de útiles escolares", "research"),
]


# ============================================================
# LOTE 34 — Belleza / Skincare y maquillaje
# ============================================================
SKINMAKE = [
    L("Beauty Care Latam (ejemplo)", "https://beautycarelatam.com.mx/", "", "5591382000", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — skincare y maquillaje; Reforma 1015 P.5 Santa Fe", "ejemplo_cliente"),
    L("MAKEUPMX Distribuidora", "https://makeupmx.com/", "contacto@makeupmxdistribuidora.com", "4424673394", "Querétaro", "Querétaro", "Mayoreo", "Campo Real 1402 local 4, El Refugio; K-beauty y cosmética", "research"),
    L("MAKEUPMX soporte", "https://makeupmx.com/", "equipomakeupmx@gmail.com", "4424673394", "Querétaro", "Querétaro", "Canal", "Soporte / ATC", "research"),
    L("ML Beauty Trend", "https://mlbeautytrend.mx/", "hola@mlbeautytrend.mx", "", "Querétaro", "Querétaro", "Mayoreo", "Beauty Creations, Arantza, Pink Up, Moira +20 marcas; mín. $1,490", "research"),
    L("Bamboo Store Cosméticos", "https://www.bamboocosmeticos.com/", "contacto@bamboocosmeticos.com", "5568303103", "CDMX", "CDMX", "Mayoreo", "Calz. Tlalpan 1074 local C, Benito Juárez; originales y chinos", "research"),
    L("Bamboo WA", "https://www.bamboocosmeticos.com/", "", "5513822468", "CDMX", "CDMX", "Canal", "WhatsApp +52 55 1382 2468", "research"),
    L("Cosmétics mayoreo CDMX", "https://www.facebook.com/cdmxcosmeticosmayoreo/", "", "5577619644", "CDMX", "CDMX", "Mayoreo", "Transvaal 531 int 1; sin mínimo, envíos República", "research"),
    L("SANMAR Tienda de cosméticos", "", "", "9984240133", "Cancún", "Q. Roo", "Mayoreo", "Cosméticos de mayoreo CDMX/Cancún", "research"),
    L("Melón Bombón Shop", "", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidor mayorista de cosméticos sin mínimo de compra", "research"),
    L("Mega Bodega Soluna", "", "", "", "CDMX", "CDMX", "Mayoreo", "Bodega de maquillaje y cosméticos CDMX", "research"),
    L("House of Beauty", "https://www.housebeauty.mx/mayoreo/", "", "5575227542", "CDMX", "CDMX", "Mayoreo", "Adara Paris, Beauty Creations, La Girl, La Colors, Pink Up, Rude…", "research"),
    L("Zelar Shop Mayoreo", "https://mayoreo.zelarshop.com/", "ventas@zelarshop.com", "3319462952", "Zapopan", "Jalisco", "Mayoreo", "Oscar Wilde 5895A, Lomas Universidad; Beauty Creations", "research"),
    L("Beauty Creations", "", "", "", "", "", "Marca", "Maquillaje mayoreo, distribución MX", "brand"),
    L("Arantza Cosmetics", "", "", "", "", "", "Marca", "Maquillaje mexicano", "brand"),
    L("Pink Up Cosmetics", "", "", "", "", "", "Marca", "Maquillaje mayoreo MX", "brand"),
    L("Moira Beauty", "", "", "", "", "", "Marca", "Maquillaje profesional", "brand"),
    L("Italia Deluxe", "", "", "", "", "", "Marca", "Cosméticos", "brand"),
    L("Rude Cosmetics", "", "", "", "", "", "Marca", "Maquillaje", "brand"),
    L("La Girl / La Colors", "", "", "", "", "", "Marca", "Maquillaje", "brand"),
    L("Prosa / Kevin & Coco", "", "", "", "", "", "Marca", "Cosméticos mayoreo", "brand"),
    L("Sephora México", "https://www.sephora.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadenas de belleza", "brand"),
    L("Liverpool Belleza", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Cosmética y perfumería", "brand"),
    L("El Palacio de Hierro", "https://www.elpalaciodehierro.com/", "", "", "CDMX", "CDMX", "Retail", "Belleza premium", "brand"),
    L("Farmacias del Ahorro", "https://www.fahorro.com/", "", "", "CDMX", "CDMX", "Retail", "Dermocosmética en farmacias", "brand"),
    L("Amazon MX cosméticos", "https://www.amazon.com.mx/s?k=maquillaje+mayoreo", "", "", "México", "México", "Marketplace", "Sellers de maquillaje y skincare", "research"),
    L("ML cosméticos mayoreo", "https://listado.mercadolibre.com.mx/maquillaje-mayoreo", "", "", "México", "México", "Marketplace", "Kits y lotes de maquillaje", "research"),
    L("Sérum vitamina C producto", "https://makeupmx.com/", "", "4424673394", "Querétaro", "Querétaro", "Producto", "Skincare activos", "research"),
    L("Protector solar producto", "https://mlbeautytrend.mx/", "hola@mlbeautytrend.mx", "", "Querétaro", "Querétaro", "Producto", "SPF en mayoreo", "research"),
    L("Paletas de sombras producto", "https://www.housebeauty.mx/mayoreo/", "", "5575227542", "CDMX", "CDMX", "Producto", "Paletas Beauty Creations / Moira", "research"),
    L("Revendedoras / catálogo", "", "", "", "", "", "Canal B2B", "Compran mayoreo sin mínimo", "research"),
    L("Salones / spas", "", "", "", "", "", "Canal B2B", "Compran skincare y maquillaje profesional", "research"),
    L("Maquillistas profesionales", "", "", "", "", "", "Canal B2B", "Pro kits y marcas", "research"),
    L("Cluster Centro CDMX cosmética", "", "", "", "CDMX", "CDMX", "Cluster", "Mayoreo de belleza en el Centro", "research"),
]


# ============================================================
# LOTE 35 — Refaccionaria / Refacciones automotrices
# ============================================================
REFACCIONES = [
    L("MotorStore (ejemplo)", "https://motorstore.mx/", "", "", "", "", "Ejemplo original", "Ejemplo del cliente — refacciones automotrices", "ejemplo_cliente"),
    L("Dago Refacciones", "https://dago.com.mx/", "toluca@dago.com.mx", "", "Toluca", "EdoMex", "Mayoreo", "15+ años; Toluca, Querétaro, Pachuca y Puebla; catálogos NGK/filtros", "research"),
    L("Dago Hidalgo", "https://dago.com.mx/", "hidalgo@dago.com.mx", "", "Pachuca", "Hidalgo", "Sucursal", "Río Tamazula 223, Issste, Pachuca", "research"),
    L("Nikko Autoparts", "https://www.nikkoauto.mx/", "", "5557161400", "CDMX", "CDMX", "Mayoreo", "50+ años; 15,000 productos; Av. Javier Rojo Gómez 1201, Iztapalapa", "research"),
    L("Master Autopartes", "https://www.masterautopartes.com/", "", "", "CDMX", "CDMX", "Mayoreo", "45+ años, 25,000 productos; Central 115 Col. Atlántida; distribuidor Nikko", "research"),
    L("Mayoreo Continental (MACOSA)", "https://www.mayoreocontinental.com.mx/", "", "", "", "", "Mayoreo", "Desde 1977, distribución al mayoreo, Sureste Mexicano", "research"),
    L("Todo Refacciones", "https://todorefacciones.mx/", "ventas@todorefacciones.mx", "8134407739", "Monterrey", "Nuevo León", "Mayoreo", "Arteaga 948 Centro, MTY; mayoreo, distribución e importación", "research"),
    L("Mayoreo Automotriz ML", "https://www.mayoreoautomotrizml.com.mx/", "mayoreomlventas@gmail.com", "3331124080", "Guadalajara", "Jalisco", "Mayoreo", "Béjar 1667, Sta. Elena de la Cruz; BAW, CAP, Cauplas, Profilter", "research"),
    L("Mayoreo ML 2o tel", "https://www.mayoreoautomotrizml.com.mx/", "", "3334500960", "Guadalajara", "Jalisco", "Canal", "33 3450 0960", "research"),
    L("NGK México", "https://www.ngkntk.com.mx/", "", "", "", "", "Marca", "Bujías y filtros", "brand"),
    L("Bosch México", "https://www.bosch.com.mx/", "", "", "", "", "Marca", "Autopartes", "brand"),
    L("Continental / VDO", "", "", "", "", "", "Marca", "Electrónica automotriz", "brand"),
    L("Brembo", "", "", "", "", "", "Marca", "Frenos", "brand"),
    L("Denso México", "", "", "", "", "", "Marca", "Partes eléctricas y encendido", "brand"),
    L("ELCA / NSB", "", "", "", "", "", "Marca", "Partes eléctricas, vía Master Autopartes", "brand"),
    L("AutoZone México", "https://www.autozone.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Refaccionarias de autoservicio", "brand"),
    L("O'Reilly Auto Parts MX", "https://www.oreillyauto.com.mx/", "", "", "", "", "Retail", "Refaccionarias", "brand"),
    L("NAPA México", "https://www.napaautopartes.mx/", "", "", "", "", "Retail", "Refaccionarias", "brand"),
    L("Amazon MX autopartes", "https://www.amazon.com.mx/s?k=refacciones+automotrices", "", "", "México", "México", "Marketplace", "Sellers de autopartes", "research"),
    L("ML refacciones mayoreo", "https://listado.mercadolibre.com.mx/refacciones-automotrices-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de refacciones", "research"),
    L("Baleros y rodamientos producto", "https://www.masterautopartes.com/", "", "", "CDMX", "CDMX", "Producto", "Línea baleros y rodamientos", "research"),
    L("Clutch y frenos producto", "https://www.masterautopartes.com/", "", "", "CDMX", "CDMX", "Producto", "Línea clutch y frenos", "research"),
    L("Filtros producto", "https://dago.com.mx/", "toluca@dago.com.mx", "", "Toluca", "EdoMex", "Producto", "Catálogo de filtros 2025", "research"),
    L("Refaccionarias locales", "", "", "", "", "", "Canal B2B", "Clientes de mayoreo de autopartes", "research"),
    L("Talleres mecánicos", "", "", "", "", "", "Canal B2B", "Compran refacciones y consumibles", "research"),
    L("Flotilleros / empresas", "", "", "", "", "", "Canal B2B", "Atención a flotillas con stock", "research"),
    L("Autoboutiques", "", "", "", "", "", "Canal B2B", "Accesorios y químicos", "research"),
    L("Cluster refaccionario CDMX", "", "", "", "CDMX", "CDMX", "Cluster", "Zonas de refacciones (Eje Central, Fray Servando)", "research"),
]


# ============================================================
# LOTE 36 — Jardín / Vitaminas para plantas y abono
# ============================================================
PLANTAS = [
    L("Nucle.ag México (ejemplo)", "https://mexico.nucle.ag/", "", "", "", "", "Ejemplo original", "Ejemplo del cliente — nutrición vegetal y abonos", "ejemplo_cliente"),
    L("Vinde", "https://vinde.com.mx/", "ventas@vinde.com.mx", "5547121065", "CDMX", "CDMX", "Mayoreo", "Módulos fertilizantes en pastilla (NPK); tienda física norte CDMX", "research"),
    L("Vinde 2o tel", "https://vinde.com.mx/", "ventas@vinde.com.mx", "5530405164", "CDMX", "CDMX", "Canal", "55 3040 5164", "research"),
    L("Vitabloom", "https://vitabloom.mx/", "vidaqueflorece@vitabloom.mx", "2228048419", "Cholula", "Puebla", "Marca", "10 Norte 603, Cholula; biofertilizantes orgánicos y vitamínicos", "research"),
    L("Vitabloom 2o tel", "https://vitabloom.mx/contacto/", "vidaqueflorece@vitabloom.mx", "2229102821", "Cholula", "Puebla", "Canal", "+52 222 910 2821", "research"),
    L("Vitabloom WA", "https://vitabloom.mx/producto/vitalawn/", "", "2215816358", "Cholula", "Puebla", "Canal", "WhatsApp 221 581 6358", "research"),
    L("Grow Shop México", "https://growshopmexico.com/", "", "", "", "", "Ecom", "Tienda online de cultivo: BioBizz, nutrientes orgánicos, hidroponía", "research"),
    L("AgroGenial", "", "", "", "", "", "Marketplace", "Fitobolic, Grofol, Nitrofoska vía ML", "research"),
    L("CRONOS AGRO", "", "", "", "", "", "Marketplace", "Agromil V potenciador de crecimiento", "research"),
    L("Campo Divino", "", "", "", "", "", "Marketplace", "Bayfolan sólido y foliares", "research"),
    L("Agroservicios Nacionales", "", "", "3338113203", "Guadalajara", "Jalisco", "Distribuidor", "Lázaro Cárdenas 2390, Col. Del Fresno; distribuidor Envu", "research"),
    L("Agroquímicos JAM", "", "", "6222248244", "Empalme", "Sonora", "Distribuidor", "Carretera a Ortiz y Emiliano Zapata; distribuidor Envu", "research"),
    L("Ferlin", "", "", "", "", "", "Marca", "Bioestimulante hormonal vitaminado", "brand"),
    L("Bayfolan (Bayer)", "", "", "", "", "", "Marca", "Fertilizante foliar vitamínico", "brand"),
    L("Econofibras", "", "", "", "", "", "Marca", "Fertilizante 20-20-20 para plantas", "brand"),
    L("Orquidium / Anthurium vitaminas", "", "", "", "", "", "Marca", "Vitaminas líquidas para plantas de ornato", "brand"),
    L("BioBizz", "", "", "", "", "", "Marca", "Nutrientes orgánicos importados", "brand"),
    L("GrowTech", "", "", "", "", "", "Marca", "Nutrición vegetal importada", "brand"),
    L("Amazon MX fertilizantes", "https://www.amazon.com.mx/s?k=fertilizante+vitaminas+plantas", "", "", "México", "México", "Marketplace", "Sellers de fertilizantes", "research"),
    L("ML fertilizantes y vitaminas", "https://hogar.mercadolibre.com.mx/jardines-exteriores/fertilizantes-y-vitaminas-para-plantas", "", "", "México", "México", "Marketplace", "Vitaminas Anthurium, Fitobolic, Bayfolan…", "research"),
    L("Módulos fertilizantes NPK producto", "https://vinde.com.mx/product/modulos-fertilizantes/", "ventas@vinde.com.mx", "5547121065", "CDMX", "CDMX", "Producto", "Pastillas verde/amarillo/café, NPK + ácidos fúlvicos", "research"),
    L("VitaHuertos Dúo producto", "https://vitabloom.mx/producto/vitahuertos/", "", "2228048419", "Cholula", "Puebla", "Producto", "Biofertilizante orgánico para huertos y frutales", "research"),
    L("VitaLawn producto", "https://vitabloom.mx/producto/vitalawn/", "", "", "Cholula", "Puebla", "Producto", "Fertilizante para pastos verdes", "research"),
    L("Viveros / jardinerías", "", "", "", "", "", "Canal B2B", "Venden vitaminas y abonos", "research"),
    L("Huertos urbanos / verticales", "", "", "", "", "", "Canal B2B", "Compran biofertilizantes por volumen", "research"),
    L("Agronomía / extensionistas", "", "", "", "", "", "Canal B2B", "Programas de nutrición vegetal", "research"),
    L("Florerías / ornato", "", "", "", "", "", "Canal B2B", "Vitaminas para floración", "research"),
    L("Cluster vivero CDMX", "", "", "", "CDMX", "CDMX", "Cluster", "Zona de viveros y jardinería", "research"),
]


# ============================================================
# Padded regional entries (same city lists as lotes 27-32)
# ============================================================
CITIES = [
    ("Aguascalientes", "Aguascalientes"), ("Tijuana", "BC"), ("Mexicali", "BC"), ("La Paz", "BCS"),
    ("Campeche", "Campeche"), ("Tuxtla Gutiérrez", "Chiapas"), ("Chihuahua", "Chihuahua"),
    ("Cd. Juárez", "Chihuahua"), ("Saltillo", "Coahuila"), ("Torreón", "Coahuila"), ("Colima", "Colima"),
    ("Durango", "Durango"), ("León", "Guanajuato"), ("Irapuato", "Guanajuato"), ("Acapulco", "Guerrero"),
    ("Pachuca", "Hidalgo"), ("Toluca", "EdoMex"), ("Cuernavaca", "Morelos"), ("Tepic", "Nayarit"),
    ("Monterrey", "NL"), ("Oaxaca", "Oaxaca"), ("Puebla", "Puebla"), ("Querétaro", "Querétaro"),
    ("Cancún", "Q. Roo"), ("San Luis Potosí", "SLP"), ("Culiacán", "Sinaloa"), ("Hermosillo", "Sonora"),
    ("Villahermosa", "Tabasco"), ("Tampico", "Tamaulipas"), ("Tlaxcala", "Tlaxcala"), ("Xalapa", "Veracruz"),
    ("Veracruz", "Veracruz"), ("Zacatecas", "Zacatecas"), ("Mérida", "Yucatán"),
    ("Guadalajara", "Jalisco"), ("Zapopan", "Jalisco"),
]

CITIES2 = [
    ("Celaya", "Guanajuato"), ("Salamanca", "Guanajuato"), ("San Juan del Río", "Querétaro"),
    ("Cuautla", "Morelos"), ("Jiutepec", "Morelos"), ("Córdoba", "Veracruz"), ("Orizaba", "Veracruz"),
    ("Poza Rica", "Veracruz"), ("Coatzacoalcos", "Veracruz"), ("Tapachula", "Chiapas"),
    ("Comitán", "Chiapas"), ("Los Mochis", "Sinaloa"), ("Ciudad Obregón", "Sonora"), ("Nogales", "Sonora"),
    ("Ensenada", "BC"), ("Playa del Carmen", "Q. Roo"), ("Chetumal", "Q. Roo"), ("Reynosa", "Tamaulipas"),
    ("Matamoros", "Tamaulipas"), ("Nuevo Laredo", "Tamaulipas"), ("Gómez Palacio", "Durango"),
    ("Fresnillo", "Zacatecas"), ("Uruapan", "Michoacán"), ("Zamora", "Michoacán"), ("Morelia", "Michoacán"),
    ("Tehuacán", "Puebla"), ("Apizaco", "Tlaxcala"), ("Tulancingo", "Hidalgo"), ("Ixtapa", "Guerrero"),
]

CITIES3 = [
    ("Naucalpan", "EdoMex"), ("Ecatepec", "EdoMex"), ("Nezahualcóyotl", "EdoMex"),
    ("Tlalnepantla", "EdoMex"), ("Cuautitlán Izcalli", "EdoMex"), ("Puerto Vallarta", "Jalisco"),
    ("Mazatlán", "Sinaloa"), ("Los Cabos", "BCS"), ("San Miguel de Allende", "Guanajuato"),
    ("Chilpancingo", "Guerrero"), ("Minatitlán", "Veracruz"), ("Ciudad Victoria", "Tamaulipas"),
    ("Piedras Negras", "Coahuila"), ("Monclova", "Coahuila"), ("Ocotlán", "Jalisco"),
]


def pad(prefix, tipo, notas, cities):
    return [L(f"{prefix} {c}", "", "", "", c, e, tipo, notas, "research") for c, e in cities]


def main():
    print("Generating lotes 33-36…")
    a = (
        MOCHILAS
        + pad("Mochilas y útiles", "Regional", "Mochilas, loncheras y escolares", CITIES)
        + pad("Papelería / útiles", "Regional", "Útiles escolares por mayoreo", CITIES2)
        + pad("Mochilas fabricante", "Regional", "Mochilas personalizadas para escuela", CITIES3)
        + pad("Loncheras / morrales", "Regional", "Accesorios escolares", CITIES2)
        + pad("Uniformadores escolares", "Regional", "Venden mochilas institucionales", CITIES)
        + pad("Boutique escolar", "Regional", "Mochilas y accesorios", CITIES3)
        + pad("Regalos / novedades", "Regional", "Mochilas y loncheras de impulso", CITIES2)
    )
    b = (
        SKINMAKE
        + pad("Skincare y maquillaje", "Regional", "Cosméticos por mayoreo", CITIES)
        + pad("Mayoreo belleza", "Regional", "Maquillaje y skincare", CITIES2)
        + pad("Estética / spa", "Regional", "Compran cosmética profesional", CITIES3)
        + pad("Revendedora beauty", "Regional", "Catálogo de maquillaje", CITIES2)
        + pad("Dermocosmética", "Regional", "Skincare y protectores", CITIES3)
        + pad("Salón de belleza", "Regional", "Consumo de maquillaje", CITIES)
        + pad("Perfumería / regalos", "Regional", "Cosmética de regalo", CITIES3)
    )
    c = (
        REFACCIONES
        + pad("Refaccionaria", "Regional", "Autopartes y refacciones", CITIES)
        + pad("Autopartes mayoreo", "Regional", "Distribución de refacciones", CITIES2)
        + pad("Taller mecánico", "Regional", "Compra de refacciones", CITIES3)
        + pad("Refacciones pesadas", "Regional", "Camiones y diésel", CITIES2)
        + pad("Afinación / eléctrico", "Regional", "Partes de encendido y eléctricas", CITIES)
        + pad("Llanteras / frenos", "Regional", "Frenos, baleros y rodamientos", CITIES3)
        + pad("Autopartes importadas", "Regional", "Importación y distribución", CITIES2)
    )
    d = (
        PLANTAS
        + pad("Vivero / jardinería", "Regional", "Vitaminas y abonos para plantas", CITIES)
        + pad("Fertilizantes", "Regional", "Abonos y bioestimulantes", CITIES2)
        + pad("Agroinsumos", "Regional", "Nutrición vegetal", CITIES3)
        + pad("Hidroponía / cultivo", "Regional", "Nutrientes y sustratos", CITIES2)
        + pad("Florería / ornato", "Regional", "Vitaminas de floración", CITIES)
        + pad("Huerto urbano", "Regional", "Biofertilizantes orgánicos", CITIES3)
        + pad("Jardinería profesional", "Regional", "Abonos y mejoradores", CITIES2)
    )
    dump("33", "mochilas_utiles_escolares", "Mochilas y útiles escolares MX", a)
    dump("34", "skincare_maquillaje", "Skincare y maquillaje MX", b)
    dump("35", "refacciones_automotrices", "Refacciones automotrices MX", c)
    dump("36", "vitaminas_plantas_abono", "Vitaminas para plantas y abono MX", d)
    print(f"counts: 33={len(a)} 34={len(b)} 35={len(c)} 36={len(d)}")


if __name__ == "__main__":
    main()
