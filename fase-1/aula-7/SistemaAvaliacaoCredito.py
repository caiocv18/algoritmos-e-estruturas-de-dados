def sistema_avaliacao_credito():
    """
    Sistema simplificado para avaliação de crédito.
    """
    print("\n===== SISTEMA DE AVALIAÇÃO DE CRÉDITO =====")
    print("Bem-vindo ao sistema de análise de crédito.")
    
    # Coleta de dados do solicitante
    dados = coletar_dados_solicitante()
    if not dados:
        return
    
    # Análise de crédito
    resultado = analisar_credito(dados)
    
    # Exibição do resultado
    exibir_resultado_credito(dados, resultado)

def coletar_dados_solicitante():
    """Coleta e valida os dados do solicitante de crédito."""
    print("\n--- Dados do Solicitante ---")
    
    try:
        nome = input("Nome completo: ")
        if not nome.strip():
            print("Erro: Nome não pode estar vazio.")
            return None
        
        # Validação de idade
        try:
            idade = int(input("Idade: "))
            if idade < 18:
                print("Erro: Solicitante deve ser maior de idade.")
                return None
            if idade > 80:
                print("Aviso: Idade acima do comum para solicitação de crédito.")
                confirmacao = input("Deseja continuar? (s/n): ").lower()
                if confirmacao != 's':
                    return None
        except ValueError:
            print("Erro: Idade deve ser um número inteiro.")
            return None
        
        # Validação de renda
        try:
            renda = float(input("Renda mensal (R$): "))
            if renda <= 0:
                print("Erro: Renda deve ser um valor positivo.")
                return None
        except ValueError:
            print("Erro: Renda deve ser um valor numérico.")
            return None
        
        # Histórico de crédito
        print("\nHistórico de crédito:")
        print("1. Excelente")
        print("2. Bom")
        print("3. Regular")
        print("4. Ruim")
        print("5. Inexistente")
        
        historico_opcao = input("Selecione uma opção (1-5): ")
        if not historico_opcao.isdigit() or int(historico_opcao) not in range(1, 6):
            print("Erro: Opção inválida.")
            return None
        
        historicos = ["excelente", "bom", "regular", "ruim", "inexistente"]
        historico = historicos[int(historico_opcao) - 1]
        
        # Tempo de emprego atual
        try:
            tempo_emprego = float(input("Tempo no emprego atual (anos): "))
            if tempo_emprego < 0:
                print("Erro: Tempo de emprego não pode ser negativo.")
                return None
        except ValueError:
            print("Erro: Tempo de emprego deve ser um valor numérico.")
            return None
        
        # Valor solicitado
        try:
            valor_solicitado = float(input("Valor do crédito solicitado (R$): "))
            if valor_solicitado <= 0:
                print("Erro: Valor solicitado deve ser positivo.")
                return None
        except ValueError:
            print("Erro: Valor solicitado deve ser um valor numérico.")
            return None
        
        # Prazo de pagamento
        try:
            prazo = int(input("Prazo para pagamento (meses): "))
            if prazo <= 0:
                print("Erro: Prazo deve ser um valor positivo.")
                return None
            if prazo > 360:  # 30 anos
                print("Aviso: Prazo excepcionalmente longo.")
                confirmacao = input("Deseja continuar? (s/n): ").lower()
                if confirmacao != 's':
                    return None
        except ValueError:
            print("Erro: Prazo deve ser um número inteiro.")
            return None
        
        # Outras informações
        possui_imovel = input("Possui imóvel próprio? (s/n): ").lower() == 's'
        possui_veículo = input("Possui veículo próprio? (s/n): ").lower() == 's'
        
        # Perguntas adicionais para análise
        print("\nPerguntas adicionais:")
        possui_outros_emprestimos = input("Possui outros empréstimos ativos? (s/n): ").lower() == 's'
        
        if possui_outros_emprestimos:
            try:
                valor_parcelas_atuais = float(input("Valor total das parcelas mensais atuais (R$): "))
                if valor_parcelas_atuais < 0:
                    print("Erro: Valor das parcelas não pode ser negativo.")
                    return None
            except ValueError:
                print("Erro: Valor das parcelas deve ser um valor numérico.")
                return None
        else:
            valor_parcelas_atuais = 0
        
        # Montagem dos dados do solicitante
        dados = {
            "nome": nome,
            "idade": idade,
            "renda": renda,
            "historico": historico,
            "tempo_emprego": tempo_emprego,
            "valor_solicitado": valor_solicitado,
            "prazo": prazo,
            "possui_imovel": possui_imovel,
            "possui_veículo": possui_veículo,
            "possui_outros_emprestimos": possui_outros_emprestimos,
            "valor_parcelas_atuais": valor_parcelas_atuais
        }
        
        return dados
        
    except Exception as e:
        print(f"Erro ao coletar dados: {e}")
        return None

