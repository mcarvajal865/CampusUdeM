from typing import Any, List
from collections import deque

class GrafoCampus:

  def __init__(self):
    self.matrizAdy : List[List[int]] = []
    self.vertices : List[Any] = [] ## Lista con los nodos
    self.tamano : int = 0

  def agregarVertice(self, valor: any): ## Agrega el nodo pero desconectado
    if valor in self.vertices: ## Si el valor ya estaba agregado no hace nada mas
      return None
    self.vertices.append(valor) ## Agrega el vertice a lista de vertices
    self.tamano = self.tamano + 1 ## Incrementa el tamaño del grafo

    for fila in self.matrizAdy:
      fila.append(0) ## Agrega una fila de ceros
    self.matrizAdy.append([0] * self.tamano) ## Agrega una columna de ceros

  def agregarConexion(self, vertice1, vertice2, dirigido = False, peso = 1):
    if vertice1 not in self.vertices:
      self.agregarVertice(vertice1)
    if vertice2 not in self.vertices:
      self.agregarVertice(vertice2)

    posV1 = self.vertices.index(vertice1) ## Entrega la posicion de el vertice 1 en la matriz de ady
    posV2 = self.vertices.index(vertice2) ## Entrega la posicion del vertice 2 en la matriz de adyacencia

    self.matrizAdy[posV1][posV2] = peso ## Hay un camino entre v1 y v2

    if not dirigido: ## Si no es dirigido debo agregar la relacion contraria
      self.matrizAdy[posV2][posV1] = peso

