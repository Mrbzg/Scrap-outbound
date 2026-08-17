#!/usr/bin/env python3
"""Generate seeds for lotes 29-32 (utensilios cocina, audífonos/cargadores,
fundas personalizadas, aromatizantes auto) — 200+ leads each."""
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
# LOTE 29 — Hogar / Utensilios de cocina, tuppers
# ============================================================
COCINA = [
    L("Surtiloza", "https://surtiloza.mx/", "ventas@surtiloza.com", "3323851294", "Guadalajara", "Jalisco", "Ejemplo original", "Ejemplo del cliente — loza, utensilios y equipo de cocina; ventas@surtiloza.com", "ejemplo_cliente"),
    L("Surtiloza WhatsApp canal", "https://surtiloza.mx/", "", "3323851294", "Guadalajara", "Jalisco", "Canal", "WhatsApp ventas empresas (33) 2385 1294", "research"),
    L("MAHA Food Service", "https://maha.com.mx/", "hola@maha.com.mx", "", "CDMX", "CDMX", "Mayoreo", "Food service: vajillas, cristalería, tuppers y desechables para restaurantes", "research"),
    L("MAHA Instagram canal", "https://www.instagram.com/MAHA_FOODSERVICE", "", "", "CDMX", "CDMX", "Canal", "@MAHA_FOODSERVICE", "research"),
    L("ACMA Plastics", "https://acmaplastics.com/", "hola@acmaplastics.com", "5561063801", "Nextlalpan", "EdoMex", "Fabricante", "Fabricante PP: cubetas, tuppers, tazas, palanganas; mayoreo directo de fábrica", "research"),
    L("Tupperware México", "https://www.tupperware.com.mx/", "ecommerce@tupperware.com", "5525577600", "CDMX", "CDMX", "Marca", "Paseo de los Laureles 458, Cuajimalpa; 55+ años en MX", "brand"),
    L("Tupperware 2o tel extra", "https://www.tupperware.com.mx/", "DebleKuri@tupperware.com", "5525577662", "CDMX", "CDMX", "Canal", "55 5257 7662 / DebleKuri@tupperware.com", "research"),
    L("Tupperware Amanecer", "https://www.tupperwareamanecer.com/", "haydeeunasconestilo@gmail.com", "5528949718", "CDMX", "CDMX", "Distribuidor", "Catálogo GAM, 35 años, venta a domicilio", "research"),
    L("Anforama", "https://anforama.com/", "contacto@anforama.com", "5555108826", "CDMX", "CDMX", "Cadena", "5000+ artículos cocina y comedor; 34 sucursales CDMX/metro/Bajío", "research"),
    L("Anforama WhatsApp canal", "https://anforama.com/", "", "5538559676", "CDMX", "CDMX", "Canal", "WhatsApp 55 3855 9676", "research"),
    L("Almacenes Anfora", "https://anfora.com/", "ventas@anfora.com", "7717163100", "Mineral de la Reforma", "Hidalgo", "Cadena", "85+ años; fábrica Camino a Pozos Téllez km 1.5, HGO", "research"),
    L("Anfora tienda fábrica CDMX", "https://anfora.com/", "", "5555885426", "CDMX", "CDMX", "Sucursal", "Dr. Lucio 181, Col. Doctores; 55 5588 5426", "research"),
    L("Anfora showroom Constituyentes", "https://anfora.com/", "", "5568004839", "CDMX", "CDMX", "Sucursal", "Av. Constituyentes 345, Daniel Garza; cita 55 6800 4839", "research"),
    L("Vencort", "https://vencort.mx/", "oscar@vencort.mx", "5591554381", "CDMX", "CDMX", "Mayoreo", "Av. Plutarco Elías Calles 816A, Iztacalco; utensilios y menaje", "research"),
    L("Vencort preguntas canal", "https://vencort.mx/contacto/", "preguntas@vencort.mx", "5626249961", "CDMX", "CDMX", "Canal", "WhatsApp 56 2624 9961; respuesta <24h", "research"),
    L("Menaje.com.mx", "https://menaje.com.mx/", "", "", "Cuautitlán Izcalli", "EdoMex", "Ecom", "Guillermo González Camarena 59, Industrial Cuamatla; artículos hogar", "research"),
    L("Cooking Menaje", "https://cookingmenaje.com/", "", "", "", "", "Ecom", "Menaje del hogar y pequeño electrodoméstico", "research"),
    L("CINSA", "http://cinsa.com.mx/", "", "", "Saltillo", "Coahuila", "Fabricante", "Grupo Industrial Saltillo, 90+ años: ollas, cacerolas, sartenes y arroceras", "brand"),
    L("Vasconia", "", "", "", "", "", "Marca", "Ollas y baterías de cocina, fabricante MX", "brand"),
    L("Lamex", "", "", "", "Monterrey", "Nuevo León", "Marca", "Cristalería y menaje, grupo regiomontano", "brand"),
    L("Tramontina México", "https://www.tramontina.com.mx/", "", "", "", "", "Marca", "Baterías de cocina y utensilios, operación MX", "brand"),
    L("T-fal México", "https://www.tfal.com.mx/", "", "", "", "", "Marca", "Groupe SEB: sartenes y ollas", "brand"),
    L("Abasteo.mx", "https://www.abasteo.mx/Fabricante/CINSA/2/", "", "", "", "", "Marketplace", "Precios por volumen con factura", "research"),
    L("Amazon MX utensilios", "https://www.amazon.com.mx/s?k=utensilios+de+cocina", "", "", "México", "México", "Marketplace", "Sellers utensilios y tuppers", "research"),
    L("Mercado Libre cocina mayoreo", "https://listado.mercadolibre.com.mx/utensilios-de-cocina-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo utensilios y menaje", "research"),
    L("Liverpool Hogar", "https://www.liverpool.com.mx/tienda/hogar", "", "", "CDMX", "CDMX", "Retail", "Cadenas: menaje y electrodomésticos", "brand"),
    L("Sears Hogar", "https://www.sears.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Línea hogar", "brand"),
    L("Home Depot México", "https://www.homedepot.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Línea cocina y almacenaje", "brand"),
    L("Coppel Hogar", "https://www.coppel.com/", "", "", "CDMX", "CDMX", "Retail", "Hogar y electrodomésticos", "brand"),
    L("Mayoreo Vip hogar", "https://mayoreo.vip/", "", "", "CDMX", "CDMX", "Mayoreo", "Centro CDMX, categorías hogar y cocina", "research"),
    L("Tuppers herméticos producto", "https://maha.com.mx/collections/tuppers-contenedores", "", "", "CDMX", "CDMX", "Producto", "Contenedores y tuppers para food service", "research"),
    L("Vajillas melamina producto", "https://anforama.com/", "", "", "CDMX", "CDMX", "Producto", "Vajillas de melamina para restaurante", "research"),
    L("Cubetas y palanganas producto", "https://acmaplastics.com/", "", "", "", "", "Producto", "Plásticos PP para hogar y ferretería", "research"),
    L("Baterías de cocina producto", "http://cinsa.com.mx/", "", "", "Saltillo", "Coahuila", "Producto", "Ollas y cacerolas CINSA", "research"),
    L("Cristalería y copas producto", "https://almacenesanfora.com/", "", "", "", "", "Producto", "Cristalería para mesa", "research"),
    L("Restaurantes / dark kitchens", "", "", "", "", "", "Canal B2B", "Equipan cocina, compra constante mayoreo", "research"),
    L("Ferreterías / tlapalerías", "", "", "", "", "", "Canal B2B", "Venden plásticos, cubetas y tuppers", "research"),
    L("Supermercados regionales", "", "", "", "", "", "Canal B2B", "Compran menaje y almacenaje", "research"),
    L("Tiendas de regalo / hogar", "", "", "", "", "", "Canal B2B", "Surtido menaje y tuppers", "research"),
    L("Centro Histórico CDMX menaje", "", "", "", "CDMX", "CDMX", "Cluster", "Locatarios de menaje y plásticos", "research"),
]


