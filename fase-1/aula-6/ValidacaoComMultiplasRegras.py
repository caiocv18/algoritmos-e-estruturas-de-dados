def validar_pedido(itens, endereco, forma_pagamento, cupom=None):
    erros = []
    
    # Validação de itens
    if not itens:
        erros.append("O pedido deve conter pelo menos um item")
    
    valor_total = sum(item["preco"] * item["quantidade"] for item in itens)
    
    # Validação de valor mínimo
    if valor_total < 30:
        erros.append("O valor mínimo para pedidos é R$ 30,00")
    
    # Validação de endereço
    campos_obrigatorios = ["rua", "numero", "bairro", "cidade", "estado", "cep"]
    for campo in campos_obrigatorios:
        if campo not in endereco or not endereco[campo]:
            erros.append(f"Campo '{campo}' do endereço é obrigatório")
    
    # Validação de forma de pagamento
    formas_aceitas = ["credito", "debito", "pix", "boleto"]
    if forma_pagamento not in formas_aceitas:
        erros.append(f"Forma de pagamento deve ser uma das seguintes: {', '.join(formas_aceitas)}")
    
    # Validação de cupom
    if cupom:
        # Simulação de verificação de cupom válido em um banco de dados
        cupons_validos = ["PRIMEIRA10", "DESCONTO20", "FRETE0"]
        if cupom not in cupons_validos:
            erros.append("Cupom inválido")
    
    # Verificação final
    if erros:
        return False, erros
    else:
        return True, "Pedido válido"