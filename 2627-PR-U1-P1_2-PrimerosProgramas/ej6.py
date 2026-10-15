def main():
    conIva: float = float(input("Introduce el importe con IVA: "))

    iva: float = conIva * 10 / 110
    sinIva: float = conIva - iva


    print("El importe sin IVA es: ", sinIva)
    print("El IVA es: ", iva)

if __name__ == "__main__":
    main()
