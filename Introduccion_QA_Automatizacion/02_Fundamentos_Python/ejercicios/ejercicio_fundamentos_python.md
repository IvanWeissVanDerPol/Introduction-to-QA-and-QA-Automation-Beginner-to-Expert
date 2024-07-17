# Tarea: Crear un Módulo de Calculadora

## Objetivo

Crear un módulo de Python para una calculadora utilizando Programación Orientada a Objetos (OOP) que incluya todas las operaciones matemáticas básicas. Luego, crear un archivo principal separado para importar y usar el módulo de la calculadora. Este módulo se utilizará más adelante para las tareas de pruebas en otra sección del curso.

## Parte 1: Módulo de Calculadora

### Paso 1: Crear el Módulo de Calculadora

1. Crear un archivo llamado `calculadora.py`.
2. Este archivo contendrá una clase `Calculadora` con métodos para cada operación matemática.
3. Implementar los siguientes métodos en la clase `Calculadora`:
   - Suma
   - Resta
   - Multiplicación
   - División
   - Módulo
   - Exponenciación
   - División Entera
4. Asegurarse de que cada método:
   - Tome dos entradas numéricas.
   - Devuelva el resultado de la operación.
   - Maneje adecuadamente casos especiales, como la división por cero.

### Paso 2: Crear el Archivo Principal

1. Crear un archivo llamado `main.py`.
2. Este archivo importará y usará la clase `Calculadora` de `calculadora.py`.
3. Implementar lo siguiente en `main.py`:
   - Importar la clase `Calculadora`.
   - Crear una instancia de la clase `Calculadora`.
   - Realizar algunos cálculos utilizando los métodos de la clase `Calculadora`.
   - Imprimir los resultados de los cálculos.

### Paso 3: Probar la Calculadora

1. Ejecutar `main.py`.
2. Asegurarse de que todas las operaciones estén correctamente implementadas y muestren los resultados esperados.

### Ejemplo de Salida

```terminal
Operaciones de Calculadora
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
10 % 5 = 0
10 ** 5 = 100000
10 // 5 = 2
```
