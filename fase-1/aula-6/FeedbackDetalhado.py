def calcular_estatisticas(dados, coluna):
    """Calcula estatísticas para uma coluna específica, com tratamento abrangente de erros."""
    resultados = {
        "sucesso": False,
        "mensagem": "",
        "estatisticas": {},
        "erros": []
    }
    
    # Verificação de dados vazios
    if not dados:
        resultados["mensagem"] = "Os dados estão vazios."
        resultados["erros"].append({
            "tipo": "DadosVazios",
            "mensagem": "Não há registros para processar.",
            "resolucao": "Verifique se o arquivo de dados contém registros."
        })
        return resultados
    
    # Verificação da existência da coluna
    if coluna not in dados[0]:
        resultados["mensagem"] = f"Coluna '{coluna}' não encontrada nos dados."
        resultados["erros"].append({
            "tipo": "ColunaInexistente",
            "mensagem": f"A coluna '{coluna}' não existe nos dados.",
            "resolucao": f"Verifique se o nome da coluna está correto. Colunas disponíveis: {', '.join(dados[0].keys())}"
        })
        return resultados
    
    # Extração dos valores da coluna
    try:
        valores = []
        valores_invalidos = []
        
        for i, registro in enumerate(dados):
            try:
                # Verificação de valor ausente
                if registro[coluna] == "" or registro[coluna] is None:
                    valores_invalidos.append({
                        "linha": i + 1,
                        "valor": registro[coluna],
                        "erro": "Valor ausente"
                    })
                    continue
                
                # Conversão para numérico, se necessário
                if isinstance(registro[coluna], (int, float)):
                    valor = registro[coluna]
                else:
                    valor = float(registro[coluna])
                
                valores.append(valor)
                
            except ValueError:
                valores_invalidos.append({
                    "linha": i + 1,
                    "valor": registro[coluna],
                    "erro": "Valor não numérico"
                })
            except Exception as e:
                valores_invalidos.append({
                    "linha": i + 1,
                    "valor": registro[coluna],
                    "erro": str(e)
                })
        
        # Verificação se há valores válidos
        if not valores:
            resultados["mensagem"] = f"Não foi possível extrair valores numéricos da coluna '{coluna}'."
            resultados["erros"].append({
                "tipo": "DadosInvalidos",
                "mensagem": "Todos os valores da coluna são inválidos ou não numéricos.",
                "resolucao": "Verifique se a coluna contém valores numéricos válidos."
            })
            return resultados
        
        # Cálculo das estatísticas
        resultados["estatisticas"]["contagem"] = len(valores)
        resultados["estatisticas"]["soma"] = sum(valores)
        resultados["estatisticas"]["media"] = resultados["estatisticas"]["soma"] / resultados["estatisticas"]["contagem"]
        resultados["estatisticas"]["minimo"] = min(valores)
        resultados["estatisticas"]["maximo"] = max(valores)
        
        # Cálculo do desvio padrão
        if len(valores) > 1:
            media = resultados["estatisticas"]["media"]
            soma_quadrados_diferencas = sum((x - media) ** 2 for x in valores)
            resultados["estatisticas"]["variancia"] = soma_quadrados_diferencas / len(valores)
            resultados["estatisticas"]["desvio_padrao"] = resultados["estatisticas"]["variancia"] ** 0.5
        else:
            resultados["estatisticas"]["variancia"] = 0
            resultados["estatisticas"]["desvio_padrao"] = 0
        
        # Informações sobre valores inválidos
        if valores_invalidos:
            resultados["mensagem"] = f"Estatísticas calculadas para {len(valores)} valores. {len(valores_invalidos)} valores inválidos foram ignorados."
            resultados["erros"].append({
                "tipo": "ValoresIgnorados",
                "mensagem": f"{len(valores_invalidos)} valores foram ignorados por serem inválidos.",
                "resolucao": "Verifique os detalhes dos valores inválidos para corrigir os dados.",
                "detalhes": valores_invalidos[:10]  # Limita a 10 exemplos para não sobrecarregar
            })
        else:
            resultados["mensagem"] = f"Estatísticas calculadas com sucesso para {len(valores)} valores."
        
        resultados["sucesso"] = True
        return resultados
        
    except Exception as e:
        resultados["mensagem"] = f"Erro ao calcular estatísticas: {str(e)}"
        resultados["erros"].append({
            "tipo": "ErroInesperado",
            "mensagem": str(e),
            "resolucao": "Entre em contato com o suporte técnico caso o erro persista."
        })
        return resultados