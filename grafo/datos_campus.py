from grafo.grafo_campus import GrafoCampus

def crearCampus():

    campus = GrafoCampus()

    campus.agregarConexion(
        'Entrada Principal',
        'Bloque 1',
        80, 1, 4,
        True,
        'disponible'
    )

    campus.agregarConexion(
        'Bloque 1',
        'Bloque 2',
        60, 1, 3,
        True,
        'disponible'
    )

    # TODAS las demás conexiones...

    return campus