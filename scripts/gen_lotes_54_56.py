#!/usr/bin/env python3
"""Generate seeds for lotes 54 (equipo de iluminación) y 56 (suministros
médicos/farmacéuticos). ONLY real companies — fabricantes, distribuidores
y marcas con presencia MX verificable. Target 80-120 cada uno."""
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
# LOTE 54 — Comercializadora / Equipo de iluminación
# ============================================================
ILUMINA = [
    L("Vyrsa (ejemplo)", "https://vyorsa.com.mx/", "", "", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — equipo de iluminación", "ejemplo_cliente"),
    # --- Fabricantes MX ---
    L("Grupo Construlita", "https://www.grupoconstrulita.com/", "", "4422383900", "Querétaro", "Querétaro", "Fabricante", "Líder latinoamericano; marcas Construlita y Tecnolite; planta en Querétaro; alumbrado público GDL y Torreón", "research"),
    L("Tecnolite", "https://www.grupoconstrulita.com/tecnolite", "", "", "Guadalajara", "Jalisco", "Marca", "Marca famosa IMPI; iluminación inteligente; desde 1989 en GDL", "brand"),
    L("Construlita", "https://www.construlita.com/", "", "", "Querétaro", "Querétaro", "Marca", "Desde 1984; iluminación profesional: comercial, industrial, alumbrado público", "brand"),
    L("Ilumex", "https://ilumexmx.com/", "", "5555124372", "CDMX", "CDMX", "Mayoreo", "Distribuidora de luminaria al mayoreo 25 años; Plaza de la Luz, José Marroquí 81, Centro", "research"),
    L("Ilumi de México", "", "", "", "CDMX", "CDMX", "Fabricante", "Fabricante de luminarios para alumbrado público 26+ años; distribuidor Lexalite, Acrilux, Osram, Philips", "research"),
    L("Megamex", "", "", "", "CDMX", "CDMX", "Mayoreo", "Mayorista en material eléctrico industrial, alumbrado público y residencial", "research"),
    L("PEFSA", "https://www.pefsa.com.mx/", "", "5557518292", "CDMX", "CDMX", "Retail", "Sucursal CDMX: Av. Henry Ford 257; distribuye Philips", "research"),
    L("Espacios de Construcción", "https://espaciosdeconstruccion.com/", "", "", "México", "México", "Mayoreo", "Luminarias viales, decorativas, industriales; Tecnolite, Construlita, Ledvance, Magg, Starco", "research"),
    # --- Marcas globales con operación MX ---
    L("Philips Lighting México", "https://www.lighting.philips.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Iluminación, operación MX", "brand"),
    L("Signify (Philips)", "https://www.signify.com/mx", "", "", "CDMX", "CDMX", "Marca", "Grupo que opera Philips Hue y luminarias", "brand"),
    L("Osram / Ledvance", "https://www.ledvance.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Focos y luminarias LED, operación MX", "brand"),
    L("GE Lighting (Savant)", "", "", "", "USA", "", "Marca", "Iluminación, venta MX", "brand"),
    L("Sylvania México", "", "", "", "México", "México", "Marca", "Lámparas y focos, operación MX", "brand"),
    L("Lithonia", "", "", "", "USA", "", "Marca", "Luminarias profesionales, vía distribuidores MX", "brand"),
    L("Holophane", "", "", "", "USA", "", "Marca", "Luminarias industriales, vía distribuidores MX", "brand"),
    L("Beghelli México", "", "", "", "México", "México", "Marca", "Iluminación de emergencia y LED", "brand"),
    L("Feilo Sylvania / Havells", "", "", "", "México", "México", "Marca", "Iluminación, operación MX", "brand"),
    L("Electromag", "", "", "", "México", "México", "Marca", "Material eléctrico e iluminación", "brand"),
    L("Forlighting", "", "", "", "México", "México", "Marca", "Iluminación, venta MX", "brand"),
    L("Solar (focos)", "", "", "", "México", "México", "Marca", "Focos automotrices y generales, venta MX", "brand"),
    L("LEXALITE", "", "", "", "USA", "", "Marca", "Luminarias, vía Ilumi de México", "brand"),
    L("ACRILUX", "", "", "", "México", "México", "Marca", "Luminarias, vía Ilumi de México", "brand"),
    L("LUMICOM", "", "", "", "México", "México", "Marca", "Luminarias, vía Ilumi de México", "brand"),
    L("MAGG", "", "", "", "México", "México", "Marca", "Luminarias y transformadores", "brand"),
    L("Starco", "", "", "", "México", "México", "Marca", "Luminarias", "brand"),
    L("Kichler", "", "", "", "USA", "", "Marca", "Iluminación decorativa, venta MX", "brand"),
    L("Progress Lighting", "", "", "", "USA", "", "Marca", "Iluminación residencial, venta MX", "brand"),
    L("Artika", "", "", "", "Canadá", "", "Marca", "Iluminación moderna, venta MX", "brand"),
    L("Regent Lighting", "", "", "", "USA", "", "Marca", "Iluminación profesional, venta MX", "brand"),
    L("WAC Lighting", "", "", "", "USA", "", "Marca", "Iluminación arquitectónica, venta MX", "brand"),
    L("Maxim Lighting", "", "", "", "USA", "", "Marca", "Iluminación decorativa, venta MX", "brand"),
    # --- Retail / marketplaces ---
    L("Home Depot México", "https://www.homedepot.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Sección de iluminación", "brand"),
    L("The Home Depot iluminación", "https://www.homedepot.com.mx/tienda/iluminacion", "", "", "CDMX", "CDMX", "Canal", "Lámparas, focos y luminarias", "research"),
    L("Sterling Electric", "https://www.sterlingelectric.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Material eléctrico y de iluminación", "brand"),
    L("Coel", "https://www.coel.mx/", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora de material eléctrico e iluminación", "research"),
    L("Grupo Marzam iluminación", "", "", "", "CDMX", "CDMX", "Mayoreo", "Distribución de iluminación", "research"),
    L("Amazon MX iluminación", "https://www.amazon.com.mx/s?k=lamparas+led", "", "", "México", "México", "Marketplace", "Sellers de iluminación", "research"),
    L("Mercado Libre iluminación", "https://listado.mercadolibre.com.mx/iluminacion-led-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de iluminación LED", "research"),
    L("Dirind — iluminación", "https://www.dirind.com/di/iluminacion-general2.html", "", "", "CDMX", "CDMX", "Directorio", "Directorio de proveedores de iluminación", "research"),
]


# ============================================================
# LOTE 56 — MedTech / Suministros médicos / farmacéuticos
# ============================================================
MEDICO = [
    L("Laboratorios PiSA (ejemplo)", "https://www.pisa.com.mx/", "", "", "Guadalajara", "Jalisco", "Ejemplo original", "Ejemplo del cliente — farmacéutica mexicana", "ejemplo_cliente"),
    # --- Laboratorios y fabricantes ---
    L("Laboratorios PiSA", "https://www.pisa.com.mx/", "", "", "Guadalajara", "Jalisco", "Laboratorio", "Farmacéutica mexicana; soluciones intravenosas y medicamentos", "brand"),
    L("Becton Dickinson de México", "https://www.bd.com/mx", "", "", "CDMX", "CDMX", "Fabricante", "Dispositivos médicos, jeringas y catéteres; 12 plantas en MX", "brand"),
    L("Cardinal Health México", "", "", "", "CDMX", "CDMX", "Fabricante", "Manufactura y distribución de productos médicos; 5 plantas en MX", "brand"),
    L("Stryker México", "", "", "", "CDMX", "CDMX", "Fabricante", "Tecnología médica, ortopedia y quirúrgico", "brand"),
    L("3M Health Care México", "https://www.3m.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Vendaje, antisepsia y equipo de protección", "brand"),
    L("Smith+Nephew México", "", "", "", "CDMX", "CDMX", "Marca", "Curación avanzada y ortopedia", "brand"),
    L("Medline Industries México", "", "", "", "CDMX", "CDMX", "Fabricante", "Distribución y manufactura de insumos médicos", "brand"),
    L("Baxter México", "", "", "", "CDMX", "CDMX", "Marca", "Soluciones intravenosas y terapia renal", "brand"),
    L("Johnson & Johnson MedTech", "", "", "", "CDMX", "CDMX", "Marca", "Dispositivos médicos y quirúrgicos", "brand"),
    L("Abbott Médica", "https://www.abbott.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Diagnóstico y dispositivos médicos", "brand"),
    L("Fresenius Medical Care México", "", "", "", "CDMX", "CDMX", "Marca", "Equipos de diálisis", "brand"),
    L("Roche Diagnostics México", "", "", "", "CDMX", "CDMX", "Marca", "Diagnóstico in vitro", "brand"),
    L("Siemens Healthineers México", "", "", "", "CDMX", "CDMX", "Marca", "Equipos de imagenología", "brand"),
    L("GE HealthCare México", "", "", "", "CDMX", "CDMX", "Marca", "Imagenología y monitoreo", "brand"),
    L("BD Biosciences", "", "", "", "CDMX", "CDMX", "Marca", "Citometría y laboratorio", "brand"),
    # --- Distribuidoras MX ---
    L("JTC Tienda Online", "https://jtc.com.mx/", "", "", "México", "México", "Mayoreo", "Material de curación, dental, ortopedia e instrumental médico; menudeo y mayoreo; sector privado y gobierno", "research"),
    L("Proveedores Hospitalarios de México", "https://proveedoreshospitalariosdemexico.com/", "", "", "México", "México", "Mayoreo", "Material médico al mayoreo y menudeo; cobertura nacional", "research"),
    L("J&M Distribuciones", "https://jmdistribuciones.mx/", "info@jmdistribuciones.mx", "3316578530", "Guadalajara", "Jalisco", "Mayoreo", "Material de curación y quirúrgico; San Salvador 1959 y Cruz del Sur 65, GDL", "research"),
    L("Promexsa", "https://www.promexsa.com.mx/", "", "", "México", "México", "Mayoreo", "Material de curación (gasas, vendas, soluciones) por mayoreo; 210 productos", "research"),
    L("GMMC México", "https://www.gmmcmexico.com/", "", "5555304433", "CDMX", "CDMX", "Mayoreo", "Distribuidora de material médico; Viaducto Río de la Piedad 261", "research"),
    L("Casa Marzam", "https://www.marzam.com.mx/", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora farmacéutica nacional", "brand"),
    L("Nadro", "https://www.nadro.mx/", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora farmacéutica nacional", "brand"),
    L("Fármacos Nacionales", "", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora farmacéutica", "brand"),
    L("Mega Farms", "", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora farmacéutica", "brand"),
    L("Grupo Fármacos Especializados", "", "", "", "CDMX", "CDMX", "Mayoreo", "Distribuidora farmacéutica", "brand"),
    # --- Retail farmacéutico ---
    L("Farmacias del Ahorro", "https://www.fahorro.com/", "", "", "CDMX", "CDMX", "Retail", "Cadena nacional", "brand"),
    L("Farmacias Guadalajara", "https://www.farmaciasguadalajara.com.mx/", "", "", "Guadalajara", "Jalisco", "Retail", "Cadena nacional", "brand"),
    L("Farmacias San Pablo", "https://farmaciasanpablo.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadena CDMX", "brand"),
    L("Farmacias Benavides", "https://www.benavides.com.mx/", "", "", "Monterrey", "Nuevo León", "Retail", "Cadena del norte", "brand"),
    L("Farmacias del Sol", "https://www.farmaciasdelsol.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadena CDMX", "brand"),
    L("Farmacias YZA", "https://farmaciasyza.com/", "", "", "CDMX", "CDMX", "Retail", "Cadena CDMX", "brand"),
    L("Farmacias ABC", "https://farmaciasabc.com/", "", "", "CDMX", "CDMX", "Retail", "Cadena CDMX", "brand"),
    L("Farmacias Roma", "https://www.farmaciasroma.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadena CDMX", "brand"),
    L("Farmacias Morelos", "https://www.farmaciasmorelos.com.mx/", "", "", "Cuernavaca", "Morelos", "Retail", "Cadena del sur", "brand"),
    L("Walmart México", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Sección farmacia", "brand"),
    L("Costco México", "https://www.costco.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Farmacia por mayoreo", "brand"),
    L("Sanborns Farmacia", "https://www.sanborns.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Farmacia en tiendas departamentales", "brand"),
    # --- Marcas de insumos ---
    L("Quirmex", "", "", "", "México", "México", "Marca", "Gasas y material de curación", "brand"),
    L("Ambiderm", "", "", "", "México", "México", "Marca", "Guantes y material de curación", "brand"),
    L("Nipro", "", "", "", "Japón", "", "Marca", "Jeringas y venoclisis, venta MX", "brand"),
    L("Tuk (curitas)", "", "", "", "México", "México", "Marca", "Cintas y material de curación", "brand"),
    L("Dibar", "", "", "", "México", "México", "Marca", "Material médico", "brand"),
    L("Drotasa", "", "", "", "México", "México", "Marca", "Guantes y material médico", "brand"),
    L("Dryper", "", "", "", "México", "México", "Marca", "Toallitas y productos desechables", "brand"),
    L("Jaloma", "", "", "", "México", "México", "Marca", "Guantes de látex", "brand"),
    L("Medicel", "", "", "", "México", "México", "Marca", "Material de curación", "brand"),
    L("Vendamax", "", "", "", "México", "México", "Marca", "Vendas y curitas", "brand"),
    L("Sensi Medical", "", "", "", "México", "México", "Marca", "Material de curación", "brand"),
    L("Tegaderm (3M)", "", "", "", "USA", "", "Marca", "Apósitos transparentes, venta MX", "brand"),
    L("Alcomex", "", "", "", "México", "México", "Marca", "Alcohol y antisépticos", "brand"),
    L("Bsn (BSN Medical)", "", "", "", "Alemania", "", "Marca", "Vendaje, venta MX", "brand"),
    # --- Marketplaces ---
    L("Amazon MX material médico", "https://www.amazon.com.mx/s?k=material+medico", "", "", "México", "México", "Marketplace", "Sellers de insumos médicos", "research"),
    L("Mercado Libre insumos médicos", "https://listado.mercadolibre.com.mx/material-medico-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de material médico", "research"),
]


def main():
    print("Generating lotes 54 y 56 (solo empresas reales)…")
    dump("54", "equipo_iluminacion", "Equipo de iluminación MX", ILUMINA)
    dump("56", "suministros_medicos_farmaceuticos", "Suministros médicos / farmacéuticos MX", MEDICO)
    print(f"counts: 54={len(ILUMINA)} 56={len(MEDICO)}")


if __name__ == "__main__":
    main()
