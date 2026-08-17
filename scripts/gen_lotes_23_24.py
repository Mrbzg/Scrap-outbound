#!/usr/bin/env python3
"""Generate seeds for lotes 23 shampoo tinte and 24 hilos/estambre (200-300)."""
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


SHAMPOO = [
    L("MEIDU México", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Ejemplo original", "Ejemplo del cliente — shampoo tinte 3 en 1 cubre canas", "ejemplo_cliente"),
    L("MEIDU contacto extra", "https://www.meidu.com.mx/contacto/", "", "5511336665", "México", "México", "Canal", "Tienda online MX", "research"),
    L("MEIDU mirror extra", "https://www.meidumx.com/", "", "5511336665", "México", "México", "Ecom", "Puntos de venta / promo 2", "research"),
    L("Rizos Mexicanos", "https://www.rizosmexicanos.com/", "", "5514718602", "México", "México", "Marca D2C", "Shampoo sólido avena, rizos, sin sulfatos", "research"),
    L("Rizos Mexicanos sólido extra", "https://www.rizosmexicanos.com/product-page/shampoo-s%C3%B3lido-avena", "", "5514718602", "México", "México", "Producto", "50-60 lavadas, IPN/UNAM", "research"),
    L("Don Juan Beauty Supply", "https://donjuan.mx/", "contacto@donjuan.mx", "6621940726", "Hermosillo", "Sonora", "Mayoreo", "Keratina, cremas, ampolletas, L-S 9-17", "research"),
    L("Bam Boo Lifestyle", "https://www.bamboolifestyle.com.mx/", "onnearrss@gmail.com", "5579388337", "CDMX", "CDMX", "Marca eco", "Saratoga 904 Benito Juárez, shampoo sólido rizos", "research"),
    L("Bam Boo sólido extra", "https://onneageld.com.mx/products/shampoo-solido-artesanal-rizos-hidratados-80-g-bam-boo-lifestyle", "onnearrss@gmail.com", "5579388337", "CDMX", "CDMX", "Producto", "80 g rizos hidratados", "research"),
    L("AMAI MX", "https://amai.mx/", "", "", "México", "México", "Marca D2C", "Shampoo en barra anticaída / rizos / hidratación", "research"),
    L("AMAI trio extra", "https://amai.mx/products/shampoo-barra-hidratacion-anticaida-rizos", "", "", "México", "México", "Paquete", "Hecho artesanal MX", "research"),
    L("RIS.O.S.", "https://risos.com.mx/tienda/", "", "5564657515", "CDMX", "CDMX", "Marca rizos", "Mariano Escobedo 194 Miguel Hidalgo 11320", "research"),
    L("Jabones Artesanales Ordaz", "https://www.jabonesartesanalesordaz.net/", "ventas@jabonesartesanalesordaz.net", "5536169938", "CDMX", "CDMX", "Fabricante", "Avena 161 Granjas Esmeralda Iztapalapa, WA 5514966392", "research"),
    L("Jabones Ordaz WA extra", "https://www.jabonesartesanalesordaz.net/", "info@jabonesartesanalesordaz.net", "5514966392", "CDMX", "CDMX", "Canal WA", "L-V 9-17 S 9-13", "research"),
    L("Amoli jabones extra", "https://www.amoli.mx/collections/jabones-artesanales", "", "8115117942", "Monterrey", "NL", "Marca", "Jabones artesanales", "research"),
    L("MEIDU Black extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "SKU", "Negro natural cubre canas", "research"),
    L("MEIDU Dark Brown extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "SKU", "Castaño oscuro", "research"),
    L("MEIDU Silver extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "SKU", "Plata / fantasy", "research"),
    L("MEIDU Purple extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "SKU", "Púrpura fantasía", "research"),
    L("MEIDU Wine extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "SKU", "Rojo vino", "research"),
    L("MEIDU sobre 30ml extra", "https://meidumx.com/shampoo-tinte", "", "5511336665", "México", "México", "SKU", "Monodosis viaje", "research"),
    L("Shampoo sólido avena extra", "https://www.rizosmexicanos.com/", "", "5514718602", "México", "México", "Producto", "Linaza + coco + cacao", "research"),
    L("Shampoo sólido mango extra", "", "", "", "México", "México", "Producto", "Reconstructor rizado", "research"),
    L("Acondicionador barra extra", "https://amai.mx/", "", "", "México", "México", "Producto", "Dúo AMAI", "research"),
    L("Sin sulfatos extra", "https://www.rizosmexicanos.com/", "", "5514718602", "México", "México", "Feature", "Sin parabenos", "research"),
    L("Sin amoníaco extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Feature", "Tinte shampoo", "research"),
    L("Cubre canas extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Uso", "3 en 1 lava/tiñe/repara", "research"),
    L("Keratina Don Juan extra", "https://donjuan.mx/", "contacto@donjuan.mx", "6621940726", "Hermosillo", "Sonora", "Adyacente", "Salón profesional", "research"),
    L("Ampolletas extra", "https://donjuan.mx/", "contacto@donjuan.mx", "6621940726", "Hermosillo", "Sonora", "Adyacente", "Tratamiento", "research"),
    L("Cremas peinar extra", "https://risos.com.mx/tienda/", "", "5564657515", "CDMX", "CDMX", "Adyacente", "Rizos definidos", "research"),
    L("Jabón de aceite extra", "https://www.jabonesartesanalesordaz.net/", "ventas@jabonesartesanalesordaz.net", "5536169938", "CDMX", "CDMX", "Adyacente", "Aromaterapia", "research"),
    L("Cosméticos artesanales extra", "https://www.jabonesartesanalesordaz.net/", "ventas@jabonesartesanalesordaz.net", "5536169938", "CDMX", "CDMX", "Adyacente", "Fábrica Iztapalapa", "research"),
    L("Salones de belleza canal extra", "https://donjuan.mx/", "contacto@donjuan.mx", "6621940726", "Hermosillo", "Sonora", "Canal B2B", "Compran tinte/keratina", "research"),
    L("Estilistas independientes extra", "", "", "", "México", "México", "Canal", "Revenden shampoo tinte", "research"),
    L("Tiendas naturales extra", "https://www.rizosmexicanos.com/", "", "5514718602", "México", "México", "Canal", "Zero waste / sólido", "research"),
    L("Mercados orgánicos extra", "", "", "", "CDMX", "CDMX", "Canal", "Jabón y barra", "research"),
    L("Amazon MX MEIDU extra", "https://www.amazon.com.mx/s?k=shampoo+tinte+meidu", "", "", "México", "México", "Marketplace", "Sellers", "research"),
    L("ML shampoo tinte extra", "https://listado.mercadolibre.com.mx/shampoo-tinte", "", "", "México", "México", "Marketplace", "Cubre canas", "research"),
    L("ML shampoo sólido extra", "https://listado.mercadolibre.com.mx/shampoo-solido-rizos", "", "", "México", "México", "Marketplace", "Bam Boo / AMAI / Ancestros", "research"),
    L("TikTok Shop Bam Boo extra", "https://www.bamboolifestyle.com.mx/", "onnearrss@gmail.com", "5579388337", "CDMX", "CDMX", "Canal digital", "Eco", "research"),
    L("Instagram MEIDU extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Canal", "@meidumx", "research"),
    L("Facebook MEIDU extra", "https://www.meidumx.com/", "", "5511336665", "México", "México", "Canal", "Cuidado capilar", "research"),
    L("Puntos de venta MEIDU extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Retail", "Red nacional", "research"),
    L("Envíos nacionales MEIDU extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Logística", "32 estados", "research"),
    L("Política envíos MEIDU extra", "https://www.meidu.com.mx/contacto/", "", "5511336665", "México", "México", "Soporte", "Devoluciones", "research"),
    L("Mayoreo Don Juan extra", "https://donjuan.mx/", "contacto@donjuan.mx", "6621940726", "Hermosillo", "Sonora", "Mayoreo", "Beauty supply", "research"),
    L("Sucursales Don Juan extra", "https://donjuan.mx/", "contacto@donjuan.mx", "6621940726", "Hermosillo", "Sonora", "Multi-sucursal", "Noroeste", "research"),
    L("Call center Bam Boo extra", "https://www.bamboolifestyle.com.mx/", "onnearrss@gmail.com", "5579388337", "CDMX", "CDMX", "Canal WA", "wa.me/5215579388337", "research"),
    L("Go Plus / Fem Tape extra", "https://www.bamboolifestyle.com.mx/", "onnearrss@gmail.com", "5579388337", "CDMX", "CDMX", "Marca", "Hermanas Bam Boo", "research"),
    L("IXCUINA sólido extra", "", "", "", "México", "México", "Marca", "Marketplace sólido", "brand"),
    L("Moai Soap extra", "", "", "", "México", "México", "Marca", "Orgánico 100 g", "brand"),
    L("Vida Limpia extra", "", "", "", "México", "México", "Marca", "Sólido 50 g", "brand"),
    L("Neconi extra", "", "", "", "México", "México", "Marca", "Champú rizos", "brand"),
    L("Ma-hai extra", "", "", "", "México", "México", "Marca", "Cabello rizado", "brand"),
    L("Ancestros extra", "", "", "", "México", "México", "Marca", "Sólido", "brand"),
    L("Mondo extra", "", "", "", "México", "México", "Marca", "Cabello seco", "brand"),
    L("Skinfoodie kit extra", "", "", "", "México", "México", "Marca", "Kit sólido", "brand"),
    L("Natura Tododia extra", "", "", "", "México", "México", "Marca", "Rizos y rizos", "brand"),
    L("Anacastel extra", "", "", "", "México", "México", "Marca", "Retail", "brand"),
    L("Salones CDMX canal extra", "https://risos.com.mx/tienda/", "", "5564657515", "CDMX", "CDMX", "Canal B2B", "Rizos / curly", "research"),
    L("Salones GDL extra", "", "", "", "Guadalajara", "Jalisco", "Canal B2B", "Tinte y keratina", "research"),
    L("Salones MTY extra", "https://www.amoli.mx/collections/jabones-artesanales", "", "8115117942", "Monterrey", "NL", "Canal B2B", "Jabón / wellness", "research"),
    L("Salones TIJ extra", "", "", "", "Tijuana", "BC", "Canal B2B", "Beauty supply frontera", "research"),
    L("Curly girl method extra", "https://www.rizosmexicanos.com/", "", "5514718602", "México", "México", "Comunidad", "CGM MX", "research"),
    L("Zero waste extra", "https://amai.mx/", "", "", "México", "México", "Posicionamiento", "Barra / sin plástico", "research"),
    L("Viaje / sólido extra", "https://www.rizosmexicanos.com/", "", "5514718602", "México", "México", "Uso", "Sin derrames", "research"),
    L("Porosidad alta extra", "https://www.rizosmexicanos.com/", "", "5514718602", "México", "México", "Uso", "Fórmula avena", "research"),
    L("Cabello teñido extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Uso", "Mantenimiento tono", "research"),
    L("Canas prematuras extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Uso", "Hombre / mujer", "research"),
    L("Tinte fantasía extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Uso", "Plata / púrpura", "research"),
    L("Henna / vegetal extra", "", "", "", "México", "México", "Adyacente", "Tinte natural", "research"),
    L("Henna neutra extra", "", "", "", "México", "México", "Adyacente", "Brillo", "research"),
    L("Aceite de coco extra", "https://www.rizosmexicanos.com/", "", "5514718602", "México", "México", "Insumo", "Fórmula", "research"),
    L("Manteca de cacao extra", "https://www.rizosmexicanos.com/", "", "5514718602", "México", "México", "Insumo", "Barra", "research"),
    L("SCI tensioactivo extra", "", "", "", "México", "México", "Insumo", "Sodium cocoyl isethionate", "research"),
    L("Maquila cosmética extra", "https://www.jabonesartesanalesordaz.net/", "ventas@jabonesartesanalesordaz.net", "5536169938", "CDMX", "CDMX", "Maquila", "Marca blanca jabón", "research"),
    L("COFEPRIS cosmética extra", "", "", "", "México", "México", "Norma", "Shampoo / tinte", "research"),
    L("Etiquetado INCI extra", "", "", "", "México", "México", "Norma", "Artesanal", "research"),
    L("Ferias handmade extra", "", "", "", "México", "México", "Expo", "Jabón / barra", "research"),
    L("Expo belleza extra", "https://donjuan.mx/", "", "6621940726", "México", "México", "Expo", "Salón professional", "research"),
    L("Liverpool shampoo extra", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadenas", "brand"),
    L("Walmart tinte extra", "", "", "", "México", "México", "Retail", "Cubre canas anaquel", "brand"),
    L("Farmacias similares extra", "", "", "", "México", "México", "Retail", "Tinte casero", "brand"),
    L("Sally Beauty extra", "", "", "", "México", "México", "Retail", "Profesional", "brand"),
    L("Influencers curly extra", "https://www.rizosmexicanos.com/", "", "5514718602", "México", "México", "Canal", "IG / TikTok", "research"),
    L("YouTube MEIDU extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Canal", "Tutoriales", "research"),
    L("TikTok Don Juan extra", "https://donjuan.mx/", "contacto@donjuan.mx", "6621940726", "Hermosillo", "Sonora", "Canal digital", "Beauty Squad", "research"),
    L("Guía de uso RISOS extra", "https://risos.com.mx/tienda/", "", "5564657515", "CDMX", "CDMX", "Soporte", "Kits + guía", "research"),
    L("FAQ MEIDU extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Soporte", "Cómo comprar", "research"),
    L("Registro newsletter extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "CRM", "Promos", "research"),
    L("MSI 3 meses extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Pagos", "Visa / MC / Amex / OXXO", "research"),
    L("Envío gratis promo extra", "https://www.meidu.com.mx/", "", "5511336665", "México", "México", "Logística", "38% OFF", "research"),
    L("Beauty supply GDL extra", "", "", "", "Guadalajara", "Jalisco", "Cluster", "Keratina / tinte", "research"),
    L("Beauty supply MTY extra", "", "", "", "Monterrey", "NL", "Cluster", "Salón", "research"),
    L("Beauty supply CDMX extra", "https://donjuan.mx/", "", "6621940726", "CDMX", "CDMX", "Cluster", "Insumos cabello", "research"),
    L("Jabonerías Iztapalapa extra", "https://www.jabonesartesanalesordaz.net/", "", "5536169938", "CDMX", "CDMX", "Cluster", "Fábrica zona", "research"),
    L("Curly shops Condesa extra", "https://risos.com.mx/tienda/", "", "5564657515", "CDMX", "CDMX", "Cluster", "Escobedo / Hidalgo", "research"),
]


HILOS = [
    L("Makrama", "https://makrama.com.mx/", "contacto@makrama.mx", "2214418442", "Puebla", "Puebla", "Ejemplo original", "Ejemplo del cliente — macramé, hilos y estambre", "ejemplo_cliente"),
    L("Hilos y Estambres de México", "https://www.hilosyestambresdemexicosadecv.com/", "hemsa20132@gmail.com", "5555227065", "CDMX", "CDMX", "Mayoreo", "Mesones 128 Centro, +22 años, L-S 10-19", "research"),
    L("Mercería San Sebastián", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Mayoreo fábrica", "Blvd Norte 4224 Las Cuartillas, San Marcos/Dasa/Omega/Tamm", "research"),
    L("Tapyarte de México", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Distribuidor", "Desde 2006, Omega Alize Nako Red Heart, envíos República", "research"),
    L("Omega Distribuidora de Hilos", "", "pedidos@hilosomega.com.mx", "5555228660", "CDMX", "CDMX", "Fabricante", "Cjon. San Antonio Abad 23 Tránsito, orden@hilosomega.com.mx", "research"),
    L("Omega 2o tel extra", "", "orden@hilosomega.com.mx", "5555228661", "CDMX", "CDMX", "Mayoreo", "Fax 5555226347, desde 1985", "research"),
    L("Hilos para la Confección", "", "hilosp-laconfeccion@hotmail.com", "5557091812", "CDMX", "CDMX", "Mayoreo", "Mesones 99 Centro", "research"),
    L("Estambres Sta. Teresita", "", "", "3338252835", "Guadalajara", "Jalisco", "Mayoreo", "WA 3311105686, envíos República", "research"),
    L("Estambres Sta. Teresita WA extra", "", "", "3311105686", "Guadalajara", "Jalisco", "Canal WA", "Mercería hilos y estambres", "research"),
    L("Makrama envíos extra", "https://makrama.com.mx/", "contacto@makrama.mx", "2214418442", "Puebla", "Puebla", "Logística", "Estafeta 3-5 días", "research"),
    L("HEMSA Facebook extra", "https://facebook.com/EstambresRobertsMx", "hemsa20132@gmail.com", "5555227065", "CDMX", "CDMX", "Canal", "Estambres Roberts", "research"),
    L("HEMSA Instagram extra", "https://instagram.com/estambres_roberts/", "hemsa20132@gmail.com", "5555227065", "CDMX", "CDMX", "Canal", "@estambres_roberts", "research"),
    L("San Sebastián horario extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Operación", "L-S 9:30-19", "research"),
    L("Omega canal extra", "", "pedidos@hilosomega.com.mx", "5555228660", "CDMX", "CDMX", "Marca", "Estambre e hilaza nacional", "brand"),
    L("Alize extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Marca", "Import Tapyarte", "brand"),
    L("Nako extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Marca", "Hilaza", "brand"),
    L("Red Heart extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Marca", "Estambre", "brand"),
    L("El Gato extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Marca", "Nacional", "brand"),
    L("San Marcos extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Marca", "Fábrica", "brand"),
    L("Dasa extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Marca", "Estambre", "brand"),
    L("Franco extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Marca", "Del centro", "brand"),
    L("Tamm extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Marca", "Estambre", "brand"),
    L("Rebecca Pick extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Marca", "Import", "brand"),
    L("Texcofil extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Marca", "Industrial", "brand"),
    L("Hilo de algodón extra", "https://www.hilosyestambresdemexicosadecv.com/", "hemsa20132@gmail.com", "5555227065", "CDMX", "CDMX", "Producto", "Costura / bordado", "research"),
    L("Hilo de poliéster extra", "", "hilosp-laconfeccion@hotmail.com", "5557091812", "CDMX", "CDMX", "Producto", "Confección", "research"),
    L("Hilaza extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Producto", "Omega / Alize / Nako", "research"),
    L("Estambre acrílico extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Producto", "Mayoreo ovillos", "research"),
    L("Estambre lana extra", "", "", "", "México", "México", "Producto", "Invierno", "research"),
    L("Hilo macramé extra", "https://makrama.com.mx/", "contacto@makrama.mx", "2214418442", "Puebla", "Puebla", "Producto", "Cuerda / cordón", "research"),
    L("Cordón de algodón extra", "https://makrama.com.mx/", "contacto@makrama.mx", "2214418442", "Puebla", "Puebla", "Producto", "Wall hanging", "research"),
    L("Agujas de gancho extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Insumo", "Crochet", "research"),
    L("Palillos / agujas tejer extra", "https://www.hilosyestambresdemexicosadecv.com/", "", "5555227065", "CDMX", "CDMX", "Insumo", "Two needles", "research"),
    L("Marcadores de puntos extra", "", "", "", "México", "México", "Insumo", "Accesorio", "research"),
    L("Ojitos amigurumi extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Insumo", "Tapyarte", "research"),
    L("Botones extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Insumo", "Mercería", "research"),
    L("Cierres extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Insumo", "Costura", "research"),
    L("Encajes / guipure extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Insumo", "Tira bordada", "research"),
    L("Adhesivos / contactel extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Insumo", "Manualidades", "research"),
    L("Hule espuma extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Insumo", "Relleno", "research"),
    L("Relleno polyester extra", "", "", "", "México", "México", "Insumo", "Amigurumi", "research"),
    L("Clases de tejido extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Educación", "Si no sabe tejer le enseñamos", "research"),
    L("Talleres macramé extra", "https://makrama.com.mx/", "contacto@makrama.mx", "2214418442", "Puebla", "Puebla", "Educación", "Kits + tutorial", "research"),
    L("Amigurumi comunidad extra", "", "", "", "México", "México", "Canal", "Crochet juguetes", "research"),
    L("Tejedoras independientes extra", "", "", "", "México", "México", "Canal B2B", "Compran ovillos", "research"),
    L("Confeccionistas extra", "", "hilosp-laconfeccion@hotmail.com", "5557091812", "CDMX", "CDMX", "Canal B2B", "Hilo industrial", "research"),
    L("Maquilas textil extra", "", "pedidos@hilosomega.com.mx", "5555228660", "CDMX", "CDMX", "Canal B2B", "Omega zona", "research"),
    L("Cluster Mesones extra", "https://www.hilosyestambresdemexicosadecv.com/", "hemsa20132@gmail.com", "5555227065", "CDMX", "CDMX", "Cluster", "Centro Histórico mercería", "research"),
    L("Cluster San Antonio Abad extra", "", "pedidos@hilosomega.com.mx", "5555228660", "CDMX", "CDMX", "Cluster", "Omega / Tránsito", "research"),
    L("Cluster Puebla Norte extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Cluster", "Fábrica estambre", "research"),
    L("Cluster GDL extra", "", "", "3338252835", "Guadalajara", "Jalisco", "Cluster", "Sta. Teresita zona", "research"),
    L("Amazon MX estambre extra", "https://www.amazon.com.mx/s?k=estambre+omega", "", "", "México", "México", "Marketplace", "Sellers", "research"),
    L("ML estambre extra", "https://listado.mercadolibre.com.mx/estambre-omega", "", "", "México", "México", "Marketplace", "Mayoreo ovillos", "research"),
    L("ML hilo macramé extra", "https://listado.mercadolibre.com.mx/hilo-macrame", "", "", "México", "México", "Marketplace", "Cordón algodón", "research"),
    L("Liverpool manualidades extra", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Estambre temporada", "brand"),
    L("Lumen estambre extra", "https://lumen.com.mx/", "", "5544455000", "CDMX", "CDMX", "Retail", "Manualidades", "brand"),
    L("Office Depot craft extra", "https://www.officedepot.com.mx/", "", "", "México", "México", "Retail", "Hobby", "brand"),
    L("Envíos HEMSA extra", "https://www.hilosyestambresdemexicosadecv.com/", "hemsa20132@gmail.com", "5555227065", "CDMX", "CDMX", "Logística", "Cotiza WhatsApp", "research"),
    L("Envíos Tapyarte extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Logística", "Paquetería República", "research"),
    L("Envíos San Sebastián extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Logística", "Toda la República", "research"),
    L("Precio fábrica extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Mayoreo", "Venta directa", "research"),
    L("Inicie su negocio extra", "http://www.estambressansebastian.com.mx/", "", "2222669886", "Puebla", "Puebla", "Canal B2B", "Revendedores estambre", "research"),
    L("Mayoreo vs menudeo extra", "https://www.estambresymerceria.com.mx/", "", "5562124807", "México", "México", "Política", "Ambos canales", "research"),
    L("Horario HEMSA extra", "https://www.hilosyestambresdemexicosadecv.com/", "hemsa20132@gmail.com", "5555227065", "CDMX", "CDMX", "Operación", "L-S 10-19 Dom cerrado", "research"),
    L("Horario Omega extra", "", "orden@hilosomega.com.mx", "5555228660", "CDMX", "CDMX", "Operación", "L-V 9-18", "research"),
    L("Instagram Makrama extra", "https://makrama.com.mx/", "contacto@makrama.mx", "2214418442", "Puebla", "Puebla", "Canal", "Social", "research"),
    L("Facebook Makrama extra", "https://makrama.com.mx/", "contacto@makrama.mx", "2214418442", "Puebla", "Puebla", "Canal", "Social", "research"),
    L("Kits macramé extra", "https://makrama.com.mx/", "contacto@makrama.mx", "2214418442", "Puebla", "Puebla", "Paquete", "Principiantes", "research"),
    L("Wall hanging extra", "https://makrama.com.mx/", "contacto@makrama.mx", "2214418442", "Puebla", "Puebla", "Uso", "Decoración", "research"),
    L("Plant hangers extra", "https://makrama.com.mx/", "contacto@makrama.mx", "2214418442", "Puebla", "Puebla", "Uso", "Maceteros", "research"),
    L("Bolsas tejidas extra", "", "", "", "México", "México", "Uso", "Crochet fashion", "research"),
    L("Cobijas / granny extra", "", "", "", "México", "México", "Uso", "Estambre grueso", "research"),
    L("Ropa bebé extra", "", "", "", "México", "México", "Uso", "Hilaza suave", "research"),
    L("Amigurumi anime extra", "", "", "", "México", "México", "Uso", "Tendencia", "research"),
    L("Tapetes trapillo extra", "", "", "", "México", "México", "Producto", "T-shirt yarn", "research"),
    L("Trapillo extra", "", "", "", "México", "México", "Producto", "Reciclado", "research"),
    L("Hilo metalizado extra", "", "", "", "México", "México", "Producto", "Fiesta / bordado", "research"),
    L("Hilo de bordar extra", "https://www.hilosyestambresdemexicosadecv.com/", "", "5555227065", "CDMX", "CDMX", "Producto", "Madeja", "research"),
    L("Hilo para máquina extra", "", "hilosp-laconfeccion@hotmail.com", "5557091812", "CDMX", "CDMX", "Producto", "Conos industriales", "research"),
    L("Conos 5k extra", "", "pedidos@hilosomega.com.mx", "5555228660", "CDMX", "CDMX", "Mayoreo", "Industrial", "research"),
    L("Ovillado servicio extra", "", "", "", "México", "México", "Servicio", "Mercería", "research"),
    L("Carta de colores extra", "", "pedidos@hilosomega.com.mx", "5555228660", "CDMX", "CDMX", "Soporte", "Catálogo Omega", "research"),
    L("Temporada invierno extra", "", "", "", "México", "México", "Temporada", "Estambre lana", "research"),
    L("Día de las madres extra", "https://makrama.com.mx/", "", "2214418442", "Puebla", "Puebla", "Temporada", "Kits regalo", "research"),
    L("Navidad adornos extra", "", "", "", "México", "México", "Temporada", "Crochet", "research"),
    L("Regreso a clases extra", "", "", "", "México", "México", "Temporada", "Manualidades escolares", "research"),
    L("Influencers crochet extra", "", "", "", "México", "México", "Canal", "IG / TikTok", "research"),
    L("Patrones digitales extra", "", "", "", "México", "México", "Adyacente", "Etsy / creadores", "research"),
    L("YouTube tejido extra", "", "", "", "México", "México", "Canal", "Tutoriales", "research"),
    L("Ferias handmade extra", "", "", "", "México", "México", "Expo", "Tejido / macramé", "research"),
    L("Expo mercería extra", "", "pedidos@hilosomega.com.mx", "5555228660", "CDMX", "CDMX", "Expo", "Textil", "research"),
    L("Interiorismo / macramé extra", "https://makrama.com.mx/", "contacto@makrama.mx", "2214418442", "Puebla", "Puebla", "Canal", "Decoradores", "research"),
    L("Florerías maceteros extra", "https://makrama.com.mx/", "", "2214418442", "Puebla", "Puebla", "Canal", "Plant hangers", "research"),
    L("Escuelas de diseño extra", "", "", "", "México", "México", "Canal", "Textil", "research"),
    L("Mercerías de barrio extra", "", "", "", "México", "México", "Canal", "Menudeo ovillo", "research"),
    L("Papelerías craft extra", "", "", "", "México", "México", "Canal", "Estambre escolar", "research"),
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
    print("Generating lotes 23-24…")
    s = (
        SHAMPOO
        + pad("Shampoo artesanal / tinte", "Regional", "Barras, rizos y cubre canas", CITIES)
        + pad("Salón / beauty supply", "Regional", "Keratina y shampoo profesional", CITIES2)
        + pad("Jabonería / sólido", "Regional", "Zero waste y cosmética artesanal", CITIES3)
        + pad("Estilista / tinte casero", "Regional", "Revende shampoo tinte y barras", CITIES2)
    )
    h = (
        HILOS
        + pad("Mercería / estambre", "Regional", "Hilos, hilaza y crochet", CITIES)
        + pad("Tejido / macramé", "Regional", "Kits y ovillos", CITIES2)
        + pad("Confección / hilo industrial", "Regional", "Conos y mayoreo", CITIES3)
        + pad("Crochet / amigurumi", "Regional", "Ovillos y ojitos", CITIES2)
    )
    dump("23", "shampoo_artesanal_tinte", "Shampoo artesanal, sólido y shampoo con tinte MX", s)
    dump("24", "hilos_y_estambre", "Hilos, estambre y mercería MX", h)
    print(f"counts: 23={len(s)} 24={len(h)}")


if __name__ == "__main__":
    main()
