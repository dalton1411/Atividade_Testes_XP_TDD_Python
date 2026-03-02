def calcular_imc(peso: float, altura: float):
    if peso <= 0 or altura <= 0:
        return None

    return peso / altura ** 2