def analisar_credito(dados):
    """
    Analisa a solicitação de crédito com base nos dados fornecidos.
    
    Returns:
        dict: Resultado da análise, incluindo aprovação, valor, taxa, etc.
    """
    # Inicialização da pontuação
    pontuacao = 0
    motivos_recusa = []
    observacoes = []
    
    # Análise de renda mínima (3x o salário mínimo)
    salario_minimo = 1320  # Valor fictício para o exemplo
    if dados["renda"] < 3 * salario_minimo:
        motivos_recusa.append("Renda abaixo do mínimo necessário")
    
    # Cálculo da pontuação
    
    # 1. Pontuação por idade
    if dados["idade"] >= 25 and dados["idade"] <= 45:
        pontuacao += 25  # Faixa ideal
    elif dados["idade"] < 25:
        pontuacao += 15  # Jovem, menos estabilidade
    else:
        pontuacao += 20  # Mais velho, maior estabilidade mas maior risco

    # 2. Pontuação por histórico de crédito
    if dados["historico"] == "excelente":
        pontuacao += 30
    elif dados["historico"] == "bom":
        pontuacao += 25
    elif dados["historico"] == "regular":
        pontuacao += 15
    elif dados["historico"] == "ruim":
        pontuacao += 5
        observacoes.append("Histórico de crédito negativo")
    else:  # inexistente
        pontuacao += 10
        observacoes.append("Sem histórico de crédito anterior")
    
    # 3. Pontuação por tempo de emprego
    if dados["tempo_emprego"] >= 5:
        pontuacao += 25  # Estabilidade alta
    elif dados["tempo_emprego"] >= 2:
        pontuacao += 15  # Estabilidade média
    elif dados["tempo_emprego"] >= 1:
        pontuacao += 10  # Estabilidade baixa
    else:
        pontuacao += 5   # Sem estabilidade
        observacoes.append("Pouco tempo no emprego atual")
    
    # 4. Pontuação por bens
    if dados["possui_imovel"]:
        pontuacao += 15
    
    if dados["possui_veículo"]:
        pontuacao += 10
    
    # 5. Relação valor solicitado / renda
    relacao_valor_renda = dados["valor_solicitado"] / (dados["renda"] * dados["prazo"] / 12)
    
    if relacao_valor_renda <= 0.3:
        pontuacao += 20  # Relação excelente
    elif relacao_valor_renda <= 0.5:
        pontuacao += 15  # Relação boa
    elif relacao_valor_renda <= 0.7:
        pontuacao += 10  # Relação aceitável
    elif relacao_valor_renda <= 1.0:
        pontuacao += 5   # Relação arriscada
        observacoes.append("Valor solicitado elevado em relação à renda")
    else:
        pontuacao += 0   # Relação muito arriscada
        motivos_recusa.append("Valor solicitado incompatível com a renda")
    
    # 6. Comprometimento da renda com outros empréstimos
    if dados["possui_outros_emprestimos"]:
        # Calculando a prestação estimada do novo empréstimo (simplificado)
        taxa_mensal = 0.015  # 1.5% ao mês (exemplo)
        prestacao_estimada = dados["valor_solicitado"] * (taxa_mensal * (1 + taxa_mensal) ** dados["prazo"]) / ((1 + taxa_mensal) ** dados["prazo"] - 1)
        
        comprometimento_atual = dados["valor_parcelas_atuais"] / dados["renda"]
        comprometimento_novo = (dados["valor_parcelas_atuais"] + prestacao_estimada) / dados["renda"]
        
        if comprometimento_novo > 0.5:
            motivos_recusa.append("Comprometimento excessivo da renda")
        elif comprometimento_novo > 0.3:
            pontuacao -= 10
            observacoes.append("Alto comprometimento da renda")
    
    # Determinação da aprovação e condições
    aprovado = True
    
    # Verificação de motivos de recusa automática
    if motivos_recusa:
        aprovado = False
    
    # Pontuação mínima para aprovação
    if pontuacao < 60:
        aprovado = False
        motivos_recusa.append(f"Pontuação insuficiente ({pontuacao} pontos, mínimo: 60)")
    
    # Determinação da taxa de juros com base na pontuação
    if pontuacao >= 90:
        taxa_juros = 0.99  # 0.99% a.m.
        classificacao = "Excelente"
    elif pontuacao >= 80:
        taxa_juros = 1.29  # 1.29% a.m.
        classificacao = "Muito Bom"
    elif pontuacao >= 70:
        taxa_juros = 1.59  # 1.59% a.m.
        classificacao = "Bom"
    else:
        taxa_juros = 1.99  # 1.99% a.m.
        classificacao = "Regular"
    
    # Possível redução no valor aprovado
    valor_aprovado = dados["valor_solicitado"]
    if aprovado and relacao_valor_renda > 0.5:
        valor_aprovado = dados["renda"] * 0.5 * (dados["prazo"] / 12)
        observacoes.append(f"Valor aprovado reduzido para adequação à capacidade de pagamento")
    
    # Cálculo da prestação
    taxa_mensal = taxa_juros / 100
    if aprovado:
        prestacao = valor_aprovado * (taxa_mensal * (1 + taxa_mensal) ** dados["prazo"]) / ((1 + taxa_mensal) ** dados["prazo"] - 1)
    else:
        prestacao = None
    
    # Resultado da análise
    resultado = {
        "aprovado": aprovado,
        "pontuacao": pontuacao,
        "classificacao": classificacao,
        "valor_solicitado": dados["valor_solicitado"],
        "valor_aprovado": valor_aprovado if aprovado else 0,
        "taxa_juros": taxa_juros if aprovado else None,
        "prazo": dados["prazo"],
        "prestacao": prestacao,
        "motivos_recusa": motivos_recusa,
        "observacoes": observacoes
    }
    
    return resultado

