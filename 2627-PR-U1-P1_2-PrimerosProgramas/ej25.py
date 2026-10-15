def main():

    fecha: str = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

    dia: str
    mes: str
    anio: str
    dia, mes, anio = fecha.split('/')

    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {anio}")

if __name__ == "__main__":
    main()