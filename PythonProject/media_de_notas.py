def calcular_media(notas):
    if not notas:
        return None

    notas_validas = [n for n in notas if 0 <= n <= 10]

    if not notas_validas:
        return None

    return sum(notas_validas) / len(notas_validas)