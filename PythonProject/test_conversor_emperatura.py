from conversor_temperatura import converter_temperatura


def test_0_c_para_f():
    assert converter_temperatura(0, "C", "F") == 32


def test_100_c_para_f():
    assert converter_temperatura(100, "C", "F") == 212


def test_32_f_para_c():
    assert converter_temperatura(32, "F", "C") == 0


def test_212_f_para_c():
    assert converter_temperatura(212, "F", "C") == 100


def test_menos_40():
    assert converter_temperatura(-40, "C", "F") == -40



