# Convertendo para inteiro
idade = int(input("Digite sua idade: "))

# Convertendo para float
altura = float(input("Digite sua altura em metros: "))

# Tratando possíveis erros de conversão
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Isso não é um número inteiro válido!")