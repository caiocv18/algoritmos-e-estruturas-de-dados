def processamento_em_fases(dados):
    # Fase 1: Filtragem
    print("Fase 1: Filtragem")
    dados_filtrados = []
    for item in dados:
        if criterio_filtragem(item):
            dados_filtrados.append(item)
    print(f"  Dados após filtragem: {len(dados_filtrados)} itens")
    
    # Fase 2: Transformação
    print("Fase 2: Transformação")
    dados_transformados = []
    for item in dados_filtrados:
        dados_transformados.append(transformar_item(item))
    print(f"  Dados após transformação: {len(dados_transformados)} itens")
    
    # Fase 3: Agregação
    print("Fase 3: Agregação")
    resultado = agregar_dados(dados_transformados)
    print(f"  Resultado final: {resultado}")
    
    return resultado