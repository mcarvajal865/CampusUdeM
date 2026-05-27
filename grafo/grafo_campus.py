
class GrafoCampus:

    def __init__(self):
        self.matrizAdy = []
        self.vertices = []
        self.tamano = 0

    def agregarVertice(self, valor):
        if valor in self.vertices:
            return

        self.vertices.append(valor)
        self.tamano += 1

        for fila in self.matrizAdy:
            fila.append(0)

        self.matrizAdy.append([0] * self.tamano)

    def agregarConexion(self, lugar1, lugar2,
                        distancia, tiempo,
                        congestion, accesible,
                        estado='disponible'):

        if lugar1 not in self.vertices:
            self.agregarVertice(lugar1)

        if lugar2 not in self.vertices:
            self.agregarVertice(lugar2)

        pos1 = self.vertices.index(lugar1)
        pos2 = self.vertices.index(lugar2)

        camino = {
            'distancia': distancia,
            'tiempo': tiempo,
            'congestion': congestion,
            'accesible': accesible,
            'estado': estado
        }

        self.matrizAdy[pos1][pos2] = camino
        self.matrizAdy[pos2][pos1] = camino

    def encontrarCaminoMasCorto(self, lugarInicial, lugarFinal, criterio='distancia'):

        if criterio not in ['distancia', 'tiempo', 'congestion', 'accesible']:
            return (float('inf'), [])

        if lugarInicial not in self.vertices or lugarFinal not in self.vertices:
            return (float('inf'), [])

        if lugarInicial == lugarFinal:
            return (0, [lugarInicial])

        distancias = {v: float('inf') for v in self.vertices}
        distancias[lugarInicial] = 0

        predecesores = {v: None for v in self.vertices}

        visitados = []
        verticeActual = lugarInicial

        while verticeActual is not None and verticeActual != lugarFinal:
            posActual = self.vertices.index(verticeActual)

            for i in range(self.tamano):
                conexion = self.matrizAdy[posActual][i]

                if conexion == 0:
                    continue

                if conexion['estado'] in ('bloqueado', 'mantenimiento'):
                    continue

                vecino = self.vertices[i]

                if vecino in visitados:
                    continue

                if criterio == 'accesible':
                    if not conexion['accesible']:
                        continue
                    peso = conexion['distancia']
                else:
                    peso = conexion[criterio]

                nuevaDistancia = distancias[verticeActual] + peso

                if nuevaDistancia < distancias[vecino]:
                    distancias[vecino] = nuevaDistancia
                    predecesores[vecino] = verticeActual

            visitados.append(verticeActual)

            menorCosto = float('inf')
            siguienteVertice = None
            for v in distancias:
                if distancias[v] < menorCosto and v not in visitados:
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

    def arbolExpansionMinimo(self):
        if self.tamano == 0:
            return (0, [])

        visitados = [self.vertices[0]]
        conexiones = []
        pesoTotal = 0

        while len(visitados) < self.tamano:
            mejorPeso = float('inf')
            mejorOrigen = None
            mejorDestino = None

            for lugar in visitados:
                fila = self.vertices.index(lugar)
                for i in range(self.tamano):
                    conexion = self.matrizAdy[fila][i]
                    if conexion == 0:
                        continue
                    if conexion['estado'] in ('bloqueado', 'mantenimiento'):
                        continue
                    vecino = self.vertices[i]
                    if vecino in visitados:
                        continue
                    if conexion['distancia'] < mejorPeso:
                        mejorPeso = conexion['distancia']
                        mejorOrigen = lugar
                        mejorDestino = vecino

            if mejorDestino is None:
                print("Advertencia: el campus no esta completamente conectado.")
                break

            visitados.append(mejorDestino)
            conexiones.append((mejorOrigen, mejorDestino, mejorPeso))
            pesoTotal += mejorPeso

        return (pesoTotal, conexiones)

