from interfaz.utilidades import mostrarLugares, explicarRuta
from grafo.datos_campus import crearCampus

campus = crearCampus()

def menuPrincipal():

    while True:

        print("\n1. Buscar ruta")
        print("2. Árbol mínimo")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == '1':

            mostrarLugares(campus)

            origen = input("Origen: ")
            destino = input("Destino: ")

            for lugar in campus.vertices:
                if lugar.lower() == origen.lower():
                    origen = lugar
                if lugar.lower() == destino.lower():
                    destino = lugar

            print("\nCriterio:")
            print("  1. Distancia")
            print("  2. Tiempo")
            print("  3. Congestion")
            print("  4. Accesible")
            opc = input("Elige (1-4): ")
            criterios = {'1': 'distancia', '2': 'tiempo',
                         '3': 'congestion', '4': 'accesible'}

            if opc not in criterios:
                print("Criterio no valido.")
                continue

            criterio = criterios[opc]
            costo, camino = campus.encontrarCaminoMasCorto(origen, destino, criterio)

            if costo == float('inf'):
                print(f"\nNo se encontro ruta entre '{origen}' y '{destino}'.")
            else:
                explicarRuta(criterio, costo, camino)

        elif opcion == '2':
            pesoTotal, conexiones = campus.arbolExpansionMinimo()
            print(f"\nRecorrido de visitantes - distancia total: {pesoTotal} metros")
            for origen, destino, dist in conexiones:
                print(f"  {origen}  →  {destino}  ({dist} m)")

        elif opcion == '3':
            print("\nHasta luego!")
            break
        else:
            print("Opcion no valida.")
