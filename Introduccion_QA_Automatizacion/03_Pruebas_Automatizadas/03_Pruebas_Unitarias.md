# Pruebas Unitarias

## Objetivos

- Entender el concepto y la importancia de las pruebas unitarias.
- Aprender a escribir y ejecutar pruebas unitarias en Python.

## Contenido

### ¿Qué son las Pruebas Unitarias?

Las pruebas unitarias son un tipo de prueba de software que verifica el funcionamiento de componentes individuales del código, como funciones o métodos. Su objetivo es asegurar que cada unidad de código funcione correctamente de manera aislada.

### Importancia de las Pruebas Unitarias

- **Detección Temprana de Errores:** Permiten identificar errores en etapas tempranas del desarrollo.
- **Facilitan el Refactorizado:** Aseguran que el código sigue funcionando correctamente después de realizar cambios.
- **Documentación:** Proveen una documentación adicional del comportamiento esperado del código.
- **Mejoran la Calidad del Código:** Fomentan el desarrollo de código modular y bien diseñado.

### Herramientas para Pruebas Unitarias en Python

- **unittest:** Módulo estándar de Python para escribir y ejecutar pruebas unitarias.
- **pytest:** Framework de pruebas más avanzado que soporta fixtures, plugins y es compatible con unittest.

### Escribiendo Pruebas Unitarias con unittest

```python
# test_calculadora_unittest.py
import unittest
from calculator import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        # Configuración: Crear una instancia de la calculadora
        self.calc = Calculadora()

    def test_sumar(self):
        # Ejecución: Realizar la operación de suma
        resultado = self.calc.sumar(10, 5)
        # Verificación: Comprobar que el resultado es el esperado
        self.assertEqual(resultado, 15)

    def tearDown(self):
        # Limpieza: Aquí podrías limpiar datos si fuera necesario
        pass

if __name__ == "__main__":
    unittest.main()

```

### Escribiendo Pruebas Unitarias con pytest

```python
# test_calculadora_pytest.py
import pytest
from calculator import Calculadora

@pytest.fixture
def calculadora():
    return Calculadora()

def test_sumar(calculadora):
    # Casos de prueba básicos
    assert calculadora.sumar(10, 5) == 15
    assert calculadora.sumar(-1, 1) == 0
    assert calculadora.sumar(-1, -1) == -2
    
    # Casos de prueba adicionales
    assert calculadora.sumar(0, 0) == 0
    assert calculadora.sumar(1000, 2000) == 3000
    assert calculadora.sumar(-1000, -2000) == -3000
    assert calculadora.sumar(1.5, 2.5) == 4.0
    assert calculadora.sumar(-1.5, 1.5) == 0.0

# Para ejecutar las pruebas, usa el comando:
# pytest test_calculadora_pytest.py

```

### Mejores Prácticas para Pruebas Unitarias

- Aislamiento: Las pruebas deben ser independientes y no depender de otras pruebas.
- Cobertura: Asegurar que se prueban todos los casos posibles, incluyendo bordes y errores.
- Nomenclatura: Utilizar nombres descriptivos para las pruebas y los métodos de prueba.
- Automatización: Integrar las pruebas en el proceso de integración continua para ejecutarlas automáticamente en cada cambio de código.
