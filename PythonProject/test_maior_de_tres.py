from maior_de_tres import definir_maior



def test_terceiro_maior():
    resultado = definir_maior(5, 2, 8)
    assert resultado == 8


def test_empate():
    resultado = definir_maior(10, 10, 5)
    assert resultado == 10


def test_negativos():
    resultado = definir_maior(-1, -5, -3)
    assert resultado == -1


def test_todos_iguais():
    resultado = definir_maior(7, 7, 7)
    assert resultado == 7


def test_decimais():
    resultado = definir_maior(2.5, 3.1, 1.9)
    assert resultado == 3.1


