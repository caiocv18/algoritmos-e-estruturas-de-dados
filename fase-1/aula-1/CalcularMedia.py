def calcular_media(valores):
    soma = sum(valores)
    media = soma / len(valores)
    return media

# Exemplo de uso
notas = [7.5, 8.0, 6.5, 9.0]
media_final = calcular_media(notas)
print(f"A média final é: {media_final}")
