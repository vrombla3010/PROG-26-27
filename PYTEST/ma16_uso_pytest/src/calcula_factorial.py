def calcula_factorial(numero):
    """Calcula el factorial de un entero entre 0 y 10."""

    if type(numero) is not int or numero < 0 or numero > 10:
        return -1

    resultado = 1

    for i in range(2, numero + 1):
        resultado *= i

    return resultado
