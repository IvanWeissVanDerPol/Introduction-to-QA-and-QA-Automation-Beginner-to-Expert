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
# funciones_matematicas.py
import unittest

def suma(a, b):
    return a + b

class TestFuncionesMatematicas(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(3, 4), 7)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(-1, -1), -2)

if __name__ == "__main__":
    unittest.main()
```
### Escribiendo Pruebas Unitarias con pytest
```python
test_funciones_matematicas.py
import pytest
from funciones_matematicas import suma

def test_suma():
    assert suma(3, 4) == 7
    assert suma(-1, 1) == 0
    assert suma(-1, -1) == -2
# Para ejecutar las pruebas, usa el comando:
# pytest test_funciones_matematicas.py
```
### Mejores Prácticas para Pruebas Unitarias
* Aislamiento: Las pruebas deben ser independientes y no depender de otras pruebas.
* Cobertura: Asegurar que se prueban todos los casos posibles, incluyendo bordes y errores.
* Nomenclatura: Utilizar nombres descriptivos para las pruebas y los métodos de prueba.
* Automatización: Integrar las pruebas en el proceso de integración continua para ejecutarlas automáticamente en cada cambio de código.

