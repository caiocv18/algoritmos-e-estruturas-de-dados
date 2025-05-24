def calcular_desconto_progressivo(valor_compra):
    """
    Calcula desconto progressivo baseado no valor da compra.

    Regras:
    - Até R$ 100: sem desconto
    - R$ 100-500: 5% de desconto
    - R$ 500-1000: 10% de desconto
    - Acima de R$ 1000: 15% de desconto
    """
    if valor_compra <= 100:
        percentual = 0
    elif valor_compra <= 500:
        percentual = 5
    elif valor_compra <= 1000:
        percentual = 10
    else:
        percentual = 15

    desconto = valor_compra * (percentual / 100)
    valor_final = valor_compra - desconto

    print(f"Valor original: R$ {valor_compra:.2f}")
    print(f"Desconto ({percentual}%): R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print("-" * 30)

# Testando diferentes valores
calcular_desconto_progressivo(50)
calcular_desconto_progressivo(250)
calcular_desconto_progressivo(750)
calcular_desconto_progressivo(1500)