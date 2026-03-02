def converter_temperatura(valor: float, origem: str, destino: str) -> float:
    origem = origem.upper()
    destino = destino.upper()

    if origem not in ("C", "F") or destino not in ("C", "F"):
        raise ValueError("Unidade inválida. Use 'C' ou 'F'.")

    if origem == destino:
        return valor

    if origem == "C" and destino == "F":
        return round((valor * 9 / 5) + 32, 2)

    if origem == "F" and destino == "C":
        return round((valor - 32) * 5 / 9, 2)