class Calculadora:
    def __init__(self):
        pass

    def sumar(self, a, b):
        """
        Suma dos números.
        :param a: Primer número
        :param b: Segundo número
        :return: Resultado de la suma
        """
        return a + b

    def restar(self, a, b):
        """
        Resta el segundo número del primero.
        :param a: Primer número
        :param b: Segundo número
        :return: Resultado de la resta
        """
        return a - b

    def multiplicar(self, a, b):
        """
        Multiplica dos números.
        :param a: Primer número
        :param b: Segundo número
        :return: Resultado de la multiplicación
        """
        return a * b

    def dividir(self, a, b):
        """
        Divide el primer número por el segundo.
        :param a: Primer número
        :param b: Segundo número
        :return: Resultado de la división o un mensaje de error si el divisor es cero
        """
        if b == 0:
            return "Error: División por cero no permitida"
        return a / b

    def modulo(self, a, b):
        """
        Calcula el módulo (resto de la división) del primer número por el segundo.
        :param a: Primer número
        :param b: Segundo número
        :return: Resto de la división
        """
        if b == 0:
            return "Error: Módulo por cero no permitido"
        return a % b

    def exponenciar(self, a, b):
        """
        Calcula la potencia del primer número elevado al segundo.
        :param a: Base
        :param b: Exponente
        :return: Resultado de la exponenciación
        """
        return a ** b

    def division_entera(self, a, b):
        """
        Realiza una división entera del primer número por el segundo.
        :param a: Primer número
        :param b: Segundo número
        :return: Resultado de la división entera o un mensaje de error si el divisor es cero
        """
        if b == 0:
            return "Error: División por cero no permitida"
        return a // b

