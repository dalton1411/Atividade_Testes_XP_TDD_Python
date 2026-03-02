from contador_de_vogais import contador_de_vogais

def test_python():
    resultado = contador_de_vogais("python")
    assert resultado == 1


def test_maiusculas():
    resultado = contador_de_vogais("AEIOU")
    assert resultado == 5


def test_sem_vogais():
    resultado = contador_de_vogais("bcdfg")
    assert resultado == 0


def test_ola_mundo():
    resultado = contador_de_vogais("Olá Mundo")
    assert resultado == 4


def test_string_vazia():
    resultado = contador_de_vogais("")
    assert resultado == 0


def test_numeros():
    resultado = contador_de_vogais("123")
    assert resultado == 0