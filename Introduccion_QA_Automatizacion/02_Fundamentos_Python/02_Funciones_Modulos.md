# Funciones y Módulos en Python

## Objetivos

- Entender cómo definir y llamar funciones en Python.
- Aprender a importar y utilizar módulos.
- Introducir los conceptos básicos de Programación Orientada a Objetos (OOP) en Python.

## Contenido

### Funciones en Python

Las funciones son bloques de código reutilizables que realizan una tarea específica. Se definen utilizando la palabra clave `def`.

#### Definición de Funciones

```Python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")
```

#### Parámetros y Argumentos

```Python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # Output: 8
```

#### Funciones con Valores Predeterminados

```Python
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}!")

saludar()  # Output: Hola, amigo!
saludar("Ana")  # Output: Hola, Ana!
```

### Módulos en Python

Un módulo es un archivo que contiene definiciones y declaraciones de Python. Se puede importar un módulo completo o partes específicas de él.

#### Importar Módulos

```Python
import math

print(math.sqrt(16))  # Output: 4.0
```

#### Importar Funciones Específicas de un Módulo

```Python
from math import sqrt

print(sqrt(25))  # Output: 5.0
```

#### Crear y Usar Módulos Propios

Crea un archivo mimodulo.py:

```Python
def saludar(nombre):
    print(f"Hola, {nombre}!")
```

Importa y usa tu módulo:

```Python
import mimodulo

mimodulo.saludar("María")  # Output: Hola, María!
```

### Programación Orientada a Objetos (OOP) en Python

La Programación Orientada a Objetos (OOP) es un paradigma de programación que utiliza "objetos" y "clases". Una clase es como un plano para crear objetos. Un objeto es una instancia de una clase.

### Definición de una Clase

```Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
juan = Persona("Juan", 30)
juan.saludar()  # Output: Hola, mi nombre es Juan y tengo 30 años.
```

### Atributos y Métodos

Los atributos son variables que pertenecen a una clase. Los métodos son funciones que pertenecen a una clase.

```Python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"La velocidad del {self.marca} {self.modelo} es {self.velocidad} km/h.")

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"La velocidad del {self.marca} {self.modelo} es {self.velocidad} km/h.")

# Crear una instancia de la clase Coche
mi_coche = Coche("Toyota", "Corolla")
mi_coche.acelerar(50)  # Output: La velocidad del Toyota Corolla es 50 km/h.
mi_coche.frenar(20)    # Output: La velocidad del Toyota Corolla es 30 km/h.
```

### Herencia

La herencia permite crear una nueva clase que es una modificación de una clase existente.

```Python
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        print(f"Este es un {self.marca} {self.modelo}.")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def descripcion(self):
        super().descripcion()
        print(f"Es una moto de tipo {self.tipo}.")

# Crear una instancia de la clase Moto
mi_moto = Moto("Honda", "CBR", "Deportiva")
mi_moto.descripcion()
# Output:
# Este es un Honda CBR.
# Es una moto de tipo Deportiva.
```

### Encapsulamiento

El encapsulamiento se refiere a la restricción del acceso a algunos de los componentes de un objeto.

```Python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"El saldo de {self.titular} es {self.__saldo}.")

# Crear una instancia de la clase CuentaBancaria
cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.mostrar_saldo()  # Output: El saldo de Ana es 1300.
```
