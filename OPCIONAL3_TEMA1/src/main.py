VOCALES: str = "aeiouáéíóúü"


def analizar_texto(frase: str) -> tuple[int, int]:

    """
    Analiza una frase y cuenta sus palabras y vocales.

    :param frase: Frase de texto que se desea analizar.
    :return: Tupla con el número de vocales y el número de palabras, en ese orden.
    """

    contador_vocales: int = 0

    for caracter in frase.lower():
        if caracter in VOCALES:
            contador_vocales += 1

    lista_palabras: list[str] = frase.split()
    contador_palabras: int = len(lista_palabras)

    return contador_vocales, contador_palabras


def main() -> None:

    """
    Función principal que solicita una frase y muestra el número de palabras
    y vocales que contiene.
    """

    frase: str = input("Introduce una frase para analizar: ")

    vocales: int
    palabras: int
    vocales, palabras = analizar_texto(frase)

    print(f"Vocales: {vocales}")
    print(f"Palabras: {palabras}")


if __name__ == "__main__":
    main()