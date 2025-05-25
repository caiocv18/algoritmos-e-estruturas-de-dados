nomes = ["Ana", "Bruno", "Carlos"]
idades = [25, 30, 22]
cidades = ["SP", "RJ", "BH"]

for nome, idade, cidade in zip(nomes, idades, cidades):
    print(f"{nome}, {idade} anos, mora em {cidade}")

# Criando dicionário a partir de listas
pessoas = dict(zip(nomes, idades))
print(pessoas)  # {'Ana': 25, 'Bruno': 30, 'Carlos': 22}
