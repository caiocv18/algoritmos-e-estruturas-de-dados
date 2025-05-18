mensagem = "  Olá, Mundo! "

# Métodos de transformação
print(mensagem.upper()) # "  OLÁ, MUNDO! "
print(mensagem.lower()) # "  olá, mundo! "
print(mensagem.strip()) # "Olá, Mundo!"
print(mensagem.replace('o', 'a')) # "  Olá, Munda! "
# Métodos de divisão e junção
palavras = "Python é incrível".split()
print(palavras) # ['Python', 'é', 'incrível']
print('-'.join(palavras)) # "Python-é-incrível"
# Métodos de busca
texto = "Python é uma linguagem de programação"
print(texto.find('linguagem')) # 11 (posição onde 'linguagem' começa)
print(texto.count('a')) # 5 (número de ocorrências de 'a')
# Métodos de verificação
print("python".startswith("py")) # True
print("python".endswith("on")) # True
print("123".isdigit()) # True
print("Python".isalpha()) # True
print("Python3".isalnum()) # True (alfanumérico)