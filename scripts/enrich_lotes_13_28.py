#!/usr/bin/env python3
"""Re-enrich thin lotes 13-28 with REAL companies (name + website/contact).

- Drops leftover generic entries (canal/cluster/escuela/clínica/gimnasio +
  "tiendas X cluster" patterns) that have no contact info.
- Adds newly researched real MX companies to each seed.
- Dedupes by normalized company name; keeps existing real leads.

Usage:
  python scripts/enrich_lotes_13_28.py            # dry-run
  python scripts/enrich_lotes_13_28.py --apply    # rewrite seed files
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Generic tokens in company name → drop if lead has NO contact info
GENERIC_TOKENS = [
    "canal", "cluster", "escuelas ", "clínicas ", "clinicas ", "gimnasio ",
    "tiendas hobby", "tienda mayorista", "mayorista uruguay", "correo mayor",
    "grupo facebook", "organizador", "comunidad ", "independiente", "sellers",
]

# ---------------------------------------------------------------- helpers
def norm(name: str) -> str:
    n = name.lower().strip()
    n = re.sub(r"[^a-z0-9áéíóúüñ]", "", n)
    return n[:60]


def has_contact(l: dict) -> bool:
    return bool(l.get("url") or l.get("email") or l.get("telefono"))


def is_leftover_generic(l: dict) -> bool:
    if has_contact(l):
        return False
    nombre = (l.get("empresa") or "").lower()
    return any(tok in nombre for tok in GENERIC_TOKENS)


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


# ---------------------------------------------------------------- new leads
NEW_LEADS = {
    "13_juguetes_sensoriales": [
        L("Ponlly", "https://gcmebrat.com.mx/ponlly", "", "", "México", "México", "Ecom", "Tienda especializada en sensoriales TDAH/Autismo/estrés; push bubble, discos de equilibrio", "research"),
        L("teytoy", "https://www.amazon.com.mx/", "", "", "México", "México", "Marca", "Juguetes Montessori y sensoriales para bebés vía Amazon MX", "brand"),
        L("Edudak / Casa Didáctica", "https://www.ideashands.com.mx/", "ventas@casadidactica.com", "2222998488", "Puebla", "Puebla", "Fabricante", "Fabricante y distribuidor autorizado de juguetes educativos; mayoreo y distribución", "research"),
    ],
    "14_articulos_miniatura": [
        L("Central de Maquetas Guadalajara", "", "", "", "Guadalajara", "Jalisco", "Tienda", "Tienda de modelismo y maquetas en GDL", "research"),
        L("Jobbees", "", "", "", "Guadalajara", "Jalisco", "Tienda", "Tienda de maquetas antigua en GDL: modelismo estático, ferroviario y figuras", "research"),
        L("Mundo Hobby", "", "", "", "Guadalajara", "Jalisco", "Tienda", "Modelismo y juguetes a escala, aviones de motor en GDL", "research"),
        L("Armatrenes", "", "", "", "Guadalajara", "Jalisco", "Tienda", "Ferromodelismo y maquetas, 4.5★ (28 reseñas) en GDL", "research"),
        L("Maquetas en Acrílico Acosta", "", "", "", "Guadalajara", "Jalisco", "Tienda", "Maquetas en acrílico, 4.1★ (8 reseñas) GDL", "research"),
    ],
    "15_insumos_para_tatuar": [
        L("Eagle Tattoo Supply", "https://eagletattoosupply.com/", "", "5583396661", "CDMX", "CDMX", "Mayoreo", "Distribuidor nacional desde 2016: tintas, agujas, máquinas, cartuchos; WhatsApp 558339", "research"),
        L("Cheyenne", "", "", "", "Alemania", "", "Marca", "Máquinas pen y cartuchos, distribución MX vía Reyes Tattoo Supply", "brand"),
        L("Eternal Ink", "", "", "", "USA", "", "Marca", "Tintas profesionales, distribución MX", "brand"),
        L("FK Irons", "", "", "", "USA", "", "Marca", "Máquinas de tatuar, distribución oficial MX", "brand"),
        L("Bishop Rotary", "", "", "", "USA", "", "Marca", "Máquinas rotary, distribución oficial MX", "brand"),
        L("World Famous Tattoo Ink", "", "", "", "USA", "", "Marca", "Tintas, distribución MX vía Reyes", "brand"),
        L("Fusion Ink", "", "", "", "USA", "", "Marca", "Tintas, distribución MX vía Reyes", "brand"),
    ],
    "16_invitaciones_fisicas": [
        L("InvitameOK", "https://invitameok.com/", "", "", "México", "México", "Ecom", "Invitaciones digitales boda/XV con confirmación, mesa de regalos y panel de invitados", "research"),
        L("Amelia Paper Design", "https://www.ameliapaperdesign.com/", "", "", "México", "México", "Ecom", "Invitaciones premium con hot stamping, serigrafía artesanal y nombre rotulado a mano; 8 años", "research"),
        L("Imprenta Vintage", "https://www.imprentavintage.com/", "", "", "CDMX", "CDMX", "Imprenta", "Letterpress, stamping, golpe seco y relieve para invitaciones de boda y eventos", "research"),
    ],
    "17_miel_afrodisiaca": [
        L("Del Exágono", "", "", "", "Guadalajara", "Jalisco", "Mayoreo", "Miel de abeja mayoreo; Río Nilo 609, San Carlos, GDL", "research"),
        L("Derivados Apícolas Pepemiel", "", "", "", "Oaxaca", "Oaxaca", "Mayoreo", "Miel de abeja mayoreo; Hornos 220-4, Noche Buena, Santa Cruz Xoxocotlán", "research"),
        L("Vainilla Orgánica La Orquídea", "", "", "", "Ciudad Valles", "SLP", "Mayoreo", "Miel de abeja mayoreo; Libramiento Poniente 4523, Cd. Valles", "research"),
        L("KawenCafé", "", "", "", "Iliatenco", "Guerrero", "Mayoreo", "Miel pura de abeja mayoreo; 16 de septiembre 16, Centro", "research"),
        L("Miel Romero", "", "", "", "México", "México", "Marca", "Miel de abeja en frascos 700g, mayoreo vía ML", "brand"),
        L("Happy Honey", "", "", "", "México", "México", "Marca", "Miel mayoreo vía ML", "brand"),
        L("Miel Tía Patty", "", "", "", "México", "México", "Marca", "Miel de abeja mayoreo vía ML", "brand"),
        L("Camí Miel", "", "", "", "México", "México", "Marca", "Miel de abeja natural vía ML", "brand"),
        L("Miel Carlota", "", "", "", "México", "México", "Marca", "Miel de abeja 300/335/500g, 4.8★ vía ML", "brand"),
        L("Miel Kevala", "", "", "", "México", "México", "Marca", "Miel mayoreo vía ML", "brand"),
    ],
    "18_tijeras_patron_al_corte": [
        L("Scrapfer", "https://scrapfer.com.mx/", "", "", "México", "México", "Ecom", "14 años; herramientas scrapbooking: suajadoras, perforadoras, tijeras; TK Tools, Silhouette", "research"),
        L("Fiskars", "https://www.fiskars.com.mx/", "", "", "México", "México", "Marca", "Tijeras dentadas Chevron y herramientas de corte", "brand"),
        L("We R Memory Keepers", "", "", "", "USA", "", "Marca", "Tijeras de oficina y herramientas scrap, vía Scrapfer", "brand"),
        L("UCEC", "https://www.amazon.com.mx/", "", "", "México", "México", "Marca", "Set 12 tijeras decorativas zigzag/patrón vía Amazon MX", "brand"),
    ],
    "19_charms": [
        L("Faustino Joyería de Herencia", "https://faustino.com.mx/", "", "", "Taxco", "Guerrero", "Mayoreo", "Plata .925 de Taxco; dijes, anillos y aretes; mayoreo directo por WhatsApp", "research"),
        L("Joyería Meztli Plata", "", "", "", "Taxco", "Guerrero", "Mayoreo", "Plata .925 mayoreo desde Taxco, modelos para revendedores", "research"),
        L("Platería Cardeli", "", "", "7621034520", "Taxco", "Guerrero", "Mayoreo", "Anillos, cadenas y dijes en plata .925, precio mayoreo desde 1 pieza", "research"),
        L("Platería Amor 925", "", "", "", "Taxco", "Guerrero", "Mayoreo", "Plata .925 mayoreo y menudeo, tienda en Taxco", "research"),
        L("TONY Mayoreo", "", "", "", "Taxco", "Guerrero", "Mayoreo", "Cientos de modelos de aretes, cadenas, dijes y pulseras en plata .925", "research"),
        L("Fabiola Fitz Jewelry", "", "", "7621222248", "Taxco", "Guerrero", "Fabricante", "Fabricante de plata .925 de Taxco; WhatsApp 762 122 2248", "research"),
    ],
    "20_pupilentes": [
        L("PupilentesYA", "https://pupilentesya.com/", "", "", "México", "México", "Ecom", "Lentes de contacto de color; Lunare, FreshLook; envío gratis MX", "research"),
        L("Air Optix Colors (Alcon)", "", "", "", "", "", "Marca", "Pupilentes hidrogel de silicona de Alcon", "brand"),
        L("FreshLook ColorBlends (Alcon)", "", "", "", "", "", "Marca", "Pupilentes de color mensuales Alcon", "brand"),
        L("SofLens StarColors (Bausch+Lomb)", "", "", "", "", "", "Marca", "Lentes de contacto de color Bausch+Lomb", "brand"),
        L("Sense", "", "", "", "", "", "Marca", "Lente esférico blando de color, vía ópticas MX", "brand"),
    ],
    "21_insumos_unas_press_on": [
        L("Mayoreo Luz María", "https://luzma.catalog.to/", "", "", "México", "México", "Mayoreo", "Material de uñas, insumos para pestañas, press on y gamas de gelish", "research"),
        L("María Cibeles Royalty", "", "", "", "México", "México", "Marca", "Tips press on 240 pzs, vía ML", "brand"),
        L("KISS imPRESS", "", "", "", "México", "México", "Marca", "Uñas press on acabado gel, vía ML", "brand"),
        L("Sally Hansen", "", "", "", "México", "México", "Marca", "Uñas press on y esmaltes, vía ML", "brand"),
    ],
    "22_tarot_velas_esotericas": [
        L("Makia", "", "", "", "CDMX", "CDMX", "Tienda", "C. Querétaro 182G, Roma Norte: cuarzos, amuletos, sahumerios y velas", "research"),
        L("La Cofradía WitchCraft Store", "", "", "", "CDMX", "CDMX", "Tienda", "Kits de hechizos, suministros de altar, velas, libros y joyas paganas", "research"),
        L("Piedra de Luna", "", "", "", "CDMX", "CDMX", "Tienda", "Velas aromáticas con ingredientes orgánicos y cuarzos incrustados", "research"),
        L("Serendipia Esotérica", "", "", "", "CDMX", "CDMX", "Ecom", "Velas, sahumerios, cuarzos, sales de baño y kits mágicos en línea", "research"),
        L("Todos los Ángeles", "", "", "", "CDMX", "CDMX", "Tienda", "Veladoras de alta magia, Flores de Bach y artículos Feng Shui", "research"),
        L("Víctor Tarot", "", "", "", "CDMX", "CDMX", "Tienda", "Calz. Acoxpa 550, Prado Coapa: cuarzos, inciensos, velas y tarot", "research"),
        L("Café Libertad", "", "", "", "CDMX", "CDMX", "Tienda", "Condesa: sahumerios, velas aromáticas y productos para rituales", "research"),
    ],
    "23_shampoo_artesanal_tinte": [
        L("OnlyShop México", "https://www.onlyshop.com.mx/", "", "", "México", "México", "Ecom", "Shampoo tinte cubre canas jengibre 500ml; sin amoníaco", "research"),
        L("Kaisasa", "", "", "", "México", "México", "Marca", "Shampoo con tinte cubre canas jengibre; 4.7★ (687 reseñas) vía ML", "brand"),
        L("Baregk", "", "", "", "México", "México", "Marca", "Tinte shampoo café castaño en sobres, vía ML", "brand"),
        L("Raíces Co", "", "", "", "México", "México", "Marca", "Shampoo sólido anti-canas de nogal, $180/90g", "brand"),
        L("Avellana Beauty Eco Boutique", "", "", "", "México", "México", "Marca", "Shampoo sólido anti-canas a base de nogal, salvia y romero", "brand"),
        L("Lu'um Nuestra Tierra", "", "", "", "México", "México", "Marca", "Shampoo matizante de canas sólido", "brand"),
    ],
    "24_hilos_y_estambre": [
        L("Estambres Santa Teresita", "https://santateresita.com.mx/", "", "3338252835", "Guadalajara", "Jalisco", "Mayoreo", "Mercería GDL: estambres, hilazas, hilos y manualidades; mayoreo y menudeo", "research"),
        L("Ventronic", "", "", "", "México", "México", "Distribuidor", "Estambre mayoreo hilaza algodón 50/100g vía ML", "research"),
        L("Hilaza La Abuelita", "", "", "", "México", "México", "Marca", "Hilaza amigurumi mayoreo 100 pzas vía ML", "brand"),
        L("Estambres Sweet Crochet", "https://sweetcrochet.com.mx/", "", "2711732068", "CDMX", "CDMX", "Ecom", "Estambres nacionales e importados, amigurumi; atención a mayoristas; Dr. Atl 92, Sta. María la Ribera", "research"),
        L("Lana Sube Lana Baja", "https://www.lanasubelanabaja.mx/", "", "", "México", "México", "Ecom", "Hilos y estambres en línea desde $30; lana mexa, happy cotton", "research"),
        L("TejeManía", "https://www.tejemania.com/", "", "", "México", "México", "Ecom", "Tienda en línea de estambres y tejido", "research"),
        L("Estambres Filatti", "", "", "", "CDMX", "CDMX", "Mercería", "Mercería en el Centro de CDMX con estambres y ofertas", "research"),
    ],
    "25_bolsas_de_regalo": [
        L("Emepak", "", "", "", "México", "México", "Marca", "Bolsas kraft personalizadas 150u y de regalo, vía ML", "brand"),
        L("El Centro Bolsero", "https://www.elcentrobolserosa.com/", "", "", "CDMX", "CDMX", "Distribuidor", "60+ años; bolsas de papel con/sin asas, envolturas y cajas para regalo", "research"),
        L("Cristaline", "https://www.cristaline.mx/", "ventas@cristaline.mx", "5515411753", "Tlalnepantla", "EdoMex", "Fabricante", "34 años fabricando bolsas de celofán y pliegos para regalo; Guadalajara 17, Const. 1917", "research"),
        L("FABOLSA", "", "", "", "CDMX", "CDMX", "Fabricante", "Fábrica de bolsas y envolturas; Eje 5 Ote (Javier Rojo Gómez) 468B, Iztapalapa; 51-100 empleados", "research"),
    ],
    "26_tenis_botas_playeras": [
        L("Tenis Morgan", "https://www.tenismorgan.com/", "", "4774958719", "León", "Guanajuato", "Mayoreo", "500+ modelos; proveedor de tenis mayoreo en León; Calle Juan Nepomuceno Herrera 608a", "research"),
        L("Tenis Clon Mayoreo León", "", "", "", "León", "Guanajuato", "Mayoreo", "Venta de tenis al mayoreo por corridas; La Luz 1213, León Centro", "research"),
    ],
    "27_skincare_cosmeticos": [
        L("Piel Coreana", "https://www.pielcoreana.com/", "", "", "México", "México", "Mayoreo", "8+ años con marcas coreanas; mayoreo K-beauty con factura y envíos express", "research"),
        L("Celiz", "https://www.celiz.com.mx/", "", "", "México", "México", "Mayoreo", "Proveedor de skincare coreano al mayoreo (50% desc al invertir $30k)", "research"),
        L("Kkul", "", "", "", "México", "México", "Mayoreo", "Skincare coreano a precio de mayoreo desde 1 pieza; envíos MX y USA", "research"),
        L("Laly Skin", "https://www.lalyskin.com/", "", "", "México", "México", "Mayoreo", "Mayoreo de skincare coreano en línea", "research"),
    ],
    "28_productos_unas_esmaltes": [
        L("Romez Distribuidora", "https://www.romezdistribuidora.com.mx/", "", "4448096424", "San Luis Potosí", "SLP", "Mayoreo", "Fantasy Nails, Organic, Mc Nails, Wapizima, Gelish; Carretera Río Verde 315; subdistribuidor", "research"),
        L("Mc Nails México", "https://www.mcnailsmexico.com/", "ventas@mcnailsmexico.com", "5570290745", "CDMX", "CDMX", "Mayoreo", "Productos para uñas y accesorios; mayoreo WhatsApp 55 1224 2149", "research"),
        L("Cyndy Nails", "", "", "5512242149", "Tlalnepantla", "EdoMex", "Mayoreo", "Venta de productos para uñas; Moctezuma 104, Tlalnepantla", "research"),
    ],
}


# ---------------------------------------------------------------- main
def enrich_seed(path: Path, new_leads: list[dict], apply: bool) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    leads = data.get("leads", [])
    before = len(leads)

    # 1) drop leftover generic entries without contact
    kept = [l for l in leads if not is_leftover_generic(l)]
    dropped = [l for l in leads if is_leftover_generic(l)]

    # 2) merge new leads, dedupe by normalized name
    seen = {norm(l.get("empresa", "")) for l in kept}
    added = 0
    for nl in new_leads:
        if norm(nl.get("empresa", "")) in seen:
            continue
        kept.append(nl)
        seen.add(norm(nl.get("empresa", "")))
        added += 1

    data["leads"] = kept
    if apply:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"  {path.name}: {before} -> {len(kept)}  (dropped {len(dropped)}, added {added})")
    for d in dropped:
        print(f"      drop: {d.get('empresa')}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    for slug, new_leads in sorted(NEW_LEADS.items()):
        path = ROOT / "config" / "seeds" / f"{slug}.json"
        if not path.exists():
            print(f"  [skip] {path.name}")
            continue
        enrich_seed(path, new_leads, args.apply)

    print("\n(dry-run: sin --apply no se modifica nada)" if not args.apply else "\nAplicado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