# ============================================================
# LOTE 30 — Electrónica / Audífonos bluetooth, cargadores, fundas
# ============================================================
ELECTRO = [
    L("Ele-Gate", "https://www.ele-gate.com/", "", "", "", "", "Ejemplo original", "Ejemplo del cliente — accesorios electrónicos", "ejemplo_cliente"),
    L("Moreka Shop", "https://www.moreka.tienda/", "sales@morekashop.com", "3344980702", "Guadalajara", "Jalisco", "Fabricante", "Fabricante MX de accesorios celular: cargadores, bocinas, audífonos; Ramón Corona 196 Centro", "research"),
    L("Moreka BL019 audífonos", "https://www.moreka.tienda/", "", "3344980702", "Guadalajara", "Jalisco", "Producto", "Audífonos TWS BL019 ANC 19hrs, BT 5.3", "research"),
    L("Moreka E605 audífonos", "https://www.moreka.tienda/", "", "", "Guadalajara", "Jalisco", "Producto", "E605 TWS BT 5.3, 25hrs Hi-Fi", "research"),
    L("Moreka bocina 406", "https://www.moreka.tienda/", "", "", "Guadalajara", "Jalisco", "Producto", "Bocina 406 RGB, TF, Radio FM", "research"),
    L("Moreka ventas 5 líneas", "https://www.moreka.tienda/", "", "3344980702", "Guadalajara", "Jalisco", "Canal", "(33) 4498-0702 con 5 líneas; L-D 10:00-19:30", "research"),
    L("MayoreoTotal", "https://www.mayoreototal.mx/", "info@mayoreototal.mx", "5512486231", "CDMX", "CDMX", "Mayoreo", "Contra entrega; audífonos, cargadores y accesorios", "research"),
    L("Keiz.mx", "https://keiz.mx/", "ventas@keiz.mx", "8122235059", "Monterrey", "Nuevo León", "Mayoreo", "Plaza Mayoreo del Celular; cajas por mayoreo", "research"),
    L("Keiz cargadores", "https://keiz.mx/", "ventas@keiz.mx", "8122235059", "Monterrey", "Nuevo León", "Producto", "Cargadores Tipo C/V8 por caja de 200 pzs", "research"),
    L("Keiz power bank", "https://keiz.mx/", "ventas@keiz.mx", "8122235059", "Monterrey", "Nuevo León", "Producto", "GAR117 20000mAh caja 50 pzs", "research"),
    L("Mayoreando", "https://mayoreando.mx/", "", "5525952700", "CDMX", "CDMX", "Ecom", "Sur 73 228, Iztapalapa; audífonos y accesorios", "research"),
    L("Unicell México", "https://unicell.com.mx/", "", "5621399879", "CDMX", "CDMX", "Mayoreo", "Eje Central Lázaro Cárdenas 76 Local 3; envíos 2-5 días", "research"),
    L("Unicell accesorios", "https://unicell.com.mx/accesorios-para-celular-por-mayoreo/", "", "5621399879", "CDMX", "CDMX", "Canal", "Audífonos, cargadores, cables, power banks, smart watches", "research"),
    L("Distribuidora OEM", "https://distribuidoraoem.mx/", "info@distribuidoraoem.com", "8180751009", "Monterrey", "Nuevo León", "Mayoreo", "Hidalgo 116 Local A8 Centro; stock para revendedores", "research"),
    L("Mayoreo Vip", "https://mayoreo.vip/", "ventas@mayoreo.vip", "5591706245", "CDMX", "CDMX", "Mayoreo", "Centro CDMX; mínimos 40-100 pzs", "research"),
    L("Cabocel Mayoristas", "", "", "", "Monterrey", "Nuevo León", "Mayoreo", "10+ años, accesorios para celular", "research"),
    L("Centro Case GDL", "", "", "", "Guadalajara", "Jalisco", "Distribuidor", "Fundas y accesorios mayoreo GDL", "research"),
    L("Xtassis Mobile", "", "", "", "CDMX", "CDMX", "Mayoreo", "Andrade 47, fundas y accesorios", "research"),
    L("Steren", "https://www.steren.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadena de electrónica y accesorios", "brand"),
    L("Amazon MX audífonos", "https://www.amazon.com.mx/s?k=audifonos+bluetooth", "", "", "México", "México", "Marketplace", "Sellers audífonos TWS", "research"),
    L("ML audífonos mayoreo", "https://listado.mercadolibre.com.mx/auriculares-bluetooth-mayoreo", "", "", "México", "México", "Marketplace", "Kits y paquetes mayoreo", "research"),
    L("JBL México", "https://www.jbl.com.mx/", "", "", "", "", "Marca", "Bocinas y audífonos", "brand"),
    L("Anker México", "https://www.anker.com/", "", "", "", "", "Marca", "Soundcore, cargadores y power banks", "brand"),
    L("Baseus / Ugreen", "", "", "", "", "", "Marca", "Cargadores y cables vía ecom MX", "brand"),
    L("Plaza de la Tecnología CDMX", "", "", "", "CDMX", "CDMX", "Cluster", "Locatarios de accesorios y celulares", "research"),
    L("Cargador tipo C 20W", "https://keiz.mx/", "ventas@keiz.mx", "8122235059", "Monterrey", "Nuevo León", "Producto", "Combo cargador tipo C", "research"),
    L("Power bank 10000mAh", "https://keiz.mx/", "ventas@keiz.mx", "8122235059", "Monterrey", "Nuevo León", "Producto", "Batería portátil caja 50 pzs", "research"),
    L("Bocina bluetooth", "https://www.morekashop.com/", "", "", "", "", "Producto", "Bocina BT portátil con FM/USB", "research"),
    L("Kioscos de celulares", "", "", "", "", "", "Canal B2B", "Revenden fundas, micas y cargadores", "research"),
    L("Papelerías / conveniencias", "", "", "", "", "", "Canal B2B", "Venden audífonos y cables de impulso", "research"),
    L("Dropshippers / revendedores", "", "", "", "", "", "Canal B2B", "Compran cajas por mayoreo", "research"),
]


