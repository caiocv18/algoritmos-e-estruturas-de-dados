def calcular_preco_final(preco_base, desconto_percentual=0, taxa_entrega=10.0, cupom=None):
    """
    Calcula o preço final de um produto com descontos e taxas.

    Args:
        preco_base: Preço original do produto
        desconto_percentual: Desconto em % (padrão: 0)
        taxa_entrega: Taxa de entrega (padrão: R$ 10.00)
        cupom: Código do cupom de desconto (padrão: None)
    """
# Aplica desconto percentual
    desconto = preco_base * (desconto_percentual / 100)
    preco_com_desconto = preco_base - desconto

# Aplica cupom se fornecido
    cupons_validos = {
        "PRIMEIRA10": 10.0,
        "BLACKFRIDAY": 20.0,
        "FRETEGRATIS": -taxa_entrega
    }

    desconto_cupom = 0
    if cupom in cupons_validos:
        if cupom == "FRETEGRATIS":
            taxa_entrega = 0
            print(f"Cupom '{cupom}' aplicado: Frete grátis!")
        else:
            desconto_cupom = cupons_validos[cupom]
            preco_com_desconto -= desconto_cupom
            print(f"Cupom '{cupom}' aplicado: -R$ {desconto_cupom:.2f}")

# Calcula total
    total = preco_com_desconto + taxa_entrega

    print(f"\nResumo do pedido:")
    print(f"Preço original: R$ {preco_base:.2f}")
    if desconto > 0:
        print(f"Desconto ({desconto_percentual}%): -R$ {desconto:.2f}")
    if desconto_cupom > 0:
        print(f"Cupom de desconto: -R$ {desconto_cupom:.2f}")
    print(f"Taxa de entrega: R$ {taxa_entrega:.2f}")
    print(f"Total: R$ {total:.2f}")

    return total

# Testando diferentes combinações
calcular_preco_final(100)# Apenas preço base
calcular_preco_final(100, 10)# Com 10% de desconto
calcular_preco_final(100, cupom="PRIMEIRA10")# Com cupom
calcular_preco_final(100, 15, 5.0, "BLACKFRIDAY")# Tudo personalizado