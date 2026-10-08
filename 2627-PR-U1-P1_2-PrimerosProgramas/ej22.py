def main():

    frase = input("Introduce una frase: ")
    vocal = input("Introduce una vocal: ")
    frase_modificada = frase.replace(vocal, vocal.upper())
    print(f"La frase modificada es: {frase_modificada}")


if __name__ == "__main__":
    main()