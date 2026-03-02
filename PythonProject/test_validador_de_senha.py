from validar_senha import validar_senha

def test_senha_valida():
    assert validar_senha("Abc12345") is True

def test_sem_maiuscula():
    assert validar_senha("abc12345") is False

def test_sem_minuscula():
    assert validar_senha("ABC12345") is False

def test_sem_numero():
    assert validar_senha("Abcdefgh") is False

def test_menos_de_8():
    assert validar_senha("Ab1") is False

def test_senha_valida_maior():
    assert validar_senha("Abc123456") is True

def test_string_vazia():
    assert validar_senha("") is False