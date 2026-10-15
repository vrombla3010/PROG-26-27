def main():

    productos: str = input("Introduce los productos de la cesta de la compra (separados por comas): ")

    productos_con_saltos: str = productos.replace(",", "\n")

    print(productos_con_saltos)


if __name__ == "__main__":
    main()