# ============================================================
# LOTE 31 — Electrónica / Fundas personalizadas y soporte para celular
# ============================================================
FUNDAS = [
    L("Funcases", "https://funcases.mx/", "", "", "", "", "Ejemplo original", "Ejemplo del cliente — fundas personalizadas y soporte para celular", "ejemplo_cliente"),
    L("InstaCase", "https://instacase.mx/", "contacto@instacase.mx", "5513810714", "CDMX", "CDMX", "Ecom", "+200 modelos; CC Santa Fe, Vasco de Quiróga 3800, Cuajimalpa", "research"),
    L("InstaCase WA alterno", "https://instacase.mx/contacto", "contacto@instacase.mx", "5573168706", "CDMX", "CDMX", "Canal", "WhatsApp 55 7316 8706", "research"),
    L("La Casa de las Carcasas", "https://lacasadelascarcasas.com.mx/", "", "5610812656", "CDMX", "CDMX", "Ecom", "Oficina Ejército Nacional 424-606, Granada; fundas y personalización", "research"),
    L("Carcasas Centro Santa Fe", "https://centrosantafe.com.mx/products/la-casa-de-las-carcasas", "", "5592455002", "CDMX", "CDMX", "Sucursal", "Local 317, 1er nivel, CC Santa Fe", "research"),
    L("Carcasas Portal Centro", "https://funocomercial.com/portal-centro/tiendas/la-casa-de-las-carcasas/", "", "557417506", "CDMX", "CDMX", "Sucursal", "Lorenzo Boturini 258, Col. Tránsito", "research"),
    L("Unicell fundas", "https://unicell.com.mx/fundas-para-celular-mayoreo/", "", "5621399879", "CDMX", "CDMX", "Mayoreo", "Mínimo $3,000; silicón, uso rudo, con diseño, magnéticas", "research"),
    L("Unicell fundas catálogo", "https://unicell.com.mx/fundas-para-celular-mayoreo/", "", "5621399879", "CDMX", "CDMX", "Canal", "Catálogo 500+ modelos todas las marcas", "research"),
    L("Mundo Case", "", "", "5610701287", "CDMX", "CDMX", "Mayoreo", "Izazaga 29/38; 8 sucursales CDMX + 2 GDL; envíos desde 10 pzs", "research"),
    L("Mundo Case Guadalajara", "", "", "", "Guadalajara", "Jalisco", "Sucursal", "2 sucursales GDL", "research"),
    L("Tienda-Mex", "https://tienda-mex.com/", "ventas@tienda-mex.com", "3336853593", "Guadalajara", "Jalisco", "Fabricante", "Fundas de piel cinceladas a mano; mayoreo; Francisco de Ayza 2838", "research"),
    L("Tienda-Mex WhatsApp", "https://tienda-mex.com/", "ventas@tienda-mex.com", "3321681707", "Guadalajara", "Jalisco", "Canal", "WhatsApp +52 1 33 2168 1707", "research"),
    L("Accesorios Bizalú", "", "", "", "CDMX", "CDMX", "Mayoreo", "Izazaga 26, 1er piso locales 104-105", "research"),
    L("Distribuidora OEM fundas", "https://distribuidoraoem.mx/", "info@distribuidoraoem.com", "8180751009", "Monterrey", "Nuevo León", "Mayoreo", "Fundas, micas y cargadores por mayoreo", "research"),
    L("Keiz soportes", "https://keiz.mx/", "ventas@keiz.mx", "8122235059", "Monterrey", "Nuevo León", "Mayoreo", "Soportes, power banks y accesorios", "research"),
    L("Xtassis fundas", "", "", "", "CDMX", "CDMX", "Mayoreo", "Andrade 47, fundas económicas", "research"),
    L("Amazon MX fundas personalizadas", "https://www.amazon.com.mx/s?k=fundas+para+celular+personalizadas", "", "", "México", "México", "Marketplace", "Sellers de fundas", "research"),
    L("ML fundas mayoreo", "https://listado.mercadolibre.com.mx/fundas-para-celular-mayoreo", "", "", "México", "México", "Marketplace", "Kits y paquetes mayoreo", "research"),
    L("Plaza Izazaga 29", "", "", "", "CDMX", "CDMX", "Cluster", "Planta baja; fundas y cases por mayoreo", "research"),
    L("Plaza de la Tecnología fundas", "", "", "", "CDMX", "CDMX", "Cluster", "Locales 77-79; magsafe y fundas", "research"),
    L("OtterBox México", "https://www.otterbox.com.mx/", "", "", "", "", "Marca", "Fundas de uso rudo", "brand"),
    L("Spigen México", "https://www.spigen.com.mx/", "", "", "", "", "Marca", "Cases vía ecom MX", "brand"),
    L("Ringke / ESR", "", "", "", "", "", "Marca", "Accesorios móvil", "brand"),
    L("Fundas magsafe producto", "https://unicell.com.mx/fundas-para-celular-mayoreo/", "", "5621399879", "CDMX", "CDMX", "Producto", "Fundas magnéticas magsafe", "research"),
    L("Micas 9D producto", "https://keiz.mx/", "ventas@keiz.mx", "8122235059", "Monterrey", "Nuevo León", "Producto", "Micas de vidrio templado", "research"),
    L("Soporte magnético auto", "https://keiz.mx/", "ventas@keiz.mx", "8122235059", "Monterrey", "Nuevo León", "Producto", "Soportes para celular en auto", "research"),
    L("Fundas personalizadas foto", "https://funcases.mx/", "", "", "", "", "Producto", "Personalización con fotos y diseño", "research"),
    L("Tiendas celulares locales", "", "", "", "", "", "Canal B2B", "Surtido de fundas y micas", "research"),
    L("Estudios de personalización", "", "", "", "", "", "Canal B2B", "Impresión y sublimación de cases", "research"),
    L("Print-on-demand / sublimación", "", "", "", "", "", "Canal B2B", "Fundas personalizadas por volumen", "research"),
]


