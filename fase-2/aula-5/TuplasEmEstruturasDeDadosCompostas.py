# Lista de tuplas - estrutura comum para dados tabulares
funcionarios = [
    ("Ana Silva", "Desenvolvedora", 8000),
    ("Bruno Costa", "Designer", 6500),
    ("Carlos Lima", "Gerente", 12000),
    ("Diana Santos", "Analista", 7000)
]

# Processando lista de tuplas
print("Relatório de Funcionários:")
for nome, cargo, salario in funcionarios:
    print(f"{nome:20} | {cargo:15} | R$ {salario:8,.2f}")

# Dicionário com tuplas como valores
estoque_produtos = {
    "PRD001": ("Notebook Dell", 3500.00, 15),
    "PRD002": ("Mouse Logitech", 120.00, 50),
    "PRD003": ("Teclado Mecânico", 450.00, 30)
}

# Calculando valor total do estoque
valor_total = 0
for codigo, (nome, preco, quantidade) in estoque_produtos.items():
    valor_produto = preco * quantidade
    valor_total += valor_produto
    print(f"{codigo}: {nome} - R$ {valor_produto:,.2f}")
print(f"\nValor total do estoque: R$ {valor_total:,.2f}")

# Conjunto de tuplas para eliminar duplicatas
transacoes = [
    ("2024-01-01", "Compra", 100),
    ("2024-01-02", "Venda", 150),
    ("2024-01-01", "Compra", 100),  # Duplicata
    ("2024-01-03", "Compra", 200)
]
transacoes_unicas = set(transacoes)
print(f"\nTransações únicas: {len(transacoes_unicas)}")

# Tuplas aninhadas para estruturas hierárquicas
arvore_organizacional = (
    "CEO",
    (
        ("CTO", (("Dev Lead", ("Dev1", "Dev2")), ("QA Lead", ("QA1",)))),
        ("CFO", (("Contador",), ("Analista Financeiro",)))
    )
)

def imprimir_arvore(no, nivel=0):
    """Imprime estrutura hierárquica"""
    if isinstance(no, str):
        print("  " * nivel + no)
    else:
        for item in no:
            imprimir_arvore(item, nivel + 1)

print("\nOrganograma:")
imprimir_arvore(arvore_organizacional)
