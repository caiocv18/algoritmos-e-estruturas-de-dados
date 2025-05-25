# Sistema de vendas simples
vendas = [
    {
        "id": 1,
        "cliente": "João Silva",
        "itens": [
            ("Notebook", 2, 3000.00),  # (produto, quantidade, preço)
            ("Mouse", 1, 50.00)
        ],
        "data": "2024-01-15"
    },
    {
        "id": 2,
        "cliente": "Maria Santos",
        "itens": [
            ("Teclado", 2, 150.00)
        ],
        "data": "2024-01-16"
    }
]

# Calculando total de uma venda
venda = vendas[0]
total = sum(qtd * preco for _, qtd, preco in venda["itens"])
print(f"Total da venda {venda['id']}: R$ {total:.2f}")
