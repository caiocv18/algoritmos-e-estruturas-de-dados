def calcular_estatisticas(numeros):
    """
    Calcula estatísticas básicas de uma lista de números.

    Parâmetros:
        numeros (list): Lista de números

    Retorno:
        dict: Dicionário contendo média, mediana e moda
    """
    # Verificar se a lista está vazia
    if not numeros:
        return {"media": None, "mediana": None, "moda": None}

    # Calcular média
    media = sum(numeros) / len(numeros)

    # Calcular mediana
    ordenados = sorted(numeros)
    n = len(ordenados)
    if n % 2 == 0:
        mediana = (ordenados[n//2 - 1] + ordenados[n//2]) / 2
    else:
        mediana = ordenados[n//2]

    # Calcular moda (valor mais frequente)
    contagem = {}
    for num in numeros:
        if num in contagem:
            contagem[num] += 1
        else:
            contagem[num] = 1

    max_frequencia = 0
    moda = None
    for num, freq in contagem.items():
        if freq > max_frequencia:
            max_frequencia = freq
            moda = num

    # Se todos os valores aparecem com a mesma frequência, não há moda
    if max_frequencia == 1:
        moda = None

    return {
        "media": media,
        "mediana": mediana,
        "moda": moda
    }