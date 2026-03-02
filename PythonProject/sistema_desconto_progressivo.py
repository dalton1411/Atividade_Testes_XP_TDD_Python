def calcular_troco(valor_compra, valor_pago):
    if valor_compra <= 0 or valor_pago <= 0:
        raise ValueError("Valores devem ser maiores que zero")

    if valor_pago < valor_compra:
        raise ValueError("Valor pago menor que o valor da compra")

    troco = round(valor_pago - valor_compra, 2)

    cedulas_moedas = [100, 50, 20, 10, 5, 2, 1,
                      0.50, 0.25, 0.10, 0.05, 0.01]

    resultado = {}

    for valor in cedulas_moedas:
        quantidade = int(troco // valor)
        if quantidade > 0:
            resultado[valor] = quantidade
            troco = round(troco - quantidade * valor, 2)

    return resultado