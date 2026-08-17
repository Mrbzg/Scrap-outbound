#!/usr/bin/env python3
"""Generate seeds for lote 43 (vitaminas y suplementos MX) — target 100+ REAL companies.
Farmacias, cadenas retail, laboratorios, marcas y distribuidores con nombre comercial real."""
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


SUP = [
    # --- Ejemplo original ---
    L("B Life (ejemplo)", "https://www.blife.mx/", "", "", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — vitaminas y suplementos D2C", "ejemplo_cliente"),
    # --- Farmacias / retail ---
    L("Farmacias del Ahorro", "https://www.fahorro.com/", "", "", "CDMX", "CDMX", "Retail", "Cadena nacional de farmacias con línea de vitaminas", "brand"),
    L("Farmacias Guadalajara", "https://www.farmaciasguadalajara.com.mx/", "", "", "Guadalajara", "Jalisco", "Retail", "Cadena nacional con sección de suplementos", "brand"),
    L("Farmacias San Pablo", "https://farmaciasanpablo.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadena de farmacias CDMX", "brand"),
    L("Farmacias Benavides", "https://www.benavides.com.mx/", "", "", "Monterrey", "Nuevo León", "Retail", "Cadena de farmacias del norte", "brand"),
    L("Farmacias del Sol", "https://www.farmaciasdelsol.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadena de farmacias CDMX", "brand"),
    L("Farmacias YZA", "https://farmaciasyza.com/", "", "", "CDMX", "CDMX", "Retail", "Cadena de farmacias CDMX", "brand"),
    L("Farmacias ABC", "https://farmaciasabc.com/", "", "", "CDMX", "CDMX", "Retail", "Cadena de farmacias CDMX", "brand"),
    L("Farmacias Roma", "https://www.farmaciasroma.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadena de farmacias CDMX", "brand"),
    L("Farmacias Morelos", "https://www.farmaciasmorelos.com.mx/", "", "", "Cuernavaca", "Morelos", "Retail", "Cadena de farmacias del sur", "brand"),
    L("Walmart México", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Autoservicio con sección de vitaminas", "brand"),
    L("Soriana", "https://www.soriana.com/", "", "", "CDMX", "CDMX", "Retail", "Autoservicio con sección de vitaminas", "brand"),
    L("Costco México", "https://www.costco.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Mayoreo de vitaminas (Kirkland)", "brand"),
    L("Sam's Club México", "https://www.sams.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Mayoreo de vitaminas (Member's Mark)", "brand"),
    L("HEB México", "https://www.heb.com.mx/", "", "", "Monterrey", "Nuevo León", "Retail", "Autoservicio del noreste", "brand"),
    L("Chedraui", "https://www.chedraui.com.mx/", "", "", "Xalapa", "Veracruz", "Retail", "Autoservicio con sección de vitaminas", "brand"),
    L("La Comer", "https://www.lacomer.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Autoservicio con sección de vitaminas", "brand"),
    L("City Club", "https://www.cityclub.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Club de precios con vitaminas por mayoreo", "brand"),
    L("Casa Ley", "https://www.casaley.mx/", "", "", "Culiacán", "Sinaloa", "Retail", "Autoservicio del noroeste", "brand"),
    # --- Laboratorios farmacéuticos MX ---
    L("Laboratorios PiSA", "https://www.pisa.com.mx/", "", "", "Guadalajara", "Jalisco", "Laboratorio", "Farmacéutica mexicana con línea de vitaminas", "brand"),
    L("Genomma Lab", "https://www.genommalab.com/", "", "", "CDMX", "CDMX", "Laboratorio", "Farmacéutica mexicana (Amino Vida, Rescata)", "brand"),
    L("Sanfer", "https://www.sanfer.com.mx/", "", "", "CDMX", "CDMX", "Laboratorio", "Farmacéutica mexicana", "brand"),
    L("Laboratorios Liomont", "https://www.liomont.com.mx/", "", "", "CDMX", "CDMX", "Laboratorio", "Farmacéutica mexicana (Frubiés, Bion)", "brand"),
    L("Laboratorios Carnot", "https://www.carnot.com.mx/", "", "", "CDMX", "CDMX", "Laboratorio", "Farmacéutica mexicana", "brand"),
    L("Bayer México", "https://www.bayer.mx/", "", "", "CDMX", "CDMX", "Laboratorio", "Berocca, Supradyn, One A Day", "brand"),
    L("GSK México", "https://www.gsk.com.mx/", "", "", "CDMX", "CDMX", "Laboratorio", "Pharmaton y multivitamínicos", "brand"),
    L("Pfizer México", "https://www.pfizer.com.mx/", "", "", "CDMX", "CDMX", "Laboratorio", "Centrum", "brand"),
    L("Merck México", "https://www.merckgroup.com/mx", "", "", "CDMX", "CDMX", "Laboratorio", "Productos de salud", "brand"),
    L("Abbott México", "https://www.abbott.com.mx/", "", "", "CDMX", "CDMX", "Laboratorio", "Ensure y nutrición", "brand"),
    L("Sanofi México", "https://www.sanofi.com.mx/", "", "", "CDMX", "CDMX", "Laboratorio", "Magnesio y suplementos", "brand"),
    L("Grisi", "https://www.grisi.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Vitaminas y salud, marca mexicana", "brand"),
    # --- Marcas de suplementos ---
    L("Omnilife", "https://www.omnilife.com/", "", "", "Guadalajara", "Jalisco", "Marca", "Suplementos alimenticios MLM mexicano", "brand"),
    L("Herbalife México", "https://www.herbalife.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Nutrición deportiva y control de peso", "brand"),
    L("GNC México", "https://www.gnc.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Tienda especializada en suplementos", "brand"),
    L("Nutrilite / Amway", "https://www.amway.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Vitaminas y suplementos por consultoría", "brand"),
    L("Vitaflor", "https://www.vitaflor.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Suplementos mexicanos", "brand"),
    L("Nature's Way", "https://www.naturesway.com/", "", "", "USA", "", "Marca", "Suplementos importados, venta ML", "brand"),
    L("NOW Foods", "https://www.nowfoods.com/", "", "", "USA", "", "Marca", "Suplementos importados, distribución MX", "brand"),
    L("Solaray", "https://www.solaray.com/", "", "", "USA", "", "Marca", "Vitaminas importadas, venta MX", "brand"),
    L("Doctor's Best", "https://www.drbvitamins.com/", "", "", "USA", "", "Marca", "Suplementos importados, venta MX", "brand"),
    L("Swanson Health", "https://www.swansonvitamins.com/", "", "", "USA", "", "Marca", "Vitaminas importadas, venta MX", "brand"),
    L("Kirkland Signature", "https://www.costco.com.mx/", "", "", "USA", "", "Marca", "Multivitamínicos por mayoreo en Costco", "brand"),
    L("Member's Mark", "https://www.sams.com.mx/", "", "", "USA", "", "Marca", "Multivitamínicos por mayoreo en Sam's", "brand"),
    L("Vitaldin", "https://www.vitaldin.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Suplementos mexicanos", "brand"),
    L("Nutriólogos / MediNat", "https://www.medinat.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Suplementos mexicanos", "brand"),
    # --- D2C / tiendas online (verificadas en investigación previa) ---
    L("Gummy Life", "https://www.gummylife.mx/", "", "", "México", "México", "D2C", "Gomitas vitamínicas mexicanas (biotina, omega 3, magnesio)", "research"),
    L("B Life", "https://www.blife.mx/", "", "", "CDMX", "CDMX", "D2C", "Suplementos y vitaminas ecom", "research"),
    L("Vital Suplementos MX", "https://vitalsuplementosmex.com/", "", "", "México", "México", "D2C", "Gomitas de vitaminas y suplementos", "research"),
    L("Plenlife", "", "", "", "México", "México", "Marca", "Gomitas calcio+vit D y multivitamínico, vía ML", "research"),
    L("Geomed", "", "", "", "México", "México", "Distribuidor", "Distribuye Plenlife en ML (4.9★)", "research"),
    L("Suplefit MX", "", "", "", "México", "México", "Distribuidor", "Vitafusion y gomitas importadas vía ML", "research"),
    L("OK Vitaminas", "", "", "", "México", "México", "Distribuidor", "Nature's Way y gomitas vía ML", "research"),
    L("Básicos de la casa", "", "", "", "México", "México", "Distribuidor", "Nature Made y Centrum vía ML", "research"),
    L("Vitamin World", "", "", "", "México", "México", "Distribuidor", "Natrol melatonina gomitas vía ML", "research"),
    L("Belabear", "", "", "", "México", "México", "Marca", "Gomitas multivitamínico women 150 pzs", "research"),
    L("C-Boost", "", "", "", "México", "México", "Marca", "Gomitas multivitamínicas 180 pzs", "research"),
    L("Heally", "", "", "", "México", "México", "Marca", "Multivitamínico + colágeno en gomitas", "research"),
    L("Vitafusion", "", "", "", "USA", "", "Marca", "Gomitas multivitamínicas, importado", "brand"),
    L("Nature Made", "", "", "", "USA", "", "Marca", "Gomitas omega 3 y magnesio, importado", "brand"),
    L("Natrol", "", "", "", "USA", "", "Marca", "Melatonina en gomitas, importado", "brand"),
    L("Nature's Bounty", "", "", "", "USA", "", "Marca", "Gomitas zinc y multivitamínicas, importado", "brand"),
    L("Nature's Truth", "", "", "", "USA", "", "Marca", "Vitamina D3 gomitas, importado", "brand"),
    L("Centrum", "", "", "", "USA", "", "Marca", "Multivitamínico + omega, importado", "brand"),
    L("Berocca (Bayer)", "", "", "", "Alemania", "", "Marca", "Efervescentes de vitaminas B+C", "brand"),
    L("Supradyn (Bayer)", "", "", "", "Alemania", "", "Marca", "Multivitamínico energético", "brand"),
    L("Pharmaton (GSK)", "", "", "", "Suiza", "", "Marca", "Multivitamínico con ginseng", "brand"),
    L("Multicentrum", "", "", "", "USA", "", "Marca", "Multivitamínico, venta MX", "brand"),
    L("One A Day", "", "", "", "USA", "", "Marca", "Multivitamínicos, venta MX", "brand"),
    L("Amino Vida (Genomma)", "https://www.genommalab.com/", "", "", "CDMX", "CDMX", "Marca", "Suplemento para cabello y uñas", "brand"),
    L("Frubiés (Liomont)", "https://www.liomont.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Vitaminas efervescentes", "brand"),
    L("Optimum Nutrition", "", "", "", "USA", "", "Marca", "Proteínas y suplementos deportivos, distribución MX", "brand"),
    L("MuscleTech", "", "", "", "USA", "", "Marca", "Suplementos deportivos, distribución MX", "brand"),
    L("Dymatize", "", "", "", "USA", "", "Marca", "Proteínas y aminoácidos, distribución MX", "brand"),
    L("BSN", "", "", "", "USA", "", "Marca", "Suplementos deportivos, distribución MX", "brand"),
    L("Universal Nutrition", "", "", "", "USA", "", "Marca", "Suplementos deportivos, distribución MX", "brand"),
    L("Myprotein", "https://www.myprotein.com.mx/", "", "", "México", "México", "D2C", "Suplementos en línea con operación MX", "brand"),
    L("Prozis", "https://www.prozis.com/mx", "", "", "México", "México", "D2C", "Suplementos en línea, operación MX", "brand"),
    L("Zumub", "https://www.zumub.com/mx/", "", "", "México", "México", "D2C", "Suplementos en línea, operación MX", "brand"),
    L("iHerb", "https://es.iherb.com/", "", "", "México", "México", "D2C", "Tienda internacional de suplementos con envío a MX", "brand"),
    L("Sundown Naturals", "", "", "", "USA", "", "Marca", "Vitaminas importadas, venta MX", "brand"),
    L("Schiff", "", "", "", "USA", "", "Marca", "Vitaminas y omega, venta MX", "brand"),
    L("Carlson Labs", "", "", "", "USA", "", "Marca", "Vitaminas y omega, venta MX", "brand"),
    L("Garden of Life", "", "", "", "USA", "", "Marca", "Suplementos orgánicos, venta MX", "brand"),
    L("Jarrow Formulas", "", "", "", "USA", "", "Marca", "Suplementos importados, venta MX", "brand"),
    L("Life Extension", "", "", "", "USA", "", "Marca", "Suplementos importados, venta MX", "brand"),
    L("Thorne Research", "", "", "", "USA", "", "Marca", "Suplementos médicos, venta MX", "brand"),
    L("MegaFood", "", "", "", "USA", "", "Marca", "Vitaminas alimentarias, venta MX", "brand"),
    L("Pure Encapsulations", "", "", "", "USA", "", "Marca", "Suplementos hipoalergénicos, venta MX", "brand"),
    L("Innvictus", "https://www.innvictus.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Tienda deportiva MX con suplementos", "brand"),
    L("Marathón Sports", "https://www.marathon-sports.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Tienda deportiva MX con suplementos", "brand"),
    L("Deportes Martí", "https://www.marti.mx/", "", "", "CDMX", "CDMX", "Retail", "Tienda deportiva MX con suplementos", "brand"),
    L("Nutrisport", "", "", "", "México", "México", "Marca", "Suplementos mexicanos", "brand"),
    # --- Distribuidores mayoristas ---
    L("Casa Marzam", "https://www.marzam.com.mx/", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora farmacéutica nacional", "brand"),
    L("Nadro", "https://www.nadro.mx/", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora farmacéutica nacional", "brand"),
    L("Fármacos Nacionales", "", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora farmacéutica", "brand"),
    L("Almacén de Medicinas", "", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora farmacéutica", "brand"),
    L("Disur", "", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora farmacéutica", "brand"),
    L("Fármacos Especializados", "", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora farmacéutica", "brand"),
    # --- Marketplaces ---
    L("Amazon MX vitaminas", "https://www.amazon.com.mx/s?k=vitaminas+y+suplementos", "", "", "México", "México", "Marketplace", "Sellers de vitaminas y suplementos", "research"),
    L("Mercado Libre suplementos", "https://listado.mercadolibre.com.mx/suplementos-alimenticios-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de suplementos", "research"),
    L("TikTok Shop suplementos", "https://shop.tiktok.com/", "", "", "México", "México", "Marketplace", "Venta de suplementos D2C", "research"),
]


def main():
    print("Generating lote 43 (vitaminas y suplementos)…")
    dump("43", "vitaminas_suplementos", "Vitaminas y suplementos MX", SUP)
    print(f"counts: 43={len(SUP)}")


if __name__ == "__main__":
    main()
