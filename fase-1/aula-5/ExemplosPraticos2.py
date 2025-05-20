# Definir mensagem com base em uma condição
preco = 85.0
desconto = 10.0 if preco > 100 else 5.0
preco_final = preco - desconto
print(f"Preço: R$ {preco:.2f}, Desconto: R$ {desconto:.2f}, Final: R$ {preco_final:.2f}")

# Validação de entrada com valor padrão
entrada = input("Digite um número (ou Enter para valor padrão): ")
numero = int(entrada) if entrada.strip() else 0
print(f"Número: {numero}")

# Tratamento de erro simplificado
divisor = float(input("Digite o divisor: "))
resultado = "Divisão impossível" if divisor == 0 else 10 / divisor
print(f"Resultado: {resultado}")

# Determinação da paridade em mapeamento
numeros = [1, 2, 3, 4, 5]
paridade = ["Par" if n % 2 == 0 else "Ímpar" for n in numeros]
print(paridade)# ['Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar']