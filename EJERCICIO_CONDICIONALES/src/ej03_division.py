"""
Ejercicio 2.1.3

Escribir un programa que pida al usuario dos números y muestre por
pantalla su división. Si el divisor es cero el programa debe mostrar un
error.
"""

def division(num1: float, num2: float) -> float:

    return num1 / num2 

def main():

    num1: float = float(input("Introduce el primero número: "))
    num2: float = float(input("Introduce el segundo número: "))

    while num2 == 0:
        num2 = float(input("Introduce otro número, el divisor no puede ser 0: "))

    print (division(num1, num2))

if __name__ == "__main__":
    main()