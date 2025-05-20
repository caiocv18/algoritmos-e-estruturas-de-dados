# Validação de login
usuario = input("Nome de usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "123456":
    print("Login bem-sucedido.")
else:
    print("Usuário ou senha incorretos.")

# Processamento condicional
pagamento = float(input("Valor do pagamento: R$ "))
metodo = input("Método de pagamento (dinheiro/cartão): ").lower()

if metodo == "dinheiro":
    desconto = pagamento * 0.1
    valor_final = pagamento - desconto
    print(f"Desconto de R$ {desconto:.2f}")
else:
    valor_final = pagamento
    print("Não há desconto para pagamento com cartão")

print(f"Valor final: R$ {valor_final:.2f}")

# Tratamento de erros simples
try:
    valor = float(input("Digite um número: "))
    if valor > 0:
        raiz = valor ** 0.5
        print(f"A raiz quadrada é: {raiz:.2f}")
    else:
        print("Impossível calcular raiz de número negativo")
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")