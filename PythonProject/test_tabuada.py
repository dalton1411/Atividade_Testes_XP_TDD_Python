from tabuada import tabuada


def test_tabuada_2():
    resultado = tabuada(2)
    assert resultado == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def test_tabuada_5():
    resultado = tabuada(5)
    assert resultado == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


def test_numero_zero():
    resultado = tabuada(0)
    assert resultado is None


def test_numero_11():
    resultado = tabuada(11)
    assert resultado is None


def test_numero_negativo():
    resultado = tabuada(-3)
    assert resultado is None