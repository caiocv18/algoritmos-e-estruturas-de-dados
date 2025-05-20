def conversor_temperatura():
    """
    Conversor de temperatura com múltiplas opções e validação.
    """
    print("\n===== CONVERSOR DE TEMPERATURA =====\n")

# Menu de opções
    print("Opções de conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Fahrenheit para Kelvin")
    print("6. Kelvin para Fahrenheit")

# Seleção da opção
    try:
        opcao = int(input("\nEscolha uma opção (1-6): "))
        if opcao < 1 or opcao > 6:
            print("Erro: Opção inválida. Escolha um número de 1 a 6.")
            return

# Entrada da temperatura
        temperatura = float(input("Digite o valor da temperatura: "))

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite valores numéricos.")
        return

# Conversão baseada na opção escolhida
    if opcao == 1:# Celsius para Fahrenheit
        unidade_origem = "Celsius"
        unidade_destino = "Fahrenheit"
        resultado = (temperatura * 9/5) + 32
        formula = "F = (C × 9/5) + 32"

    elif opcao == 2:# Fahrenheit para Celsius
        unidade_origem = "Fahrenheit"
        unidade_destino = "Celsius"
        resultado = (temperatura - 32) * 5/9
        formula = "C = (F - 32) × 5/9"

    elif opcao == 3:# Celsius para Kelvin
        unidade_origem = "Celsius"
        unidade_destino = "Kelvin"
        resultado = temperatura + 273.15
        formula = "K = C + 273.15"

    elif opcao == 4:# Kelvin para Celsius
        unidade_origem = "Kelvin"
        unidade_destino = "Celsius"
        resultado = temperatura - 273.15
        formula = "C = K - 273.15"

    elif opcao == 5:# Fahrenheit para Kelvin
        unidade_origem = "Fahrenheit"
        unidade_destino = "Kelvin"
        celsius_temp = (temperatura - 32) * 5/9
        resultado = celsius_temp + 273.15
        formula = "K = (F - 32) × 5/9 + 273.15"

    else:# Kelvin para Fahrenheit
        unidade_origem = "Kelvin"
        unidade_destino = "Fahrenheit"
        celsius_temp = temperatura - 273.15
        resultado = (celsius_temp * 9/5) + 32
        formula = "F = (K - 273.15) × 9/5 + 32"

# Exibição do resultado
    print("\n" + "=" * 40)
    print(f"CONVERSÃO DE {unidade_origem.upper()} PARA {unidade_destino.upper()}")
    print("=" * 40)
    print(f"Valor em {unidade_origem}: {temperatura:.2f}°")
    print(f"Valor em {unidade_destino}: {resultado:.2f}°")
    print(f"Fórmula utilizada: {formula}")

# Informações adicionais baseadas no resultado
    if unidade_destino == "Celsius":
        if resultado < 0:
            print("\nInformação: Temperatura abaixo do ponto de congelamento da água.")
        elif resultado == 0:
            print("\nInformação: Temperatura no ponto de congelamento da água.")
        elif resultado == 100:
            print("\nInformação: Temperatura no ponto de ebulição da água ao nível do mar.")
        elif resultado > 100:
            print("\nInformação: Temperatura acima do ponto de ebulição da água ao nível do mar.")

    elif unidade_destino == "Fahrenheit":
        if resultado < 32:
            print("\nInformação: Temperatura abaixo do ponto de congelamento da água.")
        elif resultado == 32:
            print("\nInformação: Temperatura no ponto de congelamento da água.")
        elif resultado == 212:
            print("\nInformação: Temperatura no ponto de ebulição da água ao nível do mar.")
        elif resultado > 212:
            print("\nInformação: Temperatura acima do ponto de ebulição da água ao nível do mar.")

    elif unidade_destino == "Kelvin":
        if resultado < 273.15:
            print("\nInformação: Temperatura abaixo do ponto de congelamento da água.")
        elif resultado == 273.15:
            print("\nInformação: Temperatura no ponto de congelamento da água.")
        elif resultado == 373.15:
            print("\nInformação: Temperatura no ponto de ebulição da água ao nível do mar.")
        elif resultado > 373.15:
            print("\nInformação: Temperatura acima do ponto de ebulição da água ao nível do mar.")
        elif resultado < 0:
            print("\nAlerta: Temperatura abaixo do zero absoluto (fisicamente impossível).")

    return opcao, temperatura, resultado

# Execução do programa
if __name__ == "__main__":
    conversor_temperatura()