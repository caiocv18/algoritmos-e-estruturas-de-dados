# Evite operações caras dentro de loops
nomes = ["Ana", "Bruno", "Carlos", "Diana"]

# Ineficiente: len() é chamado a cada iteração
for i in range(len(nomes)):
    print(f"Nome {i+1}/{len(nomes)}: {nomes[i]}")

# Otimizado: len() é chamado apenas uma vez
tamanho = len(nomes)
for i in range(tamanho):
    print(f"Nome {i+1}/{tamanho}: {nomes[i]}")

# Concatenação de strings
# Ineficiente: criando nova string a cada iteração
texto = ""
for i in range(1000):
    texto += str(i)

# Otimizado: usando um acumulador de lista e join
partes = []
for i in range(1000):
    partes.append(str(i))
texto = "".join(partes)

# Ou melhor ainda, com compreensão
texto = "".join(str(i) for i in range(1000))