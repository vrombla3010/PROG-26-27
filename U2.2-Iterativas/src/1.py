"""
Escribe un programa que sume todos los números del 1 al 100 usando un bucle while y luego verifica el resultado con for.
"""
def suma_numeros_while(maximo: int) ->  int:
    
    contador: int = 1
    suma_w: int = 0

    while contador <= maximo:
        
        suma_w += contador
        contador += 1

    return suma_w

def verificacion_for(maximo: int) -> int:

    suma_f: int = 0

    for n in range(1,maximo):
        suma_f += n
    
    return suma_f

def main():
    
    numero: int = int(input("Introduzca un número: "))
    
    total: int = suma_numeros_while(numero)

    confirmacion: int = verificacion_for(numero+1)


    if total == confirmacion:
        print("Bien")
    else:
        print("Mal")



if __name__ == "__main__":
    main()


