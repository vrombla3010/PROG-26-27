def main():
    payaso = 112
    muñeca = 75

    numero_de_payasos = int(input("Introduce el número de payasos: "))
    numero_de_muñecas = int(input("Introduce el número de muñecas: "))

    peso_total = (payaso * numero_de_payasos) + (muñeca * numero_de_muñecas)

    print("El peso total del paquete es:", peso_total, "gramos.")


if __name__ == "__main__":
    main()
    