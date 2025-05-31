def encontrar_max_min_vendas(lista_valores_vendas):
    if not lista_valores_vendas:
        return None, None

    max_venda = lista_valores_vendas[0]
    min_venda = lista_valores_vendas[0]

    for valor in lista_valores_vendas: # Loop 1
        if valor > max_venda:
            max_venda = valor

    for valor in lista_valores_vendas: # Loop 2
        if valor < min_venda:
            min_venda = valor
    return max_venda, min_venda