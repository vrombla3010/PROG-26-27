from src.calcula_factorial import calcula_factorial


def test_factorial_de_cero():
    assert calcula_factorial(0) == 1


def test_factorial_de_uno():
    assert calcula_factorial(1) == 1


def test_factorial_de_cinco():
    assert calcula_factorial(5) == 120


def test_factorial_de_diez():
    assert calcula_factorial(10) == 3628800


def test_rechaza_numeros_negativos():
    assert calcula_factorial(-1) == -1


def test_rechaza_numeros_mayores_que_diez():
    assert calcula_factorial(11) == -1
