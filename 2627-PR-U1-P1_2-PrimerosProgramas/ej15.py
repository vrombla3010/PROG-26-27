def main():
    interes = 0.04

    ahorros = float(input("Introduce la cantidad de dinero ahorrada: "))

    ahorros = ahorros * (1 + interes)
    print(f"Después del primer año tendrás: {ahorros:.2f} €")

    ahorros = ahorros * (1 + interes)
    print(f"Después del segundo año tendrás: {ahorros:.2f} €")

    ahorros = ahorros * (1 + interes)
    print(f"Después del tercer año tendrás: {ahorros:.2f} €")


if __name__ == "__main__":
    main()
