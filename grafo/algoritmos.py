def encontrarCaminoMasCorto(grafo, lugarInicial,
                            lugarFinal,
                            criterio='distancia'):

    if criterio not in ['distancia', 'tiempo',
                        'congestion', 'accesible']:
        return (float('inf'), [])

    if lugarInicial not in grafo.vertices \
       or lugarFinal not in grafo.vertices:
        return (float('inf'), [])

    distancias = {
        v: float('inf')
        for v in grafo.vertices
    }

    distancias[lugarInicial] = 0

    predecesores = {
        v: None
        for v in grafo.vertices
    }

    visitados = []
    verticeActual = lugarInicial

    while verticeActual is not None \
          and verticeActual != lugarFinal:

        posActual = grafo.vertices.index(verticeActual)

        for i in range(grafo.tamano):

            conexion = grafo.matrizAdy[posActual][i]

            if conexion == 0:
                continue

            if conexion['estado'] in (
                'bloqueado',
                'mantenimiento'
            ):
                continue

            vecino = grafo.vertices[i]

            if vecino in visitados:
                continue

            if criterio == 'accesible':

                if not conexion['accesible']:
                    continue

                peso = conexion['distancia']

            else:
                peso = conexion[criterio]

            nuevaDistancia = (
                distancias[verticeActual]
                + peso
            )

            if nuevaDistancia < distancias[vecino]:
                distancias[vecino] = nuevaDistancia
                predecesores[vecino] = verticeActual

        visitados.append(verticeActual)

        menorCosto = float('inf')
        siguienteVertice = None

        for v in distancias:

            if distancias[v] < menorCosto \
               and v not in visitados:

                menorCosto = distancias[v]
                siguienteVertice = v

        verticeActual = siguienteVertice

    if distancias[lugarFinal] == float('inf'):
        return (float('inf'), [])

    camino = []
    paso = lugarFinal

    while paso is not None:
        camino.insert(0, paso)
        paso = predecesores[paso]

    return (distancias[lugarFinal], camino)