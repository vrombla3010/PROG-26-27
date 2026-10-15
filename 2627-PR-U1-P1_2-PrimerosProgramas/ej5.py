def main():
    sinIva: float = float(input("Introduce el importe sin IVA: "))

    iva: float = sinIva * 0.21
    total: float = sinIva + iva

    print("El importe total con IVA es: ", total)

if __name__ == "__main__":
    main()
