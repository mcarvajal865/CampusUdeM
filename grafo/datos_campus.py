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
        'Entrada Principal',
        'Parqueadero',
        120, 2, 5,
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

    campus.agregarConexion(
        'Bloque 1',
        'Biblioteca',
        100, 2, 2,
        True,
        'bloqueado'
    )

    campus.agregarConexion(
        'Bloque 2',
        'Bloque 3',
        70, 1, 2,
        True,
        'disponible'
    )

    campus.agregarConexion(
        'Bloque 2',
        'Cafeteria',
        90, 2, 5,
        True,
        'disponible'
    )

    campus.agregarConexion(
        'Bloque 3',
        'Laboratorio',
        50, 1, 1,
        False,
        'disponible'
    )

    campus.agregarConexion(
        'Bloque 3',
        'Bloque 4',
        80, 2, 3,
        True,
        'disponible'
    )



    return campus