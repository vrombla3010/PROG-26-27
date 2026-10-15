def main():
    celsius: float = float(input("Introduce la temperatura en grados Celsius: "))

    fahrenheit: float = (celsius * 9/5) + 32

    print(celsius,"grados Celsius son", fahrenheit,"grados Fahrenheit.")

if __name__ == "__main__":
    main()
