def main():
    n: int = int(input("Introduce un número entero positivo: "))

    if n <= 0:
        print("Debes introducir un número positivo")
    else:
        print("Los divisores de", n, "son:")

        for i in range(1, n + 1):
            if n % i == 0:
                print(i)


if __name__ == "__main__":
    main()