def main():
    conIva = float(input("Introduce el importe con IVA: "))

    iva = conIva * 0.10
    sinIva = conIva - iva


    print("El importe sin IVA es: ", sinIva)
    print("El IVA es: ", iva)

if __name__ == "__main__":
    main()
