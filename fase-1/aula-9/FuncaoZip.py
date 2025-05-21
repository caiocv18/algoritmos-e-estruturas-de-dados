nomes = ["Ana", "Bruno", "Carlos"]
idades = [25, 32, 18]
cidades = ["São Paulo", "Rio de Janeiro", "Brasília"]

# Iterando três listas em paralelo
for nome, idade, cidade in zip(nomes, idades, cidades):
    print(f"{nome} tem {idade} anos e mora em {cidade}")