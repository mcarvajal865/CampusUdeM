from interfaz.utilidades import *
from grafo.algoritmos import *
from grafo.datos_campus import crearCampus

campus = crearCampus()

def menuPrincipal():

    while True:

        print("\n1. Buscar ruta")
        print("2. Árbol mínimo")
        print("3. Modificar camino")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == '1':

            mostrarLugares(campus)

            origen = input("Origen: ")
            destino = input("Destino: ")

            costo, camino = encontrarCaminoMasCorto(
                campus,
                origen,
                destino,
                'distancia'
            )

            explicarRuta(
                'distancia',
                costo,
                camino
            )

        elif opcion == '4':
            break