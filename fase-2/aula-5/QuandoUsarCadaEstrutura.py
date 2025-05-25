import random

# QUANDO USAR LISTAS:

# 1. Quando os dados precisam ser modificados
carrinho_compras = []
carrinho_compras.append("Notebook")
carrinho_compras.append("Mouse")
carrinho_compras.remove("Mouse")  # Modificação permitida

# 2. Quando o tamanho da coleção varia
numeros_aleatorios = []
for _ in range(random.randint(5, 15)):
    numeros_aleatorios.append(random.randint(1, 100))

# 3. Quando você precisa de métodos como sort(), reverse(), etc.
notas = [8.5, 7.0, 9.2, 6.5]
notas.sort()  # Modifica a lista in-place

# QUANDO USAR TUPLAS:

# 1. Quando os dados são constantes/imutáveis
DIAS_SEMANA = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
COORDENADAS_ORIGEM = (0, 0)
CONFIG_SERVIDOR = ('localhost', 8080, 'https')

# 2. Quando você precisa usar como chave de dicionário
cache_pontos = {}
ponto1 = (10, 20)
ponto2 = (30, 40)
cache_pontos[ponto1] = "Dados do ponto 1"
cache_pontos[ponto2] = "Dados do ponto 2"

# 3. Quando retornando múltiplos valores de função
def calcular_estatisticas(numeros):
    return (min(numeros), max(numeros), sum(numeros) / len(numeros))

minimo, maximo, media = calcular_estatisticas([1, 2, 3, 4, 5])