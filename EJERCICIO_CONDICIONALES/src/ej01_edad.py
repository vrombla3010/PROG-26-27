"""
Ejercicio 2.1.1

Escribir un programa que pregunte al usuario su edad y muestre por
pantalla si es mayor de edad o no.
"""


def mayor_edad (edad: int) -> bool:

    if edad < 18:
        return False
    else:
        return True

def main():

    edad: int = int(input("Introduce tu edad: "))

    if mayor_edad(edad):
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

if __name__ == "__main__":
    main()
