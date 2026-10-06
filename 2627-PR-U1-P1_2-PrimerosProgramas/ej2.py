def main():
    horas = int(input("Introduce el número de horas trabajadas: "))
    tarifa = float(input("Introduce la tarifa por hora: "))

    sueldo = horas * tarifa

    print("El sueldo total es: ", sueldo)

if __name__ == "__main__":
    main()