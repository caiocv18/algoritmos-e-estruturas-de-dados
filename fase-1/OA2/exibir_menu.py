def exibir_menu():
    """Exibe o menu de opções."""
    print("\n==== MENU DE ALGORITMOS ====")
    print("1. Converter temperatura")
    print("2. Verificar se um número é primo")
    print("3. Calcular estatísticas de uma lista")
    print("0. Sair")
    return input("Escolha uma opção: ")

def executar_menu():
    """Executa o menu interativo."""
    while True:
        opcao = exibir_menu()

        if opcao == '0':
            print("Encerrando o programa. Até mais!")
            break

        elif opcao == '1':
            try:
                valor = float(input("Digite o valor da temperatura: "))
                origem = input("Digite a unidade de origem (C, F ou K): ").upper()
                destino = input("Digite a unidade de destino (C, F ou K): ").upper()
                resultado = converter_temperatura(valor, origem, destino)
                print(f"{valor}{origem} equivale a {resultado:.2f}{destino}")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == '2':
            try:
                numero = int(input("Digite um número inteiro: "))
                if verificar_primo(numero):
                    print(f"{numero} é um número primo.")
                else:
                    print(f"{numero} não é um número primo.")
            except ValueError:
                print("Erro: Por favor, digite um número inteiro válido.")

        elif opcao == '3':
            try:
                entrada = input("Digite uma lista de números separados por espaço: ")
                numeros = [float(x) for x in entrada.split()]
                estatisticas = calcular_estatisticas(numeros)
                print(f"Média: {estatisticas['media']:.2f}")
                print(f"Mediana: {estatisticas['mediana']:.2f}")
                print(f"Moda: {estatisticas['moda'] if estatisticas['moda'] is not None else 'Não há moda'}")
            except ValueError:
                print("Erro: Entrada inválida. Certifique-se de digitar apenas números.")

        else:
            print("Opção inválida. Por favor, tente novamente.")

# Executar o menu se este arquivo for executado diretamente
if __name__ == "__main__":
    executar_menu()
