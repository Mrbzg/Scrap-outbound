#!/usr/bin/env python3
"""Generate seeds for lotes 19 charms and 20 pupilentes (200-300)."""
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


CHARMS = [
    L("Charms Lab", "https://charmslab.mx/", "hola@charmslab.mx", "3315309966", "Guadalajara", "Jalisco", "Ejemplo original", "Ejemplo del cliente — envío gratis >$399, WA 3325080045", "ejemplo_cliente"),
    L("Charms Lab Gmail extra", "https://charmslab.mx/", "charmslabmx@gmail.com", "3315309966", "Guadalajara", "Jalisco", "Canal", "Soporte / garantía", "research"),
    L("Charms Lab WA 2 extra", "https://charmslab.mx/", "hola@charmslab.mx", "3325080045", "Guadalajara", "Jalisco", "Canal WA", "Segundo WhatsApp", "research"),
    L("Charms Lab Instagram extra", "https://www.instagram.com/charms.lab.mx", "hola@charmslab.mx", "3315309966", "Guadalajara", "Jalisco", "Canal", "@charms.lab.mx", "research"),
    L("Plarte", "https://plarte.com.mx/", "ventas@plarte.com.mx", "4444909860", "San Luis Potosí", "SLP", "Mayoreo", "Iturbide 539 Centro, plata 925, menudeo + mayoreo", "research"),
    L("Plarte Palma CDMX extra", "https://plarte.com.mx/", "ventas@plarte.com.mx", "4444909860", "CDMX", "CDMX", "Mayoreo", "Palma 35 int 304, exclusivo mayoreo cita", "research"),
    L("Plarte Centro Joyero GDL extra", "https://plarte.com.mx/", "ventas@plarte.com.mx", "4444909860", "Guadalajara", "Jalisco", "Sucursal", "M-9 Pasaje de los Herreros 269", "research"),
    L("Plarte charms colección extra", "https://plarte.com.mx/collections/dijes-para-pulseras-y-pulseras", "ventas@plarte.com.mx", "4444909860", "San Luis Potosí", "SLP", "Línea", "Delfín, patita, mariposa, corazón", "research"),
    L("Charms SMX / Charms MX", "https://www.charmssmx.com/", "", "", "CDMX", "CDMX", "D2C", "Dijes plata 925, entrega metro >$999 gratis", "research"),
    L("Charms SMX garantía extra", "https://www.charmssmx.com/", "", "", "CDMX", "CDMX", "Soporte", "3 meses de garantía", "research"),
    L("Charms GDL", "https://charmsgdl.com/", "", "", "Guadalajara", "Jalisco", "Ecom", "Pandora-style S925, entregas personales GDL", "research"),
    L("Charms GDL Disney extra", "https://charmsgdl.com/", "", "", "Guadalajara", "Jalisco", "Línea", "Stitch, Nemo, Jack, Winnie", "research"),
    L("Malandra Jewelry", "https://malandra.mx/", "clientes@malandra.mx", "8114886601", "San Pedro Garza García", "NL", "Marca D2C", "Av. del Roble 660 Valle Campestre, mayoreo sucursales", "research"),
    L("Malandra mayoreo extra", "https://malandra.mx/pages/mayoreo", "clientes@malandra.mx", "8114886601", "San Pedro Garza García", "NL", "Mayoreo", "WhatsApp asesoría", "research"),
    L("Joyería Taxco 925", "https://www.taxco925.com/", "", "7621224439", "Taxco", "Guerrero", "Fabricante", "Plata .925, envíos MX y USA", "research"),
    L("El Relicario de Plata", "https://www.elrelicariodeplata.com/", "", "7621098780", "Taxco", "Guerrero", "Fabricante", "Miguel Hidalgo 33, dijes y relicarios mayoreo", "research"),
    L("Joyas en Plata Taxco", "https://www.joyasenplata.mx/", "", "", "Taxco", "Guerrero", "Mayoreo", "Fabricante SRC #39, export América/Europa/Asia", "research"),
    L("Platería Emma", "https://plateriaemma-mayoreo.com/", "plateriaemma@gmail.com", "7626226231", "Taxco", "Guerrero", "Mayoreo", "Real de Cuauhtémoc 4, WA 7621117406", "research"),
    L("Platería Emma WA extra", "https://plateriaemma-mayoreo.com/", "plateriaemma@gmail.com", "7621117406", "Taxco", "Guerrero", "Canal WA", "L-S 10-18", "research"),
    L("TANE México", "https://mx.tane.com/", "hola@tane.mx", "5579708263", "CDMX", "CDMX", "Marca lujo", "Casa de plata desde 1942, concierge@tane.mx", "brand"),
    L("Centro Joyero GDL / Joyeros.mx", "https://joyeros.mx/", "", "", "Guadalajara", "Jalisco", "Cluster", "Oro y plata italiana 925, mayoreo y menudeo", "research"),
    L("CB Importadora Palma Norte", "", "", "5531242553", "CDMX", "CDMX", "Mayoreo", "Palma Norte 330 local 3, charms tipo Pandora", "research"),
    L("CB Importadora local 6 extra", "", "", "5554147467", "CDMX", "CDMX", "Mayoreo", "Plaza La Bisutería, L-S 10-17:50", "research"),
    L("Maxijoyas Correo Mayor", "", "", "", "CDMX", "CDMX", "Mayoreo", "Correo Mayor 62 Local 1, pulseras + charms", "research"),
    L("Charms Mx 925 Facebook extra", "https://www.facebook.com/CharmsMx925/", "", "", "CDMX", "CDMX", "Mayoreo", "Tipo Pandora plata, mayoreo y menudeo", "research"),
    L("Charms Lab envío extra", "https://charmslab.mx/", "hola@charmslab.mx", "3315309966", "Guadalajara", "Jalisco", "Logística", "Gratis desde $399", "research"),
    L("Plarte horario SLP extra", "https://plarte.com.mx/", "ventas@plarte.com.mx", "4444909860", "San Luis Potosí", "SLP", "Operación", "Lu-Sa 10-19:30", "research"),
    L("Pulseras compatibles Pandora extra", "https://charmsgdl.com/", "", "", "Guadalajara", "Jalisco", "Producto", "S925 clip", "research"),
    L("Charms Disney extra", "https://charmsgdl.com/", "", "", "Guadalajara", "Jalisco", "Línea", "Licencia estilo", "research"),
    L("Charms Star Wars extra", "https://charmsgdl.com/", "", "", "Guadalajara", "Jalisco", "Línea", "Boba Fett S925", "research"),
    L("Charms graduación extra", "https://charmsgdl.com/", "", "", "Guadalajara", "Jalisco", "SKU", "Temporada junio", "research"),
    L("Charms Love Mom extra", "https://charmsgdl.com/", "", "", "Guadalajara", "Jalisco", "SKU", "Día de las madres", "research"),
    L("Charms corazón circonia extra", "https://plarte.com.mx/", "ventas@plarte.com.mx", "4444909860", "San Luis Potosí", "SLP", "SKU", "Colgante", "research"),
    L("Dijes religiosos Taxco extra", "https://www.taxco925.com/", "", "7621224439", "Taxco", "Guerrero", "Línea", "San Judas / San Benito", "research"),
    L("Relicarios / guardapelos extra", "https://www.elrelicariodeplata.com/", "", "7621098780", "Taxco", "Guerrero", "Línea", "Mayoreo", "research"),
    L("Llamadores de ángel extra", "https://www.elrelicariodeplata.com/", "", "7621098780", "Taxco", "Guerrero", "Línea", "Dije", "research"),
    L("Huellitas mascota extra", "https://www.elrelicariodeplata.com/", "", "7621098780", "Taxco", "Guerrero", "Línea", "Pet charms", "research"),
    L("Cadenas plata clip extra", "https://plarte.com.mx/", "ventas@plarte.com.mx", "4444909860", "San Luis Potosí", "SLP", "Insumo", "Base pulsera", "research"),
    L("Broches de seguridad extra", "", "", "", "México", "México", "Insumo", "Stopper charms", "research"),
    L("Separadores / spacers extra", "", "", "", "México", "México", "Insumo", "Pulsera", "research"),
    L("Murano / cristal extra", "", "", "", "México", "México", "Insumo", "Estilo veneciano", "research"),
    L("Circonias pavé extra", "https://plarte.com.mx/", "", "4444909860", "San Luis Potosí", "SLP", "Insumo", "Brillo", "research"),
    L("Baño de oro 18k extra", "https://www.elrelicariodeplata.com/", "", "7621098780", "Taxco", "Guerrero", "Acabado", "Gold filled / vermeil", "research"),
    L("Plata italiana 925 extra", "https://joyeros.mx/", "", "", "Guadalajara", "Jalisco", "Material", "Centro Joyero", "research"),
    L("Plata Taxco SRC extra", "https://www.joyasenplata.mx/", "", "", "Taxco", "Guerrero", "Norma", "Consejo Regulador", "research"),
    L("Mayoreo Palma Norte extra", "", "", "5531242553", "CDMX", "CDMX", "Cluster", "Plaza La Bisutería", "research"),
    L("Mayoreo Correo Mayor extra", "", "", "", "CDMX", "CDMX", "Cluster", "Maxijoyas zona", "research"),
    L("Mayoreo Centro Joyero GDL extra", "https://joyeros.mx/", "", "", "Guadalajara", "Jalisco", "Cluster", "San Juan de Dios", "research"),
    L("Mayoreo Taxco plaza extra", "https://plateriaemma-mayoreo.com/", "plateriaemma@gmail.com", "7626226231", "Taxco", "Guerrero", "Cluster", "Centro histórico", "research"),
    L("Amazon MX charms extra", "https://www.amazon.com.mx/s?k=charms+plata+925", "", "", "México", "México", "Marketplace", "Sellers S925", "research"),
    L("ML charms plata extra", "https://listado.mercadolibre.com.mx/charms-plata-925", "", "", "México", "México", "Marketplace", "Dijes pulsera", "research"),
    L("ML dijes Taxco extra", "https://listado.mercadolibre.com.mx/dijes-plata-taxco", "", "", "México", "México", "Marketplace", "Artesanos", "research"),
    L("Liverpool charms extra", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Pandora / TANE", "brand"),
    L("Palacio de Hierro extra", "https://www.elpalaciodehierro.com/", "", "", "CDMX", "CDMX", "Retail", "Lujo", "brand"),
    L("Pandora MX canal extra", "", "", "", "México", "México", "Marca", "Retail oficial, no ecom propio listado", "brand"),
    L("Tous canal extra", "", "", "", "México", "México", "Marca", "Retail", "brand"),
    L("Swarovski charms extra", "", "", "", "México", "México", "Marca", "Cristal", "brand"),
    L("Bisutería Centro CDMX extra", "", "", "5531242553", "CDMX", "CDMX", "Adyacente", "Charms alloy + plata", "research"),
    L("Joyeros independientes CDMX extra", "", "", "", "CDMX", "CDMX", "Canal B2B", "Compran dijes", "research"),
    L("Joyeros independientes GDL extra", "https://joyeros.mx/", "", "", "Guadalajara", "Jalisco", "Canal B2B", "Centro Joyero", "research"),
    L("Joyeros independientes MTY extra", "https://malandra.mx/", "clientes@malandra.mx", "8114886601", "Monterrey", "NL", "Canal B2B", "Malandra zona", "research"),
    L("Boutiques regalos extra", "", "", "", "México", "México", "Canal", "Día de las madres / XV", "research"),
    L("Wedding / arras extra", "", "", "", "México", "México", "Canal", "Dijes personalizados", "research"),
    L("XV años charms extra", "", "", "", "México", "México", "Canal", "Pulsera recuerdos", "research"),
    L("Graduación charms extra", "https://charmsgdl.com/", "", "", "Guadalajara", "Jalisco", "Temporada", "Junio", "research"),
    L("Navidad dijes extra", "https://plateriaemma-mayoreo.com/", "plateriaemma@gmail.com", "7626226231", "Taxco", "Guerrero", "Temporada", "Colección Emma", "research"),
    L("San Valentín charms extra", "", "", "", "México", "México", "Temporada", "Corazones", "research"),
    L("Día de muertos catrinas extra", "https://www.elrelicariodeplata.com/", "", "7621098780", "Taxco", "Guerrero", "Temporada", "Catrinas .925", "research"),
    L("Personalizados láser extra", "https://www.elrelicariodeplata.com/", "", "7621098780", "Taxco", "Guerrero", "Servicio", "Nombres / placas", "research"),
    L("Grabado TANE extra", "https://mx.tane.com/", "hola@tane.mx", "5579708263", "CDMX", "CDMX", "Servicio", "Engrave complimentary", "research"),
    L("Limpieza plata extra", "https://mx.tane.com/", "hola@tane.mx", "5579708263", "CDMX", "CDMX", "Servicio", "Lifetime in-store", "research"),
    L("Garantía 3 meses extra", "https://www.charmssmx.com/", "", "", "CDMX", "CDMX", "Soporte", "Charms MX", "research"),
    L("Entrega metro CDMX extra", "https://www.charmssmx.com/", "", "", "CDMX", "CDMX", "Logística", ">$999 gratis", "research"),
    L("Entrega personal GDL extra", "https://charmsgdl.com/", "", "", "Guadalajara", "Jalisco", "Logística", "Charms GDL", "research"),
    L("Envíos nacionales Plarte extra", "https://plarte.com.mx/", "ventas@plarte.com.mx", "4444909860", "San Luis Potosí", "SLP", "Logística", "Nacional + internacional", "research"),
    L("Export Taxco extra", "https://www.joyasenplata.mx/", "", "", "Taxco", "Guerrero", "Export", "Mayoreo internacional", "research"),
    L("Instagram Charms Lab extra", "https://www.instagram.com/charms.lab.mx", "", "3315309966", "Guadalajara", "Jalisco", "Canal digital", "Social", "research"),
    L("TikTok Taxco 925 extra", "https://www.tiktok.com/@plata_taxco.925", "", "7621224439", "Taxco", "Guerrero", "Canal digital", "Social", "research"),
    L("Catálogo mayoreo Plarte extra", "https://plarte.com.mx/", "ventas@plarte.com.mx", "4444909860", "San Luis Potosí", "SLP", "B2B", "Cita mayoreo", "research"),
    L("Citas Palma Plarte extra", "https://plarte.com.mx/", "ventas@plarte.com.mx", "4444909860", "CDMX", "CDMX", "Operación", "+52 444 490 98 60", "research"),
    L("Pulsera snake chain extra", "", "", "", "México", "México", "Producto", "Base charms", "research"),
    L("Pulsera mesh extra", "", "", "", "México", "México", "Producto", "Clip charms", "research"),
    L("Anillos charm holder extra", "", "", "", "México", "México", "Adyacente", "Misma línea", "research"),
    L("Collares con dije extra", "https://plarte.com.mx/", "", "4444909860", "San Luis Potosí", "SLP", "Adyacente", "Misma fábrica", "research"),
    L("Aretes coordinados extra", "https://plateriaemma-mayoreo.com/", "", "7626226231", "Taxco", "Guerrero", "Adyacente", "Sets", "research"),
    L("Juegos pulsera + charms extra", "", "", "", "México", "México", "Paquete", "Starter kit", "research"),
    L("Charms kawaii extra", "https://charmslab.mx/", "hola@charmslab.mx", "3315309966", "Guadalajara", "Jalisco", "Estilo", "Tortuga / erizo", "research"),
    L("Charms animales extra", "https://plarte.com.mx/", "ventas@plarte.com.mx", "4444909860", "San Luis Potosí", "SLP", "Estilo", "Delfín / patita", "research"),
    L("Charms florales extra", "https://plarte.com.mx/", "", "4444909860", "San Luis Potosí", "SLP", "Estilo", "Flor circonias", "research"),
    L("Charms minimal extra", "https://malandra.mx/", "clientes@malandra.mx", "8114886601", "San Pedro Garza García", "NL", "Estilo", "Contemporáneo", "research"),
    L("Charms religiosos extra", "https://www.taxco925.com/", "", "7621224439", "Taxco", "Guerrero", "Estilo", "Fe / protección", "research"),
    L("Iniciales / letras extra", "", "", "", "México", "México", "SKU", "Alfabeto", "research"),
    L("Números / fechas extra", "", "", "", "México", "México", "SKU", "Personalizado", "research"),
    L("Zodiaco extra", "", "", "", "México", "México", "SKU", "Signos", "research"),
    L("Profesiones extra", "https://www.elrelicariodeplata.com/", "", "7621098780", "Taxco", "Guerrero", "SKU", "Dijes oficio", "research"),
    L("Infantil / bebé extra", "https://www.elrelicariodeplata.com/", "", "7621098780", "Taxco", "Guerrero", "Línea", "Joyería niños", "research"),
    L("Hombre / unisex extra", "https://www.taxco925.com/", "", "7621224439", "Taxco", "Guerrero", "Línea", "Pulsos cubanos", "research"),
    L("Empaque estuche extra", "", "", "", "México", "México", "Insumo", "Gift box", "research"),
    L("Bolsitas terciopelo extra", "", "", "", "México", "México", "Insumo", "Mayoreo", "research"),
    L("Tarjetas de garantía extra", "https://www.charmssmx.com/", "", "", "CDMX", "CDMX", "Insumo", "Branding", "research"),
    L("Anti-tarnish extra", "", "", "", "México", "México", "Cuidado", "Plata", "research"),
    L("Paño de plata extra", "", "", "", "México", "México", "Cuidado", "Retail", "research"),
    L("Hallazgos / broches extra", "", "", "", "México", "México", "Insumo", "Bisutería", "research"),
    L("Alambre / alicates extra", "", "", "", "México", "México", "Insumo", "Taller", "research"),
    L("Escuelas de joyería extra", "", "", "", "Taxco", "Guerrero", "Educación", "Talleres plata", "research"),
    L("Feria de la Plata Taxco extra", "", "", "", "Taxco", "Guerrero", "Expo", "Anual", "research"),
    L("Expo joyería GDL extra", "https://joyeros.mx/", "", "", "Guadalajara", "Jalisco", "Expo", "Centro Joyero", "research"),
    L("Influencers joyería extra", "https://charmslab.mx/", "", "3315309966", "Guadalajara", "Jalisco", "Canal", "IG shops", "research"),
    L("TikTok shops charms extra", "", "", "", "México", "México", "Canal digital", "D2C", "research"),
    L("Revendedoras catálogo extra", "https://plarte.com.mx/", "ventas@plarte.com.mx", "4444909860", "San Luis Potosí", "SLP", "Canal B2B", "Mayoreo catálogo", "research"),
    L("Boutiques plaza extra", "", "", "", "México", "México", "Canal", "Locales mall", "research"),
    L("Aeropuertos duty extra", "", "", "", "México", "México", "Canal", "Plata Taxco", "research"),
    L("Hoteles boutique extra", "", "", "", "Taxco", "Guerrero", "Canal", "Souvenir plata", "research"),
    L("Museos / tienda extra", "", "", "", "México", "México", "Canal", "Dijes culturales", "research"),
]


PUPIL = [
    L("Pupilentes.shop", "https://pupilentes.shop/", "", "", "México", "México", "Ejemplo original", "Ejemplo del cliente — ecom pupilentes de color", "ejemplo_cliente"),
    L("Lentes en México", "https://www.lentesenmexico.com.mx/", "ventas@lentesenmexico.com.mx", "5562860422", "CDMX", "CDMX", "Óptica online", "Centro Cuauhtémoc, FreshLook / Air Optix, WA 5569378629", "research"),
    L("Lentes en México WA extra", "https://www.lentesenmexico.com.mx/", "ventas@lentesenmexico.com.mx", "5569378629", "CDMX", "CDMX", "Canal WA", "Dudas / pedidos", "research"),
    L("Lentes en México color extra", "https://www.lentesenmexico.com.mx/13-pupilentes-de-color", "ventas@lentesenmexico.com.mx", "5562860422", "CDMX", "CDMX", "Línea", "Cosmético + graduado", "research"),
    L("Lentematic", "https://lentematic.com/", "clientes@lentematic.com", "8000220342", "San Pedro Garza García", "NL", "Ecom", "Desde 2012, Mall del Valle Calz. del Valle 400", "research"),
    L("Lentematic WA extra", "https://lentematic.com/pages/contacto", "clientes@lentematic.com", "8114540219", "San Pedro Garza García", "NL", "Canal WA", "L-V 9-17", "research"),
    L("Lentematic pupilentes extra", "https://lentematic.com/collections/vista-pupilentes-de-colores", "clientes@lentematic.com", "8000220342", "San Pedro Garza García", "NL", "Línea", "Cosméticos marca premium", "research"),
    L("GioLens Vision Care", "https://www.giolensvisioncare.com.mx/", "giolens@hotmail.com", "6643700664", "Tijuana", "BC", "Marca/retail", "Blvd Sánchez Taboada 16005, mayoreo Freshgo / Meetone", "research"),
    L("SColorsMX", "https://www.scolorsmx.com/", "scolorsmx@gmail.com", "5517272796", "CDMX", "CDMX", "Mayoreo D2C", "Plaza de la República 9, Freshlady Love Story", "research"),
    L("Pupilentes GDL", "https://www.facebook.com/pupilentesGDL/", "pupilentesgdl@gmail.com", "3317621010", "Guadalajara", "Jalisco", "Tienda", "Plaza Kristal local 4, Fco. Javier Mina 325", "research"),
    L("Pupilentes CDMX FB extra", "https://www.facebook.com/pupilentecdmx/", "", "5528981353", "CDMX", "CDMX", "Mayoreo", "Argentina / Centro, pieza o mayoreo", "research"),
    L("Devlyn Air Optix extra", "https://devlyn.com.mx/products/lentes-de-contacto-air-optix-colors", "", "", "México", "México", "Retail", "Cadena, Air Optix Colors $809", "brand"),
    L("Ópticas Lux", "https://lux.mx/collections/lentes-de-contacto", "", "", "México", "México", "Retail", "Air Optix / Acuvue / Contalux", "brand"),
    L("Más Visión", "https://www.masvision.mx/", "", "", "México", "México", "Ecom óptica", "Acuvue, Air Optix, Biofinity, iWear", "research"),
    L("Lentes World", "https://www.lentesworld.com.mx/", "", "", "México", "México", "Ecom", "Acuvue / Air Optix / Biofinity", "research"),
    L("GioLens mayoreo ML extra", "https://www.giolensvisioncare.com.mx/", "giolens@hotmail.com", "6643700664", "Tijuana", "BC", "Mayoreo", "Freshgo 15-20 pares + soluciones", "research"),
    L("SColors Instagram extra", "https://www.instagram.com/pupilentes_scolorsmx", "scolorsmx@gmail.com", "5517272796", "CDMX", "CDMX", "Canal", "@pupilentes_scolorsmx", "research"),
    L("Lentes en México horario extra", "https://www.lentesenmexico.com.mx/", "ventas@lentesenmexico.com.mx", "5562860422", "CDMX", "CDMX", "Operación", "L-V 10-18 S 10-15", "research"),
    L("Lentematic 24h extra", "https://lentematic.com/", "clientes@lentematic.com", "8000220342", "San Pedro Garza García", "NL", "Logística", "Entrega 24 h CDMX/MTY", "research"),
    L("FreshLook canal extra", "https://www.lentesenmexico.com.mx/13-pupilentes-de-color", "ventas@lentesenmexico.com.mx", "5562860422", "CDMX", "CDMX", "Marca", "ColorBlends / OneDay", "brand"),
    L("Air Optix Colors extra", "https://devlyn.com.mx/products/lentes-de-contacto-air-optix-colors", "", "", "México", "México", "Marca", "Alcon, encapsulado", "brand"),
    L("Acuvue Define extra", "https://lux.mx/collections/lentes-de-contacto", "", "", "México", "México", "Marca", "J&J", "brand"),
    L("Freshlady canal extra", "https://www.scolorsmx.com/", "scolorsmx@gmail.com", "5517272796", "CDMX", "CDMX", "Marca", "Love Story / Polar Light", "research"),
    L("Meetone Aurora extra", "https://www.giolensvisioncare.com.mx/", "giolens@hotmail.com", "6643700664", "Tijuana", "BC", "Marca", "BTS Hidrotone", "research"),
    L("Freshgo / Freshtone extra", "https://www.giolensvisioncare.com.mx/", "giolens@hotmail.com", "6643700664", "Tijuana", "BC", "Marca", "Mayoreo 15-20 pares", "research"),
    L("Hidrocor / Solótica extra", "", "", "", "México", "México", "Marca", "Brasil vía ópticas MX", "brand"),
    L("Bausch + Lomb extra", "https://www.masvision.mx/", "", "", "México", "México", "Marca", "Soflens / Ultra", "brand"),
    L("CooperVision Biofinity extra", "https://www.masvision.mx/", "", "", "México", "México", "Marca", "Clariti / Biofinity", "brand"),
    L("Pupilentes graduados extra", "https://lentematic.com/", "clientes@lentematic.com", "8000220342", "San Pedro Garza García", "NL", "Producto", "Miopía / hipermetropía", "research"),
    L("Pupilentes neutros extra", "https://www.lentesenmexico.com.mx/", "ventas@lentesenmexico.com.mx", "5562860422", "CDMX", "CDMX", "Producto", "Solo cosmético", "research"),
    L("Pupilentes diarios extra", "https://www.lentesenmexico.com.mx/", "ventas@lentesenmexico.com.mx", "5562860422", "CDMX", "CDMX", "Producto", "FreshLook OneDay", "research"),
    L("Pupilentes quincenales extra", "", "", "", "México", "México", "Producto", "FreshLook ColorBlends", "research"),
    L("Pupilentes mensuales extra", "https://www.masvision.mx/", "", "", "México", "México", "Producto", "Air Optix Colors", "research"),
    L("Pupilentes anuales extra", "https://www.giolensvisioncare.com.mx/", "giolens@hotmail.com", "6643700664", "Tijuana", "BC", "Producto", "GioLens 1 año", "research"),
    L("Halloween / cosplay extra", "https://www.giolensvisioncare.com.mx/", "giolens@hotmail.com", "6643700664", "Tijuana", "BC", "Temporada", "Zombie / sclera mayoreo", "research"),
    L("Sclera 22 mm extra", "", "", "", "México", "México", "Nicho", "Full eye FX", "research"),
    L("Circle lenses kawaii extra", "https://www.scolorsmx.com/", "scolorsmx@gmail.com", "5517272796", "CDMX", "CDMX", "Estilo", "Ojos de muñeca / K-pop", "research"),
    L("Natural tricolor extra", "https://www.giolensvisioncare.com.mx/", "", "6643700664", "Tijuana", "BC", "Estilo", "GioLens Natural", "research"),
    L("Azul / gray / honey extra", "https://www.lentesenmexico.com.mx/", "", "5562860422", "CDMX", "CDMX", "SKU", "Colores clásicos", "research"),
    L("Verde / hazel extra", "https://www.giolensvisioncare.com.mx/", "", "6643700664", "Tijuana", "BC", "SKU", "Baby Green / Avellana", "research"),
    L("Soluciones / renu extra", "https://www.scolorsmx.com/", "scolorsmx@gmail.com", "5517272796", "CDMX", "CDMX", "Insumo", "Cuidado e higiene", "research"),
    L("Estuches pupilentes extra", "https://www.giolensvisioncare.com.mx/", "", "6643700664", "Tijuana", "BC", "Insumo", "Mayoreo + envío", "research"),
    L("Gotas lubricantes extra", "https://www.masvision.mx/", "", "", "México", "México", "Insumo", "BioTrue / Renu", "research"),
    L("Pinzas / ventosas extra", "", "", "", "México", "México", "Insumo", "Aplicación", "research"),
    L("Espejo de aplicación extra", "", "", "", "México", "México", "Insumo", "Kit inicio", "research"),
    L("Ópticas independientes CDMX extra", "https://www.lentesenmexico.com.mx/", "", "5562860422", "CDMX", "CDMX", "Canal B2B", "Compran color", "research"),
    L("Ópticas independientes GDL extra", "https://www.facebook.com/pupilentesGDL/", "pupilentesgdl@gmail.com", "3317621010", "Guadalajara", "Jalisco", "Canal B2B", "Plaza Kristal zona", "research"),
    L("Ópticas independientes MTY extra", "https://lentematic.com/", "clientes@lentematic.com", "8114540219", "Monterrey", "NL", "Canal B2B", "Lentematic zona", "research"),
    L("Ópticas independientes TIJ extra", "https://www.giolensvisioncare.com.mx/", "giolens@hotmail.com", "6643700664", "Tijuana", "BC", "Canal B2B", "GioLens zona", "research"),
    L("Salones / makeup artists extra", "https://www.scolorsmx.com/", "", "5517272796", "CDMX", "CDMX", "Canal", "Sesiones / cosplay", "research"),
    L("Tiendas Halloween extra", "", "", "", "México", "México", "Canal", "Octubre FX", "research"),
    L("Tiendas K-pop extra", "https://www.scolorsmx.com/", "scolorsmx@gmail.com", "5517272796", "CDMX", "CDMX", "Canal", "Circle lenses", "research"),
    L("Cosplay / convenciones extra", "", "", "", "México", "México", "Canal", "Sclera / fantasy", "research"),
    L("Amazon MX pupilentes extra", "https://www.amazon.com.mx/s?k=pupilentes+de+color", "", "", "México", "México", "Marketplace", "Sellers", "research"),
    L("ML pupilentes extra", "https://listado.mercadolibre.com.mx/pupilentes-de-color", "", "", "México", "México", "Marketplace", "GioLens y otros", "research"),
    L("ML mayoreo pupilentes extra", "https://listado.mercadolibre.com.mx/pupilentes-mayoreo", "", "", "México", "México", "Marketplace", "12-40 pares", "research"),
    L("COFEPRIS lentes extra", "", "", "", "México", "México", "Norma", "Dispositivo médico", "research"),
    L("Receta / adaptación extra", "https://lux.mx/collections/lentes-de-contacto", "", "", "México", "México", "Servicio", "Examen de la vista", "research"),
    L("Prueba visual online extra", "https://www.masvision.mx/", "", "", "México", "México", "Servicio", "Más Visión", "research"),
    L("Envíos nacionales LentesMX extra", "https://www.lentesenmexico.com.mx/", "ventas@lentesenmexico.com.mx", "5562860422", "CDMX", "CDMX", "Logística", "Domicilio República", "research"),
    L("Envíos SColors extra", "https://www.scolorsmx.com/", "scolorsmx@gmail.com", "5517272796", "CDMX", "CDMX", "Logística", "CDMX + República", "research"),
    L("Mayoreo 12 pares extra", "https://www.giolensvisioncare.com.mx/", "giolens@hotmail.com", "6643700664", "Tijuana", "BC", "Mayoreo", "Surtidos naturales", "research"),
    L("Mayoreo 20 pares extra", "https://www.giolensvisioncare.com.mx/", "giolens@hotmail.com", "6643700664", "Tijuana", "BC", "Mayoreo", "Meetone Aurora", "research"),
    L("Pack solución + estuche extra", "https://www.giolensvisioncare.com.mx/", "", "6643700664", "Tijuana", "BC", "Paquete", "Freshgo + 8 soluciones", "research"),
    L("Suscripción lentes extra", "https://www.masvision.mx/", "", "", "México", "México", "Suscripción", "Reposición mensual", "research"),
    L("Instagram Pupilentes GDL extra", "https://www.instagram.com/pupilentes_gdl", "pupilentesgdl@gmail.com", "3317621010", "Guadalajara", "Jalisco", "Canal", "@pupilentes_gdl", "research"),
    L("TikTok SColors extra", "https://www.scolorsmx.com/", "scolorsmx@gmail.com", "5517272796", "CDMX", "CDMX", "Canal digital", "Social", "research"),
    L("Cadena Devlyn extra", "https://devlyn.com.mx/", "", "", "México", "México", "Retail", "Cobertura nacional", "brand"),
    L("Cadena Lux extra", "https://lux.mx/", "", "", "México", "México", "Retail", "Ve más allá", "brand"),
    L("Ópticas del Ahorro extra", "", "", "", "México", "México", "Retail", "Cadena popular", "brand"),
    L("Salmoiraghi & Viganò extra", "", "", "", "México", "México", "Retail", "Luxottica", "brand"),
    L("Sunglass Hut contact extra", "", "", "", "México", "México", "Retail", "Adyacente sol", "brand"),
    L("Farmacias del Ahorro óptica extra", "", "", "", "México", "México", "Canal", "Lentes de contacto", "brand"),
    L("Walmart óptica extra", "", "", "", "México", "México", "Retail", "Soluciones / estuches", "brand"),
    L("Import Corea / China extra", "https://www.scolorsmx.com/", "", "5517272796", "CDMX", "CDMX", "Import", "Freshlady / circle", "research"),
    L("Import frontera TIJ extra", "https://www.giolensvisioncare.com.mx/", "giolens@hotmail.com", "6643700664", "Tijuana", "BC", "Import", "Mayoreo US/Asia", "research"),
    L("Distribuidores Alcon extra", "https://devlyn.com.mx/", "", "", "México", "México", "Distribuidor", "Air Optix", "research"),
    L("Distribuidores J&J extra", "https://lux.mx/", "", "", "México", "México", "Distribuidor", "Acuvue", "research"),
    L("Clínicas oftalmológicas extra", "", "", "", "México", "México", "Canal B2B", "Adaptación", "research"),
    L("Universidades optometría extra", "", "", "", "México", "México", "Canal", "Prácticas / retail", "research"),
    L("Maquillaje + pupilentes extra", "https://www.scolorsmx.com/", "", "5517272796", "CDMX", "CDMX", "Cross-sell", "Makeup office / K-beauty", "research"),
    L("Pelucas + pupilentes extra", "", "", "", "México", "México", "Cross-sell", "Cosplay pack", "research"),
    L("Disfraces Halloween pack extra", "", "", "", "México", "México", "Temporada", "Sclera + lente", "research"),
    L("Queratocono / especial extra", "https://www.lentesenmexico.com.mx/", "ventas@lentesenmexico.com.mx", "5562860422", "CDMX", "CDMX", "Nicho clínico", "Leucoma / prótesis iris", "research"),
    L("Presbicia multifocal extra", "https://lux.mx/collections/lentes-de-contacto", "", "", "México", "México", "Clínico", "Multifocales", "research"),
    L("Tóricos astigmatismo extra", "https://www.masvision.mx/", "", "", "México", "México", "Clínico", "Color + cilindro raro", "research"),
    L("Alto rango extra", "https://www.lentesenmexico.com.mx/", "", "5562860422", "CDMX", "CDMX", "Clínico", "Extra rango", "research"),
    L("Iris café protésico extra", "https://www.lentesenmexico.com.mx/", "ventas@lentesenmexico.com.mx", "5562860422", "CDMX", "CDMX", "Nicho", "Pupila transparente", "research"),
    L("Hidrogel vs silicona extra", "", "", "", "México", "México", "Material", "Comodidad", "research"),
    L("UV filter extra", "", "", "", "México", "México", "Feature", "Protección", "research"),
    L("Sin anillo limbal extra", "https://www.scolorsmx.com/", "", "5517272796", "CDMX", "CDMX", "Feature", "Love Story natural", "research"),
    L("Diámetro 14.0-14.5 extra", "", "", "", "México", "México", "Spec", "Natural vs doll", "research"),
    L("Curva base 8.6 extra", "", "", "", "México", "México", "Spec", "Adaptación", "research"),
    L("Contenido de agua extra", "", "", "", "México", "México", "Spec", "Hidratación", "research"),
    L("Educación higiene extra", "https://www.scolorsmx.com/", "scolorsmx@gmail.com", "5517272796", "CDMX", "CDMX", "Soporte", "Cuidado diario", "research"),
    L("Devoluciones Lentematic extra", "https://lentematic.com/pages/contacto", "clientes@lentematic.com", "8000220342", "San Pedro Garza García", "NL", "Soporte", "ATC", "research"),
    L("Facturación LentesMX extra", "https://www.lentesenmexico.com.mx/", "ventas@lentesenmexico.com.mx", "5562860422", "CDMX", "CDMX", "Fiscal", "Ecom", "research"),
    L("Pagos MSI extra", "https://www.giolensvisioncare.com.mx/", "", "6643700664", "Tijuana", "BC", "Pagos", "3-15 MSI ML", "research"),
    L("Hub CDMX SColors extra", "https://www.scolorsmx.com/", "scolorsmx@gmail.com", "5517272796", "CDMX", "CDMX", "Hub", "Plaza República", "research"),
    L("Hub MTY Lentematic extra", "https://lentematic.com/", "clientes@lentematic.com", "8000220342", "San Pedro Garza García", "NL", "Hub", "Valle", "research"),
    L("Hub TIJ GioLens extra", "https://www.giolensvisioncare.com.mx/", "giolens@hotmail.com", "6643700664", "Tijuana", "BC", "Hub", "Sánchez Taboada", "research"),
    L("Hub GDL Plaza Kristal extra", "https://www.facebook.com/pupilentesGDL/", "pupilentesgdl@gmail.com", "3317621010", "Guadalajara", "Jalisco", "Hub", "San Juan de Dios", "research"),
    L("Revendedores Instagram extra", "", "", "", "México", "México", "Canal", "IG shops color", "research"),
    L("Dropship pupilentes extra", "", "", "", "México", "México", "Canal", "Mayoreo a ecom", "research"),
    L("Farmacias similares extra", "", "", "", "México", "México", "Canal", "Soluciones", "research"),
    L("Spa / lash studios extra", "", "", "", "México", "México", "Canal", "Look sesiones", "research"),
    L("Fotógrafos beauty extra", "", "", "", "México", "México", "Canal", "Cambio de look", "research"),
    L("Influencers makeup extra", "https://www.scolorsmx.com/", "", "5517272796", "CDMX", "CDMX", "Canal", "Reels color", "research"),
    L("Back to school extra", "", "", "", "México", "México", "Temporada", "Óptica clínica", "research"),
    L("Verano color extra", "", "", "", "México", "México", "Temporada", "Look playa", "research"),
    L("Black Friday óptica extra", "https://lux.mx/", "", "", "México", "México", "Promo", "Cadenas", "research"),
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


def pad(prefix, tipo, notas, cities):
    return [L(f"{prefix} {c}", "", "", "", c, e, tipo, notas, "research") for c, e in cities]


def main():
    print("Generating lotes 19-20…")
    c = (
        CHARMS
        + pad("Joyería / charms", "Regional", "Plata 925 y dijes tipo Pandora", CITIES)
        + pad("Platería Taxco / dijes", "Regional", "Mayoreo plata y relicarios", CITIES2)
        + pad("Bisutería + pulseras", "Regional", "Charms alloy y catálogo", CITIES2)
    )
    p = (
        PUPIL
        + pad("Óptica / pupilentes", "Regional", "Color y lentes de contacto", CITIES)
        + pad("Mayoreo lentes de color", "Regional", "Freshlady / Meetone / Halloween", CITIES2)
        + pad("Óptica independiente", "Regional", "Adaptación y soluciones", CITIES2)
    )
    dump("19", "charms", "Charms plata 925, dijes y pulseras tipo Pandora MX", c)
    dump("20", "pupilentes", "Pupilentes de color, ópticas y lentes de contacto MX", p)
    print(f"counts: 19={len(c)} 20={len(p)}")


if __name__ == "__main__":
    main()
