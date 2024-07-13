# solucion_factorial.py
def factorial(n):
    """
    Calcula el factorial de un número dado.
    El factorial de n es el producto de todos los enteros positivos menores o iguales a n.
    Por ejemplo, el factorial de 5 (5!) es 5 * 4 * 3 * 2 * 1 = 120.
    """
    if n == 0:
        # El factorial de 0 es 1 por definición.
        return 1
    else:
        # Llamada recursiva para calcular el factorial.
        return n * factorial(n-1)

# Ejemplo de uso
# Calcula el factorial de 5.
print(factorial(5))  # Output: 120
