def verificar_meta_produto(vendas_produto, meta):
    if vendas_produto >= meta:
        return "Meta Atingida"
    else:
        return "Meta Não Atingida"