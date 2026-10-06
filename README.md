# 2627-PR-U1-P1_2-PrimerosProgramas

En esta práctica resolverás una colección de pequeños problemas utilizando Python. El objetivo es aplicar los contenidos estudiados hasta ahora sobre **estructura de un programa, variables, tipos de datos, operadores, entrada y salida, conversiones y cadenas de caracteres**.

Los enunciados de los ejercicios se encuentran en:

[Práctica 1.2 - Primeros programas](https://revilofe.github.io/section1/u01/practica/PROG-U1.-Practica002/?utm_source=chatgpt.com)

Para resolverlos debes utilizar principalmente los contenidos estudiados en:

- [1.2 - Práctica con un lenguaje](https://revilofe.github.io/section1/u01/teoria/PROG-U1.2.-PracticaConUnLenguajes/?utm_source=chatgpt.com)
- [1.3 - Tipos de datos](https://revilofe.github.io/section1/u01/teoria/PROG-U1.3.-TiposDeDatos/?utm_source=chatgpt.com)

La mayoría de los ejercicios pueden resolverse directamente con estos contenidos. En algunos de ellos necesitarás utilizar alguna instrucción que todavía no hemos estudiado. Encontrarás más adelante una breve explicación y un ejemplo para poder utilizarla.

**RECUERDA** entregar en Moodle la actividad una vez consideres que has terminado y **ElIAs** puede revisarla.

<img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/69371875-02b1-4e36-93c2-71712e8f69e0" />

**AYUDA Extra**

[Entrada y salida de datos](entrada_salida.md)

---

## 1. Organización de los ejercicios

Cada ejercicio debe realizarse en un **módulo Python diferente**:

```text
ej1.py
ej2.py
ej3.py
...
ej32.py
```

Por ejemplo, la solución del ejercicio 1.2.7 deberá encontrarse en:

```text
ej7.py
```

Recuerda que un módulo de Python es simplemente un archivo con extensión `.py`.

---

## 2. Punto único de entrada

Todos los programas deberán utilizar una función `main()` como punto de entrada:

```python
def main():
    # Instrucciones del programa


if __name__ == "__main__":
    main()
```

Por tanto, no debes escribir directamente todo el programa fuera de `main()`.

Por ejemplo:

```python
def main():
    nombre = input("Introduce tu nombre: ")
    print(f"Hola, {nombre}")


if __name__ == "__main__":
    main()
```

La condición:

```python
if __name__ == "__main__":
```

permite distinguir entre **ejecutar directamente un módulo** e **importarlo desde otro programa**.

---

## 3. Ejercicios que necesitan alguna instrucción adicional

Los ejercicios **1-12, 14-21, 24, 25 y 27** pueden resolverse directamente utilizando los contenidos estudiados en 1.2 y 1.3.

En algunos de los restantes necesitarás utilizar alguna herramienta adicional o anticipar ligeramente contenidos que estudiaremos posteriormente.

### Ejercicio 13 — `if / else`

Debes tratar el caso en el que el divisor sea cero. Para decidir qué instrucciones ejecutar dependiendo de una condición utilizamos `if`:

```python
edad = 17

if edad >= 18:
    print("Puede entrar")
else:
    print("No puede entrar")
```

La estructura general es:

```python
if condicion:
    # Se ejecuta si la condición es True
else:
    # Se ejecuta si la condición es False
```

Utiliza esta estructura para evitar realizar una operación que no sea válida.

---

### Ejercicio 22 — `replace()`

Necesitas sustituir determinadas apariciones dentro de una cadena.

Python proporciona el método:

```python
cadena.replace(texto_original, texto_nuevo)
```

Por ejemplo:

```python
mensaje = "Me gusta Java"
nuevo_mensaje = mensaje.replace("Java", "Python")

print(nuevo_mensaje)
```

Resultado:

```text
Me gusta Python
```

`replace()` devuelve una **nueva cadena**; no modifica la cadena original.

---

### Ejercicio 23 — `split()`

Puedes utilizar `split()` para dividir una cadena utilizando un separador. Este método sí aparece en el apartado 1.3.

Por ejemplo:

```python
dato = "Cádiz:11000"
partes = dato.split(":")

print(partes[0])
print(partes[1])
```

Resultado:

```text
Cádiz
11000
```

`split()` devuelve una lista con las partes obtenidas.

---

### Ejercicio 26 — recorrer los elementos obtenidos

Puedes utilizar:

```python
productos = texto.split(",")
```

para separar los productos.

Pero si no sabes cuántos productos se han introducido necesitarás recorrerlos. Para ello puedes anticipar el bucle `for`, que estudiaremos en la U2.

Ejemplo:

```python
colores = "rojo,verde,azul".split(",")

for color in colores:
    print(color)
```

Resultado:

```text
rojo
verde
azul
```

La estructura:

```python
for elemento in coleccion:
    # instrucciones
```

ejecuta las instrucciones una vez por cada elemento.

---

### Ejercicio 28 — `if` y operadores lógicos

Para comprobar si unas determinadas longitudes pueden formar un triángulo necesitas tomar una decisión.

Ya hemos visto los operadores:

```python
>
<
>=
<=
==
!=
```

y los operadores lógicos:

```python
and
or
not
```

Pero todavía no hemos utilizado esas expresiones para controlar el flujo del programa.

Ejemplo:

```python
edad = 20
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Cumple las dos condiciones")
else:
    print("No cumple las condiciones")
```

`and` exige que **todas las condiciones** sean verdaderas.

---

### Ejercicio 29 — números aleatorios

Para generar números aleatorios podemos utilizar el módulo `random` de Python.

Primero se importa:

```python
import random
```

Después podemos utilizar:

```python
numero = random.randint(1, 6)
```

Por ejemplo:

```python
import random

dado = random.randint(1, 6)

print(dado)
```

`randint(a, b)` genera un número entero aleatorio comprendido entre `a` y `b`, **ambos incluidos**.

---

### Ejercicio 30 — `if`, `for`, `range()` y `break`

Para determinar si un número es primo tendrás que probar posibles divisores. Necesitarás repetir una operación y tomar decisiones.

`range()` permite generar una secuencia de números:

```python
for numero in range(1, 5):
    print(numero)
```

Resultado:

```text
1
2
3
4
```

Observa que el último valor de `range()` **no se incluye**.

También puedes utilizar `break` para terminar un bucle anticipadamente:

```python
for numero in range(1, 10):
    if numero == 4:
        break

    print(numero)
```

Cuando se ejecuta `break`, se abandona inmediatamente el bucle.

---

### Ejercicio 31 — `for`, `range()` e `if`

Para encontrar todos los valores que cumplen una determinada condición tendrás que recorrer diferentes posibilidades.

Por ejemplo:

```python
for numero in range(1, 11):
    if numero % 3 == 0:
        print(numero)
```

Resultado:

```text
3
6
9
```

Recuerda que:

```python
a % b
```

devuelve el **resto** de dividir `a` entre `b`.

---

### Ejercicio 32 — `while`

En algunas ocasiones no sabemos de antemano cuántas veces debemos repetir una operación.

Para ello podemos utilizar:

```python
while condicion:
    # instrucciones
```

Por ejemplo:

```python
contador = 1

while contador <= 4:
    print(contador)
    contador += 1
```

Resultado:

```text
1
2
3
4
```

`while` repite las instrucciones mientras su condición sea `True`.

**Importante:** alguna de las instrucciones del bucle debe provocar que la condición termine siendo falsa. De lo contrario crearíamos un bucle infinito.

---

## 4. OPCIONAL — Menú de ejercicios

Como ampliación puedes crear un módulo:

```text
main.py
```

desde el que ejecutar cualquiera de los 32 ejercicios.

El menú deberá tener este aspecto:

```text
MENÚ Primeros Programas resueltos
---------------------------------

Introduzca el número del ejercicio (0 para salir):
```

Al introducir un número entre `1` y `32`, se ejecutará el módulo correspondiente.

Para poder ejecutar las funciones de otro módulo debes **importarlo**.

Por ejemplo, si tenemos:

```text
ej1.py
ej2.py
main.py
```

desde `main.py` podemos hacer:

```python
import ej1
import ej2
```

y ejecutar:

```python
ej1.main()
```

o:

```python
ej2.main()
```

Después de ejecutar cada ejercicio se deberá:

1. pausar la ejecución;
2. limpiar la terminal;
3. volver a mostrar el menú.

Para ello se proporcionará un módulo auxiliar con las funciones `limpiar()` y `pausar()`, que puedes llamar `utilidades.py`:

```python
import os
import subprocess


def limpiar():
    """Limpia la terminal de forma segura en Windows, Linux y macOS."""
    if os.name == "nt":
        # Windows necesita shell=True porque 'cls' es un comando interno
        # de la consola.
        subprocess.run("cls", shell=True)
    else:
        # Linux y macOS ejecutan 'clear' directamente.
        subprocess.run(["clear"])


def pausar():
    input("\n\nPulsa <ENTER> para continuar...")
```

Puedes importar estas funciones desde `main.py`.

**No es necesario comprender todavía cómo funcionan internamente `os` y `subprocess`.** Utiliza las funciones proporcionadas como herramientas auxiliares.

---

## 5. [Actividades de Ampliación](ampliacion.md)

---

## 6. Estructura final del proyecto

Si realizas únicamente la parte obligatoria:

```text
proyecto/
├── ej1.py
├── ej2.py
├── ...
└── ej32.py
```

Si realizas también el menú:

```text
proyecto/
├── main.py
├── utilidades.py
├── ej1.py
├── ej2.py
├── ...
└── ej32.py
```

Y si completas las actividades extra y los retos:

```text
proyecto/
├── main.py
├── utilidades.py
│
├── ej1.py
├── ej2.py
├── ...
├── ej32.py
│
├── extra1.py
├── extra2.py
├── ...
└── extra10.py
```

El objetivo del reto no es únicamente resolver más ejercicios, sino empezar a construir un programa formado por **varios módulos y funciones que colaboran entre sí**.

