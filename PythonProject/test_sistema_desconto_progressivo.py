
from sistema_desconto_progressivo import calcular_troco

def test_troco_50():
    assert calcular_troco(50, 100) == {50: 1}

def test_troco_20():
    assert calcular_troco(30, 50) == {20: 1}

def test_troco_7():
    assert calcular_troco(43, 50) == {5: 1, 2: 1}

def test_troco_250():
    assert calcular_troco(47.50, 50) == {2: 1, 0.50: 1}

