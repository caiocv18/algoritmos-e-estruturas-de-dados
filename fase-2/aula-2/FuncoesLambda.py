# Sintaxe: lambda argumentos: expressão
quadrado = lambda x: x ** 2
print(f"Quadrado de 5: {quadrado(5)}")

# Comparando com função normal
def quadrado_normal(x):
    return x ** 2

# Lambdas são úteis como argumentos
numeros = [1, 2, 3, 4, 5]

# Ordenação customizada
pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 30},
    {"nome": "Carlos", "idade": 20}
]

# Ordenar por idade
pessoas_por_idade = sorted(pessoas, key=lambda p: p["idade"])
print("Ordenado por idade:")
for pessoa in pessoas_por_idade:
    print(f"  {pessoa['nome']}: {pessoa['idade']} anos")

# Ordenar por nome
pessoas_por_nome = sorted(pessoas, key=lambda p: p["nome"])
print("\nOrdenado por nome:")
for pessoa in pessoas_por_nome:
    print(f"  {pessoa['nome']}: {pessoa['idade']} anos")

# Exemplo prático - Processamento de dados
vendas = [
    {"produto": "Notebook", "preco": 3000, "quantidade": 2},
    {"produto": "Mouse", "preco": 50, "quantidade": 10},
    {"produto": "Teclado", "preco": 150, "quantidade": 5}
]

# Calcular total de cada venda
vendas_com_total = list(map(
    lambda v: {**v, "total": v["preco"] * v["quantidade"]},
    vendas
))

print("\nVendas com totais:")
for venda in vendas_com_total:
    print(f"  {venda['produto']}: R$ {venda['total']}")

# Operações matemáticas com lambdas
operacoes = {
    "somar": lambda x, y: x + y,
    "subtrair": lambda x, y: x - y,
    "multiplicar": lambda x, y: x * y,
    "dividir": lambda x, y: x / y if y != 0 else "Erro: divisão por zero"
}

# Calculadora simples
a, b = 10, 3
for nome, operacao in operacoes.items():
    resultado = operacao(a, b)
    print(f"{nome}({a}, {b}) = {resultado}")