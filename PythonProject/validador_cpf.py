def validar_cpf(cpf: str) -> bool:
    if len(cpf) != 11:
        return False
    
    for caractere in cpf:
        if not caractere.isdigit():
            return False

    return True
