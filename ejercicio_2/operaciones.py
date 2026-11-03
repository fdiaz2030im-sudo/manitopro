"""EJERCICIO 10 — Lógica del reporte

Implementa generar_reporte(productos). Cada producto tiene nombre único,
precio y stock enteros no negativos, y categoria.
Devuelve un diccionario con:
- disponibles: lista de nombres con stock > 0, en el orden original.
  Usa filter y map con lambda.
- valor_total: suma de precio * stock de todos los productos.
  Usa map y reduce con lambda, con valor inicial 0.
- hay_agotados: booleano que indica si algún stock es 0.
  Usa any sobre map con lambda.
- categorias: set con todas las categorías. Usa comprensión de sets.
- precios_con_recargo: lista de tuplas (nombre, precio con recargo del 10 %),
  solo para productos con stock > 0, en el orden original.
  Define una lambda para el recargo, redondeado a dos decimales con round,
  e invócala dentro de una comprensión de listas.
No modifiques productos ni imprimas dentro de la función.
Para [] devuelve listas y set vacíos, valor_total=0 y hay_agotados=False.
"""

"""EJERCICIO 10 — Lógica del reporte"""

from functools import reduce


def generar_reporte(productos):
    # 1. disponibles: lista de nombres con stock > 0 usando filter y map con lambda
    disponibles = list(
        map(
            lambda p: p["nombre"],
            filter(lambda p: p["stock"] > 0, productos)
        )
    )

    # 2. valor_total: suma de precio * stock usando map y reduce con lambda (inicio en 0)
    valor_total = reduce(
        lambda acc, x: acc + x,
        map(lambda p: p["precio"] * p["stock"], productos),
        0
    )

    # 3. hay_agotados: booleano usando any sobre map con lambda
    hay_agotados = any(map(lambda p: p["stock"] == 0, productos))

    # 4. categorias: set con todas las categorías usando comprensión de sets
    categorias = {p["categoria"] for p in productos}

    # 5. precios_con_recargo: tuplas con recargo del 10% (round 2) solo para disponibles
    calcular_recargo = lambda precio: round(precio * 1.1, 2)
    precios_con_recargo = [
        (p["nombre"], calcular_recargo(p["precio"]))
        for p in productos
        if p["stock"] > 0
    ]

    return {
        "disponibles": disponibles,
        "valor_total": valor_total,
        "hay_agotados": hay_agotados,
        "categorias": categorias,
        "precios_con_recargo": precios_con_recargo
    }