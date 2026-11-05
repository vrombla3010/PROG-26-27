"""
Ejercicio 2.1.2

Escribir un programa que almacene la cadena de caracteres
`contraseña` en una variable, pregunte al usuario por la contraseña e
imprima por pantalla si la contraseña introducida por el usuario
coincide con la guardada en la variable sin tener en cuenta mayúsculas
y minúsculas.
"""

def comprobar_contraseña(contraseña: str, contraseña_usuario: str) -> bool:

    if contraseña.lower() == contraseña_usuario.lower():
        return True
    else:
        return False

def main():
    contraseña: str = "contraseña"
    contraseña_usuario: str = input("Introduce la contraseña: ")

    if comprobar_contraseña(contraseña, contraseña_usuario):
        print("La contraseña es correcta")
    else:
        print("La contraseña es incorrecta")

if __name__ == "__main__":
    main()