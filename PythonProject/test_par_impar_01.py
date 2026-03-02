from par_impar_01 import par_impar

def test_numero_par():
    resultado = par_impar(4)
    assert resultado == "Par"


def test_numero_impar():
    resultado = par_impar(5)
    assert resultado == "Impar"


def test_zero():
    resultado = par_impar(0)
    assert resultado == "Par"


def test_numero_negativo_par():
    resultado = par_impar(-2)
    assert resultado == "Par"


def test_numero_negativo_impar():
    resultado = par_impar(-3)
    assert resultado == "Impar"