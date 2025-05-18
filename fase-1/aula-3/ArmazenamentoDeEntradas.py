# Entrada básica
nome = input("Digite seu nome: ")
idade_str = input("Digite sua idade: ")
idade = int(idade_str)# Conversão para processamento
# Validação de entrada
while True:
    try:
        altura_str = input("Digite sua altura em metros: ")
        altura = float(altura_str)
        if 0.5 <= altura <= 2.5:# Validação de valores plausíveis
            break
        else:
            print("Altura fora do intervalo razoável. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Entradas com valores padrão
resposta = input("Deseja prosseguir? (S/N) [S]: ").strip().upper()
prosseguir = resposta if resposta in ["S", "N"] else "S"

# Entradas múltiplas
valores_str = input("Digite vários números separados por espaço: ")
valores = [int(x) for x in valores_str.split()]