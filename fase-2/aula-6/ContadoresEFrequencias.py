# Contando ocorrências
texto = "hello world"
frequencia = {}

for letra in texto:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1
