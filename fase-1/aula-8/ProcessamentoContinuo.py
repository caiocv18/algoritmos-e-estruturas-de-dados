# Servidor simples
while servidor_ativo:
    conexao = aguardar_conexao()
    processar_requisicao(conexao)