#!/usr/bin/env python3
"""Generate seeds for lotes 21 press-on nails and 22 tarot/velas (200-300)."""
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


UNAS = [
    L("Unika Studio México", "https://unikastudiomexico.com/", "", "", "México", "México", "Ejemplo original", "Ejemplo del cliente — press on e insumos", "ejemplo_cliente"),
    L("Círculo B", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Mayoreo", "Plaza Kristal local 5, Independencia Ote 316, L-S 9-20:30", "research"),
    L("Círculo B 2o tel extra", "https://circulob.mx/", "contacto@circulob.mx", "2383835992", "Tehuacán", "Puebla", "Mayoreo", "Independencia Ote 113 Centro", "research"),
    L("Círculo B 3er tel extra", "https://circulob.mx/", "contacto@circulob.mx", "2381080231", "Tehuacán", "Puebla", "Canal", "ATC / WhatsApp", "research"),
    L("Nails Shop SLP", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Mayoreo", "Río Verde 315 Genovevo Rivas, mín. $6000, Fantasy/Organic/Wapizima", "research"),
    L("Nails Shop WA extra", "https://www.nailsshop.com.mx/", "", "4443288908", "San Luis Potosí", "SLP", "Canal WA", "Subdistribuidor desde $16k", "research"),
    L("Nails Shop press on extra", "https://www.nailsshop.com.mx/products/tips-press-on-fantasy", "", "4448096424", "San Luis Potosí", "SLP", "Línea", "Tips press on / almond short Fantasy", "research"),
    L("Kiss México", "https://www.kissmexico.mx/collections/press-on", "", "", "México", "México", "Marca", "imPRESS press-on, sin pegamento extra", "brand"),
    L("Fantasy Nails Shop CDMX", "https://www.facebook.com/fantasynailscdmx/", "", "5579007784", "CDMX", "CDMX", "Mayoreo", "Envíos nacionales e internacionales", "research"),
    L("Wapizima", "https://wapizima.shop/", "antonio@wapizima.info", "", "México", "México", "Marca", "Mayoreo nacional, Av Benito Juárez Sur 105-308", "research"),
    L("Wapizima CDMX academia extra", "https://www.facebook.com/p/Wapizima-CDMX-100064729597051/", "", "", "CDMX", "CDMX", "Educación", "Pino Suárez 41 piso 7", "research"),
    L("Cololab press on", "", "", "5539946917", "CDMX", "CDMX", "Tienda", "Izazaga 89 mezanine local 108, L-D 11-18", "research"),
    L("Mi Shop MX", "https://www.mishop.mx/", "", "", "México", "México", "Mayoreo", "Press on y accesorios belleza", "research"),
    L("Organic Nails canal extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Protein bond / rubber gel", "brand"),
    L("Fantasy Nails canal extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Acrílico Kiss Me / gel", "brand"),
    L("MC Nails canal extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Tips press on mayoreo", "brand"),
    L("GC Nails canal extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Belcolor pack 50", "brand"),
    L("Nail Factory extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Profesional", "brand"),
    L("Studio Nails extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Insumos", "brand"),
    L("Mussa extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Gel / acrílico", "brand"),
    L("One Shot extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Pinturas", "brand"),
    L("Obelli extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Profesional", "brand"),
    L("María Cibeles extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Marca", "Insumos", "brand"),
    L("Círculo B envíos extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Logística", "Gratis >$1999, 32 estados", "research"),
    L("Círculo B horario extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Operación", "L-S 9-20:30 Dom 9-15", "research"),
    L("Círculo B Facebook extra", "https://www.facebook.com/distribuidoracirculob/", "contacto@circulob.mx", "2383835992", "Tehuacán", "Puebla", "Canal", "Distribuidora", "research"),
    L("Tips press on extra", "https://www.nailsshop.com.mx/products/tips-press-on-fantasy", "", "4448096424", "San Luis Potosí", "SLP", "Producto", "Almond / coffin / square", "research"),
    L("Pegamento press on extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Insumo", "Nail glue", "research"),
    L("Adhesivo imPRESS extra", "https://www.kissmexico.mx/collections/press-on", "", "", "México", "México", "Insumo", "Doble capa patentada", "research"),
    L("Lima / buffer extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Insumo", "Prep", "research"),
    L("Cutícula / palito extra", "https://circulob.mx/", "", "2381270502", "Tehuacán", "Puebla", "Insumo", "Prep", "research"),
    L("Piedritas / cristales extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Insumo", "Decoración", "research"),
    L("Esmaltes gel extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Producto", "Gelish / soak off", "research"),
    L("Acrílico monómero extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Producto", "Fantasy / Organic", "research"),
    L("Gel UV / rubber extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Producto", "Acry Love 15 ml", "research"),
    L("Primer / protein bond extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Insumo", "Organic Nails", "research"),
    L("Top coat extra", "", "", "", "México", "México", "Insumo", "Charm / sellador", "research"),
    L("Lámpara LED/UV extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Equipo", "Cabina", "research"),
    L("Drill / torno extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Equipo", "Manicure", "research"),
    L("Brocas carbide extra", "", "", "", "México", "México", "Consumible", "Torno", "research"),
    L("Formas / dual forms extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Insumo", "MC Nails", "research"),
    L("Tips coffin extra", "", "", "", "México", "México", "Producto", "Press on", "research"),
    L("Tips stiletto extra", "", "", "", "México", "México", "Producto", "Press on", "research"),
    L("Tips square extra", "", "", "", "México", "México", "Producto", "Press on", "research"),
    L("Tips almond extra", "https://www.nailsshop.com.mx/products/tips-press-on-fantasy", "", "4448096424", "San Luis Potosí", "SLP", "Producto", "Short Fantasy", "research"),
    L("Kits inicio nail tech extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Paquete", "Básicos + resina + gel", "research"),
    L("Paquetes acrílico Fantasy extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Paquete", "Mayoreo", "research"),
    L("Halloween press on extra", "https://www.kissmexico.mx/collections/press-on", "", "", "México", "México", "Temporada", "imPRESS glow", "research"),
    L("XV / novia press on extra", "", "", "", "México", "México", "Temporada", "Sets diseñadora", "research"),
    L("Mayoreo Centro CDMX extra", "", "", "5539946917", "CDMX", "CDMX", "Cluster", "Izazaga / Merced belleza", "research"),
    L("Mayoreo Tehuacán extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Hub", "Círculo B zona", "research"),
    L("Mayoreo SLP extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Hub", "Nails Shop zona", "research"),
    L("Mayoreo GDL extra", "", "", "", "Guadalajara", "Jalisco", "Cluster", "Insumos uñas", "research"),
    L("Mayoreo MTY extra", "", "", "", "Monterrey", "NL", "Cluster", "Insumos uñas", "research"),
    L("Amazon MX press on extra", "https://www.amazon.com.mx/s?k=uñas+press+on", "", "", "México", "México", "Marketplace", "Kiss / genéricas", "research"),
    L("ML press on extra", "https://listado.mercadolibre.com.mx/unas-press-on", "", "", "México", "México", "Marketplace", "MC Nails / Kiss", "research"),
    L("ML Organic Nails extra", "https://listado.mercadolibre.com.mx/productos-organic-nails-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo", "research"),
    L("Salones nail tech canal extra", "", "", "", "CDMX", "CDMX", "Canal B2B", "Compran insumos", "research"),
    L("Academias de uñas extra", "https://www.facebook.com/p/Wapizima-CDMX-100064729597051/", "", "", "CDMX", "CDMX", "Educación", "Wapizima Pino Suárez", "research"),
    L("Home nail techs extra", "", "", "", "México", "México", "Canal", "Revenden press on", "research"),
    L("Bazares / Marchanta extra", "", "", "", "CDMX", "CDMX", "Canal", "Pericoapa press on", "research"),
    L("Liverpool Kiss extra", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "imPRESS", "brand"),
    L("Walmart press on extra", "", "", "", "México", "México", "Retail", "Kiss / genéricas", "brand"),
    L("Importación Nails Shop extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Import", "Novedades mercado", "research"),
    L("Subdistribuidores extra", "https://www.nailsshop.com.mx/", "", "4443288908", "San Luis Potosí", "SLP", "Canal B2B", "Inversión $16k+", "research"),
    L("Spa + uñas extra", "", "", "", "México", "México", "Canal", "Cross-sell", "research"),
    L("Pestañas + press on extra", "", "", "", "México", "México", "Cross-sell", "Mismo salón", "research"),
    L("Pedicure insumos extra", "https://circulob.mx/", "", "2381270502", "Tehuacán", "Puebla", "Adyacente", "Belleza pies", "research"),
    L("Cuidado cutícula extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Adyacente", "Aceites", "research"),
    L("Stickers / foil extra", "https://circulob.mx/", "", "2381270502", "Tehuacán", "Puebla", "Insumo", "Nail art", "research"),
    L("Pigmentos chrome extra", "", "", "", "México", "México", "Insumo", "Espejo", "research"),
    L("Polygel extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Producto", "Híbrido", "research"),
    L("Builder gel extra", "", "", "", "México", "México", "Producto", "Estructura", "research"),
    L("Soft gel tips extra", "", "", "", "México", "México", "Producto", "Tendencia", "research"),
    L("Remover acetona extra", "", "", "", "México", "México", "Consumible", "Soak off", "research"),
    L("Sanitizante / alcohol extra", "", "", "", "México", "México", "Higiene", "Estación", "research"),
    L("Toallas sin pelusa extra", "", "", "", "México", "México", "Consumible", "Prep", "research"),
    L("Displays / packaging extra", "", "", "", "México", "México", "Insumo", "Press on D2C", "research"),
    L("Cajas de set extra", "", "", "", "México", "México", "Insumo", "Branding", "research"),
    L("Nail techs Instagram extra", "", "", "", "México", "México", "Canal", "D2C sets", "research"),
    L("TikTok press on extra", "", "", "", "México", "México", "Canal digital", "Tendencia", "research"),
    L("Cursos Wapizima extra", "https://wapizima.shop/", "antonio@wapizima.info", "", "México", "México", "Educación", "Técnicas acrílico", "research"),
    L("Distribuidores Wapizima extra", "https://wapizima.shop/", "antonio@wapizima.info", "", "México", "México", "Canal B2B", "Únete por WA", "research"),
    L("Facturación Círculo B extra", "https://circulob.mx/", "contacto@circulob.mx", "2381270502", "Tehuacán", "Puebla", "Fiscal", "Ecom", "research"),
    L("Pagos transferencia Nails extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Pagos", "Depósito / SPEI", "research"),
    L("Envíos nacionales Nails extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Logística", "Zona por CP", "research"),
    L("Mínimo pedido $6000 extra", "https://www.nailsshop.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Política", "2 pzas mín.", "research"),
    L("Regreso a clases uñas extra", "", "", "", "México", "México", "Temporada", "Sets cortos", "research"),
    L("San Valentín sets extra", "", "", "", "México", "México", "Temporada", "Rojos / corazones", "research"),
    L("Navidad glitter extra", "", "", "", "México", "México", "Temporada", "Press on", "research"),
    L("French / babyboomer extra", "", "", "", "México", "México", "Estilo", "Clásico", "research"),
    L("Nail art 3D extra", "", "", "", "México", "México", "Estilo", "Escultura", "research"),
    L("Matte vs gloss extra", "", "", "", "México", "México", "Acabado", "Top", "research"),
    L("Tallas XS-XL extra", "", "", "", "México", "México", "Spec", "Press on fit", "research"),
    L("Reutilizables extra", "", "", "", "México", "México", "Feature", "Sets diseñadora", "research"),
    L("Desechables retail extra", "https://www.kissmexico.mx/collections/press-on", "", "", "México", "México", "Feature", "imPRESS", "research"),
    L("Salón vs D2C extra", "", "", "", "México", "México", "Canal", "Dos modelos", "research"),
    L("Insumos pestañas extra", "", "", "", "México", "México", "Adyacente", "Mismo mayoreo", "research"),
    L("Cejas / laminado extra", "", "", "", "México", "México", "Adyacente", "Salón", "research"),
    L("Skin care uñas extra", "https://circulob.mx/", "", "2381270502", "Tehuacán", "Puebla", "Adyacente", "Belleza Círculo B", "research"),
    L("Cherry Pop Spa extra", "", "", "2223307517", "CDMX", "CDMX", "Salón", "Plaza Guardiola 108, sets IG", "research"),
    L("Apartado 12 press on extra", "", "", "", "CDMX", "CDMX", "Mayoreo", "Local 10 Centro", "research"),
    L("Merced belleza extra", "", "", "", "CDMX", "CDMX", "Cluster", "Insumos populares", "research"),
    L("Pino Suárez uñas extra", "https://www.facebook.com/p/Wapizima-CDMX-100064729597051/", "", "", "CDMX", "CDMX", "Cluster", "Academias + supply", "research"),
]


ESO = [
    L("Pinka", "https://pinka.com.mx/tarots-y-oraculos/tarot/", "", "", "México", "México", "Ejemplo original", "Ejemplo del cliente — tarots y oráculos", "ejemplo_cliente"),
    L("Stellum", "https://www.stellum.mx/", "tienda.stellum@icloud.com", "8123619626", "Monterrey", "NL", "Tienda", "Plaza Fiesta San Agustín 222, velas mágicas y tarot", "research"),
    L("Tienda Esotérica MX", "https://tiendaesoterica.com.mx/", "", "", "México", "México", "Ecom", "Tarot, velas, wicca, amuletos, runas", "research"),
    L("Esotérica MX mayoreo extra", "https://esotericamx.com/collections/mayoreo-joyeria", "", "", "México", "México", "Mayoreo", "Kits, velas, tarot, péndulos", "research"),
    L("Magic Ways", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "D2C", "Paseo San Isidro 202, velas soya / cuarzos / tarot", "research"),
    L("Tarots del Mundo", "https://tarotsdelmundo.com/", "info@tarotsdelmundo.com", "5519983301", "CDMX", "CDMX", "Tienda", "Horacio 136 Polanco, 555335000 / WA 5590228817", "research"),
    L("Tarots del Mundo Polanco extra", "https://tarotsdelmundo.com/", "info@tarotsdelmundo.com", "5555311300", "CDMX", "CDMX", "Sucursal", "Frente Liverpool Polanco", "research"),
    L("Tarots del Mundo WA extra", "https://tarotsdelmundo.com/pages/contacto", "info@tarotsdelmundo.com", "5590228817", "CDMX", "CDMX", "Canal WA", "Soporte", "research"),
    L("Rinconcito Mágico", "https://www.rinconcitomagico.mx/", "info@rinconcitomagico.mx", "7711429045", "Pachuca", "Hidalgo", "Tienda", "Cita previa, velas y esoterismo", "research"),
    L("Tarot México León", "https://tarotmexico.com.mx/", "informes@tarotmexico.com", "4771843418", "León", "Guanajuato", "Servicio + retail", "Loma 103 Jardines del Moral", "research"),
    L("Tarot México email extra", "https://tarotmexico.com.mx/contactame/", "tarotevolutivoleon@gmail.com", "4771843418", "León", "Guanajuato", "Canal", "Consultas", "research"),
    L("Los 7 Arcángeles Boutique", "", "", "5536431447", "CDMX", "CDMX", "Tienda", "Av. Cuauhtémoc 24 local 1, lecturas + retail", "research"),
    L("Tiara Mayorista Uruguay", "", "", "", "CDMX", "CDMX", "Mayoreo", "República de Uruguay 66, velas / santería / Yoruba", "research"),
    L("Plaza del Artesano extra", "", "", "", "CDMX", "CDMX", "Cluster", "Uruguay 75, incienso y ritual", "research"),
    L("Stellum velas extra", "https://www.stellum.mx/", "tienda.stellum@icloud.com", "8123619626", "Monterrey", "NL", "Línea", "Velas mágicas / aguas astrales", "research"),
    L("Stellum tarots extra", "https://www.stellum.mx/", "tienda.stellum@icloud.com", "8123619626", "Monterrey", "NL", "Línea", "Tarots y oráculos", "research"),
    L("Magic Ways velas extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Línea", "Abre caminos / palo santo / spell candles", "research"),
    L("Magic Ways horario extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Operación", "Mar-Sáb 11-19", "research"),
    L("Magic Ways envío extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Logística", "Gratis >$1400, pickup tienda", "research"),
    L("Pinka tarot extra", "https://pinka.com.mx/tarots-y-oraculos/tarot/", "", "", "México", "México", "Línea", "Barajas y oráculos", "research"),
    L("Rider Waite extra", "https://pinka.com.mx/tarots-y-oraculos/tarot/", "", "", "México", "México", "SKU", "Clásico", "research"),
    L("Oráculos extra", "https://pinka.com.mx/tarots-y-oraculos/tarot/", "", "", "México", "México", "SKU", "Ángeles / animales", "research"),
    L("Lenormand extra", "https://tarotsdelmundo.com/", "info@tarotsdelmundo.com", "5519983301", "CDMX", "CDMX", "SKU", "36 cartas", "research"),
    L("Tarot Marsella extra", "https://tarotsdelmundo.com/", "info@tarotsdelmundo.com", "5519983301", "CDMX", "CDMX", "SKU", "Tradicional", "research"),
    L("Runas extra", "https://tiendaesoterica.com.mx/", "", "", "México", "México", "Producto", "Piedras rúnicas", "research"),
    L("Péndulos extra", "https://www.stellum.mx/", "tienda.stellum@icloud.com", "8123619626", "Monterrey", "NL", "Producto", "Radiestesia", "research"),
    L("Cuarzos extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Producto", "Péndulos y kits", "research"),
    L("Velas de soya extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Producto", "Intencionadas", "research"),
    L("Veladoras 7 días extra", "", "", "", "CDMX", "CDMX", "Producto", "Mayoreo Centro", "research"),
    L("Velón 7 potencias extra", "", "", "", "CDMX", "CDMX", "Producto", "Santería", "research"),
    L("Lociones / aguas extra", "https://www.stellum.mx/", "tienda.stellum@icloud.com", "8123619626", "Monterrey", "NL", "Producto", "Aguas astrales", "research"),
    L("Aceites ritual extra", "https://www.stellum.mx/", "", "8123619626", "Monterrey", "NL", "Producto", "Sahumerios y aceites", "research"),
    L("Sahumerios / palo santo extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Producto", "Limpia", "research"),
    L("Incienso Centro extra", "", "", "", "CDMX", "CDMX", "Mayoreo", "Uruguay / Zócalo", "research"),
    L("Sprays mágicos extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Producto", "Mists + cuarzo", "research"),
    L("Spell jars extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Producto", "Pócimas", "research"),
    L("Caja de bruja extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Paquete", "Kit inicio", "research"),
    L("Libro de las sombras extra", "https://tiendaesoterica.com.mx/", "", "", "México", "México", "Producto", "Wicca", "research"),
    L("Amuletos / talismanes extra", "https://tiendaesoterica.com.mx/", "", "", "México", "México", "Producto", "Protección", "research"),
    L("Mal de ojo extra", "https://esotericamx.com/collections/mayoreo-joyeria", "", "", "México", "México", "Línea", "Joyería mágica", "research"),
    L("Nudo de bruja extra", "https://esotericamx.com/collections/mayoreo-joyeria", "", "", "México", "México", "Línea", "Cuarzos", "research"),
    L("Santería / Yoruba extra", "", "", "", "CDMX", "CDMX", "Línea", "Tiara / Uruguay", "research"),
    L("Arcángeles figuras extra", "https://www.stellum.mx/", "", "8123619626", "Monterrey", "NL", "Línea", "7 arcángeles", "research"),
    L("Lecturas de tarot extra", "https://www.stellum.mx/", "tienda.stellum@icloud.com", "8123619626", "Monterrey", "NL", "Servicio", "Presencial", "research"),
    L("Limpias energéticas extra", "https://www.stellum.mx/", "", "8123619626", "Monterrey", "NL", "Servicio", "Terapias", "research"),
    L("Consultas León extra", "https://tarotmexico.com.mx/", "informes@tarotmexico.com", "4771843418", "León", "Guanajuato", "Servicio", "Tarot evolutivo", "research"),
    L("Amazon MX tarot extra", "https://www.amazon.com.mx/s?k=tarot+baraja", "", "", "México", "México", "Marketplace", "Barajas", "research"),
    L("ML velas esotéricas extra", "https://listado.mercadolibre.com.mx/velas-esotericas", "", "", "México", "México", "Marketplace", "Ritual", "research"),
    L("ML tarot extra", "https://listado.mercadolibre.com.mx/tarot-baraja", "", "", "México", "México", "Marketplace", "Oráculos", "research"),
    L("Cluster Uruguay CDMX extra", "", "", "", "CDMX", "CDMX", "Cluster", "Mayoreo esotérico Centro", "research"),
    L("Cluster Sonora / Lagunilla extra", "", "", "", "CDMX", "CDMX", "Cluster", "Religioso popular", "research"),
    L("Cluster Metepec extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Cluster", "Magic Ways zona", "research"),
    L("Cluster MTY extra", "https://www.stellum.mx/", "tienda.stellum@icloud.com", "8123619626", "Monterrey", "NL", "Cluster", "San Agustín", "research"),
    L("Librerías esotéricas extra", "https://tiendaesoterica.com.mx/", "", "", "México", "México", "Canal", "Libros + tarot", "research"),
    L("Herbolarias canal extra", "", "", "", "CDMX", "CDMX", "Canal", "Lociones / velas", "research"),
    L("Yoga / wellness extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Canal", "Cuarzos y sahumo", "research"),
    L("Cafeterías ritual extra", "", "", "", "CDMX", "CDMX", "Canal", "Café Libertad / Condesa", "research"),
    L("Talleres herbales extra", "", "", "", "CDMX", "CDMX", "Educación", "Sahumar / plantas", "research"),
    L("Cursos tarot extra", "https://tarotmexico.com.mx/", "informes@tarotmexico.com", "4771843418", "León", "Guanajuato", "Educación", "Lectura", "research"),
    L("Instagram Magic Ways extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Canal digital", "Social", "research"),
    L("Facebook Stellum extra", "https://www.stellum.mx/", "tienda.stellum@icloud.com", "8123619626", "Monterrey", "NL", "Canal", "Plaza Fiesta", "research"),
    L("Halloween kits extra", "https://esotericamx.com/collections/mayoreo-joyeria", "", "", "México", "México", "Temporada", "Colección", "research"),
    L("Día de muertos extra", "", "", "", "México", "México", "Temporada", "Veladoras / copal", "research"),
    L("Año nuevo ritual extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Temporada", "Abundancia", "research"),
    L("San Valentín amor extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Temporada", "Velas amor", "research"),
    L("Envíos nacionales Esotérica extra", "https://tiendaesoterica.com.mx/", "", "", "México", "México", "Logística", "Ecom", "research"),
    L("Pickup Metepec extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Logística", "Sin costo", "research"),
    L("Cita Pachuca extra", "https://www.rinconcitomagico.mx/contacto/", "info@rinconcitomagico.mx", "7711429045", "Pachuca", "Hidalgo", "Operación", "Previa cita", "research"),
    L("Mayoreo kits extra", "https://esotericamx.com/collections/mayoreo-joyeria", "", "", "México", "México", "Mayoreo", "Libro + velas + tarot", "research"),
    L("Revendedores Centro extra", "", "", "", "CDMX", "CDMX", "Canal B2B", "Tiara / Uruguay", "research"),
    L("Boutiques místicas extra", "", "", "5536431447", "CDMX", "CDMX", "Canal", "Roma / Condesa", "research"),
    L("Mercados brujos extra", "", "", "", "Catemaco", "Veracruz", "Cluster", "Tradicional", "research"),
    L("Catemaco brujos extra", "", "", "", "Catemaco", "Veracruz", "Cluster", "Retail ritual", "research"),
    L("Sonora Market extra", "", "", "", "CDMX", "CDMX", "Cluster", "Hierbas y velas", "research"),
    L("Mercado de Sonora extra", "", "", "", "CDMX", "CDMX", "Cluster", "Mayoreo popular", "research"),
    L("Copal / resinas extra", "", "", "", "México", "México", "Insumo", "Sahumar", "research"),
    L("Sal negra / baños extra", "https://esotericamx.com/collections/mayoreo-joyeria", "", "", "México", "México", "Insumo", "Limpia", "research"),
    L("Morteros extra", "https://esotericamx.com/collections/mayoreo-joyeria", "", "", "México", "México", "Insumo", "Kit", "research"),
    L("Altares / paños extra", "https://tiendaesoterica.com.mx/", "", "", "México", "México", "Insumo", "Wicca", "research"),
    L("Figuras deidades extra", "https://tiendaesoterica.com.mx/", "", "", "México", "México", "Producto", "Resina", "research"),
    L("Lámparas de sal extra", "https://tiendaesoterica.com.mx/", "", "", "México", "México", "Producto", "Ambiente", "research"),
    L("Jabones ritual extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Adyacente", "Cuarzo", "research"),
    L("Joyería mágica extra", "https://esotericamx.com/collections/mayoreo-joyeria", "", "", "México", "México", "Adyacente", "Mayoreo", "research"),
    L("Brazalete italiano extra", "https://esotericamx.com/collections/mayoreo-joyeria", "", "", "México", "México", "Adyacente", "Arma tu pulsera", "research"),
    L("Zodiaco línea extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Línea", "Rituales", "research"),
    L("Luna / estrellas extra", "https://esotericamx.com/collections/mayoreo-joyeria", "", "", "México", "México", "Línea", "Colección", "research"),
    L("Números ángel extra", "https://esotericamx.com/collections/mayoreo-joyeria", "", "", "México", "México", "Línea", "Manifestar", "research"),
    L("Protección extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Intención", "Amuletos", "research"),
    L("Abundancia extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Intención", "Velas", "research"),
    L("Amor extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Intención", "Hechizos / velas", "research"),
    L("Abre caminos extra", "https://magicways.mx/", "", "", "Metepec", "EdoMex", "Intención", "Vela $420", "research"),
    L("Casa 7 incienso extra", "", "", "", "CDMX", "CDMX", "Tienda", "Naturales, aceites y kits", "research"),
    L("The Wizard Shop extra", "", "", "", "CDMX", "CDMX", "Tienda", "Bienestar espiritual", "research"),
    L("Brujá extra", "", "", "", "CDMX", "CDMX", "Tienda", "Desde 2018, velas intención", "research"),
    L("Gul's Incienso extra", "", "", "", "CDMX", "CDMX", "Mayoreo", "Centro / Zócalo", "research"),
    L("Tienda Esotérica & más extra", "", "", "8117639786", "Monterrey", "NL", "Tienda", "L-S 9-19 Dom 9-16", "research"),
    L("El Rincón Espiritual extra", "", "", "8125894981", "Nezahualcóyotl", "EdoMex", "Tienda", "Sesiones + retail", "research"),
    L("Influencers bruja extra", "", "", "", "México", "México", "Canal", "TikTok / IG", "research"),
    L("Ferias místicas extra", "", "", "", "México", "México", "Expo", "Cuarzos / tarot", "research"),
    L("Expo esotérica CDMX extra", "", "", "", "CDMX", "CDMX", "Expo", "Retail booth", "research"),
    L("Iglesias / veladoras extra", "", "", "", "México", "México", "Canal adyacente", "Religioso popular", "research"),
    L("Santería Centro extra", "", "", "", "CDMX", "CDMX", "Canal", "Yoruba / imágenes", "research"),
    L("Wicca comunidad extra", "https://tiendaesoterica.com.mx/", "", "", "México", "México", "Canal", "Retail especializado", "research"),
    L("Astrología / carta natal extra", "https://tarotmexico.com.mx/", "", "4771843418", "León", "Guanajuato", "Servicio", "Adyacente tarot", "research"),
    L("Numerología extra", "", "", "", "México", "México", "Servicio", "Consultas", "research"),
    L("Péndulo dowsing extra", "https://www.stellum.mx/", "", "8123619626", "Monterrey", "NL", "Servicio", "Retail + uso", "research"),
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
    print("Generating lotes 21-22…")
    u = (
        UNAS
        + pad("Nail supply / press on", "Regional", "Insumos uñas y sets", CITIES)
        + pad("Salón de uñas", "Regional", "Compran gel acrílico y tips", CITIES2)
        + pad("Mayoreo belleza uñas", "Regional", "Organic Fantasy Wapizima", CITIES2)
        + pad("Nail tech independiente", "Regional", "Sets press on y gel", CITIES3)
    )
    e = (
        ESO
        + pad("Tienda esotérica", "Regional", "Tarot, velas y cuarzos", CITIES)
        + pad("Veladoras / ritual", "Regional", "Mayoreo lociones y sahumerios", CITIES2)
        + pad("Lectora / tarotista", "Regional", "Consultas + retail oráculos", CITIES2)
        + pad("Herbolaria / velas", "Regional", "Lociones y sahumerios", CITIES3)
    )
    dump("21", "insumos_unas_press_on", "Insumos para uñas, press on y nail supply MX", u)
    dump("22", "tarot_velas_esotericas", "Tarot, lociones y velas esotéricas MX", e)
    print(f"counts: 21={len(u)} 22={len(e)}")


if __name__ == "__main__":
    main()
