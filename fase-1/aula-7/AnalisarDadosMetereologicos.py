def analisar_dados_meteorologicos():
    """
    Sistema simplificado para análise de dados meteorológicos.
    """
    print("\n===== SISTEMA DE ANÁLISE METEOROLÓGICA =====")
    
    # Simulação de dados meteorológicos (normalmente viriam de um arquivo ou API)
    dados = [
        {"data": "2023-07-01", "temperatura": 25.5, "umidade": 65, "pressao": 1013, "vento": 12, "precipitacao": 0},
        {"data": "2023-07-02", "temperatura": 28.2, "umidade": 70, "pressao": 1010, "vento": 15, "precipitacao": 0},
        {"data": "2023-07-03", "temperatura": 30.0, "umidade": 75, "pressao": 1008, "vento": 20, "precipitacao": 10},
        {"data": "2023-07-04", "temperatura": 22.8, "umidade": 85, "pressao": 1005, "vento": 25, "precipitacao": 35},
        {"data": "2023-07-05", "temperatura": 20.5, "umidade": 80, "pressao": 1007, "vento": 18, "precipitacao": 15},
        {"data": "2023-07-06", "temperatura": 23.0, "umidade": 75, "pressao": 1012, "vento": 10, "precipitacao": 5},
        {"data": "2023-07-07", "temperatura": 26.5, "umidade": 60, "pressao": 1015, "vento": 8, "precipitacao": 0}
    ]
    
    while True:
        print("\nOpções de análise:")
        print("1. Resumo geral")
        print("2. Análise de temperatura")
        print("3. Análise de precipitação")
        print("4. Previsão simples")
        print("5. Alertas meteorológicos")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            resumo_geral(dados)
        elif opcao == "2":
            analise_temperatura(dados)
        elif opcao == "3":
            analise_precipitacao(dados)
        elif opcao == "4":
            previsao_simples(dados)
        elif opcao == "5":
            alertas_meteorologicos(dados)
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def resumo_geral(dados):
    """Exibe um resumo geral dos dados meteorológicos."""
    print("\n--- Resumo Geral ---")
    
    # Cálculo de médias
    temp_total = sum(dia["temperatura"] for dia in dados)
    umid_total = sum(dia["umidade"] for dia in dados)
    press_total = sum(dia["pressao"] for dia in dados)
    vento_total = sum(dia["vento"] for dia in dados)
    precip_total = sum(dia["precipitacao"] for dia in dados)
    
    num_dias = len(dados)
    temp_media = temp_total / num_dias
    umid_media = umid_total / num_dias
    press_media = press_total / num_dias
    vento_media = vento_total / num_dias
    
    # Encontrar valores extremos
    temp_max = max(dados, key=lambda dia: dia["temperatura"])
    temp_min = min(dados, key=lambda dia: dia["temperatura"])
    precip_max = max(dados, key=lambda dia: dia["precipitacao"])
    
    # Contagem de dias com precipitação
    dias_chuvosos = sum(1 for dia in dados if dia["precipitacao"] > 0)
    
    # Exibição do resumo
    print(f"Período: {dados[0]['data']} a {dados[-1]['data']}")
    print(f"Total de dias analisados: {num_dias}")
    print(f"Temperatura média: {temp_media:.1f}°C")
    print(f"Temperatura máxima: {temp_max['temperatura']:.1f}°C em {temp_max['data']}")
    print(f"Temperatura mínima: {temp_min['temperatura']:.1f}°C em {temp_min['data']}")
    print(f"Umidade média: {umid_media:.1f}%")
    print(f"Pressão média: {press_media:.1f} hPa")
    print(f"Velocidade média do vento: {vento_media:.1f} km/h")
    print(f"Precipitação total: {precip_total:.1f} mm")
    print(f"Dia com maior precipitação: {precip_max['data']} ({precip_max['precipitacao']:.1f} mm)")
    print(f"Dias com chuva: {dias_chuvosos} ({dias_chuvosos/num_dias*100:.1f}% do período)")

