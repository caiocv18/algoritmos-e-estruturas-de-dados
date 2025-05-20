# Código original com gargalo condicional
def calcular_desconto_original(cliente, produto, valor_compra):
    # Verificações em cascata, difíceis de manter
    if cliente["tipo"] == "premium":
        if produto["categoria"] == "eletrônicos":
            if valor_compra > 1000:
                desconto = 0.15
            else:
                desconto = 0.10
        elif produto["categoria"] == "vestuário":
            if valor_compra > 500:
                desconto = 0.12
            else:
                desconto = 0.08
        else:
            if valor_compra > 300:
                desconto = 0.10
            else:
                desconto = 0.05
    elif cliente["tipo"] == "regular":
        if produto["categoria"] == "eletrônicos":
            if valor_compra > 1000:
                desconto = 0.10
            else:
                desconto = 0.05
        elif produto["categoria"] == "vestuário":
            if valor_compra > 500:
                desconto = 0.08
            else:
                desconto = 0.05
        else:
            if valor_compra > 300:
                desconto = 0.05
            else:
                desconto = 0.03
    else:  # Novo cliente
        if produto["categoria"] == "eletrônicos":
            if valor_compra > 1000:
                desconto = 0.07
            else:
                desconto = 0.03
        elif produto["categoria"] == "vestuário":
            if valor_compra > 500:
                desconto = 0.05
            else:
                desconto = 0.02
        else:
            if valor_compra > 300:
                desconto = 0.03
            else:
                desconto = 0.01
    
    return valor_compra * desconto

# Versão refatorada usando tabela de decisão
def calcular_desconto_refatorado(cliente, produto, valor_compra):
    # Tabela de descontos por tipo de cliente, categoria e valor
    tabela_descontos = {
        "premium": {
            "eletrônicos": {
                "alto": 0.15,   # Valor > 1000
                "baixo": 0.10   # Valor <= 1000
            },
            "vestuário": {
                "alto": 0.12,   # Valor > 500
                "baixo": 0.08   # Valor <= 500
            },
            "outros": {
                "alto": 0.10,   # Valor > 300
                "baixo": 0.05   # Valor <= 300
            }
        },
        "regular": {
            "eletrônicos": {
                "alto": 0.10,
                "baixo": 0.05
            },
            "vestuário": {
                "alto": 0.08,
                "baixo": 0.05
            },
            "outros": {
                "alto": 0.05,
                "baixo": 0.03
            }
        },
        "novo": {
            "eletrônicos": {
                "alto": 0.07,
                "baixo": 0.03
            },
            "vestuário": {
                "alto": 0.05,
                "baixo": 0.02
            },
            "outros": {
                "alto": 0.03,
                "baixo": 0.01
            }
        }
    }
    
    # Determinação dos fatores de pesquisa
    tipo_cliente = cliente["tipo"]
    categoria = produto["categoria"] if produto["categoria"] in ["eletrônicos", "vestuário"] else "outros"
    
    # Determinação da faixa de valor
    if categoria == "eletrônicos":
        faixa_valor = "alto" if valor_compra > 1000 else "baixo"
    elif categoria == "vestuário":
        faixa_valor = "alto" if valor_compra > 500 else "baixo"
    else:
        faixa_valor = "alto" if valor_compra > 300 else "baixo"
    
    # Consulta à tabela de decisão
    percentual_desconto = tabela_descontos[tipo_cliente][categoria][faixa_valor]
    
    return valor_compra * percentual_desconto