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

def validar_edad(edad: int) -> None:
    """
    Valida que la edad introducida es correcta.
    Si no lo es, lanzará las siguientes excepciones:
    Edad... 
    Edad...
    """
    if edad <= 0:
        raise ValueError("La edad debe ser mayor que cero.")

    if edad > 120:
        raise ValueError("La edad debe ser menor que 120.")


def entrada_usuario(mensaje: str) -> int:
    try:
        entrada: int = int(input(mensaje))
    except ValueError:
        raise ValueError("Debes introducir un número entero válido.")

    return entrada 


def pedir_edad() -> int:
    """
    Solicita una edad válida al usuario.

    Repite la petición hasta obtener un entero positivo.

    Returns:
        Edad introducida por el usuario.
    """
    edad_valida: bool = False

    while not edad_valida:
        try:
            edad: int = entrada_usuario("Introduce tu edad: ")
            validar_edad(edad)
        except ValueError as e:
            print(e)
        else:
            edad_valida = True

    return edad


def mostrar_anios(edad: int) -> None:
    """
    Muestra todos los años cumplidos desde 1 hasta la edad.

    Args:
        edad: Edad de la persona.
    """
    # TODO: Implementar función según su documentación técnica
    for i in range(1, edad + 1):
        print(i)


def main() -> None:
    """Ejecuta el programa principal."""
    # TODO: Realizar las llamadas a las funciones de forma correcta para solucionar el ejercicio
    edad: int = pedir_edad()
    mostrar_anios(edad)



if __name__ == "__main__":
    main()

