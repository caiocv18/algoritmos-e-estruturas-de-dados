# Tupla para demonstração
frutas = ('maçã', 'banana', 'laranja', 'banana', 'pera', 'banana')

# Método count() - conta ocorrências
contagem_banana = frutas.count('banana')
contagem_uva = frutas.count('uva')
print(f"Bananas: {contagem_banana}")  # 3
print(f"Uvas: {contagem_uva}")  # 0

# Método index() - encontra primeira ocorrência
try:
    indice_laranja = frutas.index('laranja')
    print(f"Laranja está no índice: {indice_laranja}")  # 2

    # index() com limites de busca
    segunda_banana = frutas.index('banana', 2)  # Busca a partir do índice 2
    print(f"Segunda banana no índice: {segunda_banana}")  # 3

    # Tentando encontrar item inexistente
    indice_uva = frutas.index('uva')
except ValueError as e:
    print(f"Erro: {e}")  # tuple.index(x): x not in tuple

# Implementando busca segura
def indice_seguro(tupla, item, padrao=-1):
    """Retorna o índice do item ou um valor padrão se não encontrado"""
    try:
        return tupla.index(item)
    except ValueError:
        return padrao

print(f"Índice de 'pera': {indice_seguro(frutas, 'pera')}")  # 4
print(f"Índice de 'uva': {indice_seguro(frutas, 'uva')}")  # -1
