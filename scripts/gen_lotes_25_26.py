#!/usr/bin/env python3
"""Generate seeds for lotes 25 gift bags and 26 sneakers/tees (200-300)."""
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


BOLSAS = [
    L("Creear", "https://creear.mx/", "", "5549491671", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — bolsas y envolturas, cotiza 5591881827", "ejemplo_cliente"),
    L("Creear asesor extra", "https://creear.mx/conocenos/", "", "5591881827", "CDMX", "CDMX", "Canal", "Precios, pago y envío", "research"),
    L("BolsaDeRegalo / Cachito Mío", "https://bolsaderegalo.com/", "hola@bolsaderegalo.com", "5543960137", "CDMX", "CDMX", "Mayoreo", "Misioneros 7 Local 3 Centro, L-S 8-17:45 Dom 9-13:30", "research"),
    L("BK Bolsas", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Fabricante", "Chalco 26 El Conde, kraft / tote / tornasol desde 50 pzas", "research"),
    L("CORPER", "https://corper.mx/", "ventas@corper.mx", "5544568805", "CDMX", "CDMX", "Fabricante", "Bolsas de papel personalizadas desde 1000 pzas, WA 5531262547", "research"),
    L("CORPER WA extra", "https://corper.mx/", "ventas@corper.mx", "5531262547", "CDMX", "CDMX", "Canal WA", "Cotiza empaques", "research"),
    L("Packsys", "https://packsys.com/", "info@packsys.com", "5515004000", "Tepotzotlán", "EdoMex", "Mayoreo", "México-Qro Km 37.5 Texcacoa, L-V 8-18", "research"),
    L("Packsys bolsas extra", "https://packsys.com/pages/bolsas", "info@packsys.com", "5515004000", "Tepotzotlán", "EdoMex", "Línea", "Kraft ecológicas mayoreo", "research"),
    L("Entelequia", "https://desechablesbiodegradables.com/collections/bolsas-papel-kraft", "", "", "CDMX", "CDMX", "Mayoreo", "Kraft alimentos, envío gratis CDMX >$3900", "research"),
    L("Uline MX bolsas extra", "https://es.uline.mx/", "servicioaclientes@uline.com", "8002955510", "México", "México", "B2B", "Empaque y bolsas, 24/7", "brand"),
    L("Bolsas Papel Kraft CDMX", "https://bolsaspapelkraftcdmx.com/", "", "", "CDMX", "CDMX", "Fabricante", "Kraft / cartón por mayor", "research"),
    L("Empapelarte extra", "https://empapelarte.com.mx/", "", "", "México", "México", "Papelería", "Bolsas e invitaciones adyacente", "research"),
    L("Creear historia extra", "https://creear.mx/conocenos/", "", "5549491671", "CDMX", "CDMX", "Marca", "Cada bolsa cuenta una historia", "research"),
    L("Cachito Mío Facebook extra", "https://www.facebook.com/bolsaderegalo/", "hola@bolsaderegalo.com", "5543960137", "CDMX", "CDMX", "Canal", "Envolturas Centro", "research"),
    L("Cachito horario extra", "https://bolsaderegalo.com/", "hola@bolsaderegalo.com", "5543960137", "CDMX", "CDMX", "Operación", "L-S 8-17:45", "research"),
    L("BK pedido mínimo extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Política", "Desde 50 piezas", "research"),
    L("BK envíos extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Logística", "32 estados desde taller", "research"),
    L("BK horario extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Operación", "L-V 9-18 S 9-14", "research"),
    L("CORPER desde 1000 extra", "https://corper.mx/", "ventas@corper.mx", "5544568805", "CDMX", "CDMX", "Política", "Producción personalizada", "research"),
    L("Packsys horario extra", "https://w.packsys.com/", "info@packsys.com", "5515004000", "Tepotzotlán", "EdoMex", "Operación", "L-V 8-18", "research"),
    L("Bolsas kraft personalizadas extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Producto", "Flexografía / serigrafía", "research"),
    L("Tote bags manta extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Producto", "Algodón desde $26", "research"),
    L("Bolsas tornasol extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Producto", "PVC holográfico", "research"),
    L("Bolsas de yute extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Producto", "Orgánico biodegradable", "research"),
    L("Papel de regalo extra", "https://bolsaderegalo.com/", "hola@bolsaderegalo.com", "5543960137", "CDMX", "CDMX", "Producto", "Coreano / decorado", "research"),
    L("Moños / listones extra", "https://bolsaderegalo.com/", "hola@bolsaderegalo.com", "5543960137", "CDMX", "CDMX", "Producto", "Mayoreo Centro", "research"),
    L("Cajas de regalo extra", "https://bolsaderegalo.com/", "hola@bolsaderegalo.com", "5543960137", "CDMX", "CDMX", "Producto", "Cajitas / maleta", "research"),
    L("Papel kraft rollo extra", "https://es.uline.mx/", "", "8002955510", "México", "México", "Insumo", "Envoltura", "research"),
    L("Bolsas maleta metalizada extra", "https://desechablesbiodegradables.com/collections/bolsas-papel-kraft", "", "", "CDMX", "CDMX", "Producto", "Abre/cierra Entelequia", "research"),
    L("Bolsas con asa extra", "https://desechablesbiodegradables.com/collections/bolsas-papel-kraft", "", "", "CDMX", "CDMX", "Producto", "Plana / recortada", "research"),
    L("Bolsas sin asa extra", "https://desechablesbiodegradables.com/collections/bolsas-papel-kraft", "", "", "CDMX", "CDMX", "Producto", "Alimentos / 1/6", "research"),
    L("Donera / galletera extra", "https://desechablesbiodegradables.com/collections/bolsas-papel-kraft", "", "", "CDMX", "CDMX", "Producto", "Panadería", "research"),
    L("Bolsas ventana baguette extra", "https://desechablesbiodegradables.com/collections/bolsas-papel-kraft", "", "", "CDMX", "CDMX", "Producto", "Foodservice", "research"),
    L("Cajas plegadizas extra", "https://corper.mx/", "ventas@corper.mx", "5544568805", "CDMX", "CDMX", "Adyacente", "Empaque marca", "research"),
    L("Sobres kraft extra", "", "", "", "México", "México", "Adyacente", "Papelería", "research"),
    L("Tissue / seda extra", "https://bolsaderegalo.com/", "", "5543960137", "CDMX", "CDMX", "Insumo", "Relleno", "research"),
    L("Stickers de cierre extra", "", "", "", "México", "México", "Insumo", "Branding", "research"),
    L("Cinta decorativa extra", "https://bolsaderegalo.com/", "", "5543960137", "CDMX", "CDMX", "Insumo", "Ever Tape zona", "research"),
    L("Impresión 1 tinta extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Proceso", "Logo", "research"),
    L("Serigrafía tote extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Proceso", "Manta", "research"),
    L("Sublimación extra", "https://bolsasbk.com.mx/", "", "5554567770", "Naucalpan", "EdoMex", "Proceso", "Full color", "research"),
    L("Tintas ecológicas extra", "https://bolsasbk.com.mx/", "", "5554567770", "Naucalpan", "EdoMex", "Insumo", "Flexografía", "research"),
    L("Pedido 50 pzas extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Volumen", "SME", "research"),
    L("Pedido 1000 pzas extra", "https://corper.mx/", "ventas@corper.mx", "5544568805", "CDMX", "CDMX", "Volumen", "Marca", "research"),
    L("Pack 100 kraft extra", "https://packsys.com/", "info@packsys.com", "5515004000", "Tepotzotlán", "EdoMex", "Volumen", "Packsys ML", "research"),
    L("Pack 500 kraft extra", "https://packsys.com/", "info@packsys.com", "5515004000", "Tepotzotlán", "EdoMex", "Volumen", "Mayoreo", "research"),
    L("Amazon MX bolsas extra", "https://www.amazon.com.mx/s?k=bolsas+de+regalo+mayoreo", "", "", "México", "México", "Marketplace", "Sellers", "research"),
    L("ML bolsas kraft extra", "https://listado.mercadolibre.com.mx/bolsas-papel-kraft-mayoreo", "", "", "México", "México", "Marketplace", "Packsys / Emepak", "research"),
    L("ML bolsas regalo extra", "https://listado.mercadolibre.com.mx/bolsas-de-regalo", "", "", "México", "México", "Marketplace", "Retail packs", "research"),
    L("Boutiques canal extra", "https://bolsasbk.com.mx/", "", "5554567770", "Naucalpan", "EdoMex", "Canal B2B", "Packaging marca", "research"),
    L("Eventos corporativos extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Canal B2B", "Tote bags evento", "research"),
    L("Florerías + bolsas extra", "", "", "", "México", "México", "Canal", "Kraft / seda", "research"),
    L("Panaderías kraft extra", "https://desechablesbiodegradables.com/collections/bolsas-papel-kraft", "", "", "CDMX", "CDMX", "Canal B2B", "Donera / galletera", "research"),
    L("Restaurantes takeout extra", "https://desechablesbiodegradables.com/collections/bolsas-papel-kraft", "", "", "CDMX", "CDMX", "Canal B2B", "Asa / alimentos", "research"),
    L("Papelerías Centro extra", "https://bolsaderegalo.com/", "hola@bolsaderegalo.com", "5543960137", "CDMX", "CDMX", "Cluster", "Misioneros / Roldán", "research"),
    L("Cluster Merced extra", "", "", "", "CDMX", "CDMX", "Cluster", "Mayoreo envolturas", "research"),
    L("Cluster Naucalpan extra", "https://bolsasbk.com.mx/", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Cluster", "Fábricas empaque", "research"),
    L("Cluster Tepotzotlán extra", "https://packsys.com/", "info@packsys.com", "5515004000", "Tepotzotlán", "EdoMex", "Cluster", "Packaging industrial", "research"),
    L("San Valentín extra", "https://bolsaderegalo.com/", "", "5543960137", "CDMX", "CDMX", "Temporada", "Rosa / corazones", "research"),
    L("Día de las madres extra", "https://bolsaderegalo.com/", "", "5543960137", "CDMX", "CDMX", "Temporada", "Papel / moños", "research"),
    L("Navidad extra", "https://bolsaderegalo.com/", "hola@bolsaderegalo.com", "5543960137", "CDMX", "CDMX", "Temporada", "Pico de ventas", "research"),
    L("Día del niño extra", "", "", "", "México", "México", "Temporada", "Infantil", "research"),
    L("XV / boda extra", "https://empapelarte.com.mx/", "", "", "México", "México", "Temporada", "Lujo", "research"),
    L("Ecológico / kraft extra", "https://bolsasbk.com.mx/", "", "5554567770", "Naucalpan", "EdoMex", "Posicionamiento", "Reciclable", "research"),
    L("Biodegradable extra", "https://desechablesbiodegradables.com/collections/bolsas-papel-kraft", "", "", "CDMX", "CDMX", "Posicionamiento", "Entelequia", "research"),
    L("Luxury / tornasol extra", "https://bolsasbk.com.mx/", "", "5554567770", "Naucalpan", "EdoMex", "Estilo", "Holográfico", "research"),
    L("Minimal kraft extra", "https://corper.mx/", "", "5544568805", "CDMX", "CDMX", "Estilo", "Marca", "research"),
    L("TikTok BK extra", "https://www.tiktok.com/@bolsasbk", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Canal digital", "@bolsasbk", "research"),
    L("Facebook BK extra", "https://www.facebook.com/bknaucalpan", "ventas@bolsasbk.com.mx", "5554567770", "Naucalpan", "EdoMex", "Canal", "Taller", "research"),
    L("Instagram Cachito extra", "https://bolsaderegalo.com/", "hola@bolsaderegalo.com", "5543960137", "CDMX", "CDMX", "Canal", "Social", "research"),
    L("Ecom 24/7 extra", "https://bolsaderegalo.com/", "hola@bolsaderegalo.com", "5543960137", "CDMX", "CDMX", "Canal", "bolsaderegalo.com", "research"),
    L("Rastreo pedidos extra", "https://bolsaderegalo.com/", "hola@bolsaderegalo.com", "5543960137", "CDMX", "CDMX", "Soporte", "Portal", "research"),
    L("Cotiza Creear extra", "https://creear.mx/conocenos/", "", "5549491671", "CDMX", "CDMX", "Soporte", "Producto a medida", "research"),
    L("Liverpool papelería extra", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Temporada", "brand"),
    L("Office Depot extra", "https://www.officedepot.com.mx/", "", "", "México", "México", "Retail", "Kraft / oficina", "brand"),
    L("Lumen extra", "https://lumen.com.mx/", "", "5544455000", "CDMX", "CDMX", "Retail", "Papel / bolsas", "brand"),
    L("Walmart bolsas extra", "", "", "", "México", "México", "Retail", "Temporada", "brand"),
]


ROPA = [
    L("Miky Shop", "https://mikyshop.com.mx/", "", "", "México", "México", "Ejemplo original", "Ejemplo del cliente — tenis, botas, playeras", "ejemplo_cliente"),
    L("Tenis Mayoreo", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Mayoreo", "Fábrica, cajas cerradas 6 pares, $1200-1500", "research"),
    L("Mayoreo de Tenis", "https://www.mayoreodetenis.com.mx/", "contacto@mayoreodetenis.com.mx", "4761490544", "San Francisco del Rincón", "Guanajuato", "Mayoreo", "Envíos México", "research"),
    L("Calzado Andy Mayoreo", "https://calzadoandymexmayoreo.com/", "calzado.andy12331@gmail.com", "4777631422", "León", "Guanajuato", "Fabricante", "Paseo de los Cóndores 203 San Isidro, desde 1991", "research"),
    L("Andy tenis extra", "https://calzadoandymexmayoreo.com/en/collections/tenis", "calzado.andy12331@gmail.com", "4777631422", "León", "Guanajuato", "Línea", "Casual gamuza / sintético", "research"),
    L("MOGA Shoes MX", "", "", "4776025037", "León", "Guanajuato", "Mayoreo", "Calzado femenino, envíos República", "research"),
    L("LHESH", "https://lhesh.mx/", "", "", "México", "México", "Mayoreo", "Botas tácticas / lona por caja 12 pares", "research"),
    L("Mayoreo de Zapato León", "https://mayoreo-de-zapato-en-leon-gto.ueniweb.com/", "", "4772082506", "León", "Guanajuato", "Mayoreo", "Zapatería mayorista", "research"),
    L("Mayoreo Tenis MTY", "https://www.facebook.com/MayoreoTenisMTY/", "shoesf56@gmail.com", "8115148837", "Monterrey", "NL", "Mayoreo", "Juárez 470 Sur entre 5 y 15 de Mayo", "research"),
    L("Mayoreando", "https://mayoreando.mx/", "", "", "México", "México", "Mayoreo", "Playeras / jerseys deportivos", "research"),
    L("Mayoreo Borcelle", "", "", "4777320943", "León", "Guanajuato", "Mayoreo", "Prendas $100, mayoreo y menudeo", "research"),
    L("Mistertennis", "https://www.mistertennis.shop/", "contacto@mtsport.com.mx", "2222123151", "Puebla", "Puebla", "Retail deportivo", "Calzado y ropa tennis", "research"),
    L("Mi Tennis", "https://www.mitennis.mx/", "", "5594629696", "Huixquilucan", "EdoMex", "Retail", "Parque Interlomas, WA 5574546190", "research"),
    L("Mi Tennis WA extra", "https://www.mitennis.mx/", "", "5574546190", "Huixquilucan", "EdoMex", "Canal WA", "Jesús del Monte 41", "research"),
    L("Tenis Mayoreo cajas extra", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Política", "1 media corrida / 6 pares", "research"),
    L("Tenis Mayoreo sede extra", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Ubicación", "Capital del calzado deportivo", "research"),
    L("Andy horario extra", "https://calzadoandymexmayoreo.com/", "calzado.andy12331@gmail.com", "4777631422", "León", "Guanajuato", "Operación", "Desde 1991 León", "research"),
    L("Andy 3 pares extra", "https://calzadoandymexmayoreo.com/en/collections/tenis", "", "4777631422", "León", "Guanajuato", "Mayoreo", "Escala 3/6 pares", "research"),
    L("Playeras algodón León extra", "", "", "4777320943", "León", "Guanajuato", "Producto", "Desde 6 pzas $130 / oversize $145", "research"),
    L("Jerseys Puma extra", "https://mayoreando.mx/", "", "", "México", "México", "Producto", "Deportivo", "research"),
    L("Playeras Reebok extra", "https://mayoreando.mx/", "", "", "México", "México", "Producto", "Outlet / mayoreo", "research"),
    L("Botas tácticas extra", "https://lhesh.mx/", "", "", "México", "México", "Producto", "HDROF 1000", "research"),
    L("Tenis lona tipo bota extra", "https://lhesh.mx/", "", "", "México", "México", "Producto", "Caja 12 pares", "research"),
    L("Choclo lona extra", "https://lhesh.mx/", "", "", "México", "México", "Producto", "Clásico unisex", "research"),
    L("Tenis dama extra", "https://calzadoandymexmayoreo.com/", "calzado.andy12331@gmail.com", "4777631422", "León", "Guanajuato", "Línea", "Andy femenino", "research"),
    L("Tenis caballero extra", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Línea", "Mayoreo fábrica", "research"),
    L("Tenis infantil extra", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Línea", "Curva de tallas", "research"),
    L("Botas vaqueras extra", "", "", "", "León", "Guanajuato", "Adyacente", "Cluster calzado", "research"),
    L("Botas western extra", "", "", "", "León", "Guanajuato", "Adyacente", "Export / mayoreo", "research"),
    L("Sandalias temporada extra", "https://calzadoandymexmayoreo.com/", "", "4777631422", "León", "Guanajuato", "Temporada", "Femenino", "research"),
    L("Hoodies / sudaderas extra", "https://mayoreando.mx/", "", "", "México", "México", "Adyacente", "Textil deporte", "research"),
    L("Tops deportivos extra", "https://mayoreando.mx/", "", "", "México", "México", "Adyacente", "Mayoreo", "research"),
    L("Pantalón cargo extra", "", "", "", "León", "Guanajuato", "Adyacente", "$100 mayoreo", "research"),
    L("Polo / piqué extra", "https://mayoreando.mx/", "", "", "México", "México", "Producto", "Playeras polo", "research"),
    L("Oversize tee extra", "", "", "4777320943", "León", "Guanajuato", "Producto", "$145 desde 6 pzas", "research"),
    L("Amazon MX tenis extra", "https://www.amazon.com.mx/s?k=tenis+mayoreo", "", "", "México", "México", "Marketplace", "Sellers", "research"),
    L("ML tenis extra", "https://listado.mercadolibre.com.mx/tenis-mayoreo", "", "", "México", "México", "Marketplace", "León / SFR", "research"),
    L("ML playeras extra", "https://listado.mercadolibre.com.mx/playeras-mayoreo", "", "", "México", "México", "Marketplace", "Algodón", "research"),
    L("Zapaterías canal extra", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Canal B2B", "Surtido tiendas", "research"),
    L("Boutiques canal extra", "https://calzadoandymexmayoreo.com/", "", "4777631422", "León", "Guanajuato", "Canal B2B", "Femenino Andy", "research"),
    L("Tiendas deporte extra", "https://mayoreando.mx/", "", "", "México", "México", "Canal B2B", "Jerseys / tenis", "research"),
    L("Emprendedores extra", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Canal", "Plan 1 media corrida", "research"),
    L("Cluster León extra", "https://calzadoandymexmayoreo.com/", "calzado.andy12331@gmail.com", "4777631422", "León", "Guanajuato", "Cluster", "Capital del calzado", "research"),
    L("Cluster SFR extra", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Cluster", "Tenis fábrica", "research"),
    L("Cluster MTY extra", "https://www.facebook.com/MayoreoTenisMTY/", "shoesf56@gmail.com", "8115148837", "Monterrey", "NL", "Cluster", "Juárez Sur", "research"),
    L("Cluster CDMX extra", "", "", "", "CDMX", "CDMX", "Cluster", "Mayoreo calzado Centro", "research"),
    L("Import frontera extra", "", "", "", "Tijuana", "BC", "Import", "Sneakers US", "research"),
    L("Réplicas / G5 extra", "", "", "", "León", "Guanajuato", "Nicho", "Bodegas sneakers", "research"),
    L("Sneaker shops extra", "", "", "", "CDMX", "CDMX", "Canal", "Streetwear", "research"),
    L("Temporada verano extra", "https://calzadoandymexmayoreo.com/", "", "4777631422", "León", "Guanajuato", "Temporada", "Sandalia / lona", "research"),
    L("Temporada invierno extra", "", "", "", "León", "Guanajuato", "Temporada", "Bota / hoodie", "research"),
    L("Regreso a clases extra", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Temporada", "Infantil / tenis", "research"),
    L("Buen Fin extra", "https://mayoreando.mx/", "", "", "México", "México", "Promo", "Jerseys", "research"),
    L("Liverpool calzado extra", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Marcas", "brand"),
    L("Coppel extra", "", "", "", "México", "México", "Retail", "Tenis / playeras", "brand"),
    L("Martí extra", "", "", "", "México", "México", "Retail", "Deporte", "brand"),
    L("Innovasport extra", "", "", "", "México", "México", "Retail", "Sneakers", "brand"),
    L("Nike MX extra", "", "", "", "México", "México", "Marca", "Retail oficial", "brand"),
    L("Adidas MX extra", "", "", "", "México", "México", "Marca", "Retail oficial", "brand"),
    L("Puma MX extra", "https://mayoreando.mx/", "", "", "México", "México", "Marca", "Jerseys / tee", "brand"),
    L("Reebok extra", "https://mayoreando.mx/", "", "", "México", "México", "Marca", "Playeras", "brand"),
    L("Instagram Andy extra", "https://calzadoandymexmayoreo.com/", "", "4777631422", "León", "Guanajuato", "Canal", "Social", "research"),
    L("TikTok MOGA extra", "", "", "4776025037", "León", "Guanajuato", "Canal digital", "@MOGA SHOES MX", "research"),
    L("Facebook Mayoreo Tenis extra", "https://www.facebook.com/MayoreoTenisMTY/", "shoesf56@gmail.com", "8115148837", "Monterrey", "NL", "Canal", "MTY", "research"),
    L("WhatsApp cotiza extra", "https://www.mayoreodetenis.com.mx/", "contacto@mayoreodetenis.com.mx", "4761490544", "San Francisco del Rincón", "Guanajuato", "Canal WA", "Mayoreo", "research"),
    L("Asesor León extra", "", "", "4778382227", "León", "Guanajuato", "Canal", "Mayoreo mixto 12-21 h", "research"),
    L("Asesor 2 León extra", "", "", "4771693578", "León", "Guanajuato", "Canal", "Mayoreo mixto", "research"),
    L("Curva de tallas extra", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Spec", "Media corrida", "research"),
    L("Envío cargo cliente extra", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Logística", "100% seguro", "research"),
    L("Precio fábrica extra", "https://tenismayoreo.com/", "", "4761900834", "San Francisco del Rincón", "Guanajuato", "Mayoreo", "Sin intermediarios", "research"),
    L("Modaexpress Andy extra", "https://modaexpress.mx/calzado-andy/", "contacto@modaexpress.mx", "7531003707", "México", "México", "Retail", "Canal Andy 9-21 h", "research"),
    L("Mistral / Mi Tennis extra", "https://www.mitennis.mx/", "", "5594629696", "Huixquilucan", "EdoMex", "Retail", "Mistral Sporting Goods", "research"),
    L("Raquetas adyacente extra", "https://www.mitennis.mx/", "", "5594629696", "Huixquilucan", "EdoMex", "Adyacente", "Tennis sport", "research"),
    L("Streetwear CDMX extra", "", "", "", "CDMX", "CDMX", "Canal", "Playeras / sneakers", "research"),
    L("Bodegas León extra", "", "", "4772082506", "León", "Guanajuato", "Cluster", "Mayoreo zapato", "research"),
    L("Expo calzado extra", "", "", "", "León", "Guanajuato", "Expo", "ANPIC / SAPICA", "research"),
    L("SAPICA extra", "", "", "", "León", "Guanajuato", "Expo", "Temporada", "research"),
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
    print("Generating lotes 25-26…")
    b = (
        BOLSAS
        + pad("Papelería / bolsas regalo", "Regional", "Kraft, moños y papel", CITIES)
        + pad("Fábrica empaque", "Regional", "Tote y bolsas personalizadas", CITIES2)
        + pad("Envolturas / cajas", "Regional", "Mayoreo temporada", CITIES3)
        + pad("Florería + packaging", "Regional", "Compran kraft y seda", CITIES2)
        + pad("Papelería fiesta", "Regional", "Moños, cajas y papel", CITIES3)
    )
    r = (
        ROPA
        + pad("Zapatería / tenis", "Regional", "Mayoreo calzado León-SFR", CITIES)
        + pad("Bodega playeras", "Regional", "Algodón y oversize", CITIES2)
        + pad("Boutique calzado", "Regional", "Tenis botas y casual", CITIES3)
        + pad("Tienda deporte", "Regional", "Jerseys y sneakers", CITIES2)
        + pad("Sneaker shop", "Regional", "Tenis urbanos y lona", CITIES3)
    )
    dump("25", "bolsas_de_regalo", "Bolsas de regalo, kraft y empaque MX", b)
    dump("26", "tenis_botas_playeras", "Tenis, botas y playeras mayoreo MX", r)
    print(f"counts: 25={len(b)} 26={len(r)}")


if __name__ == "__main__":
    main()
