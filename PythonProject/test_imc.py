from imc import calcular_imc

def test_imc_70_175():
    resultado = calcular_imc(70, 1.75)
    assert round(resultado, 2) == 22.86


def test_imc_50_160():
    resultado = calcular_imc(50, 1.60)
    assert round(resultado, 2) == 19.53


def test_peso_zero():
    resultado = calcular_imc(0, 1.75)
    assert resultado is None


def test_altura_zero():
    resultado = calcular_imc(70, 0)
    assert resultado is None


def test_valores_negativos():
    assert calcular_imc(-70, 1.75) is None
    assert calcular_imc(70, -1.75) is None