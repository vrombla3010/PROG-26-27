def main():
    nombre: str = input("Escribe tu nombre: ")
    repeticiones: int = int(input("Introduce el número de repeticiones: "))

    i: int
    for i in range(repeticiones):
        print("Hola, " + nombre + ".")

if __name__ == "__main__":
    main()
