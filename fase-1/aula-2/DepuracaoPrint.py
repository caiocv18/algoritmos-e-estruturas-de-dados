def calcular_media(valores):
    print(f"Valores recebidos: {valores}")
    soma = sum(valores)
    print(f"Soma: {soma}")
    media = soma / len(valores)
    print(f"Média calculada: {media}")
    return media