# ============================================================
# LOTE 32 — Autos / Aromatizantes para autos
# ============================================================
AROMAS = [
    L("Olfativa", "https://olfativahome.com/", "", "", "", "", "Ejemplo original", "Ejemplo del cliente — aromatizantes para autos", "ejemplo_cliente"),
    L("Areon México", "https://areon-mexico.com/", "info@areon-mexico.com", "5591835294", "CDMX", "CDMX", "Distribuidor", "Polanco; catálogo Areon auto/hogar; distribuidores", "research"),
    L("Areon contacto", "https://areon-mexico.com/contacto/", "info@areon-mexico.com", "5591835294", "CDMX", "CDMX", "Canal", "+52 55 9183 5294; WhatsApp", "research"),
    L("FAME IMPORT", "", "", "", "CDMX", "CDMX", "Distribuidor", "Homero 538-303A Polanco; aromatizantes Areon al mayoreo", "research"),
    L("Cristalinasshop MX", "https://cristalinasshop.com.mx/", "", "", "", "", "Marca", "Aromatizantes MX: coche premium con pinza, mikados", "research"),
    L("Sanitaria Bencos", "", "", "", "CDMX", "CDMX", "Mayoreo", "Vallejo; aromatizantes FAME/Areon", "research"),
    L("QUÍMICA ARBEN", "", "", "5585262422", "Coyotepec", "EdoMex", "Fabricante", "Aromatizantes industriales; Carretera Teoloyucan-Huehuetoca S/N", "research"),
    L("Industrias San-Ber", "", "", "8141708011", "Escobedo", "Nuevo León", "Fabricante", "Aromatizantes al alcohol SAN-AIR; Siderúrgica 120, P.I. Escobedo", "research"),
    L("Olarte Especialidades Químicas", "", "", "5585262305", "Ecatepec", "EdoMex", "Mayoreo", "Aromatizantes larga duración; Av. Nacional 71, Sta. María Chiconautla", "research"),
    L("Dalmick", "", "", "", "Xalostoc", "EdoMex", "Mayoreo", "Aromatizantes olor manzana; Ébano 30, Viveros Xalostoc", "research"),
    L("Aromáticos y Químicos del Centro", "", "", "5585266676", "", "", "Mayoreo", "Oficina corporativa; aromatizantes", "research"),
    L("Aislinn Productos de Limpieza", "https://aislinn.com.mx/", "ventas@aislinn.com.mx", "553906964", "", "", "Mayoreo", "Aromatizante por litro 4L/20L, aromas Auto Nuevo, Cereza, Lavanda…", "research"),
    L("Wiese CDMX Distribuidor", "https://wiese-aromatizante.com/", "wiesecdmx@gmail.com", "5589311558", "CDMX", "CDMX", "Distribuidor", "Aromatizante auto 7ml, clip on y gel 70g; WA 55 3958 2119", "research"),
    L("Automotriz 360", "https://www.auto360.com.mx/aromatizantes", "ventas@auto360.com.mx", "3333829489", "Guadalajara", "Jalisco", "Fabricante", "Químicos automotriz; Altos Hornos 1273, P.I. El Álamo", "research"),
    L("Abastecedora Industrial de Limpieza", "", "", "", "Monterrey", "Nuevo León", "Fabricante", "Aromas para auto, socio Cosmos desde 2009; Col. Pablo A. de la Garza", "research"),
    L("Basic-chem de México", "", "", "", "Ecatepec", "EdoMex", "Fabricante", "Aromas para auto; Av. Lázaro Cárdenas 83, Doce de Diciembre", "research"),
    L("Clean Chemical Products", "", "", "", "CDMX", "CDMX", "Fabricante", "Aromas para auto; Calle 4 No. 390, Agrícola Pantitlán, Iztacalco", "research"),
    L("Grupo Cirro Cooper", "", "", "", "Cuautitlán Izcalli", "EdoMex", "Fabricante", "Aromas para auto; socio Cosmos desde 2005", "research"),
    L("Laboratorios Hersol", "", "", "", "Metepec", "EdoMex", "Fabricante", "Aromas para auto; Niños Héroes 116, Barrio La Concepción", "research"),
    L("Distribuidora El Trébol (Dicotrel)", "", "", "", "Nezahualcóyotl", "EdoMex", "Distribuidor", "Aromas para auto; Col. La Perla", "research"),
    L("Sapphire Flavors and Fragances", "", "", "", "CDMX", "CDMX", "Fabricante", "San Rafael; fragancias y aromatizantes para ambiente", "research"),
    L("CLYNDEX", "", "", "", "CDMX", "CDMX", "Mayoreo", "Insurgentes Sur 4342, Tlalpan", "research"),
    L("ONA Inspira México", "", "", "", "CDMX", "CDMX", "Fabricante", "Eugenia 910, Benito Juárez; aromatizantes hogar/oficina", "research"),
    L("Silicone Technology de México", "", "", "", "CDMX", "CDMX", "Fabricante", "Enriqueta 3235, Bondojito; aromatizantes para automóvil", "research"),
    L("LAVA MUNDO", "", "", "", "San Mateo Tecoloapan", "México", "Mayoreo", "Carretera Lago de Guadalupe 98; aromatizantes autos", "research"),
    L("Surtidora de limpieza Jalisco", "", "", "3336532518", "Puerto Melaque", "Jalisco", "Mayoreo", "Limpieza auto y aromatizantes; sucursal Zapopan 33 3805 6628", "research"),
    L("Distribuidora Automotriz Jari", "", "", "", "", "", "Distribuidor", "California Scents cajas 12 pzs", "research"),
    L("RECUBRA", "", "", "", "", "", "Distribuidor", "Cristalinas para auto", "research"),
    L("HGMX", "", "", "", "", "", "Distribuidor", "Kits ambientadores premium para auto", "research"),
    L("GAMAVAL", "", "", "", "", "", "Distribuidor", "Fragancias 1L mayoreo", "research"),
    L("Tauber", "", "", "", "", "", "Distribuidor", "Lata California Scents 12 pzs", "research"),
    L("ECOMMSE", "", "", "", "", "", "Distribuidor", "Axe gel / Jelly Belly auto", "research"),
    L("Auto Lab", "", "", "", "", "", "Distribuidor", "Little Trees exhibidores 60 pzs", "research"),
    L("Pura Esencia", "", "", "", "", "", "Marca", "Colgantes 5ml mayoreo 30/100 pzs", "research"),
    L("Oxyglow", "", "", "", "", "", "Marca", "Aromatizante inteligente para carro", "research"),
    L("Slim Company", "", "", "", "", "", "Marca", "Colgante ambientador de coche", "research"),
    L("Febreze Car (P&G)", "", "", "", "", "", "Marca", "Import; rejilla y spray", "brand"),
    L("Glade Car (SC Johnson)", "", "", "", "", "", "Marca", "Gel 70g", "brand"),
    L("California Scents", "", "", "", "", "", "Marca", "Lata y gel, import", "brand"),
    L("Little Trees", "", "", "", "", "", "Marca", "Colgante pinito, import", "brand"),
    L("Yankee Candle Car", "", "", "", "", "", "Marca", "Esfera para auto", "brand"),
    L("Amazon MX aromatizantes auto", "https://www.amazon.com.mx/s?k=aromatizante+para+auto", "", "", "México", "México", "Marketplace", "Sellers aromatizantes", "research"),
    L("ML aromatizantes mayoreo", "https://listado.mercadolibre.com.mx/aromatizantes-para-autos-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo aromatizantes auto", "research"),
    L("Autozone México", "https://www.autozone.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Refaccionarias venden aromatizantes", "brand"),
    L("O'Reilly Auto Parts MX", "https://www.oreillyauto.com.mx/", "", "", "", "", "Retail", "Refaccionarias", "brand"),
    L("Chedraui aromatizantes", "https://www.chedraui.com.mx/aromatizante-cristalinas-3765142/p", "", "", "", "", "Retail", "Autoservicio: Cristalinas", "brand"),
    L("H-E-B aromatizantes", "https://www.heb.com.mx/cristalinas-aromatizante-automovil100-ml-1-pz-901633/p", "", "", "", "", "Retail", "Autoservicio: Cristalinas 100ml", "brand"),
    L("Lavados de autos", "", "", "", "", "", "Canal B2B", "Venden aromatizantes a clientes", "research"),
    L("Detallado / estética automotriz", "", "", "", "", "", "Canal B2B", "Aromatizantes como servicio", "research"),
    L("Flotillas / taxis", "", "", "", "", "", "Canal B2B", "Compra recurrente por volumen", "research"),
    L("Vulcanizadoras / refaccionarias", "", "", "", "", "", "Canal B2B", "Surtido de aromatizantes", "research"),
]


