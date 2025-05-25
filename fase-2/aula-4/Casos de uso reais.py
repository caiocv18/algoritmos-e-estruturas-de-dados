# 1. Processamento de log de vendas
def analisar_vendas(vendas):
    """
    Analisa uma lista de vendas e retorna estatísticas
    vendas: lista de tuplas (produto, quantidade, preco)
    """
    total_vendas = len(vendas)
    receita_total = sum(qtd * preco for _, qtd, preco in vendas)

    # Produtos mais vendidos
    produtos_qtd = {}
    for produto, qtd, _ in vendas:
        produtos_qtd[produto] = produtos_qtd.get(produto, 0) + qtd

    mais_vendido = max(produtos_qtd.items(), key=lambda x: x[1])

    return {
        'total_vendas': total_vendas,
        'receita_total': receita_total,
        'produto_mais_vendido': mais_vendido[0],
        'quantidade_mais_vendida': mais_vendido[1]
    }

# 2. Sistema de recomendação simples
def recomendar_produtos(historico_cliente, catalogo, n=5):
    """
    Recomenda produtos baseado no histórico de compras
    """
    # Contar categorias compradas
    categorias_compradas = {}
    for produto in historico_cliente:
        cat = produto['categoria']
        categorias_compradas[cat] = categorias_compradas.get(cat, 0) + 1

    # Ordenar categorias por preferência
    preferencias = sorted(categorias_compradas.items(),
                         key=lambda x: x[1], reverse=True)

    # Recomendar produtos não comprados das categorias preferidas
    recomendacoes = []
    produtos_comprados = {p['id'] for p in historico_cliente}

    for categoria, _ in preferencias:
        for produto in catalogo:
            if (produto['categoria'] == categoria and
                produto['id'] not in produtos_comprados and
                len(recomendacoes) < n):
                recomendacoes.append(produto)

    return recomendacoes

# 3. Análise de texto
def analisar_texto(texto):
    """
    Analisa um texto e retorna estatísticas
    """
    palavras = texto.lower().split()

    # Remover pontuação
    import string
    palavras = [p.strip(string.punctuation) for p in palavras]

    # Estatísticas
    total_palavras = len(palavras)
    palavras_unicas = len(set(palavras))

    # Frequência de palavras
    frequencia = {}
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1

    # Top 10 palavras mais comuns
    mais_comuns = sorted(frequencia.items(),
                        key=lambda x: x[1], reverse=True)[:10]

    return {
        'total_palavras': total_palavras,
        'palavras_unicas': palavras_unicas,
        'palavras_mais_comuns': mais_comuns,
        'diversidade_lexical': palavras_unicas / total_palavras
    }
