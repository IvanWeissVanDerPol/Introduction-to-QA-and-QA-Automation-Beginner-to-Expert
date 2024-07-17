# Escribiendo Scripts de Prueba

## Objetivos

- Aprender a escribir scripts de prueba automatizados.
- Conocer las mejores prácticas para la creación de scripts de prueba.

## Contenido

### ¿Qué es un Script de Prueba?

Un script de prueba es un conjunto de instrucciones que se ejecutan de manera automatizada para validar el comportamiento de una aplicación. Estos scripts están diseñados para simular acciones del usuario y verificar que el sistema responda como se espera.

### Estructura de un Script de Prueba

1. **Configuración:** Preparar el entorno de prueba y los datos necesarios.
2. **Ejecución:** Realizar las acciones necesarias para la prueba.
3. **Verificación:** Comprobar que los resultados son los esperados.
4. **Limpieza:** Dejar el sistema en un estado limpio después de la prueba.

### Ejemplo de Script de Prueba Simple con `pytest` (Python)

```python
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

```
