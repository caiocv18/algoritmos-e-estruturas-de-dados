números = [1, 2, 3, 4, 5]
soma = 0

for número in números:
    dobro = número * 2
    soma += dobro
    print(f"O dobro de {número} é {dobro}")

print(f"A soma dos dobros é {soma}")