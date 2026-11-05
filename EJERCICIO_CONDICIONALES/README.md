# Práctica 2.1: Sentencias condicionales

## Objetivo

Desarrollar los **10 ejercicios de la Práctica 2.1**, aplicando estructuras condicionales en Python y organizando el código mediante funciones y módulos independientes.

[Consultar los ejercicios originales](https://revilofe.github.io/section1/u02/practica/PROG-U2.-Practica001/)

## Requisitos de desarrollo

### 1. Implementación de los ejercicios

- Resolver los **10 ejercicios** propuestos.
- Para cada ejercicio, identificar la función o funciones necesarias para resolverlo.
- Definir funciones con nombres descriptivos.
- Utilizar **anotaciones de tipo (*type hints*)** en los parámetros y valores de retorno de todas las funciones.
- Utilizar también **anotaciones de tipo en las variables**, indicando su tipo en la primera definición o asignación. No será necesario repetir la anotación en asignaciones posteriores.
- Documentar todas las funciones mediante **docstrings**, incluyendo su descripción, parámetros de entrada y valor de retorno cuando corresponda.
- Separar la lógica del programa de la entrada y salida de datos siempre que sea posible.

Por ejemplo, para el **Ejercicio 2.1.1**, podríamos identificar la siguiente función:

```python
def es_mayor(edad: int) -> bool:
    """
    Comprueba si una persona es mayor de edad.

    :param edad: Edad de la persona.
    :return: True si es mayor de edad y False en caso contrario.
    """
    return edad >= 18
```

Ejemplo de anotaciones de tipo en variables:

```python
edad: int = 18
nombre: str = "Ana"
precios: list[float] = [12.5, 18.0, 9.75]

edad = 20  # No es necesario repetir la anotación
```

Cada ejercicio deberá tener su propia implementación, utilizando las funciones que consideréis necesarias.

### 2. Estructura del repositorio

Utilizar una estructura básica de proyecto Python, separando el código fuente de la documentación.

Cada ejercicio deberá implementarse en un módulo independiente, respetando los siguientes nombres:

```text
.
├── src/
│   ├── ej01_edad.py
│   ├── ej02_password.py
│   ├── ej03_division.py
│   ├── ej04_par_impar.py
│   ├── ej05_tributar.py
│   ├── ej06_grupo.py
│   ├── ej07_renta.py
│   ├── ej08_empleados.py
│   ├── ej09_precio_entrada.py
│   └── ej10_pizzeria.py
├── doc/
│   └── index.md
├── .gitignore
└── README.md
```

### 3. Documentación de los ejercicios

Crear el archivo `doc/index.md` y copiar en él los enunciados originales de los 10 ejercicios de la página web indicada.

Para elaborar este documento, investigad y utilizad correctamente la sintaxis de **Markdown**:

- **Encabezado de nivel 1:** `Práctica 2.1: Sentencias condicionales`.
- **Encabezado de nivel 2:** `P2.1 - Ejercicios`.
- **Encabezados de nivel 3:** desde `Ejercicio 2.1.1` hasta `Ejercicio 2.1.10`.
- **Tablas:** investigad cómo construir tablas en Markdown y cómo destacar sus cabeceras utilizando negrita.
- **Al final del archivo `README.md`**, añadid una línea horizontal y, a continuación, un enlace relativo al archivo `doc/index.md`, cuyo texto visible sea «Enlace al enunciado de los ejercicios».

Respetad la estructura y el contenido de los enunciados originales, incluyendo las tablas de los ejercicios que las contengan.

## Entrega

Una vez finalizada la práctica:

- Subir todos los archivos del proyecto al repositorio de GitHub.
- Comprobar que el código y la documentación están correctamente organizados.
- Entregar la tarea en **Moodle**, indicando **«Finalizado»**.

**Se tendrá en cuenta hasta el último commit realizado antes del cierre de la tarea en Classroom50.**

---

[Enlace al enunciado de los ejercicios](doc/index.md)
