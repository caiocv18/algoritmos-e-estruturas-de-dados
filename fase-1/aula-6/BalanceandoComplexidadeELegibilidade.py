# Versão muito simplificada - difícil de entender a lógica
def verificar_elegibilidade_simples(renda, score, idade, historico):
    return renda >= 3000 and score >= 700 and (idade >= 21 and idade <= 65) and historico != "negativo"

# Versão muito detalhada - verbosa e repetitiva
def verificar_elegibilidade_verbosa(renda, score, idade, historico):
    if renda < 3000:
        print("Renda insuficiente. Mínimo necessário: R$ 3.000,00")
        return False
    
    if score < 700:
        print("Score de crédito insuficiente. Mínimo necessário: 700")
        return False
    
    if idade < 21:
        print("Idade mínima não atingida. Mínimo necessário: 21 anos")
        return False
        
    if idade > 65:
        print("Idade máxima excedida. Máximo permitido: 65 anos")
        return False
    
    if historico == "negativo":
        print("Histórico de crédito negativo")
        return False
    
    print("Cliente elegível!")
    return True

# Versão balanceada - legível e concisa
def verificar_elegibilidade_balanceada(renda, score, idade, historico):
    # Lista para armazenar os motivos de rejeição
    motivos_rejeicao = []
    
    # Verificação dos critérios
    if renda < 3000:
        motivos_rejeicao.append("Renda insuficiente")
    
    if score < 700:
        motivos_rejeicao.append("Score de crédito baixo")
    
    if idade < 21 or idade > 65:
        motivos_rejeicao.append("Idade fora do intervalo permitido (21-65)")
    
    if historico == "negativo":
        motivos_rejeicao.append("Histórico de crédito negativo")
    
    # Determinação do resultado
    elegivel = len(motivos_rejeicao) == 0
    
    # Montagem do feedback
    if elegivel:
        return {"elegivel": True, "mensagem": "Cliente elegível para o empréstimo."}
    else:
        return {
            "elegivel": False,
            "mensagem": "Cliente não elegível.",
            "motivos": motivos_rejeicao
        }