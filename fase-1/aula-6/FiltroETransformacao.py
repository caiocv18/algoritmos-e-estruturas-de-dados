def analisar_vendas(produtos):
    # Filtragem: separar produtos por categoria
    tecnologia = []
    vestuario = []
    alimentos = []
    
    for produto in produtos:
        if produto["categoria"] == "tecnologia":
            tecnologia.append(produto)
        elif produto["categoria"] == "vestuario":
            vestuario.append(produto)
        elif produto["categoria"] == "alimentos":
            alimentos.append(produto)
    
    # Transformação: calcular total de vendas por categoria
    total_tecnologia = sum(produto["preco"] * produto["quantidade"] for produto in tecnologia)
    total_vestuario = sum(produto["preco"] * produto["quantidade"] for produto in vestuario)
    total_alimentos = sum(produto["preco"] * produto["quantidade"] for produto in alimentos)
    
    return {
        "tecnologia": total_tecnologia,
        "vestuario": total_vestuario,
        "alimentos": total_alimentos
    }