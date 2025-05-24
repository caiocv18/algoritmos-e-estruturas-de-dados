def analisar_dados(dados):
    """
    Analisa um conjunto de dados e retorna estatísticas básicas.

    Esta função calcula média, mediana e desvio padrão
    de uma lista de números.
    """
# Verifica se a lista não está vazia
    if not dados:
        return None

# Ordena os dados para calcular a mediana
    dados_ordenados = sorted(dados)

# Calcula a média
    media = sum(dados) / len(dados)

# Calcula a mediana
    n = len(dados_ordenados)
    if n % 2 == 0:
        mediana = (dados_ordenados[n//2-1] + dados_ordenados[n//2]) / 2
    else:
        mediana = dados_ordenados[n//2]

    return {"media": media, "mediana": mediana}