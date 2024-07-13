# Manipulación de Datos en Python

## Objetivos
- Conocer las estructuras de datos básicas en Python.
- Aprender a manipular listas, tuplas, diccionarios y conjuntos.

## Contenido

### Listas
Las listas son colecciones ordenadas y mutables que permiten almacenar múltiples elementos.

#### Crear y Acceder a Listas
```python
    frutas = ["manzana", "banana", "cereza"]
    print(frutas[0])  # Output: manzana
```
#### Operaciones con Listas
```python
    frutas.append("naranja")
    print(frutas)  # Output: ["manzana", "banana", "cereza", "naranja"]

    frutas.remove("banana")
    print(frutas)  # Output: ["manzana", "cereza", "naranja"]

    print(len(frutas))  # Output: 3
```
### Tuplas
Las tuplas son colecciones ordenadas e inmutables.

#### Crear y Acceder a Tuplas
```python
    numeros = (1, 2, 3, 4)
    print(numeros[1])  # Output: 2
```
### Diccionarios
Los diccionarios son colecciones no ordenadas de pares clave-valor.

#### Crear y Acceder a Diccionarios
```python
    estudiante = {"nombre": "Juan", "edad": 25, "carrera": "Ingeniería"}
    print(estudiante["nombre"])  # Output: Juan
```
#### Operaciones con Diccionarios
```python
    estudiante["edad"] = 26
    print(estudiante)  # Output: {"nombre": "Juan", "edad": 26, "carrera": "Ingeniería"}

    estudiante["universidad"] = "MIT"
    print(estudiante)  # Output: {"nombre": "Juan", "edad": 26, "carrera": "Ingeniería", "universidad": "MIT"}

    del estudiante["carrera"]
    print(estudiante)  # Output: {"nombre": "Juan", "edad": 26, "universidad": "MIT"}
```
### Conjuntos
Los conjuntos son colecciones desordenadas de elementos únicos.

#### Crear y Operar con Conjuntos
```python
    frutas = {"manzana", "banana", "cereza"}
    frutas.add("naranja")
    print(frutas)  # Output: {"manzana", "banana", "cereza", "naranja"}

    frutas.remove("banana")
    print(frutas)  # Output: {"manzana", "cereza", "naranja"}
```