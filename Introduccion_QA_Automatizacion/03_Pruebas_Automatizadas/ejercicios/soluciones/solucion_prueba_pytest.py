# solucion_prueba_pytest.py
import pytest

# Función que vamos a probar
def es_par(num):
    return num % 2 == 0

def test_es_par():
    assert es_par(4) == True
    assert es_par(5) == False
    assert es_par(0) == True

# Para ejecutar las pruebas, usa el comando:
# pytest solucion_prueba_pytest.py
