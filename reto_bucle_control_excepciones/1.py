"""
Ejercicio 2.3.1 — Años cumplidos. Solicita una edad entera y muestra todos los años 
cumplidos desde 1 hasta esa edad. Captura una entrada que no sea un entero, rechaza 
edades negativas y documenta la salida para la edad 0.

Ejemplo de ejecución:

    Introduce tu edad: hola
    Debes introducir un número entero válido.
    Introduce tu edad: -3
    La edad debe ser mayor que cero.
    Introduce tu edad: 5
    1
    2
    3
    4
    5
"""

def pedir_edad() -> int:
    """
    Solicita una edad válida al usuario.

    Repite la petición hasta obtener un entero positivo.

    Returns:
        Edad introducida por el usuario.
    """
    edad = None
    while edad is None:
        try:
            entrada = input("Introduce tu edad: ")
            valor = int(entrada)  
            validar_edad(valor)   
            edad = valor
        except ValueError as e:
            
            print(e)
    return edad


def validar_edad(edad: int):

    if edad < 0:
        raise ValueError("La edad debe ser mayor que cero.")
    elif edad == 0: 
        raise ValueError("La edad debe ser mayor que cero.")


def mostrar_anios(edad: int) -> None:
    """
    Muestra todos los años cumplidos desde 1 hasta la edad.

    Args:
        edad: Edad de la persona.
    """
    for i in range(1, edad + 1):
            print(i)



def main() -> None:
    """Ejecuta el programa principal."""
    edad = pedir_edad()
    mostrar_anios(edad)
    

if __name__ == "__main__":
    main()