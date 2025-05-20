# Exemplo de código com repetição
def calcular_imposto_ruim(valor_produto, categoria, estado):
    if categoria == "eletrônicos":
        if estado == "SP":
            imposto = valor_produto * 0.18
        elif estado == "RJ":
            imposto = valor_produto * 0.20
        elif estado == "MG":
            imposto = valor_produto * 0.17
        else:
            imposto = valor_produto * 0.15
    elif categoria == "vestuário":
        if estado == "SP":
            imposto = valor_produto * 0.12
        elif estado == "RJ":
            imposto = valor_produto * 0.15
        elif estado == "MG":
            imposto = valor_produto * 0.10
        else:
            imposto = valor_produto * 0.08
    else:
        if estado == "SP":
            imposto = valor_produto * 0.10
        elif estado == "RJ":
            imposto = valor_produto * 0.12
        elif estado == "MG":
            imposto = valor_produto * 0.08
        else:
            imposto = valor_produto * 0.05
    
    return imposto

# Versão melhorada usando o princípio DRY
def calcular_imposto_bom(valor_produto, categoria, estado):
    # Tabela de alíquotas por categoria e estado
    aliquotas = {
        "eletrônicos": {"SP": 0.18, "RJ": 0.20, "MG": 0.17, "default": 0.15},
        "vestuário": {"SP": 0.12, "RJ": 0.15, "MG": 0.10, "default": 0.08},
        "default": {"SP": 0.10, "RJ": 0.12, "MG": 0.08, "default": 0.05}
    }
    
    # Obtém a alíquota correta ou usa valor padrão se não encontrada
    categoria_aliquotas = aliquotas.get(categoria, aliquotas["default"])
    aliquota = categoria_aliquotas.get(estado, categoria_aliquotas["default"])
    
    # Cálculo do imposto
    imposto = valor_produto * aliquota
    
    return imposto