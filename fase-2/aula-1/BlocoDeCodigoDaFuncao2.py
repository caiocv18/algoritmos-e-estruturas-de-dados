def analisar_vendas():
    """Analisa vendas e gera estatísticas."""
# Variáveis locais
    vendas = [150, 200, 175, 300, 225]

# Estruturas condicionais
    if len(vendas) > 0:
        total = sum(vendas)
        media = total / len(vendas)

# Loops
        print("Vendas diárias:")
        for i, venda in enumerate(vendas, 1):
            print(f"  Dia {i}: R$ {venda}")

        print(f"\nTotal: R$ {total}")
        print(f"Média: R$ {media:.2f}")
    else:
        print("Nenhuma venda registrada.")

analisar_vendas()