# Versão NÃO otimizada
def calcular_soma_e_media_v1(numeros):
    soma = 0
    for num in numeros: # O(n)
        soma += num

    contagem = 0
    for _ in numeros: # O(n) de novo!
        contagem += 1

    if contagem == 0:
        return 0, 0
    media = soma / contagem
    return soma, media