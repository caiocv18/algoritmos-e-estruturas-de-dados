def calcular_pontuacao_credito(renda, historico, tempo_emprego, bens):
    pontuacao = 0
    
    # Acumulando pontos com base em várias condições
    if renda > 5000:
        pontuacao += 30
    elif renda > 3000:
        pontuacao += 20
    else:
        pontuacao += 10
    
    if historico == "bom":
        pontuacao += 30
    elif historico == "regular":
        pontuacao += 15
    else:
        pontuacao += 0
    
    if tempo_emprego > 5:
        pontuacao += 20
    elif tempo_emprego > 2:
        pontuacao += 10
    else:
        pontuacao += 5
    
    if bens > 100000:
        pontuacao += 20
    else:
        pontuacao += bens // 10000  # 1 ponto para cada R$ 10.000 em bens
    
    return pontuacao