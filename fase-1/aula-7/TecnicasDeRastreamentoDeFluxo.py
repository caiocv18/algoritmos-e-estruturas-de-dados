def rastrear_fluxo_execucao(idade, renda, score):
    """Demonstra técnicas de rastreamento de fluxo de execução para depuração."""
    print("\n--- Início da Análise ---")
    print(f"Entrada: idade={idade}, renda={renda}, score={score}")
    
    # Etapa 1: Verificação de elegibilidade básica
    print("\nEtapa 1: Verificação de elegibilidade básica")
    
    elegivel_idade = idade >= 21 and idade <= 65
    print(f"- Idade entre 21 e 65: {elegivel_idade} ({idade})")
    
    elegivel_renda = renda >= 3000
    print(f"- Renda mínima de R$ 3000: {elegivel_renda} ({renda})")
    
    elegivel_score = score >= 700
    print(f"- Score mínimo de 700: {elegivel_score} ({score})")
    
    elegivel_basico = elegivel_idade and elegivel_renda and elegivel_score
    print(f"Resultado da etapa 1: {elegivel_basico}")
    
    if not elegivel_basico:
        print("Análise encerrada na etapa 1: requisitos básicos não atendidos")
        return False
    
    # Etapa 2: Cálculo da capacidade de pagamento
    print("\nEtapa 2: Cálculo da capacidade de pagamento")
    
    comprometimento_maximo = 0.3  # 30% da renda
    
    if idade < 30:
        comprometimento_maximo += 0.05  # +5% para jovens
        print("- Ajuste de idade: +5% (idade < 30)")
    
    if score > 800:
        comprometimento_maximo += 0.05  # +5% para score excepcional
        print("- Ajuste de score: +5% (score > 800)")
    
    capacidade_pagamento = renda * comprometimento_maximo
    print(f"Capacidade de pagamento: R$ {capacidade_pagamento:.2f} ({comprometimento_maximo*100:.0f}% da renda)")
    
    # Etapa 3: Determinação do limite de crédito
    print("\nEtapa 3: Determinação do limite de crédito")
    
    fator_multiplicador = 0
    
    if score >= 900:
        fator_multiplicador = 15
        print("- Fator alto: 15x (score >= 900)")
    elif score >= 800:
        fator_multiplicador = 12
        print("- Fator bom: 12x (score >= 800)")
    elif score >= 750:
        fator_multiplicador = 10
        print("- Fator médio: 10x (score >= 750)")
    else:  # score entre 700 e 749
        fator_multiplicador = 8
        print("- Fator básico: 8x (score >= 700)")
    
    limite_credito = capacidade_pagamento * fator_multiplicador
    print(f"Limite de crédito: R$ {limite_credito:.2f} ({fator_multiplicador}x)")
    
    # Etapa 4: Ajustes finais
    print("\nEtapa 4: Ajustes finais")
    
    # Limitador baseado na idade
    if idade > 60:
        limite_anterior = limite_credito
        limite_credito = min(limite_credito, 50000)
        reducao = limite_anterior - limite_credito
        
        if reducao > 0:
            print(f"- Limitador de idade: redução de R$ {reducao:.2f} (idade > 60)")
    
    # Verificação de limite mínimo viável
    limite_minimo = 5000
    if limite_credito < limite_minimo:
        print(f"- Limite calculado abaixo do mínimo: R$ {limite_credito:.2f} < R$ {limite_minimo:.2f}")
        print("Análise encerrada na etapa 4: limite abaixo do mínimo viável")
        return False
    
    print(f"\nResultado final: Aprovado com limite de R$ {limite_credito:.2f}")
    print("--- Fim da Análise ---")
    
    return True