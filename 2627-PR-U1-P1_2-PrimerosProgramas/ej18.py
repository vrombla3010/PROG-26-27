def main():
    nombreCompleto = input("Escribe tu nombre completo: ")
    nombre = nombreCompleto.split()[0]

    minusculas = nombre.lower()
    mayusculas = nombre.upper()
    primeraLetraEnMayusculas = nombreCompleto.title()

    print(f"Nombre en minúsculas: {minusculas}")
    print(f"Nombre en mayúsculas: {mayusculas}")
    print(f"Nombre con primera letra de cada palabra en mayúsculas: {primeraLetraEnMayusculas}")

if __name__ == "__main__":
    main()