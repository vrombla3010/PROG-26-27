"""
Ejercicio 2.1.4

Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es par o impar.
"""

def par_impar(numero : int) -> bool:

    if numero % 2 == 0:
        return True
    else:
        return False

def main():

    numero = int(input(""))

