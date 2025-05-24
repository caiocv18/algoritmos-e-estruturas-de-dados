# Contador de operações
operacoes_realizadas = 0

def realizar_operacao(tipo):
    """Realiza operação e atualiza contador global."""
    global operacoes_realizadas

    print(f"Executando operação: {tipo}")
    operacoes_realizadas += 1
    print(f"Total de operações: {operacoes_realizadas}")

# Testando
realizar_operacao("salvar")
realizar_operacao("deletar")
realizar_operacao("atualizar")
print(f"\nOperações totais realizadas: {operacoes_realizadas}")

# Exemplo mais complexo - Sistema de cache
cache_requisicoes = {}
hits = 0
misses = 0

def buscar_com_cache(chave):
    """Busca valor com sistema de cache."""
    global hits, misses

    if chave in cache_requisicoes:
        hits += 1
        print(f"Cache HIT! Valor: {cache_requisicoes[chave]}")
        return cache_requisicoes[chave]
    else:
        misses += 1
        print(f"Cache MISS! Buscando valor...")
# Simula busca em banco de dados
        valor = f"Dados de {chave}"
        cache_requisicoes[chave] = valor
        return valor

# Usando o cache
buscar_com_cache("usuario_1")
buscar_com_cache("usuario_2")
buscar_com_cache("usuario_1")# Hit!
buscar_com_cache("usuario_3")

print(f"\nEstatísticas do cache:")
print(f"  Hits: {hits}")
print(f"  Misses: {misses}")
print(f"  Taxa de acerto: {hits/(hits+misses)*100:.1f}%")