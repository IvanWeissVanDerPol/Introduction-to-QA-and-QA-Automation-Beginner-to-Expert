# Desarrollo de Pruebas Unitarias con pytest para Calculadora

## Objetivo

Desarrollar pruebas unitarias utilizando pytest para verificar todas las funciones de la calculadora creada previamente. Las pruebas deben asegurar que cada operación matemática se realiza correctamente y manejar casos de borde como la división por cero.

## Instrucciones

### Preparar el entorno de pruebas

Asegúrate de tener pytest instalado en tu entorno. Puedes instalarlo usando el siguiente comando:

```bash
pip install pytest
```
### Crear el archivo de pruebas

Crea un archivo llamado `test_calculadora.py` en el mismo directorio donde se encuentra tu módulo `calculator.py`.

### Implementar las pruebas

Escribe pruebas unitarias para cada función de tu clase `Calculadora` en `calculator.py`. Asegúrate de probar los siguientes métodos:

- sumar
- restar
- multiplicar
- dividir
- modulo
- exponenciar
- dividir_piso

### Estructura del archivo de pruebas

1. Define una fixture para inicializar una instancia de la calculadora.
2. Escribe una función de prueba para cada operación matemática.
3. Asegúrate de incluir casos de prueba que cubran:
   - Operaciones básicas con números positivos y negativos.
   - Casos de borde, como la división por cero.
