# Obtendo o nome do usuário
nome = input("Digite seu nome: ")  # Exibe a mensagem e aguarda entrada
print(f"Olá, {nome}!")

# Importante: input() sempre retorna uma string
idade = input("Digite sua idade: ")  # idade será uma string, não um número
print(f"Daqui a 5 anos você terá {int(idade) + 5} anos.")  # Convertemos para inteiro