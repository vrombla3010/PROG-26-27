def compara_numeros(primer_numero, segundo_numero):
    """Devuelve el mayor de dos números o 0 si son iguales."""
    if primer_numero == segundo_numero:
        return 0
    return max(primer_numero, segundo_numero)
