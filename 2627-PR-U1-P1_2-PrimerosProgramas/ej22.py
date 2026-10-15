def main():

    frase: str = input("Introduce una frase: ")
    vocal: str = input("Introduce una vocal: ")
    frase_modificada: str = frase.replace(vocal, vocal.upper())
    print(f"La frase modificada es: {frase_modificada}")


if __name__ == "__main__":
    main()