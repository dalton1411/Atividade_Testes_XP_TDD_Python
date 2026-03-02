from validador_idade import validar_idade

def test_maior_idade():
    resultado=validar_idade(20)
    assert resultado==True

def test_menor_idade():
    resultado=validar_idade(17)
    assert resultado==False