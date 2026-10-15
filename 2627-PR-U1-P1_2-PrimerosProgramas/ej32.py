def main():
    limite: int = int(input("Introduce un número: "))

    a: int = 0
    b: int = 1

    while a <= limite:
        print(a)
        siguiente = a + b
        a = b
        b = siguiente

if __name__ == "__main__":
    main()