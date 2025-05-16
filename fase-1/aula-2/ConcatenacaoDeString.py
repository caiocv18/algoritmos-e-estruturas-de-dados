# Usando o operador +
primeiro_nome = "João"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome  # "João Silva"

# Usando o método join()
palavras = ["Python", "é", "incrível"]
frase = " ".join(palavras)  # "Python é incrível"

# Usando formatação com %
template = "Olá, %s! Você tem %d anos."
mensagem = template % ("Ana", 25)  # "Olá, Ana! Você tem 25 anos."

# Usando o método format()
template = "Olá, {}! Você tem {} anos."
mensagem = template.format("Ana", 25)  # "Olá, Ana! Você tem 25 anos."

# Usando f-strings (Python 3.6+, recomendado)
nome = "Ana"
idade = 25
mensagem = f"Olá, {nome}! Você tem {idade} anos."  # "Olá, Ana! Você tem 25 anos."