def exibir_resultado_credito(dados, resultado):
    """Exibe o resultado da análise de crédito de forma organizada."""
    print("\n" + "=" * 60)
    print("RESULTADO DA ANÁLISE DE CRÉDITO")
    print("=" * 60)
    
    print(f"Nome: {dados['nome']}")
    print(f"Idade: {dados['idade']} anos")
    print(f"Renda: R$ {dados['renda']:.2f}")
    
    print("\n" + "-" * 60)
    print(f"Status: {'APROVADO' if resultado['aprovado'] else 'NEGADO'}")
    print(f"Pontuação: {resultado['pontuacao']} pontos")
    print(f"Classificação: {resultado['classificacao']}")
    print("-" * 60)
    
    if resultado["aprovado"]:
        print("\nDetalhes da aprovação:")
        print(f"Valor solicitado: R$ {resultado['valor_solicitado']:.2f}")
        print(f"Valor aprovado: R$ {resultado['valor_aprovado']:.2f}")
        print(f"Taxa de juros: {resultado['taxa_juros']:.2f}% ao mês")
        print(f"Prazo: {resultado['prazo']} meses")
        print(f"Prestação mensal: R$ {resultado['prestacao']:.2f}")
        
        # Cálculo e exibição do CET (Custo Efetivo Total)
        valor_total = resultado['prestacao'] * resultado['prazo']
        juros_total = valor_total - resultado['valor_aprovado']
        
        print(f"Total de juros: R$ {juros_total:.2f}")
        print(f"Valor total a pagar: R$ {valor_total:.2f}")
        
        # Verificação do comprometimento da renda
        comprometimento = resultado['prestacao'] / dados['renda'] * 100
        print(f"Comprometimento da renda: {comprometimento:.1f}%")
        
        if comprometimento > 30:
            print("\nAtenção: O valor da prestação compromete mais de 30% da sua renda.")
            print("Considere aumentar o prazo ou reduzir o valor solicitado.")
    else:
        print("\nMotivos da recusa:")
        for motivo in resultado["motivos_recusa"]:
            print(f"- {motivo}")
        
        print("\nSugestões para melhorar suas chances:")
        if any("renda" in motivo.lower() for motivo in resultado["motivos_recusa"]):
            print("- Considere solicitar um valor menor")
            print("- Aumente o prazo para reduzir o valor das prestações")
        
        if any("histórico" in motivo.lower() for motivo in resultado["motivos_recusa"]):
            print("- Regularize pendências financeiras anteriores")
            print("- Mantenha pagamentos em dia por pelo menos 6 meses")
        
        if any("pontuação" in motivo.lower() for motivo in resultado["motivos_recusa"]):
            print("- Aumente sua renda")
            print("- Adquira bens como imóveis ou veículos")
            print("- Aumente seu tempo no emprego atual")
    
    if resultado["observacoes"]:
        print("\nObservações adicionais:")
        for obs in resultado["observacoes"]:
            print(f"- {obs}")
    
    print("\n" + "=" * 60)
    print("SIMULAÇÃO DE OUTRAS CONDIÇÕES")
    print("=" * 60)
    
    if resultado["aprovado"]:
        # Simulação com prazo estendido
        if resultado["prazo"] < 60:
            novo_prazo = min(60, resultado["prazo"] + 12)
            taxa_mensal = resultado["taxa_juros"] / 100
            nova_prestacao = resultado["valor_aprovado"] * (taxa_mensal * (1 + taxa_mensal) ** novo_prazo) / ((1 + taxa_mensal) ** novo_prazo - 1)
            
            print(f"\nSimulação com prazo estendido ({novo_prazo} meses):")
            print(f"Nova prestação mensal: R$ {nova_prestacao:.2f}")
            reducao = resultado["prestacao"] - nova_prestacao
            print(f"Redução na prestação: R$ {reducao:.2f} ({reducao/resultado['prestacao']*100:.1f}%)")
        
        # Simulação com valor reduzido
        if resultado["valor_aprovado"] > 5000:
            valor_reduzido = resultado["valor_aprovado"] * 0.8
            taxa_mensal = resultado["taxa_juros"] / 100
            prestacao_reduzida = valor_reduzido * (taxa_mensal * (1 + taxa_mensal) ** resultado["prazo"]) / ((1 + taxa_mensal) ** resultado["prazo"] - 1)
            
            print(f"\nSimulação com valor reduzido (80% do valor aprovado):")
            print(f"Novo valor: R$ {valor_reduzido:.2f}")
            print(f"Nova prestação mensal: R$ {prestacao_reduzida:.2f}")
    else:
        # Sugestão de valor máximo possível
        valor_sugerido = dados["renda"] * 0.3 * (min(48, dados["prazo"]) / 12)
        if valor_sugerido >= 1000:
            print("\nSugestão de valor alternativo:")
            print(f"Com base na sua renda, sugerimos um empréstimo de até R$ {valor_sugerido:.2f}")
            print(f"Prazo sugerido: {min(48, dados['prazo'])} meses")
            print("Entre em contato conosco para uma nova análise com estes valores.")
        else:
            print("\nNo momento, não podemos oferecer alternativas de crédito compatíveis com seu perfil.")
            print("Recomendamos melhorar os fatores mencionados e tentar novamente após 3 meses.")

# Execução do exemplo
if __name__ == "__main__":
    sistema_avaliacao_credito()        