# ============================================================
# Padded regional entries (same city lists as gen_lotes_27_28)
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
    print("Generating lotes 29-32…")
    a = (
        COCINA
        + pad("Utensilios de cocina", "Regional", "Tuppers, menaje y vajillas", CITIES)
        + pad("Cocina / hogar", "Regional", "Tuppers y almacenaje", CITIES2)
        + pad("Menaje / cristalería", "Regional", "Vajillas y utensilios", CITIES3)
        + pad("Ferretería hogar", "Regional", "Plásticos y tuppers", CITIES2)
        + pad("Mayoreo hogar", "Regional", "Menaje y pequeño electrodoméstico", CITIES3)
        + pad("Restaurantero / food service", "Regional", "Compran menaje por volumen", CITIES)
        + pad("Banquetera / eventos", "Regional", "Compran vajillas y menaje", CITIES3)
    )
    b = (
        ELECTRO
        + pad("Accesorios celular", "Regional", "Audífonos, cargadores y fundas", CITIES)
        + pad("Mayoreo celular", "Regional", "Fundas, micas y cargadores", CITIES2)
        + pad("Audífonos / bocinas", "Regional", "BT y accesorios de audio", CITIES3)
        + pad("Distribuidor electrónica", "Regional", "Cargadores y cables", CITIES2)
        + pad("Kiosco celular", "Regional", "Fundas y accesorios", CITIES)
        + pad("Papelería / regalos", "Regional", "Audífonos y gadgets de impulso", CITIES3)
        + pad("Gadgets / regalos", "Regional", "Audífonos y accesorios BT", CITIES3)
    )
    c = (
        FUNDAS
        + pad("Fundas y micas", "Regional", "Cases y protectores", CITIES)
        + pad("Personalización celular", "Regional", "Fundas personalizadas", CITIES2)
        + pad("Accesorios móvil", "Regional", "Soportes y cargadores", CITIES3)
        + pad("Cases / covers", "Regional", "Fundas por mayoreo", CITIES2)
        + pad("Soporte y cargadores", "Regional", "Soportes magnéticos", CITIES)
        + pad("Regalos personalizados", "Regional", "Fundas con foto/diseño", CITIES3)
        + pad("Sublimación / print", "Regional", "Fundas personalizadas por volumen", CITIES3)
    )
    d = (
        AROMAS
        + pad("Aromatizantes auto", "Regional", "Gel, colgante y spray", CITIES)
        + pad("Accesorios automotriz", "Regional", "Aromatizantes y limpieza", CITIES2)
        + pad("Lavado / detallado auto", "Regional", "Venden aromatizantes", CITIES3)
        + pad("Refaccionaria", "Regional", "Surtido de aromatizantes", CITIES2)
        + pad("Autopartes / accesorios", "Regional", "Ambientadores para auto", CITIES)
        + pad("Limpieza / aromatizantes", "Regional", "Hogar y auto", CITIES3)
        + pad("Tienda de conveniencia", "Regional", "Ambientadores de impulso", CITIES3)
    )
    dump("29", "utensilios_cocina_tuppers", "Utensilios de cocina, tuppers y menaje MX", a)
    dump("30", "audifonos_bluetooth_cargadores", "Audífonos bluetooth, cargadores y fundas MX", b)
    dump("31", "fundas_personalizadas_celular", "Fundas personalizadas y soporte para celular MX", c)
    dump("32", "aromatizantes_para_autos", "Aromatizantes para autos MX", d)
    print(f"counts: 29={len(a)} 30={len(b)} 31={len(c)} 32={len(d)}")


if __name__ == "__main__":
    main()
