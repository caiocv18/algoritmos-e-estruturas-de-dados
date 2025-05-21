# Iteração em duas listas simultaneamente com while
nomes = ["Ana", "Bruno", "Carlos"]
idades = [25, 30, 22]

i = 0
while i < len(nomes) and i < len(idades):
    print(f"{nomes[i]} tem {idades[i]} anos")
    i += 1