def analise_temperatura(dados):
    """Realiza análise detalhada das temperaturas."""
    print("\n--- Análise de Temperatura ---")
    
    # Coleta de temperaturas
    temperaturas = [dia["temperatura"] for dia in dados]
    
    # Cálculo de estatísticas
    temp_media = sum(temperaturas) / len(temperaturas)
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    amplitude = temp_max - temp_min
    
    # Cálculo de variação diária
    variacoes = []
    for i in range(1, len(temperaturas)):
        variacao = temperaturas[i] - temperaturas[i-1]
        variacoes.append(variacao)
    
    # Classificação de dias
    dias_quentes = sum(1 for temp in temperaturas if temp > 28)
    dias_amenos = sum(1 for temp in temperaturas if 20 <= temp <= 28)
    dias_frios = sum(1 for temp in temperaturas if temp < 20)
    
    # Exibição da análise
    print(f"Temperatura média: {temp_media:.1f}°C")
    print(f"Temperatura máxima: {temp_max:.1f}°C")
    print(f"Temperatura mínima: {temp_min:.1f}°C")
    print(f"Amplitude térmica: {amplitude:.1f}°C")
    
    if variacoes:
        maior_aumento = max(variacoes)
        maior_queda = min(variacoes)
        print(f"Maior aumento de temperatura: {maior_aumento:.1f}°C")
        print(f"Maior queda de temperatura: {maior_queda:.1f}°C")
    
    print("\nClassificação de dias:")
    print(f"- Dias quentes (>28°C): {dias_quentes}")
    print(f"- Dias amenos (20-28°C): {dias_amenos}")
    print(f"- Dias frios (<20°C): {dias_frios}")
    
    print("\nEvolução da temperatura:")
    for i, dia in enumerate(dados):
        temp = dia["temperatura"]
        tendencia = ""
        if i > 0:
            if temperaturas[i] > temperaturas[i-1]:
                tendencia = "↑"
            elif temperaturas[i] < temperaturas[i-1]:
                tendencia = "↓"
            else:
                tendencia = "→"
        
        # Classificação visual
        if temp > 28:
            classe = "QUENTE"
        elif temp >= 20:
            classe = "AMENO"
        else:
            classe = "FRIO"
        
        print(f"{dia['data']}: {temp:.1f}°C {tendencia} [{classe}]")

def analise_precipitacao(dados):
    """Realiza análise detalhada das precipitações."""
    print("\n--- Análise de Precipitação ---")
    
    # Coleta de dados de precipitação
    precipitacoes = [dia["precipitacao"] for dia in dados]
    
    # Cálculo de estatísticas
    total_precipitacao = sum(precipitacoes)
    media_precipitacao = total_precipitacao / len(precipitacoes)
    max_precipitacao = max(precipitacoes)
    
    # Identificação do dia com maior precipitação
    dia_max_precip = None
    for dia in dados:
        if dia["precipitacao"] == max_precipitacao:
            dia_max_precip = dia
            break
    
    # Classificação de intensidade
    sem_chuva = sum(1 for p in precipitacoes if p == 0)
    chuva_fraca = sum(1 for p in precipitacoes if 0 < p <= 5)
    chuva_moderada = sum(1 for p in precipitacoes if 5 < p <= 20)
    chuva_forte = sum(1 for p in precipitacoes if p > 20)
    
    # Sequência de dias chuvosos
    dias_chuvosos_consecutivos = 0
    maior_sequencia = 0
    sequencia_atual = 0
    
    for precip in precipitacoes:
        if precip > 0:
            sequencia_atual += 1
        else:
            maior_sequencia = max(maior_sequencia, sequencia_atual)
            sequencia_atual = 0
    
    maior_sequencia = max(maior_sequencia, sequencia_atual)
    
    # Exibição da análise
    print(f"Precipitação total no período: {total_precipitacao:.1f} mm")
    print(f"Média diária de precipitação: {media_precipitacao:.1f} mm")
    print(f"Dia com maior precipitação: {dia_max_precip['data']} ({max_precipitacao:.1f} mm)")
    
    print("\nClassificação dos dias:")
    print(f"- Sem chuva: {sem_chuva} dias")
    print(f"- Chuva fraca (até 5 mm): {chuva_fraca} dias")
    print(f"- Chuva moderada (5-20 mm): {chuva_moderada} dias")
    print(f"- Chuva forte (>20 mm): {chuva_forte} dias")
    
    print(f"\nMaior sequência de dias chuvosos consecutivos: {maior_sequencia}")
    
    print("\nDetalhe diário:")
    for dia in dados:
        precip = dia["precipitacao"]
        
        # Classificação visual
        if precip == 0:
            classe = "SEM CHUVA"
        elif precip <= 5:
            classe = "FRACA"
        elif precip <= 20:
            classe = "MODERADA"
        else:
            classe = "FORTE"
        
        # Exibição com barras visuais
        barras = "█" * int(precip / 5 + 1) if precip > 0 else ""
        print(f"{dia['data']}: {precip:.1f} mm {barras} [{classe}]")

