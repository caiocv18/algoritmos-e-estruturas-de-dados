# Calculando média, mínimo e máximo
dados = [14, 8, 23, 5, 19, 36, 12]

soma = 0
mínimo = dados[0]
máximo = dados[0]

for valor in dados:
    soma += valor
    if valor < mínimo:
        mínimo = valor
    if valor > máximo:
        máximo = valor

média = soma / len(dados)
print(f"Média: {média}, Mínimo: {mínimo}, Máximo: {máximo}")

# Contando frequência de elementos
texto = "Algoritmos e Estruturas de Dados"
frequência = {}

for caractere in texto.lower():
    if caractere.isalpha():
        frequência[caractere] = frequência.get(caractere, 0) + 1

# Ordenando por frequência
for caractere, contagem in sorted(frequência.items(), key=lambda x: x[1], reverse=True):
    print(f"'{caractere}': {contagem} vezes")