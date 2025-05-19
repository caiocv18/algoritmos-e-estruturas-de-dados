# Verificação de número par/ímpar
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")

# Verificação de elegibilidade para desconto
valor_compra = float(input("Digite o valor da compra: "))

if valor_compra >= 200:
    print("Você tem direito a um desconto de 10%!")
    valor_final = valor_compra * 0.9
    print(f"Valor com desconto: R$ {valor_final:.2f}")

# Validação de entrada
nome = input("Digite seu nome: ")

if len(nome) == 0:
    print("Por favor, digite um nome válido.")