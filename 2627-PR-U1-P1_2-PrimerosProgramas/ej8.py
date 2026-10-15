def main():
    numero: int = int(input("Introduce el primer número: "))
    suma: int = numero

    numero: int = int(input("Introduce el segundo número: "))
    suma = suma + numero

    numero: int = int(input("Introduce el tercer número: "))
    suma = suma + numero

    print("La suma de los tres números es: ", suma)

if __name__ == "__main__":
    main()
