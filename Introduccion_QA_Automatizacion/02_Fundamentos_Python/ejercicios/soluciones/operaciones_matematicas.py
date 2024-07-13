# operaciones_matematicas.py
# Definición de una función que suma dos números.
def suma(a, b):
    return a + b

# Definición de una función que resta dos números.
def resta(a, b):
    return a - b

# Definición de una función que multiplica dos números.
def multiplicacion(a, b):
    return a * b

# Definición de una función que divide dos números.
# Verifica si el divisor es cero para evitar división por cero.
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "División por cero no permitida"
