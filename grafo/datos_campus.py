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
        'disponible'
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

    campus.agregarConexion(
        'Biblioteca',
        'Cafeteria',
        40, 1, 2,
        True,
        'mantenimiento'
    )

    campus.agregarConexion(
        'Biblioteca',
        'Bloque 4',
        110, 2, 1,
        True,
        'disponible'
    )

    campus.agregarConexion(
        'Cafeteria',
        'Teatro',
        150, 3, 4,
        True,
        'disponible'
    )

    campus.agregarConexion(
        'Laboratorio',
        'Bloque 4',
        60, 1, 1,
        False,
        'disponible'
    )

    campus.agregarConexion(
        'Bloque 4',
        'Enfermeria',
        90, 2, 2,
        True,
        'disponible'
    )

    campus.agregarConexion(
        'Bloque 4',
        'Zona Deportiva',
        130, 3, 3,
        True,
        'disponible'
    )

    campus.agregarConexion(
        'Teatro',
        'Enfermeria',
        100, 2, 1,
        True,
        'disponible'
    )

    campus.agregarConexion(
        'Enfermeria',
        'Zona Deportiva',
        70, 2, 2,
        True,
        'disponible'
    )

    campus.agregarConexion(
        'Zona Deportiva',
        'Administrativo',
        120, 3, 2,
        True,
        'disponible'
    )

    campus.agregarConexion(
        'Administrativo',
        'Entrada Principal',
        200, 4, 3,
        True,
        'disponible'
    )

    campus.agregarConexion(
        'Parqueadero',
        'Bloque 1',
        100, 2, 3,
        True,
        'bloqueado'
    )

    campus.agregarConexion(
        'Cafeteria',
        'Administrativo',
        180, 4, 4,
        True,
        'disponible'
    )



    return campus