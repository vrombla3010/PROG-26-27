## 5. OPCIONAL — Actividades extra de ampliación

Si terminas los ejercicios anteriores puedes realizar las siguientes actividades:

[Actividades extra de ampliación](https://revilofe.github.io/section1/u01/practica/PROG-U1.-Ampliacion001/?utm_source=chatgpt.com)

Cada actividad deberá realizarse también en un módulo independiente:

```text
extra1.py
extra2.py
extra3.py
...
extra10.py
```

Y deberá utilizar el mismo punto de entrada:

```python
def main():
    # Instrucciones


if __name__ == "__main__":
    main()
```

Las actividades **1-5 y 7** pueden resolverse esencialmente con los contenidos estudiados.

Las actividades **6 y 8** requieren además crear funciones auxiliares. Las actividades **9 y 10** anticipan estructuras de control de la U2.

### Extra 6 — Crear funciones que devuelven un resultado

En esta actividad se pide expresamente crear funciones.

Una función puede recibir información mediante **parámetros**:

```python
def calcular_doble(numero):
    return numero * 2
```

Podemos utilizarla:

```python
resultado = calcular_doble(7)

print(resultado)
```

Resultado:

```text
14
```

`return` termina la función y devuelve un resultado al código que la llamó.

## Extra 8 — Función y repetición de cadenas

También tendrás que crear una función que reciba información y devuelva un resultado.

Recuerda además que una cadena puede repetirse utilizando `*`:

```python
separador = "-" * 10

print(separador)
```

Resultado:

```text
----------
```

Puedes combinar esta operación con `len()`, slicing y las operaciones con cadenas estudiadas.

### Extra 9 — `if` y `any()`

Para validar una contraseña necesitamos tomar una decisión, por lo que utilizaremos `if`.

Además, necesitamos comprobar si **algún carácter** cumple una determinada condición.

Podemos utilizar:

```python
any(...)
```

Por ejemplo:

```python
palabras = ["sol", "casa", "ordenador"]

if any(len(palabra) > 5 for palabra in palabras):
    print("Hay alguna palabra con más de 5 caracteres")
```

No necesitas comprender todavía completamente la expresión que aparece dentro de `any()`.

Interprétala como:

> ¿Existe al menos un elemento que cumple esta condición?

También puedes utilizar:

```python
texto.isdigit()
```

para comprobar si una cadena contiene únicamente dígitos:

```python
texto = "1234"

print(texto.isdigit())
```

Resultado:

```text
True
```

### Extra 10 — `if / else`

La mayor parte del problema se puede resolver mediante los operadores `//` y `%`, que ya conocemos.

Sin embargo, necesitamos comprobar primero si una cantidad cumple una determinada condición.

Ejemplo:

```python
numero = 18

if numero % 2 == 0:
    print("Es múltiplo de 2")
else:
    print("No es múltiplo de 2")
```

Utiliza este mismo mecanismo de decisión para validar los datos que necesites antes de realizar los cálculos.

---

## 5.1. RETO — Menú principal y submenús

Si has realizado las actividades extra puedes ampliar `main.py` para crear un sistema de **tres menús**.

El programa comenzará mostrando:

```text
MENÚ PPAL
---------

1. Primeros programas.
2. Actividades extra.
3. Salir
```

Si seleccionas `1`:

```text
MENÚ Primeros Programas resueltos
---------------------------------

Introduzca el número del ejercicio (0 para volver):
```

Desde este menú se podrán ejecutar los ejercicios `ej1.py` hasta `ej32.py`.

Al introducir `0`, el programa deberá **volver al menú principal**, no terminar.

Si seleccionas `2`:

```text
MENÚ Actividades extra
----------------------

Introduzca el número del ejercicio (0 para volver):
```

Desde este menú se podrán ejecutar `extra1.py` hasta `extra10.py`.

Al introducir `0`, también se deberá volver al menú principal.

La opción `3` del menú principal finalizará el programa.

---

## 5.2. RETO — Validación de los menús

Todos los menús deberán controlar que el usuario introduce un **número entero válido dentro del rango permitido**.

Para ello deberás implementar las siguientes funciones.

### `es_numerico()`

```python
def es_numerico(texto):
    """Comprueba si una cadena de texto contiene únicamente dígitos numéricos.

    Args:
        texto (str): La cadena de texto que se va a validar.

    Returns:
        bool: True si la cadena no está vacía y todos sus caracteres son
        dígitos del 0 al 9, False en caso contrario.
    """
```

Ya hemos visto que las comparaciones producen valores `True` o `False`. Una función puede devolver directamente ese resultado.

### `pedir_entero()`

```python
def pedir_entero(minimo, maximo):
    """Solicita un número entero por consola dentro de un rango específico.

    La función repite la solicitud indefinidamente hasta que el usuario
    introduce un valor válido (que consista solo en dígitos y se encuentre
    dentro de los límites establecidos).

    Args:
        minimo (int): El valor entero mínimo permitido.
        maximo (int): El valor entero máximo permitido.

    Returns:
        int: El número entero validado introducido por el usuario que se
        encuentra entre `minimo` y `maximo` (ambos inclusive).
    """
```

Por tanto, `pedir_entero(minimo, maximo)` deberá:

1. solicitar el dato mediante `input()`;
2. comprobar mediante `es_numerico()` que contiene únicamente dígitos;
3. convertirlo a `int`;
4. comprobar que está entre `minimo` y `maximo`;
5. devolverlo mediante `return` si es correcto;
6. volver a solicitarlo si no lo es.
