from collections import deque

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