# solucion_lambda.py
# Definición de una función lambda que suma dos números.
# Las funciones lambda son funciones anónimas que se definen en una sola línea.
suma = lambda a, b: a + b

# Ejemplo de uso de la función lambda.
# Suma de 5 y 3.
print(suma(5, 3))  # Output: 8

# Definición de una función lambda que multiplica dos números.
multiplica = lambda x, y: x * y

# Ejemplo de uso de la función lambda.
# Multiplicación de 4 y 5.
print(multiplica(4, 5))  # Output: 20

# Definición de una función lambda que devuelve el mayor de dos números.
mayor = lambda a, b: a if a > b else b

# Ejemplo de uso de la función lambda.
# Encuentra el mayor entre 10 y 20.
print(mayor(10, 20))  # Output: 20

# Definición de una función lambda que eleva un número al cuadrado.
cuadrado = lambda x: x ** 2

# Ejemplo de uso de la función lambda.
# Eleva 7 al cuadrado.
print(cuadrado(7))  # Output: 49

# Uso de una función lambda dentro de una función de orden superior (map).
# Eleva al cuadrado cada número en la lista.
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))

# Imprime la lista de cuadrados.
print(cuadrados)  # Output: [1, 4, 9, 16, 25]

# Uso de una función lambda dentro de una función de orden superior (filter).
# Filtra los números impares en la lista.
impares = list(filter(lambda x: x % 2 != 0, numeros))

# Imprime la lista de números impares.
print(impares)  # Output: [1, 3, 5]

# Uso de una función lambda dentro de una función de orden superior (sorted).
# Ordena una lista de tuplas por el segundo valor.
tuplas = [(1, 3), (2, 1), (3, 2)]
ordenadas = sorted(tuplas, key=lambda x: x[1])

# Imprime la lista de tuplas ordenadas.
print(ordenadas)  # Output: [(2, 1), (3, 2), (1, 3)]

# Explicación de funciones lambda.
"""
Las funciones lambda en Python son funciones anónimas y pequeñas que se definen usando la palabra clave `lambda`. 
Son útiles cuando se necesita una función simple para una operación temporal, especialmente como argumento de otra función.

Sintaxis:
lambda argumentos: expresión

- `lambda` es la palabra clave utilizada para definir una función lambda.
- `argumentos` es una lista separada por comas de argumentos (como en una función normal).
- `expresión` es una sola expresión que se evalúa y devuelve.

Características:
- No tienen nombre (anónimas).
- Se definen en una sola línea.
- Pueden tener múltiples argumentos pero solo una expresión.
- Son útiles en funciones de orden superior como `map`, `filter` y `sorted`.

Ejemplos adicionales:
1. `lambda a, b: a + b` define una función que suma dos números.
2. `lambda x, y: x * y` define una función que multiplica dos números.
3. `lambda a, b: a if a > b else b` define una función que devuelve el mayor de dos números.
4. `lambda x: x ** 2` define una función que eleva un número al cuadrado.
"""
