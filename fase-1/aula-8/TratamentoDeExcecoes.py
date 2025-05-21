def obter_numero_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Por favor, digite um valor positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def calcular_divisoes_sucessivas():
    numero = obter_numero_positivo("Digite um número para iniciar as divisões sucessivas: ")
    divisor = 2
    iteracoes = 0
    
    print(f"Iniciando com o número: {numero}")
    while numero > 0.01:  # Continua até o número ficar muito pequeno
        try:
            numero /= divisor
            iteracoes += 1
            print(f"Após divisão {iteracoes}: {numero:.4f}")
        except ZeroDivisionError:
            print("Erro: Divisão por zero!")
            divisor = obter_numero_positivo("Digite um novo divisor: ")

calcular_divisoes_sucessivas()