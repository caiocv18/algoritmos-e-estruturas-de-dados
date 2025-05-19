# Entrada de múltiplos valores em uma linha
entrada = input("Digite três números separados por espaço: ")
numeros = [float(x) for x in entrada.split()]

# Entrada de múltiplos valores com quantidade indeterminada
valores = []
print("Digite os valores (um por linha). Digite 'fim' para terminar:")
while True:
    entrada = input("> ")
    if entrada.lower() == 'fim':
        break
    valores.append(float(entrada))

# Entrada de pares chave-valor
pessoa = {}
campos = ["nome", "idade", "cidade"]
for campo in campos:
    pessoa[campo] = input(f"Digite seu {campo}: ")