def main():
    horas: int = int(input("Introduce el número de horas trabajadas: "))
    tarifa: float = float(input("Introduce la tarifa por hora: "))

    sueldo: float = horas * tarifa

    print("El sueldo total es: ", sueldo)

if __name__ == "__main__":
    main()