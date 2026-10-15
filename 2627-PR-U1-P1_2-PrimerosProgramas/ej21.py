def main():

    frase: str = input("Introduce una frase: ")
    frase_invertida: str = frase[::-1]
    print(f"La frase invertida es: {frase_invertida}")


if __name__ == "__main__":
    main()