def main():
    producto: str = input("Introduce el nombre del producto: ")
    precio: float = float(input("Introduce el precio unitario: "))
    unidades: float = int(input("Introduce el número de unidades: "))

    total = precio * unidades

    print(f"{producto}: {precio:09.2f} {unidades:03d} {total:011.2f}")


if __name__ == "__main__":
    main()