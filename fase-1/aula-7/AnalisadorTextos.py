def analisador_textos():
    """
    Sistema simplificado para análise de textos com estatísticas condicionais.
    """
    print("\n===== ANALISADOR DE TEXTOS =====")
    print("Este sistema analisa textos e gera estatísticas personalizadas.")
    
    # Obtenção do texto a ser analisado
    texto = obter_texto()
    if not texto:
        return
    
    # Menu de análises disponíveis
    while True:
        print("\nOpções de análise:")
        print("1. Estatísticas básicas")
        print("2. Análise de palavras")
        print("3. Análise de frases")
        print("4. Análise de legibilidade")
        print("5. Análise de sentimento (simplificada)")
        print("6. Comparação com texto de referência")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            estatisticas_basicas(texto)
        elif opcao == "2":
            analise_palavras(texto)
        elif opcao == "3":
            analise_frases(texto)
        elif opcao == "4":
            analise_legibilidade(texto)
        elif opcao == "5":
            analise_sentimento(texto)
        elif opcao == "6":
            texto_referencia = obter_texto("referência")
            if texto_referencia:
                comparar_textos(texto, texto_referencia)
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def obter_texto(tipo="principal"):
    """Obtém e valida o texto a ser analisado."""
    print(f"\n--- Entrada do Texto {tipo.capitalize()} ---")
    
    print("Digite o texto para análise (digite 'FIM' em uma linha separada para terminar):")
    linhas = []
    
    while True:
        linha = input()
        if linha == "FIM":
            break
        linhas.append(linha)
    
    texto = "\n".join(linhas)
    
    if not texto.strip():
        print("Erro: O texto não pode estar vazio.")
        return None
    
    return texto

def estatisticas_basicas(texto):
    """Calcula e exibe estatísticas básicas sobre o texto."""
    print("\n--- Estatísticas Básicas ---")
    
    # Contagem de caracteres
    caracteres_total = len(texto)
    caracteres_sem_espaco = sum(1 for c in texto if not c.isspace())
    
    # Contagem de palavras
    palavras = [p for p in texto.lower().replace("\n", " ").split() if p]
    num_palavras = len(palavras)
    
    # Contagem de frases
    frases = [f.strip() for f in texto.replace("!", ".").replace("?", ".").split(".") if f.strip()]
    num_frases = len(frases)
    
    # Contagem de parágrafos
    paragrafos = [p for p in texto.split("\n\n") if p.strip()]
    num_paragrafos = len(paragrafos)
    
    # Exibição das estatísticas básicas
    print(f"Total de caracteres: {caracteres_total}")
    print(f"Caracteres (sem espaços): {caracteres_sem_espaco}")
    print(f"Total de palavras: {num_palavras}")
    print(f"Total de frases: {num_frases}")
    print(f"Total de parágrafos: {num_paragrafos}")
    
    if num_palavras > 0:
        tamanho_medio_palavra = sum(len(p) for p in palavras) / num_palavras
        print(f"Tamanho médio das palavras: {tamanho_medio_palavra:.1f} caracteres")
    
    if num_frases > 0:
        palavras_por_frase = num_palavras / num_frases
        print(f"Média de palavras por frase: {palavras_por_frase:.1f}")
    
    if num_paragrafos > 0:
        frases_por_paragrafo = num_frases / num_paragrafos
        print(f"Média de frases por parágrafo: {frases_por_paragrafo:.1f}")
    
    # Análise de densidade léxica
    palavras_unicas = len(set(palavras))
    if num_palavras > 0:
        densidade_lexica = palavras_unicas / num_palavras
        print(f"Palavras únicas: {palavras_unicas}")
        print(f"Densidade léxica: {densidade_lexica:.2f}")
        
        if densidade_lexica > 0.7:
            print("Observação: Texto com alta variedade de vocabulário.")
        elif densidade_lexica < 0.4:
            print("Observação: Texto com vocabulário limitado ou repetitivo.")

