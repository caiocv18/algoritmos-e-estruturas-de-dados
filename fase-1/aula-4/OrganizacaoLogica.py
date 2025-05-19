# Coleta e validação de dados
nome = obter_nome_valido()
idade = obter_idade_valida()
altura = obter_altura_valida()

# Cálculos e processamento
imc = calcular_imc(peso, altura)
classificacao = obter_classificacao(imc)
recomendacoes = gerar_recomendacoes(imc, idade, sexo)

# Apresentação dos resultados
mostrar_cabecalho(nome)
mostrar_resultados_imc(imc, classificacao)
mostrar_recomendacoes(recomendacoes)