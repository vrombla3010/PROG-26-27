def sumar(num1: float, num2: float) -> float:

    """
    Suma dos números.

    :param num1: Primer número.
    :param num2: Segundo número.
    :return: Resultado de la suma.
    """

    return num1 + num2


def restar(num1: float, num2: float) -> float:

    """
    Resta dos números.

    :param num1: Primer número.
    :param num2: Segundo número.
    :return: Resultado de la resta.
    """

    return num1 - num2


def multiplicar(num1: float, num2: float) -> float:

    """
    Multiplica dos números.

    :param num1: Primer número.
    :param num2: Segundo número.
    :return: Resultado de la multiplicación.
    """

    return num1 * num2


def dividir(num1: float, num2: float) -> float:

    """
    Divide el primer número entre el segundo.

    :param num1: Dividendo.
    :param num2: Divisor, distinto de cero.
    :return: Resultado de la división.
    """

    return num1 / num2


def main() -> None:

    """Solicita dos números y muestra los resultados de las operaciones."""

    num1: float = float(input("Introduce el primer numero: "))
    num2: float = float(input("Introduce el segundo numero: "))

    print(f"Suma: {sumar(num1, num2)}")
    print(f"Resta: {restar(num1, num2)}")
    print(f"Multiplicación: {multiplicar(num1, num2)}")

    if num2 != 0:
        print(f"División: {dividir(num1, num2)}")
    else:
        print("División: No se puede dividir entre cero.")


if __name__ == "__main__":
    main()

