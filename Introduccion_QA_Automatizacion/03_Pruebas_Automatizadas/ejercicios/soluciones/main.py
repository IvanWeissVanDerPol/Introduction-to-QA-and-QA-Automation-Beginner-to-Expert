from calculator import Calculadora

def main():
    calc = Calculadora()

    # Realizar algunas operaciones y mostrar los resultados
    a, b = 10, 5

    print(f"Calculadora Operaciones")
    print(f"{a} + {b} = {calc.sumar(a, b)}")
    print(f"{a} - {b} = {calc.restar(a, b)}")
    print(f"{a} * {b} = {calc.multiplicar(a, b)}")
    print(f"{a} / {b} = {calc.dividir(a, b)}")
    print(f"{a} % {b} = {calc.modulo(a, b)}")
    print(f"{a} ** {b} = {calc.exponenciar(a, b)}")
    print(f"{a} // {b} = {calc.division_entera(a, b)}")

    # Probar casos adicionales
    c, d = 7, 3
    print(f"{c} + {d} = {calc.sumar(c, d)}")
    print(f"{c} - {d} = {calc.restar(c, d)}")
    print(f"{c} * {d} = {calc.multiplicar(c, d)}")
    print(f"{c} / {d} = {calc.dividir(c, d)}")
    print(f"{c} % {d} = {calc.modulo(c, d)}")
    print(f"{c} ** {d} = {calc.exponenciar(c, d)}")
    print(f"{c} // {d} = {calc.division_entera(c, d)}")

    # Probar división por cero
    e, f = 10, 0
    print(f"{e} / {f} = {calc.dividir(e, f)}")
    print(f"{e} % {f} = {calc.modulo(e, f)}")
    print(f"{e} // {f} = {calc.division_entera(e, f)}")

if __name__ == "__main__":
    main()
