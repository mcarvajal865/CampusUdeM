def mostrarLugares(campus):

    print("\nLugares disponibles:\n")

    for i, lugar in enumerate(campus.vertices):
        print(f"{i+1}. {lugar}")


def explicarRuta(criterio, costo, camino):

    unidades = {
        'distancia': ('metros', 'distancia'),
        'tiempo': ('minutos', 'tiempo'),
        'congestion': ('puntos', 'congestion'),
        'accesible': ('metros', 'ruta accesible')
    }

    unidad, descripcion = unidades[criterio]

    print(f"\nRuta: {' → '.join(camino)}")
    print(f"Costo total: {costo} {unidad}")