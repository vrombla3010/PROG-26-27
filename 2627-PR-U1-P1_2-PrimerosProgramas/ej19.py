def main():
    nombre: str = input("Escribe tu nombre: ")
    n: int = len(nombre)
    print(f"{nombre.upper()} tiene {n} letras.")
    
if __name__ == "__main__":
    main()