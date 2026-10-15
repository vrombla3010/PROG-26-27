def main():
    precio: str = input("Introduce el precio en euros con dos decimales: ")

    partes: list[str] = precio.split(".")

    euros: str = partes[0]
    centimos: str = partes[1]

    print("Número de euros:", euros)
    print("Número de céntimos:", centimos)

if __name__ == "__main__":
    main()