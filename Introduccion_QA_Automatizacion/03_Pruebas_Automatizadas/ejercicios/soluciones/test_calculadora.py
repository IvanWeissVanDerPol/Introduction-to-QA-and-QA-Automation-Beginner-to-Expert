import pytest
from calculator import Calculadora

@pytest.fixture
def calculadora():
    return Calculadora()

def test_sumar(calculadora):
    assert calculadora.sumar(10, 5) == 15
    assert calculadora.sumar(-1, 1) == 0
    assert calculadora.sumar(-1, -1) == -2
    assert calculadora.sumar(0, 0) == 0

def test_restar(calculadora):
    assert calculadora.restar(10, 5) == 5
    assert calculadora.restar(-1, 1) == -2
    assert calculadora.restar(-1, -1) == 0
    assert calculadora.restar(0, 0) == 0

def test_multiplicar(calculadora):
    assert calculadora.multiplicar(10, 5) == 50
    assert calculadora.multiplicar(-1, 1) == -1
    assert calculadora.multiplicar(-1, -1) == 1
    assert calculadora.multiplicar(0, 100) == 0

def test_dividir(calculadora):
    assert calculadora.dividir(10, 5) == 2
    assert calculadora.dividir(-10, 2) == -5
    assert calculadora.dividir(1, -1) == -1
    assert calculadora.dividir(0, 1) == 0
    assert calculadora.dividir(10, 0) == "Error: División por cero no permitida"

def test_modulo(calculadora):
    assert calculadora.modulo(10, 3) == 1
    assert calculadora.modulo(-10, 3) == 2
    assert calculadora.modulo(10, -3) == -2
    assert calculadora.modulo(-10, 0) == "Error: Módulo por cero no permitido"
def test_exponenciar(calculadora):
    assert calculadora.exponenciar(2, 3) == 8
    assert calculadora.exponenciar(-2, 3) == -8
    assert calculadora.exponenciar(2, -2) == 0.25
    assert calculadora.exponenciar(2, 0) == 1
