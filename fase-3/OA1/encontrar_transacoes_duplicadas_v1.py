def encontrar_transacoes_duplicadas_v1(lista_ids_transacao):
    duplicadas = []
    vistos = [] # Armazena todos os IDs já vistos
    for id_transacao in lista_ids_transacao:
        if id_transacao in vistos: # 'in' em lista é O(k) onde k é o tamanho de 'vistos'
            if id_transacao not in duplicadas: # 'in' em lista é O(m) onde m é o tamanho de 'duplicadas'
                duplicadas.append(id_transacao)
        else:
            vistos.append(id_transacao)
    return duplicadas