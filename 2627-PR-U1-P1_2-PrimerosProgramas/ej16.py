def main():
    PAN = 3.49

    descuento = 0.60
    numeroBarras = int(input("Introduce el número de barras de pan: "))

    totalConDescuento = numeroBarras * PAN * (1 - descuento)

    print("El precio habitual de una barra de pan es: ", PAN, "€ se le hace un descuento del 60% y el precio final es: ", totalConDescuento, "€"   )

if __name__ == "__main__":
    main()
