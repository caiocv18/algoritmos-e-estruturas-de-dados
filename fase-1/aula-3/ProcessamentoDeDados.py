# Algoritmo simples: cálculo de média
def calcular_media(valores):
    """Calcula a média aritmética de uma lista de valores."""
    soma = 0
    contador = 0

    for valor in valores:
        soma += valor
        contador += 1

    return soma / contador if contador > 0 else 0

# Algoritmo: encontrar o maior valor
def encontrar_maior(valores):
    """Encontra o maior valor em uma lista."""
    if not valores:
        return None

    maior = valores[0]
    for valor in valores[1:]:
        if valor > maior:
            maior = valor

    return maior

# Algoritmo: verificar se um número é primo
def eh_primo(numero):
    """Verifica se um número é primo."""
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True