def tabuada(numero: int):
    if numero <= 0 or numero >= 10:
        return None

    resultado = []

    for i in range(1, 11):
        resultado.append(numero * i)

    return resultado
