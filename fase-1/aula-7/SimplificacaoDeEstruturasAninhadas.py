# Código original com estruturas aninhadas complexas
def validar_pagamento_original(pagamento):
    if pagamento["status"] == "aguardando":
        if pagamento["metodo"] == "cartao":
            if pagamento["cartao"]["validade"] > "2023-12":
                if pagamento["valor"] <= pagamento["cartao"]["limite"]:
                    if pagamento["cartao"]["verificado"]:
                        return {"aprovado": True, "mensagem": "Pagamento aprovado"}
                    else:
                        return {"aprovado": False, "mensagem": "Cartão não verificado"}
                else:
                    return {"aprovado": False, "mensagem": "Valor excede o limite do cartão"}
            else:
                return {"aprovado": False, "mensagem": "Cartão expirado"}
        elif pagamento["metodo"] == "boleto":
            if pagamento["boleto"]["data_vencimento"] > "2023-07-15":
                return {"aprovado": True, "mensagem": "Aguardando pagamento do boleto"}
            else:
                return {"aprovado": False, "mensagem": "Boleto vencido"}
        else:
            return {"aprovado": False, "mensagem": "Método de pagamento não suportado"}
    else:
        return {"aprovado": False, "mensagem": "Status de pagamento inválido"}

# Versão refatorada usando early returns
def validar_pagamento_refatorado(pagamento):
    # Verificações iniciais
    if pagamento["status"] != "aguardando":
        return {"aprovado": False, "mensagem": "Status de pagamento inválido"}
    
    # Verificação de método de pagamento
    metodo = pagamento["metodo"]
    if metodo not in ["cartao", "boleto"]:
        return {"aprovado": False, "mensagem": "Método de pagamento não suportado"}
    
    # Validação específica para cartão
    if metodo == "cartao":
        cartao = pagamento["cartao"]
        
        # Verificações sequenciais com early returns
        if cartao["validade"] <= "2023-12":
            return {"aprovado": False, "mensagem": "Cartão expirado"}
        
        if pagamento["valor"] > cartao["limite"]:
            return {"aprovado": False, "mensagem": "Valor excede o limite do cartão"}
        
        if not cartao["verificado"]:
            return {"aprovado": False, "mensagem": "Cartão não verificado"}
        
        return {"aprovado": True, "mensagem": "Pagamento aprovado"}
    
    # Validação específica para boleto
    if pagamento["boleto"]["data_vencimento"] <= "2023-07-15":
        return {"aprovado": False, "mensagem": "Boleto vencido"}
    
    return {"aprovado": True, "mensagem": "Aguardando pagamento do boleto"}