def verificar_primo(numero):
    """
    Verifica se um número é primo.

    Parâmetros:
        numero (int): O número a ser verificado

    Retorno:
        bool: True se o número for primo, False caso contrário
    """
    # Tratar casos especiais
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    # Verificar divisibilidade por números da forma 6k±1
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True
