# Impressão básica
print("Olá, mundo!")                     # Exibe: Olá, mundo!

# Variáveis em print
nome = "Maria"
idade = 25
print("Nome:", nome, "Idade:", idade)    # Exibe: Nome: Maria Idade: 25

# Formatação de strings (f-strings)
print(f"{nome} tem {idade} anos.")       # Exibe: Maria tem 25 anos.

# Múltiplos argumentos
print("Um", "Dois", "Três")             # Exibe: Um Dois Três

# Personalização do separador
print("Um", "Dois", "Três", sep="-")    # Exibe: Um-Dois-Três

# Controlando quebra de linha
print("Linha 1", end=" >>> ")           # Não quebra a linha
print("Linha 2")                        # Exibe: Linha 1 >>> Linha 2