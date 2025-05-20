def categorizar_risco_credito(idade, renda, historico_credito, tempo_emprego):
    """
    Determina a categoria de risco de crédito com base em diversos fatores.
    """
    # Definição de pontos para cada fator
    pontos = 0
    
    # Idade
    if idade < 25:
        pontos += 1
    elif idade < 35:
        pontos += 2
    elif idade < 50:
        pontos += 3
    else:
        pontos += 2
    
    # Renda
    if renda < 3000:
        pontos += 1
    elif renda < 5000:
        pontos += 2
    elif renda < 10000:
        pontos += 3
    else:
        pontos += 4
    
    # Histórico de crédito
    if historico_credito == "ruim":
        pontos += 0
    elif historico_credito == "regular":
        pontos += 2
    elif historico_credito == "bom":
        pontos += 4
    else:  # "excelente"
        pontos += 5
    
    # Tempo de emprego
    if tempo_emprego < 1:
        pontos += 1
    elif tempo_emprego < 3:
        pontos += 2
    elif tempo_emprego < 5:
        pontos += 3
    else:
        pontos += 4
    
    # Determinação da categoria com base no total de pontos
    if pontos <= 6:
        categoria = "alto risco"
    elif pontos <= 10:
        categoria = "médio risco"
    elif pontos <= 14:
        categoria = "baixo risco"
    else:
        categoria = "risco mínimo"
    
    return {
        "pontos": pontos,
        "categoria": categoria,
        "taxa_juros_recomendada": obter_taxa_juros(pontos)
    }

def obter_taxa_juros(pontos):
    """Determina a taxa de juros com base na pontuação de crédito."""
    # Tabela de taxas de juros por faixa de pontuação
    tabela_taxas = {
        range(0, 7): 28.5,    # 0-6 pontos
        range(7, 11): 22.0,   # 7-10 pontos
        range(11, 15): 18.0,  # 11-14 pontos
        range(15, 21): 14.5   # 15-20 pontos
    }
    
    # Busca na tabela a faixa que contém a pontuação
    for faixa, taxa in tabela_taxas.items():
        if pontos in faixa:
            return taxa
    
    # Valor padrão caso não encontre (não deveria ocorrer)
    return 30.0