def analise_palavras(texto):
    """Realiza análise detalhada das palavras no texto."""
    print("\n--- Análise de Palavras ---")
    
    # Processamento do texto
    palavras = [p.strip(".,!?():;\"'").lower() for p in texto.replace("\n", " ").split() if p]
    
    if not palavras:
        print("Não há palavras para analisar.")
        return
    
    # Contagem de cada palavra
    contagem_palavras = {}
    for palavra in palavras:
        if len(palavra) > 1 or palavra.isalnum():  # Ignora caracteres isolados não alfanuméricos
            contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    
    # Palavras mais comuns
    palavras_comuns = sorted(contagem_palavras.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\nTotal de palavras: {len(palavras)}")
    print(f"Palavras únicas: {len(contagem_palavras)}")
    
    # Palavras mais frequentes
    print("\nPalavras mais frequentes:")
    for palavra, contagem in palavras_comuns[:10]:
        print(f"- '{palavra}': {contagem} ocorrências ({contagem/len(palavras)*100:.1f}%)")
    
    # Análise por tamanho
    tamanhos = [len(p) for p in palavras]
    tamanho_medio = sum(tamanhos) / len(tamanhos)
    maior_palavra = max(palavras, key=len)
    
    print(f"\nTamanho médio das palavras: {tamanho_medio:.1f} caracteres")
    print(f"Palavra mais longa: '{maior_palavra}' ({len(maior_palavra)} caracteres)")
    
    # Distribuição por tamanho
    distribuicao = {}
    for tamanho in tamanhos:
        distribuicao[tamanho] = distribuicao.get(tamanho, 0) + 1
    
    print("\nDistribuição por tamanho:")
    for tamanho in sorted(distribuicao.keys()):
        percentual = distribuicao[tamanho] / len(palavras) * 100
        barra = "#" * int(percentual / 2)
        print(f"{tamanho:2} letras: {distribuicao[tamanho]:4} ({percentual:5.1f}%) {barra}")
    
    # Detecção de palavras repetidas em sequência
    repeticoes = []
    for i in range(1, len(palavras)):
        if palavras[i] == palavras[i-1] and len(palavras[i]) > 3:
            repeticoes.append(palavras[i])
    
    if repeticoes:
        print("\nPalavras repetidas em sequência detectadas:")
        for palavra in set(repeticoes):
            print(f"- '{palavra}'")

def analise_frases(texto):
    """Realiza análise detalhada das frases no texto."""
    print("\n--- Análise de Frases ---")
    
    # Identificação de frases
    frases = []
    for s in texto.replace("!", ".").replace("?", ".").split("."):
        s = s.strip()
        if s:
            frases.append(s)
    
    if not frases:
        print("Não há frases para analisar.")
        return
    
    # Análise de comprimento
    tamanhos = [len(f) for f in frases]
    palavras_por_frase = [len(f.split()) for f in frases]
    
    print(f"Total de frases: {len(frases)}")
    print(f"Comprimento médio: {sum(tamanhos)/len(frases):.1f} caracteres")
    print(f"Média de palavras por frase: {sum(palavras_por_frase)/len(frases):.1f}")
    
    # Frases mais curtas e mais longas
    frase_mais_curta = min(frases, key=lambda f: len(f.split()))
    frase_mais_longa = max(frases, key=lambda f: len(f.split()))
    
    print(f"\nFrase mais curta ({len(frase_mais_curta.split())} palavras):")
    print(f'"{frase_mais_curta}"')
    
    print(f"\nFrase mais longa ({len(frase_mais_longa.split())} palavras):")
    print(f'"{frase_mais_longa}"')
    
    # Distribuição de tamanhos
    print("\nDistribuição de tamanhos (em palavras):")
    
    faixas = {
        "1-5": 0,
        "6-10": 0,
        "11-15": 0,
        "16-20": 0,
        "21-25": 0,
        "26+": 0
    }
    
    for num_palavras in palavras_por_frase:
        if num_palavras <= 5:
            faixas["1-5"] += 1
        elif num_palavras <= 10:
            faixas["6-10"] += 1
        elif num_palavras <= 15:
            faixas["11-15"] += 1
        elif num_palavras <= 20:
            faixas["16-20"] += 1
        elif num_palavras <= 25:
            faixas["21-25"] += 1
        else:
            faixas["26+"] += 1
    
    for faixa, contagem in faixas.items():
        if contagem > 0:
            percentual = contagem / len(frases) * 100
            print(f"{faixa:5} palavras: {contagem:3} frases ({percentual:5.1f}%)")
    
    # Análise de inícios de frases
    inicios = {}
    for frase in frases:
        palavras = frase.split()
        if palavras:
            inicio = palavras[0].lower()
            inicios[inicio] = inicios.get(inicio, 0) + 1
    
    print("\nInícios de frases mais comuns:")
    inicios_comuns = sorted(inicios.items(), key=lambda x: x[1], reverse=True)
    for inicio, contagem in inicios_comuns[:5]:
        print(f"- '{inicio}': {contagem} ocorrências")

def analise_legibilidade(texto):
    """
    Analisa a legibilidade do texto usando índices simplificados.
    """
    print("\n--- Análise de Legibilidade ---")
    
    # Preparação do texto
    palavras = [p for p in texto.lower().replace("\n", " ").split() if p]
    frases = [f.strip() for f in texto.replace("!", ".").replace("?", ".").split(".") if f.strip()]
    
    if not palavras or not frases:
        print("Texto insuficiente para análise de legibilidade.")
        return
    
    # Contagens básicas
    num_palavras = len(palavras)
    num_frases = len(frases)
    num_silabas = estimar_silabas(palavras)
    
    # Cálculo do índice de Flesch-Kincaid simplificado
    try:
        palavras_por_frase = num_palavras / num_frases
        silabas_por_palavra = num_silabas / num_palavras
        
        # Fórmula simplificada do índice de Flesch
        indice_flesch = 206.835 - (1.015 * palavras_por_frase) - (84.6 * silabas_por_palavra)
        
        # Ajuste para valores fora da escala
        indice_flesch = max(0, min(100, indice_flesch))
        
        print(f"Número de palavras: {num_palavras}")
        print(f"Número de frases: {num_frases}")
        print(f"Número estimado de sílabas: {num_silabas}")
        print(f"Média de palavras por frase: {palavras_por_frase:.1f}")
        print(f"Média de sílabas por palavra: {silabas_por_palavra:.1f}")
        
        print(f"\nÍndice de Flesch (adaptado): {indice_flesch:.1f}")
        
        # Interpretação do índice de Flesch
        if indice_flesch >= 90:
            nivel = "Muito fácil"
            descricao = "Adequado para crianças dos primeiros anos do ensino fundamental."
        elif indice_flesch >= 80:
            nivel = "Fácil"
            descricao = "Adequado para crianças do ensino fundamental."
        elif indice_flesch >= 70:
            nivel = "Razoavelmente fácil"
            descricao = "Adequado para adolescentes."
        elif indice_flesch >= 60:
            nivel = "Padrão"
            descricao = "Adequado para estudantes do ensino médio e adultos."
        elif indice_flesch >= 50:
            nivel = "Razoavelmente difícil"
            descricao = "Adequado para estudantes do ensino superior."
        elif indice_flesch >= 30:
            nivel = "Difícil"
            descricao = "Adequado para universitários e profissionais."
        else:
            nivel = "Muito difícil"
            descricao = "Adequado para profissionais especializados."
        
        print(f"Classificação: {nivel}")
        print(f"Interpretação: {descricao}")
        
        # Análise adicional
        print("\nAnálise adicional:")
        
        palavras_longas = sum(1 for p in palavras if len(p) > 6)
        percentual_longas = palavras_longas / num_palavras * 100
        print(f"Palavras longas (>6 letras): {palavras_longas} ({percentual_longas:.1f}%)")
        
        frases_longas = sum(1 for f in frases if len(f.split()) > 20)
        percentual_frases_longas = frases_longas / num_frases * 100 if num_frases > 0 else 0
        print(f"Frases longas (>20 palavras): {frases_longas} ({percentual_frases_longas:.1f}%)")
        
        # Recomendações condicionais
        print("\nRecomendações:")
        
        if indice_flesch < 50:
            print("- Considere simplificar o vocabulário")
            print("- Use frases mais curtas")
            
        if percentual_longas > 25:
            print("- Substitua algumas palavras longas por alternativas mais simples")
            
        if percentual_frases_longas > 20:
            print("- Divida frases muito longas em frases mais curtas")
            print("- Evite informações excessivas em uma única frase")
        
        if silabas_por_palavra > 2.0:
            print("- Use palavras com menos sílabas para melhorar a fluidez")
        
    except ZeroDivisionError:
        print("Erro no cálculo. Verifique se o texto contém palavras e frases válidas.")

def estimar_silabas(palavras):
    """
    Estima o número de sílabas em uma lista de palavras.
    Este é um método simplificado para o português.
    """
    vogais = "aeiouyáàâãäéèêëíìîïóòôõöúùûü"
    
    total_silabas = 0
    
    for palavra in palavras:
        # Contador de sílabas por palavra
        contagem = 0
        vogal_anterior = False
        
        for c in palavra.lower():
            vogal_atual = c in vogais
            
            if vogal_atual and not vogal_anterior:
                contagem += 1
                
            vogal_anterior = vogal_atual
        
        # Ajuste para palavras que terminam com 'e' mudo ou similares
        if palavra.endswith(('e', 'es', 'em')) and len(palavra) > 2:
            contagem = max(1, contagem - 1)
        
        # Garantir que toda palavra tenha pelo menos uma sílaba
        contagem = max(1, contagem)
        
        total_silabas += contagem
    
    return total_silabas

def analise_sentimento(texto):
    """
    Realiza uma análise de sentimento simplificada do texto.
    """
    print("\n--- Análise de Sentimento ---")
    
    # Palavras com conotação positiva
    palavras_positivas = {
        "bom", "ótimo", "excelente", "incrível", "maravilhoso", "fantástico", 
        "feliz", "alegre", "contente", "satisfeito", "positivo", "admirável",
        "impressionante", "agradável", "adorável", "prazeroso", "amar", "gostar",
        "sucesso", "vitória", "vencer", "aprovação", "êxito", "elogiar",
        "melhor", "superior", "eficiente", "recomendo", "confiar", "confiança",
        "sorriso", "esperança", "motivador", "promissor", "generoso"
    }
    
    # Palavras com conotação negativa
    palavras_negativas = {
        "ruim", "péssimo", "terrível", "horrível", "desagradável", "lamentável",
        "triste", "infeliz", "descontente", "insatisfeito", "negativo", "reprovável",
        "decepcionante", "desagradável", "detestável", "doloroso", "odiar", "detestar",
        "fracasso", "derrota", "perder", "reprovação", "falha", "criticar",
        "pior", "inferior", "ineficiente", "desaprovo", "desconfiar", "desconfiança",
        "lágrima", "desesperança", "desmotivador", "desanimador", "egoísta"
    }
    
    # Processamento do texto
    palavras = []
    for p in texto.lower().replace("\n", " ").replace(".", " ").replace(",", " ").split():
        palavra = p.strip(".,!?():;\"'")
        if palavra:
            palavras.append(palavra)
    
    if not palavras:
        print("Não há palavras suficientes para análise de sentimento.")
        return
    
    # Contagem de palavras positivas e negativas
    cont_positivas = sum(1 for p in palavras if p in palavras_positivas)
    cont_negativas = sum(1 for p in palavras if p in palavras_negativas)
    
    # Análise de frases negativas (contendo "não", "nunca", etc.)
    palavras_negacao = {"não", "nunca", "jamais", "nenhum", "nada"}
    cont_negacoes = sum(1 for p in palavras if p in palavras_negacao)
    
    # Cálculo do score de sentimento
    total_sentimento = cont_positivas - cont_negativas
    porcentagem_positiva = cont_positivas / len(palavras) * 100
    porcentagem_negativa = cont_negativas / len(palavras) * 100
    
    # Determinação da polaridade
    if cont_positivas == 0 and cont_negativas == 0:
        polaridade = "neutra"
        pontuacao = 0
    else:
        pontuacao = total_sentimento / (cont_positivas + cont_negativas) * 100
        
        if pontuacao > 60:
            polaridade = "muito positiva"
        elif pontuacao > 20:
            polaridade = "positiva"
        elif pontuacao > -20:
            polaridade = "neutra"
        elif pontuacao > -60:
            polaridade = "negativa"
        else:
            polaridade = "muito negativa"
    
    # Ajuste para presença de muitas negações
    if cont_negacoes > 5 and polaridade in ["positiva", "muito positiva"]:
        polaridade = "possivelmente menos positiva do que parece"
        print("Observação: Detectado alto uso de palavras de negação, o que pode inverter o sentimento.")
    
    # Exibição dos resultados
    print(f"Total de palavras analisadas: {len(palavras)}")
    print(f"Palavras com conotação positiva: {cont_positivas} ({porcentagem_positiva:.1f}%)")
    print(f"Palavras com conotação negativa: {cont_negativas} ({porcentagem_negativa:.1f}%)")
    print(f"Palavras de negação: {cont_negacoes}")
    
    print(f"\nPolaridade do texto: {polaridade.capitalize()}")
    print(f"Pontuação de sentimento: {pontuacao:.1f}")
    
    # Exibição das palavras mais impactantes
    palavras_positivas_encontradas = [p for p in palavras if p in palavras_positivas]
    palavras_negativas_encontradas = [p for p in palavras if p in palavras_negativas]
    
    if palavras_positivas_encontradas:
        print("\nPalavras positivas mais relevantes:")
        for palavra in sorted(set(palavras_positivas_encontradas))[:5]:
            contagem = palavras_positivas_encontradas.count(palavra)
            print(f"- '{palavra}': {contagem} ocorrência(s)")
    
    if palavras_negativas_encontradas:
        print("\nPalavras negativas mais relevantes:")
        for palavra in sorted(set(palavras_negativas_encontradas))[:5]:
            contagem = palavras_negativas_encontradas.count(palavra)
            print(f"- '{palavra}': {contagem} ocorrência(s)")
    
    # Observações condicionais
    print("\nObservações:")
    
    if cont_positivas > 0 and cont_negativas > 0:
        if abs(pontuacao) < 20:
            print("- O texto apresenta um equilíbrio entre elementos positivos e negativos.")
        elif pontuacao > 0:
            print("- O texto apresenta predominância de elementos positivos.")
        else:
            print("- O texto apresenta predominância de elementos negativos.")
    elif cont_positivas > 0:
        print("- O texto apresenta apenas elementos positivos identificados.")
    elif cont_negativas > 0:
        print("- O texto apresenta apenas elementos negativos identificados.")
    else:
        print("- Não foram identificados elementos claros de sentimento no texto.")
    
    print("\nNota: Esta é uma análise simplificada e pode não captar nuances, ironia ou contexto cultural.")

def comparar_textos(texto1, texto2):
    """
    Compara dois textos e identifica semelhanças e diferenças.
    """
    print("\n--- Comparação de Textos ---")
    
    # Processamento dos textos
    palavras1 = [p.strip(".,!?():;\"'").lower() for p in texto1.replace("\n", " ").split() if p]
    palavras2 = [p.strip(".,!?():;\"'").lower() for p in texto2.replace("\n", " ").split() if p]
    
    # Contagens básicas
    num_palavras1 = len(palavras1)
    num_palavras2 = len(palavras2)
    
    print("Comparação de tamanho:")
    print(f"Texto principal: {num_palavras1} palavras")
    print(f"Texto de referência: {num_palavras2} palavras")
    
    diferenca_percentual = abs(num_palavras1 - num_palavras2) / max(num_palavras1, num_palavras2) * 100
    print(f"Diferença de tamanho: {diferenca_percentual:.1f}%")
    
    # Vocabulário comum
    palavras_unicas1 = set(palavras1)
    palavras_unicas2 = set(palavras2)
    
    palavras_comuns = palavras_unicas1.intersection(palavras_unicas2)
    palavras_exclusivas1 = palavras_unicas1 - palavras_unicas2
    palavras_exclusivas2 = palavras_unicas2 - palavras_unicas1
    
    print("\nComparação de vocabulário:")
    print(f"Palavras únicas no texto principal: {len(palavras_unicas1)}")
    print(f"Palavras únicas no texto de referência: {len(palavras_unicas2)}")
    print(f"Palavras comuns aos dois textos: {len(palavras_comuns)}")
    
    if palavras_unicas1 and palavras_unicas2:
        indice_jaccard = len(palavras_comuns) / len(palavras_unicas1.union(palavras_unicas2))
        print(f"Índice de similaridade Jaccard: {indice_jaccard:.3f} ({indice_jaccard*100:.1f}%)")
        
        if indice_jaccard > 0.8:
            print("Os textos compartilham vocabulário muito similar.")
        elif indice_jaccard > 0.5:
            print("Os textos compartilham vocabulário moderadamente similar.")
        elif indice_jaccard > 0.3:
            print("Os textos compartilham algum vocabulário comum.")
        else:
            print("Os textos têm vocabulário significativamente diferente.")
    
    # Palavras mais comuns em cada texto
    if palavras_exclusivas1:
        print("\nPalavras mais comuns apenas no texto principal:")
        contagem1 = {}
        for palavra in palavras1:
            if palavra in palavras_exclusivas1:
                contagem1[palavra] = contagem1.get(palavra, 0) + 1
        
        for palavra, contagem in sorted(contagem1.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"- '{palavra}': {contagem} ocorrências")
    
    if palavras_exclusivas2:
        print("\nPalavras mais comuns apenas no texto de referência:")
        contagem2 = {}
        for palavra in palavras2:
            if palavra in palavras_exclusivas2:
                contagem2[palavra] = contagem2.get(palavra, 0) + 1
        
        for palavra, contagem in sorted(contagem2.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"- '{palavra}': {contagem} ocorrências")
    
    # Análise de legibilidade comparativa
    silabas1 = estimar_silabas(palavras1)
    silabas2 = estimar_silabas(palavras2)
    
    frases1 = [f.strip() for f in texto1.replace("!", ".").replace("?", ".").split(".") if f.strip()]
    frases2 = [f.strip() for f in texto2.replace("!", ".").replace("?", ".").split(".") if f.strip()]
    
    if frases1 and frases2:
        palavras_por_frase1 = num_palavras1 / len(frases1)
        palavras_por_frase2 = num_palavras2 / len(frases2)
        
        print("\nComparação de estrutura:")
        print(f"Texto principal: {palavras_por_frase1:.1f} palavras por frase")
        print(f"Texto de referência: {palavras_por_frase2:.1f} palavras por frase")
        
        if abs(palavras_por_frase1 - palavras_por_frase2) > 5:
            print("Os textos apresentam estruturas de frase significativamente diferentes.")
        else:
            print("Os textos apresentam estruturas de frase similares.")
    
    # Análise de tom e estilo
    if num_palavras1 > 0 and num_palavras2 > 0:
        # Palavras longas
        palavras_longas1 = sum(1 for p in palavras1 if len(p) > 6) / num_palavras1
        palavras_longas2 = sum(1 for p in palavras2 if len(p) > 6) / num_palavras2
        
        print("\nComparação de estilo:")
        print(f"Texto principal: {palavras_longas1*100:.1f}% de palavras longas")
        print(f"Texto de referência: {palavras_longas2*100:.1f}% de palavras longas")
        
        if abs(palavras_longas1 - palavras_longas2) > 0.1:
            print("Os textos apresentam diferenças significativas na complexidade do vocabulário.")
        else:
            print("Os textos apresentam complexidade de vocabulário similar.")

# Execução do exemplo
if __name__ == "__main__":
    analisador_textos()