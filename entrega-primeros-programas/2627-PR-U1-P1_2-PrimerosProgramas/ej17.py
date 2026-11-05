def main():
    nombre = input("Escribe tu nombre: ")
    repeticiones = int(input("Introduce el número de repeticiones: "))
    
    for i in range(repeticiones):
        print("Hola, " + nombre + ".")

if __name__ == "__main__":
    main()
    