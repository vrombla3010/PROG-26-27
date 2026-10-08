def main():

    cambiar = "ceu.es"
    correo = input("Introduce tu correo electronico: ")
    parte = correo.split("@")

    nuevo_correo = parte[0] + "@" + cambiar
    print("Tu nuevo correo es:", nuevo_correo)

if __name__ == "__main__":
    main()