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

### Ejemplo de Script de Prueba Simple con `unittest` (Python)
```python
import unittest

# Función que vamos a probar
def suma(a, b):
    return a + b

class TestFuncionesMatematicas(unittest.TestCase):

    def setUp(self):
        # Configuración: Preparar cualquier dato necesario
        self.a = 10
        self.b = 5

    def test_suma(self):
        # Ejecución: Realizar la operación de suma
        resultado = suma(self.a, self.b)
        # Verificación: Comprobar que el resultado es el esperado
        self.assertEqual(resultado, 15)

    def tearDown(self):
        # Limpieza: Aquí podrías limpiar datos si fuera necesario
        pass

if __name__ == "__main__":
    unittest.main()
```

### Explicación del Ejemplo
* Función suma(a, b): Esta es una función simple que toma dos argumentos y devuelve su suma. Esta será la función que probaremos.
* Clase TestFuncionesMatematicas: Esta es nuestra clase de prueba que hereda de unittest.TestCase.
* Método setUp(self): Este método se ejecuta antes de cada prueba. Aquí, inicializamos los datos necesarios para las pruebas (en este caso, dos números a y b).
* Método test_suma(self): Este es el método de prueba real. Realizamos la operación de suma usando la función suma(a, b) y usamos self.assertEqual(resultado, 15) para verificar que el resultado es el esperado.
* Método tearDown(self): Este método se ejecuta después de cada prueba. Es útil para limpiar cualquier dato o estado modificado durante la prueba. En este caso, no necesitamos hacer nada en tearDown, así que simplemente usamos pass.

