def main():
    n: int = int(input("Introduce el primer número: "))
    m: int = int(input("Introduce el segundo número: "))

    while n < 0 or m <= 0:
        print("Error: el primer número debe ser positivo y el segundo número debe ser mayor que cero.")
        n: int = int(input("Introduce el primer número: "))
        m: int = int(input("Introduce el segundo número: "))

    c: int = n // m
    r: int = n % m

    print("la división entera de", n, "entre", m, "da como cociente", c, "y como resto", r)


if __name__ == "__main__":
    main()