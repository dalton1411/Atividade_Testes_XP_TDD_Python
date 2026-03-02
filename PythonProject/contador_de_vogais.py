def contador_de_vogais(palavra: str) -> int:
    resultado = 0
    for letra in palavra.lower():
        if letra in "aeiouáéíóú":
            resultado += 1
    return resultado

