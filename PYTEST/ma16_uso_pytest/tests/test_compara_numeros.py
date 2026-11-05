from src.compara_numeros import compara_numeros


def test_devuelve_el_mayor_de_dos_positivos():
    assert compara_numeros(8, 3) == 8
    assert compara_numeros(3, 8) == 8


def test_devuelve_el_mayor_de_dos_negativos():
    assert compara_numeros(-2, -7) == -2
    assert compara_numeros(-7, -2) == -2


def test_devuelve_cero_si_los_numeros_son_iguales():
    assert compara_numeros(5, 5) == 0
    assert compara_numeros(-4, -4) == 0