def previsao_simples(dados):
    """Realiza uma previsão simples baseada em tendências recentes."""
    print("\n--- Previsão Simples ---")
    
    if len(dados) < 3:
        print("Dados insuficientes para fazer uma previsão.")
        return
    
    # Análise de tendências de temperatura
    temp_ultimos_3_dias = [dia["temperatura"] for dia in dados[-3:]]
    tendencia_temp = sum(temp_ultimos_3_dias) / 3
    
    # Análise de tendências de pressão
    pressao_ultimos_3_dias = [dia["pressao"] for dia in dados[-3:]]
    tendencia_pressao = pressao_ultimos_3_dias[-1] - pressao_ultimos_3_dias[0]
    
    # Análise de tendências de umidade
    umidade_ultimos_dias = [dia["umidade"] for dia in dados[-3:]]
    tendencia_umidade = umidade_ultimos_dias[-1] - umidade_ultimos_dias[0]
    
    # Previsão baseada em tendências
    print("Previsão para o próximo dia:")
    
    # Temperatura prevista (média dos últimos 3 dias com ajuste pela tendência)
    ajuste_temp = (temp_ultimos_3_dias[-1] - temp_ultimos_3_dias[0]) / 2
    temp_prevista = tendencia_temp + ajuste_temp
    print(f"Temperatura: {temp_prevista:.1f}°C")
    
    # Condição meteorológica prevista
    if tendencia_pressao < -3:
        if umidade_ultimos_dias[-1] > 70:
            condicao = "Probabilidade de chuva"
        else:
            condicao = "Instável, possibilidade de precipitação"
    elif tendencia_pressao > 3:
        condicao = "Tempo estável, sem previsão de chuva"
    else:
        if umidade_ultimos_dias[-1] > 80:
            condicao = "Nublado com possibilidade de precipitação"
        elif umidade_ultimos_dias[-1] > 60:
            condicao = "Parcialmente nublado"
        else:
            condicao = "Predominantemente ensolarado"
    
    print(f"Condição: {condicao}")
    
    # Confiabilidade da previsão (simples)
    variabilidade = abs(max(temp_ultimos_3_dias) - min(temp_ultimos_3_dias))
    if variabilidade < 2 and abs(tendencia_pressao) < 3:
        confiabilidade = "Alta"
    elif variabilidade < 5 and abs(tendencia_pressao) < 8:
        confiabilidade = "Média"
    else:
        confiabilidade = "Baixa"
    
    print(f"Confiabilidade da previsão: {confiabilidade}")
    print("\nObservação: Esta é uma previsão simplificada para fins educacionais.")
    print("Previsões meteorológicas reais utilizam modelos matemáticos muito mais complexos.")

