def calcular_preco_final():
    # Entrada
    valor, categoria, tipo_cliente = obter_dados_compra()
    
    # Validação
    valido, mensagem = validar_dados(valor, categoria, tipo_cliente)
    if not valido:
        print(f"Erro: {mensagem}")
        return
    
    # Processamento (cálculos de desconto)
    desconto = calcular_desconto_base(valor)
    desconto = ajustar_por_categoria(desconto, categoria)
    desconto = ajustar_por_cliente(desconto, tipo_cliente)
    preco_final = valor * (1 - desconto)
    
    # Saída
    exibir_resultado(valor, desconto, preco_final)