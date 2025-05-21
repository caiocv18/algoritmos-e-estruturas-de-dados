palavra = "Python"
for caractere in palavra:
    print(caractere)

# Contando vogais
vogais = "aeiouAEIOU"
contagem = 0
texto = "Algoritmos e Estruturas de Dados"

for caractere in texto:
    if caractere in vogais:
        contagem += 1

print(f"O texto contém {contagem} vogais")