"""Calculadora básica de cuatro operaciones."""


def sumar(numero1: float, numero2: float) -> float:
    """Suma dos números.

    :param numero1: Primer sumando.
    :param numero2: Segundo sumando.
    :return: Resultado de la suma.
    """
    return numero1 + numero2


def restar(numero1: float, numero2: float) -> float:
    """Resta el segundo número al primero.

    :param numero1: Minuendo.
    :param numero2: Sustraendo.
    :return: Resultado de la resta.
    """
    return numero1 - numero2


def multiplicar(numero1: float, numero2: float) -> float:
    """Multiplica dos números.

    :param numero1: Primer factor.
    :param numero2: Segundo factor.
    :return: Resultado de la multiplicación.
    """
    return numero1 * numero2


def dividir(numero1: float, numero2: float) -> float:
    """Divide el primer número entre el segundo.

    :param numero1: Dividendo.
    :param numero2: Divisor, distinto de cero.
    :return: Cociente de la división.
    :raises ValueError: Si el divisor es cero.
    """
    if numero2 == 0:
        raise ValueError("No se puede dividir entre cero.")
    return numero1 / numero2


def main() -> None:
    """Solicita dos números y muestra los resultados de las operaciones."""
    numero1: float = float(input())
    numero2: float = float(input())

    print(f"Suma: {sumar(numero1, numero2)}")
    print(f"Resta: {restar(numero1, numero2)}")
    print(f"Multiplicación: {multiplicar(numero1, numero2)}")

    try:
        print(f"División: {dividir(numero1, numero2)}")
    except ValueError as error:
        print(f"División: {error}")


if __name__ == "__main__":
    main()
