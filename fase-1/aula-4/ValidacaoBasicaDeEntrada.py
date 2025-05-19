# Validação simples: verificação de entrada vazia
while True:
    nome = input("Digite seu nome: ").strip()
    if nome:  # Verifica se a string não está vazia após remover espaços
        break
    print("Nome não pode estar vazio. Tente novamente.")

# Validação de tipo: garantindo entrada numérica
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade > 0:
            break
        print("A idade deve ser um número positivo.")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")

# Validação com padrão específico
import re

while True:
    email = input("Digite seu email: ")
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        break
    print("Email inválido. Use o formato: usuario@dominio.com")