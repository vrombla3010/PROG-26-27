def main():
    nombreCompleto: str = input("Escribe tu nombre completo: ")
    nombre: str = nombreCompleto.split()[0]

    minusculas: str = nombre.lower()
    mayusculas: str = nombre.upper()
    primeraLetraEnMayusculas: str = nombreCompleto.title()

    print(f"Nombre en minúsculas: {minusculas}")
    print(f"Nombre en mayúsculas: {mayusculas}")
    print(f"Nombre con primera letra de cada palabra en mayúsculas: {primeraLetraEnMayusculas}")

if __name__ == "__main__":
    main()