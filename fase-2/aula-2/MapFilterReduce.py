# MAP - Aplica função a cada elemento
numeros = [1, 2, 3, 4, 5]

# Método tradicional
quadrados_tradicional = []
for num in numeros:
    quadrados_tradicional.append(num ** 2)

# Com map
quadrados_map = list(map(lambda x: x ** 2, numeros))
print(f"Quadrados: {quadrados_map}")

# Map com função nomeada
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

temperaturas_celsius = [0, 10, 20, 30, 40]
temperaturas_fahrenheit = list(map(celsius_para_fahrenheit, temperaturas_celsius))
print(f"Temperaturas em Fahrenheit: {temperaturas_fahrenheit}")

# FILTER - Filtra elementos baseado em condição
numeros = range(1, 21)

# Números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares: {pares}")

# Exemplo prático - Filtrar produtos
produtos = [
    {"nome": "Notebook", "preco": 3000, "estoque": 5},
    {"nome": "Mouse", "preco": 50, "estoque": 0},
    {"nome": "Teclado", "preco": 150, "estoque": 10},
    {"nome": "Monitor", "preco": 800, "estoque": 0}
]

# Produtos em estoque
em_estoque = list(filter(lambda p: p["estoque"] > 0, produtos))
print("\nProdutos em estoque:")
for produto in em_estoque:
    print(f"  {produto['nome']}: {produto['estoque']} unidades")

# Produtos caros (acima de R$ 500)
produtos_caros = list(filter(lambda p: p["preco"] > 500, produtos))
print("\nProdutos acima de R$ 500:")
for produto in produtos_caros:
    print(f"  {produto['nome']}: R$ {produto['preco']}")

# REDUCE - Reduz sequência a um valor único
from functools import reduce

# Soma acumulada
numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(f"\nSoma de {numeros}: {soma}")

# Produto acumulado
produto = reduce(lambda x, y: x * y, numeros)
print(f"Produto de {numeros}: {produto}")

# Exemplo prático - Calcular total de vendas
vendas = [
    {"valor": 100},
    {"valor": 250},
    {"valor": 175},
    {"valor": 300}
]

total_vendas = reduce(
    lambda total, venda: total + venda["valor"],
    vendas,
    0# Valor inicial
)
print(f"\nTotal de vendas: R$ {total_vendas}")

# Combinando map, filter e reduce# Calcular média de números pares em uma lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Filtrar pares
pares = filter(lambda x: x % 2 == 0, numeros)

# 2. Elevar ao quadrado
quadrados = map(lambda x: x ** 2, pares)

# 3. Converter para lista para usar len()
quadrados_lista = list(quadrados)

# 4. Calcular soma e média
if quadrados_lista:
    soma = reduce(lambda x, y: x + y, quadrados_lista)
    media = soma / len(quadrados_lista)
    print(f"\nQuadrados dos pares: {quadrados_lista}")
    print(f"Média: {media}")