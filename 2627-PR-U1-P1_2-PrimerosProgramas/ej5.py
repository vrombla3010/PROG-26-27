def main():
    sinIva = float(input("Introduce el importe sin IVA: "))

    iva = sinIva * 0.21
    total = sinIva + iva

    print("El importe total con IVA es: ", total)

if __name__ == "__main__":
    main()
