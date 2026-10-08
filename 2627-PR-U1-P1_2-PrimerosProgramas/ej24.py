def main():
    precio = input("Introduce el precio en euros con dos decimales: ")

    partes = precio.split(".")

    euros = partes[0]
    centimos = partes[1]

    print("Número de euros:", euros)
    print("Número de céntimos:", centimos)

if __name__ == "__main__":
    main()