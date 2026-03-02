def definir_maior(primeiro: int, segundo: int, terceiro: int):
    if primeiro >= segundo and primeiro >= terceiro:
        return primeiro
    elif segundo >= primeiro and segundo >= terceiro:
        return segundo
    else:
        return terceiro