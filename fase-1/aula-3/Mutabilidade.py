# Listas são mutáveis - podem ser modificadas após criação
lista = [1, 2, 3]
lista[0] = 10    # Modificar elemento específico
lista.append(4)  # Adicionar elemento
lista.remove(2)  # Remover elemento

# Tuplas são imutáveis - não podem ser modificadas após criação
tupla = (1, 2, 3)
# tupla[0] = 10  # Erro! Não pode modificar elemento
# tupla.append(4)# Erro! Não pode adicionar elemento
# tupla.remove(2)# Erro! Não pode remover elemento

# Implicações na performance e uso
# 1. Tuplas geralmente consomem menos memória
# 2. Tuplas podem ser usadas como chaves de dicionário, listas não
# 3. Tuplas são mais seguras para dados que não devem mudar