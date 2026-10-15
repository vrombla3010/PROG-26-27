def main():
    peso: float = float(input("Introduce tu peso en kg: "))
    estatura: float = float(input("Introduce tu estatura en metros: "))

    imc: float = peso / (estatura ** 2)
    print(f"Tu índice de masa corporal es {imc:.2f}")

if __name__ == "__main__":
    main()

