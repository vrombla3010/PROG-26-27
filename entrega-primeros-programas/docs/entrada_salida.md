## Entrada y salida de datos

### Mostrar información con `print()`

La función `print()` permite mostrar texto, variables y expresiones:

```python
nombre = "Ana"
edad = 18

print("Nombre:", nombre)
print("Edad:", edad, "años")
```

Podemos combinar texto y variables de distintas formas:

```python
# Concatenación: todos los elementos deben ser cadenas
print("Edad: " + str(edad) + " años")

# f-string (forma recomendada)
print(f"{nombre} tiene {edad} años")

# format()
print("{} tiene {} años".format(nombre, edad))
```

Las **f-strings** permiten también formatear fácilmente los valores:

```python
precio = 12.5

print(f"Precio: {precio:.2f} €")
```

`print()` admite además los parámetros `sep` y `end`:

```python
print("uno", "dos", "tres", sep="-")
# uno-dos-tres

print("Hola", end=" ")
print("mundo")
# Hola mundo
```

- `sep` indica qué se escribe **entre los valores**. Por defecto es un espacio.
- `end` indica qué se escribe **al final**. Por defecto es un salto de línea (`"\n"`).

### Leer información con `input()`

La función `input()` permite solicitar información al usuario:

```python
nombre = input("Introduce tu nombre: ")
```

**`input()` siempre devuelve una cadena (`str`)**. Si necesitamos otro tipo de dato debemos realizar la conversión:

```python
edad = int(input("Introduce tu edad: "))
altura = float(input("Introduce tu altura: "))
```

Recuerda utilizar el tipo de dato adecuado para cada información que necesite el programa.
