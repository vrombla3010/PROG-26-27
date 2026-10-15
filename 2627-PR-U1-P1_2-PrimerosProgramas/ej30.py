def main():
    n = int(input("Introduce un número: "))

    if n < 2:
        print("No es primo")
    else:
        primo: bool = True

        for i in range(2, n):
            if n % i == 0:
                primo: bool = False

        if primo:
            print("Es primo")
        else:
            print("No es primo")


if __name__ == "__main__":
    main()