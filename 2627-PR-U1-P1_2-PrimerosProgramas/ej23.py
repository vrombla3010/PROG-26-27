def main():

    cambiar: str = "ceu.es"
    correo: str = input("Introduce tu correo electronico: ")
    parte: list[str] = correo.split("@")

    nuevo_correo: str = parte[0] + "@" + cambiar
    print("Tu nuevo correo es:", nuevo_correo)

if __name__ == "__main__":
    main()