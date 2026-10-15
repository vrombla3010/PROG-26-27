def main():
    import random

    a: int = int(input("Introduce el primer numero: "))
    b: int = int(input("Introduce el segundo numero: "))

    numero: int = random.randint(a, b)

    print("El número aleatorio es:", numero)


if __name__ == "__main__":
    main()