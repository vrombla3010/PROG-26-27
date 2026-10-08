def main():

    telefono = input("Introduce un número de teléfono con el formato +34-913724710-56: ")
    partes = telefono.split("-")    

    numero = partes[1]
    print(f"El número de teléfono sin el prefijo y la extensión es: {numero}")


if __name__ == "__main__":
    main()