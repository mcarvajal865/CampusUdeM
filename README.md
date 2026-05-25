# 🏫 Campus UdeM - Sistema de Rutas Inteligentes

Sistema desarrollado en Python para la simulación y optimización de rutas dentro de un campus universitario utilizando teoría de grafos, algoritmos clásicos y programación orientada a objetos.

---

# 📌 Descripción

Este proyecto representa el campus universitario como un **grafo no dirigido ponderado** utilizando una **matriz de adyacencia**.

Cada lugar del campus es un vértice y cada camino es una arista con múltiples atributos:

- 📏 Distancia
- ⏱ Tiempo
- 🚦 Congestión
- ♿ Accesibilidad
- 🚧 Estado del camino

El sistema permite:

✅ Encontrar rutas óptimas  
✅ Simular bloqueos y mantenimiento  
✅ Calcular recorridos mínimos para visitantes  
✅ Gestionar caminos dinámicamente  

---

# 🧠 Algoritmos implementados

## 🔹 Dijkstra
Utilizado para encontrar:

- Ruta más corta
- Ruta más rápida
- Ruta con menor congestión
- Ruta accesible

---

## 🔹 Prim
Utilizado para construir:

- Árbol de expansión mínima
- Recorrido óptimo para visitantes

---

# 🏗 Estructura del Proyecto

```bash
CampusUdeM/
│
├── main.py
│
├── grafo/
│   ├── __init__.py
│   ├── grafo_campus.py
│   ├── algoritmos.py
│   └── datos_campus.py
│
├── interfaz/
│   ├── __init__.py
│   ├── menu.py
│   └── utilidades.py
│
├── .gitignore
└── README.md
```

---

# 📚 Tecnologías utilizadas

- 🐍 Python 3
- 💻 PyCharm
- 🌳 Teoría de Grafos
- 🧩 Programación Orientada a Objetos
- 📊 Matriz de Adyacencia

---

# 🔍 Tipo de Grafo

El proyecto implementa un:

## ✅ Grafo No Dirigido Ponderado

Características:

- Bidireccional
- Ponderado
- Multicriterio
- Dinámico
- Representado mediante matriz de adyacencia

---

# 🚀 Funcionalidades

## 📍 Búsqueda de rutas

El usuario puede buscar rutas según:

- Menor distancia
- Menor tiempo
- Menor congestión
- Accesibilidad

---

## 🚧 Gestión de caminos

Es posible modificar:

- Estado del camino
- Distancia
- Tiempo
- Congestión
- Accesibilidad

---

## 🗺 Recorrido de visitantes

Genera un recorrido mínimo que conecta todo el campus utilizando Prim.

---

# 🖥 Ejemplo de uso

```python
campus.agregarConexion(
    'Biblioteca',
    'Bloque 1',
    100,
    2,
    3,
    True,
    'disponible'
)
```

---

# ▶️ Ejecución

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/usuario/CampusUdeM.git
```

---

## 2️⃣ Entrar al proyecto

```bash
cd CampusUdeM
```

---

## 3️⃣ Ejecutar

```bash
python main.py
```

---

# 📸 Menú Principal

```text
=========================================
   SISTEMA DE RUTAS - CAMPUS UDEM
=========================================

1. Encontrar una ruta
2. Árbol de expansión mínima
3. Modificar caminos
4. Salir
```

---

# 🎯 Conceptos aplicados

- Estructuras de datos
- Grafos
- Algoritmos de caminos mínimos
- Árboles de expansión mínima
- Modularización
- POO
- Abstracción
- Código limpio
- Diseño de software

---

# 👨‍💻 Autores

## Manuela Martinez Gil
## Mateo Carvajal Zapata

Estudiantes de Ingeniería en Sistemas  
Universidad de Medellín

---

# 📄 Licencia

Proyecto académico desarrollado con fines educativos para Estructura de Datos.
