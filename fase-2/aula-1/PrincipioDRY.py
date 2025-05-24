# Com funções - código DRY
def calcular_preco_com_desconto(preco_original, numero_cliente):
    """Calcula e exibe o preço com desconto se aplicável."""
    print(f"=== Cálculo de Preço com Desconto - Cliente {numero_cliente} ===")

    if preco_original > 50:
        desconto = preco_original * 0.10
        preco_final = preco_original - desconto
        print(f"Preço original: R$ {preco_original:.2f}")
        print(f"Desconto aplicado: R$ {desconto:.2f}")
        print(f"Preço final: R$ {preco_final:.2f}")
    else:
        print(f"Preço: R$ {preco_original:.2f} (sem desconto)")
    print()

# Usando a função
calcular_preco_com_desconto(100.00, 1)
calcular_preco_com_desconto(75.00, 2)
calcular_preco_com_desconto(30.00, 3)