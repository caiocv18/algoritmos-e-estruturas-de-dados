# Lista de frutas
frutas = ["Banana", "Laranja", "Maçã", "Uva", "Pera"]
chave = "Maçã"
encontrado = False
posicao_encontrada = -1 # Usamos -1 para indicar que ainda não foi encontrado

# Percorrendo a lista
for i in range(len(frutas)):
  if frutas[i] == chave:
    encontrado = True
    posicao_encontrada = i
    break # Para a busca assim que encontrar

# Verificando o resultado
if encontrado:
  print(f"A fruta '{chave}' foi encontrada na posição {posicao_encontrada}.")
else:
  print(f"A fruta '{chave}' não foi encontrada na lista.")