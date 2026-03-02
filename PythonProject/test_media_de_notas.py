from media_de_notas import calcular_media

def test_media_valores_inteiros():
    assert calcular_media([7, 8, 9]) == 8.0

def test_media_mistos():
    assert calcular_media([10, 5, 6]) == 7.0

def test_ignora_invalidos():
    assert calcular_media([7, 8, -1, 9]) == 8.0

def test_todos_invalidos():
    assert calcular_media([11, 12]) is None

def test_lista_vazia():
    assert calcular_media([]) is None

def test_valores_decimais():
    assert calcular_media([7.5, 8.5, 9.5]) == 8.5