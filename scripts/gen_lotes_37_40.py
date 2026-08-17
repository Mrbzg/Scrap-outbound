#!/usr/bin/env python3
"""Generate seeds for lotes 37-40 (gomitas de vitaminas, libros de colección,
artículos de limpieza, perfumes). ONLY real companies — no generic city padding."""
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
# LOTE 37 — Alimentos / Gomitas de vitaminas
# ============================================================
GOMMIES = [
    L("Vital Suplementos MX (ejemplo)", "https://vitalsuplementosmex.com/", "", "", "México", "México", "Ejemplo original", "Ejemplo del cliente — gomitas de vitaminas y suplementos", "ejemplo_cliente"),
    L("Gummy Life", "https://www.gummylife.mx/", "", "", "México", "México", "D2C", "Marca mexicana: gomitas biotina, omega 3, magnesio; 150k+ unidades; ML/Amazon/TikTok", "research"),
    L("Gummy Life — Gomitas Néurus", "https://www.gummylife.mx/", "", "", "México", "México", "Producto", "Omega 3 + L-Teanina + Complejo B en gomitas", "research"),
    L("Gummy Life — Gomitas Zenup", "https://www.gummylife.mx/", "", "", "México", "México", "Producto", "Magnesio + 5-HTP", "research"),
    L("B Life", "https://www.blife.mx/", "", "", "CDMX", "CDMX", "D2C", "Suplementos y vitaminas, fuerte en ecom MX", "research"),
    L("Plenlife", "", "", "", "México", "México", "Marca", "Gomitas calcio + Vit D, multivitamínico adulto; venta ML", "research"),
    L("Geomed", "", "", "", "México", "México", "Distribuidor", "Distribuye Plenlife en ML (4.9★, 125 reviews)", "research"),
    L("Suplefit MX", "", "", "", "México", "México", "Distribuidor", "Vitafusion, gomitas importadas vía ML", "research"),
    L("OK Vitaminas", "", "", "", "México", "México", "Distribuidor", "Nature's Way y gomitas importadas vía ML", "research"),
    L("Vitamin World", "", "", "", "México", "México", "Retail", "Natrol melatonina gomitas vía ML", "research"),
    L("Belabear", "", "", "", "México", "México", "Marca", "Gomitas multivitamínico women 150 pzs", "research"),
    L("C-Boost", "", "", "", "México", "México", "Marca", "Gomitas multivitamínicas 180 pzs, sabor cítrico", "research"),
    L("Heally", "", "", "", "México", "México", "Marca", "Multivitamínico + colágeno gomitas zarzamora", "research"),
    L("Vitafusion", "", "", "", "USA", "", "Marca", "Gomitas multivitamínicas y calcio+D3, importado", "brand"),
    L("Nature's Way", "", "", "", "USA", "", "Marca", "Gomitas crecimiento y altura, importado", "brand"),
    L("Nature Made", "", "", "", "USA", "", "Marca", "Gomitas omega 3 / magnesio, importado", "brand"),
    L("Centrum (Pfizer)", "", "", "", "USA", "", "Marca", "Gomitas multivitamínico + omega, importado", "brand"),
    L("Natrol", "", "", "", "USA", "", "Marca", "Melatonina gomitas, importado", "brand"),
    L("Nature's Bounty", "", "", "", "USA", "", "Marca", "Gomitas zinc y multivitamínicas, importado", "brand"),
    L("Nature's Truth", "", "", "", "USA", "", "Marca", "Vitamina D3 gomitas, importado", "brand"),
    L("Básicos de la casa", "", "", "", "México", "México", "Distribuidor", "Vende Nature Made y Centrum en ML", "research"),
    L("Farmacia San Pablo", "https://farmaciasanpablo.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadena de farmacias con vitaminas", "brand"),
    L("Farmacias del Ahorro", "https://www.fahorro.com/", "", "", "CDMX", "CDMX", "Retail", "Vende gomitas y suplementos", "brand"),
    L("Farmacias Guadalajara", "https://www.farmaciasguadalajara.com.mx/", "", "", "Guadalajara", "Jalisco", "Retail", "Cadena con línea de vitaminas", "brand"),
    L("Walmart México", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Autoservicio con sección de vitaminas", "brand"),
    L("Costco México", "https://www.costco.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Gomitas por mayoreo (multipack)", "brand"),
    L("Amazon MX gomitas", "https://www.amazon.com.mx/s?k=gomitas+de+vitaminas", "", "", "México", "México", "Marketplace", "Sellers de gomitas vitamínicas", "research"),
    L("Mercado Libre gomitas", "https://listado.mercadolibre.com.mx/vitaminas-de-gomitas-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de vitaminas en gomitas", "research"),
]


# ============================================================
# LOTE 38 — Libros / Libros de colección
# ============================================================
LIBROS = [
    L("Penguin Libros MX (ejemplo)", "https://www.penguinlibros.com/mx/", "", "", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — editorial y librería en línea", "ejemplo_cliente"),
    L("Librero en Andanzas", "https://libreroenandanzas.com/", "contacto@libreroenandanzas.com", "5580820431", "CDMX", "CDMX", "Ecom", "Libros raros, usados y de colección; CDMX/GDL/Pachuca; compra bibliotecas", "research"),
    L("Librero en Andanzas GDL", "https://libreroenandanzas.com/", "", "", "Guadalajara", "Jalisco", "Sucursal", "López Cotilla 805 esq. Rayón, Americana", "research"),
    L("Librero en Andanzas Pachuca", "https://libreroenandanzas.com/", "", "", "Pachuca", "Hidalgo", "Sucursal", "Av. Juárez 102, Centro", "research"),
    L("Valis Libros Raros", "https://valislibrosraros.com/", "librosvalis@gmail.com", "5579627932", "CDMX", "CDMX", "Ecom", "Libros raros, antiguos y firmados; envíos nacionales e internacionales", "research"),
    L("Librería El Hallazgo", "", "", "", "CDMX", "CDMX", "Librería de viejo", "Libros raros, usados, nuevos y de ocasión; desde 1996, Col. Roma", "research"),
    L("Librería Jorge Cuesta", "", "", "", "CDMX", "CDMX", "Librería de viejo", "Del mismo fundador de El Hallazgo; compra/venta de libros", "research"),
    L("Libros Prohibidos", "", "", "", "CDMX", "CDMX", "Librería de viejo", "Librería de usados y curiosidades editoriales, CDMX", "research"),
    L("Subastas Morton", "https://morton.com.mx/", "", "", "CDMX", "CDMX", "Subasta", "Subastas de arte, libros y piezas de colección", "research"),
    L("Gandhi", "https://www.gandhi.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Cadena de librerías y edición", "brand"),
    L("Porrúa", "https://porrua.mx/", "", "", "CDMX", "CDMX", "Retail", "Librería y editorial histórica", "brand"),
    L("El Péndulo", "https://pendulo.com/", "", "", "CDMX", "CDMX", "Retail", "Librerías con cafetería, CDMX", "brand"),
    L("El Sótano", "https://www.elsotano.com/", "", "", "CDMX", "CDMX", "Retail", "Librería y papelería", "brand"),
    L("Fondo de Cultura Económica", "https://www.fondodeculturaeconomica.com/", "", "", "CDMX", "CDMX", "Editorial", "Editorial estatal con librerías propias", "brand"),
    L("Educal", "https://www.educal.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Red de librerías del Estado", "brand"),
    L("Librerías Gonvill", "https://gonvill.com.mx/", "", "", "Guadalajara", "Jalisco", "Retail", "Cadena de librerías del occidente", "brand"),
    L("Buscalibre México", "https://www.buscalibre.com.mx/", "", "", "CDMX", "CDMX", "Ecom", "Libros nuevos y usados, marketplace editorial", "research"),
    L("Iberlibro", "https://www.iberlibro.com/", "", "", "", "", "Marketplace", "Marketplace de libros raros y usados (vendedores MX)", "research"),
    L("eBay libros colección", "https://www.ebay.com/b/Antiquarian-Collectible-Books-in-Spanish/29223/bn_43492545", "", "", "", "", "Marketplace", "Vendedores de libros antiguos en español", "research"),
    L("Amazon MX libros colección", "https://www.amazon.com.mx/s?k=libros+de+coleccion", "", "", "México", "México", "Marketplace", "Sellers de libros de colección", "research"),
    L("Mercado Libre libros usados", "https://listado.mercadolibre.com.mx/libros-usados", "", "", "México", "México", "Marketplace", "Libros usados y de colección", "research"),
]


# ============================================================
# LOTE 39 — Hogar / Artículos de limpieza
# ============================================================
LIMPIEZA = [
    L("Uline México (ejemplo)", "https://es.uline.mx/", "", "", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — artículos de limpieza y empaque", "ejemplo_cliente"),
    L("La Avenida", "https://laavenida.com.mx/", "", "8117672929", "Monterrey", "Nuevo León", "Fabricante", "Químicos de limpieza y desinfección; granel 1L-1000L; Ruiz Cortines 104 Pte", "research"),
    L("La Avenida Escobedo", "https://laavenida.com.mx/", "", "8114920810", "Escobedo", "Nuevo León", "Sucursal", "Calle Sétima 601, Praderas Girasoles", "research"),
    L("Yanitor", "https://www.yanitor.com/", "tiendaweb@yanitor.com", "8112340500", "Monterrey", "Nuevo León", "Fabricante", "Limpieza industrial; distribuidor Rubbermaid/Purell/Diversey; Av. Fundidora 501", "research"),
    L("Energy Clean", "https://www.energyclean.mx/", "ventas@energyclean.mx", "8130685708", "Monterrey", "Nuevo León", "Fabricante", "Químicos, papel institucional y jarcería; Juventino Rosas 2008", "research"),
    L("Codelmex", "https://www.codelmex.mx/", "ventas@codelmex.mx", "5557633898", "CDMX", "CDMX", "Distribuidor", "60+ años; 600+ artículos de limpieza mayoreo; Topacio 36 Centro", "research"),
    L("MayoreoTotal", "https://www.mayoreototal.net/", "mtnotificacion@gmail.com", "5560752408", "CDMX", "CDMX", "Mayoreo", "Abarrotes y limpieza al mayoreo CDMX; detergentes, cloro, papel", "research"),
    L("Cepillos El Castor", "https://www.cepilloselcastor.com/", "", "", "Guadalajara", "Jalisco", "Fabricante", "70+ años; cepillos, escobas, trapeadores y jaladores profesionales", "research"),
    L("Alcodistribuidora", "https://alcodistribuidora.com/", "", "", "", "", "Distribuidor", "Distribuidor master de El Castor y grandes marcas de limpieza", "research"),
    L("Grupo Kryss", "", "", "", "Aguascalientes", "Aguascalientes", "Fabricante", "Escobas, cepillos y jarciería, marca mexicana", "brand"),
    L("Fábrica de Jabón La Corona", "https://www.lacorona.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Detergente Roma, Foca y jabones", "brand"),
    L("Diversey México", "https://diversey.com/es-mx", "", "", "CDMX", "CDMX", "Marca", "Limpieza institucional e higiene", "brand"),
    L("3M México", "https://www.3m.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Scotch-Brite, esponjas y limpiadores", "brand"),
    L("Clorox México", "", "", "", "CDMX", "CDMX", "Marca", "Cloro, Pinol y desinfectantes", "brand"),
    L("P&G México (Ace / Mr. Clean)", "", "", "", "CDMX", "CDMX", "Marca", "Detergentes y multiusos", "brand"),
    L("Rubbermaid Commercial", "", "", "", "USA", "", "Marca", "Contenedores y jarciería profesional, vía distribuidores MX", "brand"),
    L("Purell / GOJO", "", "", "", "USA", "", "Marca", "Sanitizantes y dispensadores, vía Yanitor", "brand"),
    L("Surtidora de Productos de Limpieza", "", "", "3336532518", "Puerto Melaque", "Jalisco", "Mayoreo", "Almorol, aromatizantes y brillo a mayoreo; suc. Zapopan 33 3805 6628", "research"),
    L("Walmart México", "https://www.walmart.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Autoservicio: limpieza de hogar", "brand"),
    L("Costco México", "https://www.costco.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Limpieza por volumen", "brand"),
    L("Home Depot México", "https://www.homedepot.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Limpieza y jarciería", "brand"),
    L("Amazon MX limpieza", "https://www.amazon.com.mx/s?k=articulos+de+limpieza", "", "", "México", "México", "Marketplace", "Sellers de artículos de limpieza", "research"),
    L("Mercado Libre limpieza", "https://listado.mercadolibre.com.mx/articulos-de-limpieza-mayoreo", "", "", "México", "México", "Marketplace", "Mayoreo de limpieza", "research"),
]


# ============================================================
# LOTE 40 — Belleza / Perfumes
# ============================================================
PERFUMES = [
    L("Arome (ejemplo)", "https://arome.mx/", "", "", "CDMX", "CDMX", "Ejemplo original", "Ejemplo del cliente — perfumes", "ejemplo_cliente"),
    L("Perfumería La Rosa", "https://perfumes-originales.com.mx/", "", "", "CDMX", "CDMX", "Mayoreo", "Perfumes originales mayoreo sin compra mínima; tienda física; árabes y diseñador", "research"),
    L("PerfumeMayoreo", "https://www.perfumemayoreo.mx/", "", "", "", "", "Mayoreo", "10+ años; 300 marcas; hasta 70% descuento; envíos MX", "research"),
    L("X Mayoreo", "https://xmayoreo.mx/", "", "", "", "", "Mayoreo", "Perfumes al por mayor para distribuidores y regalos corporativos", "research"),
    L("Bellaroma", "https://www.bellaroma.mx/", "", "", "CDMX", "CDMX", "Mayoreo", "20+ años; perfumes importados originales; precio mayoreo desde 6 pzs", "research"),
    L("Romar Perfumes Árabes", "https://romarperfumes.com/", "", "", "", "", "Mayoreo", "Perfumes árabes originales para reventa; envíos MX; importación directa", "research"),
    L("Perfumerías Estrada", "", "", "", "CDMX", "CDMX", "Retail", "Cadena de perfumerías con tienda en línea", "brand"),
    L("Juleriaque", "", "", "", "CDMX", "CDMX", "Retail", "Perfumería con sucursales y ecom", "brand"),
    L("Jafra", "https://www.jafra.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Venta por catálogo, perfumes y cosméticos", "brand"),
    L("Zermat", "", "", "", "Puebla", "Puebla", "Marca", "Perfumes y cosméticos por catálogo", "brand"),
    L("Yanbal", "", "", "", "", "", "Marca", "Perfumería por catálogo", "brand"),
    L("Esika / L'Bel (Belcorp)", "", "", "", "", "", "Marca", "Perfumería por catálogo", "brand"),
    L("Natura México", "https://www.natura.com.mx/", "", "", "CDMX", "CDMX", "Marca", "Perfumes y cosmética por consultoría", "brand"),
    L("Liverpool Perfumería", "https://www.liverpool.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Perfumería de diseñador", "brand"),
    L("El Palacio de Hierro", "https://www.elpalaciodehierro.com/", "", "", "CDMX", "CDMX", "Retail", "Perfumería premium", "brand"),
    L("Sears Perfumería", "https://www.sears.com.mx/", "", "", "CDMX", "CDMX", "Retail", "Perfumería de diseñador", "brand"),
    L("Amazon MX perfumes", "https://www.amazon.com.mx/s?k=perfumes", "", "", "México", "México", "Marketplace", "Sellers de perfumes", "research"),
    L("Mercado Libre perfumes", "https://listado.mercadolibre.com.mx/perfumes-mayoreo", "", "", "México", "México", "Marketplace", "Perfumes originales y de mayoreo", "research"),
    L("Perfume árabe — Amber Rouge", "https://romarperfumes.com/", "", "", "", "", "Producto", "Top-seller árabe, reventa", "research"),
    L("Perfume árabe — Club de Nuit", "https://romarperfumes.com/", "", "", "", "", "Producto", "Club de Nuit Sillage / Woman", "research"),
]


def main():
    print("Generating lotes 37-40 (solo empresas reales)…")
    dump("37", "gomitas_vitaminas", "Gomitas de vitaminas MX", GOMMIES)
    dump("38", "libros_coleccion", "Libros de colección MX", LIBROS)
    dump("39", "articulos_limpieza", "Artículos de limpieza MX", LIMPIEZA)
    dump("40", "perfumes", "Perfumes MX", PERFUMES)
    print(f"counts: 37={len(GOMMIES)} 38={len(LIBROS)} 39={len(LIMPIEZA)} 40={len(PERFUMES)}")


if __name__ == "__main__":
    main()
