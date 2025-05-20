def verificar_elegibilidade_emprestimo():
    """
    Verifica a elegibilidade para empréstimo com base em diversos critérios.
    """
    print("\n===== VERIFICADOR DE ELEGIBILIDADE PARA EMPRÉSTIMO =====\n")

# Coleta de dados
    try:
        nome = input("Nome do solicitante: ").strip()
        idade = int(input("Idade: "))
        renda_mensal = float(input("Renda mensal (R$): "))
        valor_emprestimo = float(input("Valor do empréstimo solicitado (R$): "))
        prazo_meses = int(input("Prazo para pagamento (meses): "))
        score_credito = int(input("Score de crédito (0-1000): "))
        possui_restricao = input("Possui restrição de crédito? (s/n): ").lower() == 's'

    except ValueError:
        print("Erro: Dados inválidos. Por favor, tente novamente.")
        return None

# Cálculos preliminares
    comprometimento_renda = (valor_emprestimo / prazo_meses) / renda_mensal
    risco = avaliar_risco(idade, score_credito, comprometimento_renda, possui_restricao)

# Análise de elegibilidade
    motivos_recusa = []

    if idade < 18:
        motivos_recusa.append("Idade menor que 18 anos")

    if idade > 65:
        motivos_recusa.append("Idade maior que 65 anos")

    if renda_mensal < 1000:
        motivos_recusa.append("Renda mensal insuficiente")

    if comprometimento_renda > 0.3:
        motivos_recusa.append("Comprometimento de renda superior a 30%")

    if score_credito < 500:
        motivos_recusa.append("Score de crédito muito baixo")

    if possui_restricao:
        motivos_recusa.append("Possui restrição de crédito")

    if valor_emprestimo > renda_mensal * 10:
        motivos_recusa.append("Valor do empréstimo superior a 10x a renda mensal")

# Determinação do resultado
    if motivos_recusa:
        elegivel = False
        taxa_juros = None
    else:
        elegivel = True
# Taxa de juros baseada no risco
        if risco == "Baixo":
            taxa_juros = 0.015# 1.5% ao mês
        elif risco == "Médio":
            taxa_juros = 0.025# 2.5% ao mês
        else:# Alto
            taxa_juros = 0.035# 3.5% ao mês

# Apresentação dos resultados
    print("\n" + "=" * 50)
    print(f"RESULTADO DA ANÁLISE PARA {nome.upper()}")
    print("=" * 50)

    print(f"Valor solicitado: R$ {valor_emprestimo:.2f}")
    print(f"Prazo: {prazo_meses} meses")
    print(f"Comprometimento de renda: {comprometimento_renda*100:.1f}%")
    print(f"Nível de risco: {risco}")

    if elegivel:
        montante_total = valor_emprestimo * (1 + taxa_juros) ** prazo_meses
        parcela_mensal = montante_total / prazo_meses

        print("\nRESULTADO: EMPRÉSTIMO APROVADO")
        print(f"Taxa de juros: {taxa_juros*100:.1f}% ao mês")
        print(f"Parcela mensal: R$ {parcela_mensal:.2f}")
        print(f"Montante total: R$ {montante_total:.2f}")
        print(f"Custo do empréstimo: R$ {montante_total - valor_emprestimo:.2f}")
    else:
        print("\nRESULTADO: EMPRÉSTIMO NEGADO")
        print("Motivos da recusa:")
        for motivo in motivos_recusa:
            print(f"- {motivo}")

# Recomendações condicionais
        print("\nRECOMENDAÇÕES:")

        if "Renda mensal insuficiente" in motivos_recusa or "Comprometimento de renda superior a 30%" in motivos_recusa:
            print("- Considere solicitar um empréstimo de menor valor")
            print("- Aumente o prazo do empréstimo para reduzir o comprometimento mensal")

        if "Score de crédito muito baixo" in motivos_recusa:
            print("- Trabalhe para melhorar seu score de crédito:")
            print("  * Pague suas contas em dia")
            print("  * Reduza o uso do limite de cartões de crédito")
            print("  * Evite realizar muitas consultas de crédito")

        if "Possui restrição de crédito" in motivos_recusa:
            print("- Regularize pendências financeiras antes de solicitar um empréstimo")

    return elegivel, motivos_recusa

def avaliar_risco(idade, score_credito, comprometimento_renda, possui_restricao):
    """
    Avalia o nível de risco do solicitante.
    """
    if possui_restricao:
        return "Alto"

# Pontuação baseada em critérios
    pontuacao = 0

# Idade
    if idade < 25 or idade > 60:
        pontuacao += 2
    elif idade < 30 or idade > 50:
        pontuacao += 1

# Score de crédito
    if score_credito >= 800:
        pontuacao += 0
    elif score_credito >= 700:
        pontuacao += 1
    elif score_credito >= 600:
        pontuacao += 2
    else:
        pontuacao += 3

# Comprometimento de renda
    if comprometimento_renda > 0.25:
        pontuacao += 2
    elif comprometimento_renda > 0.15:
        pontuacao += 1

# Classificação final
    if pontuacao <= 2:
        return "Baixo"
    elif pontuacao <= 4:
        return "Médio"
    else:
        return "Alto"

# Execução do programa
if __name__ == "__main__":
    verificar_elegibilidade_emprestimo()