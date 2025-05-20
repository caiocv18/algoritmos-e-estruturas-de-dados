def avaliar_candidato(nota_teste, experiencia, formacao, idiomas):
    # Primeira fase: nota de corte no teste
    if nota_teste < 70:
        return "Reprovado na fase de testes"
    
    # Segunda fase: requisitos mínimos
    if experiencia < 2 and formacao != "superior":
        return "Reprovado por requisitos mínimos"
    
    # Terceira fase: classificação
    if idiomas >= 2 and experiencia >= 5:
        classificacao = "Senior"
    elif idiomas >= 1 and experiencia >= 3:
        classificacao = "Pleno"
    else:
        classificacao = "Junior"
    
    # Última fase: decisão salarial
    if classificacao == "Senior":
        faixa_salarial = "R$ 10.000 - R$ 15.000"
    elif classificacao == "Pleno":
        faixa_salarial = "R$ 6.000 - R$ 9.000"
    else:
        faixa_salarial = "R$ 3.000 - R$ 5.000"
    
    return f"Aprovado como {classificacao}. Faixa salarial: {faixa_salarial}"