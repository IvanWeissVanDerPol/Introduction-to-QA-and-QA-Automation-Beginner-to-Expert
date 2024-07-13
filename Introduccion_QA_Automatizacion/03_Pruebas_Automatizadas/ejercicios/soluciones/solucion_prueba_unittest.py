# solucion_prueba_unittest.py
import unittest

# Función que vamos a probar
def producto(a, b):
    return a * b

class TestFuncionesMatematicas(unittest.TestCase):

    def setUp(self):
        # Configuración: Preparar cualquier dato necesario
        self.a = 4
        self.b = 5

    def test_producto(self):
        # Ejecución: Realizar la operación de producto
        resultado = producto(self.a, self.b)
        # Verificación: Comprobar que el resultado es el esperado
        self.assertEqual(resultado, 20)

    def tearDown(self):
        # Limpieza: Aquí podrías limpiar datos si fuera necesario
        pass

if __name__ == "__main__":
    unittest.main()
