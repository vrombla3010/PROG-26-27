def numeros_primos(ini: int, fin: int) -> str:

    cadena: str = ""

    for i in range(ini, fin +1):
        es_primo: bool = True
        
        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break
        
        if es_primo:
            cadena += f", {i}"

    return cadena[2:]

def main():

    primero = int(input("Introduce el primero numero: "))
    segundo = int(input("Introduce el segundo numero: "))

    print(numeros_primos(primero, segundo))


if __name__ == "__main__":
    main()