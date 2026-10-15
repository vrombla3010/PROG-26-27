def main():
    a: float = float(input("Introduce el primer lado: "))
    b: float = float(input("Introduce el segundo lado: "))
    c: float = float(input("Introduce el tercer lado: "))

    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        print("Las longitudes pueden formar un triángulo")
    else:
        print("Las longitudes no pueden formar un triángulo")

if __name__ == "__main__":
    main()