def alertas_meteorologicos(dados):
    """Identifica e exibe possíveis alertas meteorológicos."""
    print("\n--- Alertas Meteorológicos ---")
    
    alertas = []
    
    # Verificação de onda de calor (3 dias consecutivos acima de 30°C)
    temperaturas = [dia["temperatura"] for dia in dados]
    for i in range(len(temperaturas) - 2):
        if all(temp >= 30 for temp in temperaturas[i:i+3]):
            alertas.append({
                "tipo": "Onda de calor",
                "descricao": f"3 ou mais dias consecutivos com temperaturas acima de 30°C",
                "periodo": f"{dados[i]['data']} a {dados[i+2]['data']}",
                "gravidade": "Moderada"
            })
            break
    
    # Verificação de chuva intensa
    for dia in dados:
        if dia["precipitacao"] > 30:
            alertas.append({
                "tipo": "Chuva intensa",
                "descricao": f"Precipitação de {dia['precipitacao']:.1f} mm em um único dia",
                "periodo": dia["data"],
                "gravidade": "Alta" if dia["precipitacao"] > 50 else "Moderada"
            })
    
    # Verificação de variação brusca de temperatura
    for i in range(1, len(dados)):
        variacao = dados[i]["temperatura"] - dados[i-1]["temperatura"]
        if abs(variacao) > 8:
            alertas.append({
                "tipo": "Variação brusca de temperatura",
                "descricao": f"Variação de {abs(variacao):.1f}°C em 24 horas",
                "periodo": f"{dados[i-1]['data']} a {dados[i]['data']}",
                "gravidade": "Moderada"
            })
    
    # Verificação de baixa umidade persistente
    umidades = [dia["umidade"] for dia in dados]
    for i in range(len(umidades) - 2):
        if all(umidade < 30 for umidade in umidades[i:i+3]):
            alertas.append({
                "tipo": "Baixa umidade persistente",
                "descricao": f"3 ou mais dias consecutivos com umidade abaixo de 30%",
                "periodo": f"{dados[i]['data']} a {dados[i+2]['data']}",
                "gravidade": "Alta"
            })
            break
    
    # Verificação de ventania
    for dia in dados:
        if dia["vento"] > 50:
            alertas.append({
                "tipo": "Ventania severa",
                "descricao": f"Ventos de {dia['vento']} km/h",
                "periodo": dia["data"],
                "gravidade": "Alta"
            })
        elif dia["vento"] > 40:
            alertas.append({
                "tipo": "Ventania",
                "descricao": f"Ventos de {dia['vento']} km/h",
                "periodo": dia["data"],
                "gravidade": "Moderada"
            })
    
    # Exibição dos alertas
    if alertas:
        print(f"Foram identificados {len(alertas)} alertas meteorológicos:")
        
        for i, alerta in enumerate(alertas, 1):
            print(f"\nAlerta {i}: {alerta['tipo']}")
            print(f"Descrição: {alerta['descricao']}")
            print(f"Período: {alerta['periodo']}")
            print(f"Gravidade: {alerta['gravidade']}")
            
            # Recomendações condicionais
            print("Recomendações:")
            if alerta['tipo'] == "Onda de calor":
                print("- Beba bastante água")
                print("- Evite exposição direta ao sol nos horários de pico (10h às 16h)")
                print("- Utilize roupas leves e de cores claras")
            elif alerta['tipo'] == "Chuva intensa":
                print("- Evite áreas com risco de alagamento")
                print("- Não atravesse áreas alagadas")
                print("- Fique atento a deslizamentos em áreas de encosta")
            elif alerta['tipo'] == "Variação brusca de temperatura":
                print("- Prepare-se para mudança repentina no clima")
                print("- Mantenha agasalhos à mão")
            elif alerta['tipo'] == "Baixa umidade persistente":
                print("- Beba bastante água")
                print("- Evite atividades físicas intensas ao ar livre")
                print("- Utilize umidificadores de ambiente se possível")
            elif "Ventania" in alerta['tipo']:
                print("- Evite áreas com estruturas instáveis")
                print("- Tenha cuidado com quedas de árvores e objetos")
                print("- Verifique se há objetos soltos em áreas externas")
    else:
        print("Nenhum alerta meteorológico identificado para o período analisado.")

# Execução do exemplo
if __name__ == "__main__":
    analisar_dados_meteorologicos()