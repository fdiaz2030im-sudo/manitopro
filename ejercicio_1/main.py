"""
Mapa de puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]
0: disponible. 1: ocupado. Las coordenadas son tuplas (fila, columna), desde cero.

IMPLEMENTA
1. crear_mapa(puestos): devuelve un diccionario {(fila, columna): estado}.
   Utiliza una comprension de diccionarios.
2. obtener_disponibles(puestos): devuelve un set de coordenadas disponibles.
   Utiliza una comprension de conjuntos.
No modifiques el tablero.

COMPROBACIONES CON PRINT
- Muestra el mapa completo y los disponibles.
- Consulta el estado de (1, 2) en el mapa: debe ser 1.
- Disponibles esperados: {(0, 1), (1, 0), (1, 1)}. El orden no importa.
- Agrega y comprueba otro tablero propio.

ANALISIS EN COMENTARIOS
- Cuantas celdas se revisan al obtener los disponibles en el ejemplo?
- Cuantas se revisan para f filas y c columnas? Y para n filas y n columnas?

COMMIT SUGERIDO
Completa ejercicio 1: mapa y puestos disponibles
"""

"""
Mapa de puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]
0: disponible. 1: ocupado. Las coordenadas son tuplas (fila, columna), desde cero.
"""

def crear_mapa(puestos):
    return {
        (r, c): puestos[r][c]
        for r in range(len(puestos))
        for c in range(len(puestos[0]))
    }


def obtener_disponibles(puestos):
    return {
        (r, c)
        for r in range(len(puestos))
        for c in range(len(puestos[0]))
        if puestos[r][c] == 0
    }


if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    # 1. Mapa completo y disponibles
    mapa = crear_mapa(puestos)
    disponibles = obtener_disponibles(puestos)

    print("Mapa completo:", mapa)
    print("Puestos disponibles:", disponibles)

    # 2. Consulta de la coordenada (1, 2)
    print("Estado en (1, 2):", mapa[(1, 2)])

    # 3. Comprobación del resultado esperado
    esperados = {(0, 1), (1, 0), (1, 1)}
    print("¿Disponibles coincide con el esperado?:", disponibles == esperados)

    # 4. Caso propio adicional
    print("\n--- CASO PROPIO ---")
    puestos_propio = [
        [0, 1],
        [1, 1],
        [0, 0]
    ]
    mapa_propio = crear_mapa(puestos_propio)
    disponibles_propio = obtener_disponibles(puestos_propio)

    print("Mapa propio:", mapa_propio)
    print("Disponibles propio:", disponibles_propio)
    print("Estado en (2, 0) propio:", mapa_propio[(2, 0)])


# ANALISIS
# 1. En el ejemplo inicial (matriz de 2x3), se revisan 6 celdas en total (2 * 3).
# 2. Para un tablero de 'f' filas y 'c' columnas, se revisan f * c celdas.
# 3. Para un tablero cuadrado de 'n' filas y 'n' columnas, se revisan n^2 celdas (complejidad temporal O(n^2)).
