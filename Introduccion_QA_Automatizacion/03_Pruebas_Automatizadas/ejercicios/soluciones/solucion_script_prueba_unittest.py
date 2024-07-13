# solucion_script_prueba_unittest.py
import unittest

# Función que vamos a probar
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

class TestConversiones(unittest.TestCase):

    def setUp(self):
        # Configuración: Preparar cualquier dato necesario
        self.celsius = 0

    def test_celsius_a_fahrenheit(self):
        # Ejecución: Realizar la conversión
        resultado = celsius_a_fahrenheit(self.celsius)
        # Verificación: Comprobar que el resultado es el esperado
        self.assertEqual(resultado, 32)

    def tearDown(self):
        # Limpieza: Aquí podrías limpiar datos si fuera necesario
        pass

if __name__ == "__main__":
    unittest.main()
