from validador_cpf import validar_cpf



def test_cpf_11_digitos():
    resultado = validar_cpf("12345678909")
    assert resultado == True


def test_cpf_10_digitos():
    resultado = validar_cpf("1234567890")
    assert resultado == False


def test_cpf_com_pontuacao():
    resultado = validar_cpf("123.456.789-09")
    assert resultado == False


def test_cpf_letras():
    resultado = validar_cpf("abcdefghijk")
    assert resultado == False


def test_cpf_repetido():
    resultado = validar_cpf("11111111111")
    assert resultado == True


def test_cpf_vazio():
    resultado = validar_cpf("")
    assert resultado == False