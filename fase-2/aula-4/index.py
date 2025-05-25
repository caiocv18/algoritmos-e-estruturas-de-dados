cores = ["vermelho", "verde", "azul", "verde"]
posicao = cores.index("verde")
print(posicao)  # 1 (primeira ocorrência)

# Com limites de busca
posicao2 = cores.index("verde", 2)  # Busca a partir do índice 2
print(posicao2)  # 3

# Tratando elementos não encontrados
try:
    pos = cores.index("amarelo")
except ValueError:
    print("Cor não encontrada")