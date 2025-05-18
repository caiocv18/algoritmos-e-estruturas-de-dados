# Usando AND para evitar erros (só executa o segundo se o primeiro for True)
lista = [1, 2, 3]
indice = 5
# Verifica se o índice é válido antes de acessar
elemento = indice < len(lista) and lista[indice]
print(elemento)# False (evitou o IndexError)
# Usando OR para valores padrão
nome = None
nome_display = nome or "Usuário"
print(nome_display)# "Usuário"