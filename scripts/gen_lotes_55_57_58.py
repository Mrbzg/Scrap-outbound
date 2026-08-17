#!/usr/bin/env python3
"""Generate seeds for lotes 55 (fintech envío tarjetas), 57 (barbería/cuidado
masculino) y 58 (insumos Tattoo y Body Art). ONLY real companies."""
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
# LOTE 55 — Fintech / Servicio de envíos de tarjetas
# ============================================================
FINTECH = [
    L("Banco Plata (ejemplo)", "https://bancoplata.mx/es", "", "", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — banco digital con tarjetas", "ejemplo_cliente"),
    L("Nu México", "https://www.nu.com.mx/", "", "", "CDMX", "CDMX", "Neobanco", "Tarjeta de crédito 100% digital; envío a domicilio", "brand"),
    L("Klar", "https://klar.mx/", "", "", "CDMX", "CDMX", "Neobanco", "Cuenta digital e inversiones; 3M+ usuarios", "brand"),
    L("Stori", "https://www.stori.com.mx/", "", "", "CDMX", "CDMX", "Fintech", "Tarjeta sin historial; 2M+ usuarios", "brand"),
    L("Albo", "https://www.albo.mx/", "", "", "CDMX", "CDMX", "Neobanco", "Cuenta digital con tarjeta de débito", "brand"),
    L("Ualá México", "https://www.uala.mx/", "", "", "CDMX", "CDMX", "Neobanco", "Cuenta y tarjeta digital; alianza ABC Capital", "brand"),
    L("Hey Banco", "https://www.heybanco.com/", "", "", "Monterrey", "Nuevo León", "Neobanco", "Banco digital de Banregio; tarjetas con cashback", "brand"),
    L("Cuenca", "https://www.cuenca.mx/", "", "", "CDMX", "CDMX", "Fintech", "Cuenta digital para negocios", "brand"),
    L("Fondeadora", "https://fondeadora.com/", "", "", "CDMX", "CDMX", "Neobanco", "Cuenta digital con tarjeta física", "brand"),
    L("Vexi", "https://vexi.mx/", "", "", "CDMX", "CDMX", "Fintech", "Tarjeta de crédito sin buró, red Amex; 1M+ clientes", "brand"),
    L("NOVACARD", "https://novacard.mx/", "", "", "CDMX", "CDMX", "Fintech", "Tarjeta garantizada 100% digital desde $500", "research"),
    L("RappiCard", "https://www.rappicard.com/", "", "", "CDMX", "CDMX", "Fintech", "Tarjeta con cashback, alianza Banco J.P. Morgan", "brand"),
    L("Didi Card", "", "", "", "CDMX", "CDMX", "Fintech", "Tarjeta de crédito de Didi", "brand"),
    L("Spin by OXXO", "https://www.spin.com.mx/", "", "", "Monterrey", "Nuevo León", "Fintech", "Cuenta y tarjeta de débito de OXXO", "brand"),
    L("Mercado Pago", "https://www.mercadopago.com.mx/", "", "", "CDMX", "CDMX", "Fintech", "Wallet y tarjeta", "brand"),
    L("Bineo", "https://www.bineo.com.mx/", "", "", "CDMX", "CDMX", "Neobanco", "Banco digital de Banorte", "brand"),
    L("Openbank México", "https://www.openbank.mx/", "", "", "CDMX", "CDMX", "Neobanco", "Banco digital de Grupo Santander", "brand"),
    L("Revolut México", "https://www.revolut.com/mx/", "", "", "CDMX", "CDMX", "Neobanco", "Cuenta multi-divisa con tarjeta", "brand"),
    L("DolarApp", "https://dolarapp.com/", "", "", "CDMX", "CDMX", "Fintech", "Cuenta en dólares con tarjeta", "brand"),
    L("Kapital", "https://www.kapital.mx/", "", "", "CDMX", "CDMX", "Fintech", "Finanzas empresariales y tarjetas corporativas", "brand"),
    L("Finsus", "https://www.finsus.mx/", "", "", "CDMX", "CDMX", "Fintech", "Cuenta de ahorro y tarjeta", "brand"),
    L("Broxel", "https://broxel.com/", "", "", "CDMX", "CDMX", "Fintech", "Emisión de tarjetas y nómina digital", "brand"),
    L("Konfío", "https://konfio.mx/", "", "", "CDMX", "CDMX", "Fintech", "Tarjetas empresariales y crédito PYME", "brand"),
    L("Clara", "https://www.clara.com/mx", "", "", "CDMX", "CDMX", "Fintech", "Tarjetas corporativas B2B", "brand"),
    L("BBVA México", "https://www.bbva.mx/", "", "", "CDMX", "CDMX", "Banco", "Banco tradicional con envío de tarjetas", "brand"),
    L("Banorte", "https://www.banorte.com/", "", "", "Monterrey", "Nuevo León", "Banco", "Banco tradicional con envío de tarjetas", "brand"),
    L("Citibanamex", "https://www.banamex.com/", "", "", "CDMX", "CDMX", "Banco", "Banco tradicional con envío de tarjetas", "brand"),
    L("Santander México", "https://www.santander.com.mx/", "", "", "CDMX", "CDMX", "Banco", "Banco tradicional con envío de tarjetas", "brand"),
    L("HSBC México", "https://www.hsbc.com.mx/", "", "", "CDMX", "CDMX", "Banco", "Banco tradicional con envío de tarjetas", "brand"),
    L("Scotiabank México", "https://www.scotiabank.com.mx/", "", "", "CDMX", "CDMX", "Banco", "Banco tradicional con envío de tarjetas", "brand"),
    L("BanBajío", "https://www.banbajio.com/", "", "", "León", "Guanajuato", "Banco", "Banco con tarjetas garantizadas", "brand"),
    L("Banco Azteca", "https://www.bancoazteca.com.mx/", "", "", "CDMX", "CDMX", "Banco", "Banco con tarjetas y envíos", "brand"),
    L("American Express México", "https://www.americanexpress.com/mx", "", "", "CDMX", "CDMX", "Red", "Emisora de tarjetas premium", "brand"),
    L("Visa México", "https://www.visa.com.mx/", "", "", "CDMX", "CDMX", "Red", "Red de pagos", "brand"),
    L("Mastercard México", "https://www.mastercard.com.mx/", "", "", "CDMX", "CDMX", "Red", "Red de pagos", "brand"),
]


# ============================================================
# LOTE 57 — Grooming / Barbería y cuidado masculino
# ============================================================
BARBERIA = [
    L("Sensabien (ejemplo)", "https://www.sensabien.com/", "", "", "México", "México", "Ejemplo original", "Ejemplo del cliente — cuidado masculino", "ejemplo_cliente"),
    L("Vikingos Barber Shop", "https://www.facebook.com/vikingosbarbershopmx/", "vikingosbarbershop@gmail.com", "5550847376", "EdoMex", "EdoMex", "Barbería", "Barber shop con cortes clásicos y modernos; Periférico Norte", "research"),
    L("Baregk", "https://www.facebook.com/BarberiaBaregkMX/", "", "", "México", "México", "Marca", "Marca de barbería y cuidado personal masculino", "research"),
    L("Kiss Color / Kiss", "", "", "", "México", "México", "Marca", "Tintes y cuidado para barba, marca mexicana", "brand"),
    L("Bígaro", "", "", "", "México", "México", "Marca", "Fijadores y brillantina para cabello, marca MX", "brand"),
    L("V75", "", "", "", "México", "México", "Marca", "Cuidado capilar masculino", "brand"),
    L("El Vaquero", "", "", "", "México", "México", "Marca", "Gel y fijadores para cabello, marca MX", "brand"),
    L("Gillette México", "https://www.gillette.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Rasuradoras y cuidado masculino", "brand"),
    L("Old Spice", "", "", "", "USA", "", "Marca", "Desodorantes y cuidado masculino, venta MX", "brand"),
    L("Axe (Unilever)", "", "", "", "México", "México", "Marca", "Cuidado masculino, retail MX", "brand"),
    L("Dove Men+Care", "", "", "", "México", "México", "Marca", "Cuidado masculino, retail MX", "brand"),
    L("Proraso", "", "", "", "Italia", "", "Marca", "Productos clásicos de barbería, venta MX", "brand"),
    L("Clubman Pinaud", "", "", "", "USA", "", "Marca", "Lociones y productos de barbería, venta MX", "brand"),
    L("Andis", "", "", "", "USA", "", "Marca", "Máquinas de corte, venta MX", "brand"),
    L("Wahl", "", "", "", "USA", "", "Marca", "Clippers de barbería, venta MX", "brand"),
    L("Oster", "", "", "", "USA", "", "Marca", "Máquinas de corte, venta MX", "brand"),
    L("Babyliss Pro", "", "", "", "Francia", "", "Marca", "Herramientas de barbería, venta MX", "brand"),
    L("Marca de la Cruz", "", "", "", "México", "México", "Marca", "Jabones y cuidado personal mexicano", "brand"),
    L("American Crew", "", "", "", "USA", "", "Marca", "Productos de barbería premium, venta MX", "brand"),
    L("Jojoba / Argan Men", "", "", "", "México", "México", "Marca", "Aceites y pomadas para barba", "brand"),
    L("Suavecito Pomade", "", "", "", "USA", "", "Marca", "Pomadas de barbería, venta MX", "brand"),
    L("Amazon MX barbería", "https://www.amazon.com.mx/s?k=productos+para+barberia", "", "", "México", "México", "Marketplace", "Sellers de productos de barbería", "research"),
    L("Mercado Libre barbería", "https://listado.mercadolibre.com.mx/productos-para-barberia-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de productos de barbería", "research"),
    L("Walmart México grooming", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Sección de cuidado masculino", "brand"),
    L("Coppel grooming", "https://www.coppel.com/", "", "", "CDMX", "CDMX", "Retail", "Sección de cuidado masculino", "brand"),
]


# ============================================================
# LOTE 58 — Suministros Profesionales / Insumos para Tattoo y Body Art
# ============================================================
TATTOO = [
    L("Soulflower (ejemplo)", "https://soulflower.mx/", "soulflowercustom@gmail.com", "5545127515", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — insumos para tatuar", "ejemplo_cliente"),
    L("Zebra Tattoo Supply", "https://zebratattoosupply.com/", "ventas@zebratattoosupply.com", "5541880654", "CDMX", "CDMX", "Mayoreo", "Máquinas, cartuchos, PMU; envíos MX", "research"),
    L("Inkside Supply", "https://inksidesupply.com/", "ventas@inksidesupply.com", "5510480496", "CDMX", "CDMX", "Mayoreo", "Tintas, cartuchos y máquinas CDMX", "research"),
    L("Tarmex Tattoo Supply", "https://tarmex-vip.com/", "ventas@tarmex-vip.com", "5562786666", "CDMX", "CDMX", "Mayoreo", "Insumos profesionales para tatuar", "research"),
    L("AGMA Tattoo Supply", "https://agmatattoo.com/", "", "7711691599", "Pachuca", "Hidalgo", "Mayoreo", "Insumos para tatuaje", "research"),
    L("Daruma Supply Tattoo", "https://www.darumasupplytattoo.com/", "castillo.aguil4@gmail.com", "5519649709", "CDMX", "CDMX", "Mayoreo", "Insumos profesionales", "research"),
    L("Reyes Tattoo Supply", "https://www.reyestattoosupply.com/", "ventas@reyestattoosupply.com", "3320031187", "Zapopan", "Jalisco", "Mayoreo", "Distribuidor oficial FK Irons, Cheyenne, Eternal y Bishop; Av. Tepeyac 930A", "research"),
    L("Eagle Tattoo Supply", "https://eagletattoosupply.com/", "", "5583396661", "CDMX", "CDMX", "Mayoreo", "Distribuidor nacional desde 2016; tintas, agujas, máquinas y cartuchos", "research"),
    L("Make Art Supply", "https://makeartsupply.com/", "", "", "México", "México", "Mayoreo", "Insumos profesionales para tatuadores", "research"),
    L("Cheyenne", "", "", "", "Alemania", "", "Marca", "Máquinas pen y cartuchos, distribución MX", "brand"),
    L("FK Irons", "", "", "", "USA", "", "Marca", "Máquinas de tatuar, distribución oficial MX", "brand"),
    L("Bishop Rotary", "", "", "", "USA", "", "Marca", "Máquinas rotary, distribución oficial MX", "brand"),
    L("Eternal Ink", "", "", "", "USA", "", "Marca", "Tintas profesionales, distribución MX", "brand"),
    L("Dynamic Tattoo Ink", "", "", "", "USA", "", "Marca", "Triple Black y colores, vía Soulflower", "brand"),
    L("Radiant Colors", "", "", "", "USA", "", "Marca", "Tintas de color, vía Soulflower", "brand"),
    L("World Famous Tattoo Ink", "", "", "", "USA", "", "Marca", "Tintas, distribución MX", "brand"),
    L("Fusion Ink", "", "", "", "USA", "", "Marca", "Tintas, distribución MX", "brand"),
    L("Starbrite", "", "", "", "USA", "", "Marca", "Tintas, vía Reyes", "brand"),
    L("Panthera", "", "", "", "México", "México", "Marca", "Tinta para tatuaje, vía Soulflower", "brand"),
    L("SUPRA", "", "", "", "México", "México", "Marca", "Set de 12 tintas, vía Soulflower", "brand"),
    L("Allegory Ink", "", "", "", "México", "México", "Marca", "Tintas, vía Eagle", "brand"),
    L("EZ Cartuchos", "", "", "", "México", "México", "Marca", "Cartuchos V-Select y EZ INKin Revo", "brand"),
    L("Atomus", "", "", "", "México", "México", "Marca", "Tintas y kits profesionales, vía ML", "brand"),
    L("Muramaudi", "", "", "", "México", "México", "Marca", "Kits profesionales, vía ML", "brand"),
    L("Amazon MX tattoo supply", "https://www.amazon.com.mx/s?k=tattoo+supply", "", "", "México", "México", "Marketplace", "Sellers de insumos para tatuar", "research"),
    L("Mercado Libre tattoo", "https://listado.mercadolibre.com.mx/tintas-para-tatuar", "", "", "México", "México", "Marketplace", "Tintas, máquinas y cartuchos", "research"),
    L("Tinta Dynamic 1oz", "https://soulflower.mx/", "", "", "CDMX", "CDMX", "Producto", "Dynamic Triple Black 1oz", "research"),
    L("Kit Axis Soulflower", "https://soulflower.mx/", "", "", "CDMX", "CDMX", "Producto", "Kit profesional Soulflower x Radiant Axis", "research"),
]


def main():
    print("Generating lotes 55, 57 y 58 (solo empresas reales)…")
    dump("55", "envios_de_tarjetas", "Servicio de envíos de tarjetas MX", FINTECH)
    dump("57", "barberia_cuidado_masculino", "Barbería y cuidado masculino MX", BARBERIA)
    dump("58", "insumos_tattoo_body_art", "Insumos para Tattoo y Body Art MX", TATTOO)
    print(f"counts: 55={len(FINTECH)} 57={len(BARBERIA)} 58={len(TATTOO)}")


if __name__ == "__main__":
    main()
