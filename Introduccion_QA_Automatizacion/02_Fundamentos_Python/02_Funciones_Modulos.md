# Funciones y Módulos en Python

## Objetivos
- Entender cómo definir y llamar funciones en Python.
- Aprender a importar y utilizar módulos.

## Contenido

### Funciones en Python
Las funciones son bloques de código reutilizables que realizan una tarea específica. Se definen utilizando la palabra clave `def`.

#### Definición de Funciones
```Python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")
```
#### Parámetros y Argumentos
```Python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # Output: 8
```
#### Funciones con Valores Predeterminados
```Python
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}!")

saludar()  # Output: Hola, amigo!
saludar("Ana")  # Output: Hola, Ana!
```
### Módulos en Python
Un módulo es un archivo que contiene definiciones y declaraciones de Python. Se puede importar un módulo completo o partes específicas de él.

#### Importar Módulos
```Python
import math

print(math.sqrt(16))  # Output: 4.0
```
#### Importar Funciones Específicas de un Módulo
```Python
from math import sqrt

print(sqrt(25))  # Output: 5.0
```
#### Crear y Usar Módulos Propios
Crea un archivo mimodulo.py:
```Python
def saludar(nombre):
    print(f"Hola, {nombre}!")
```
#### Importa y usa tu módulo:
```Python
import mimodulo

mimodulo.saludar("María")  # Output: Hola, María!
```
