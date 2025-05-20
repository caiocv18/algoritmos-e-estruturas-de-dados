def realizar_operacao_resiliente():
    """Demonstra um sistema resiliente que tenta se recuperar de falhas."""
    
    MAX_TENTATIVAS = 3
    
    print("\n-- Sistema de Operação Resiliente --")
    
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        try:
            print(f"\nTentativa {tentativa} de {MAX_TENTATIVAS}")
            
            # Simulação de uma operação que pode falhar
            operacao = input("Digite a operação a realizar (soma/subtracao/multiplicacao/divisao): ").lower()
            
            if operacao not in ["soma", "subtracao", "multiplicacao", "divisao"]:
                print(f"Erro: Operação '{operacao}' não reconhecida.")
                continue
            
            # Entrada de valores
            try:
                a = float(input("Digite o primeiro valor: "))
                b = float(input("Digite o segundo valor: "))
            except ValueError:
                print("Erro: Os valores devem ser numéricos.")
                continue
            
            # Execução da operação
            resultado = None
            if operacao == "soma":
                resultado = a + b
            elif operacao == "subtracao":
                resultado = a - b
            elif operacao == "multiplicacao":
                resultado = a * b
            elif operacao == "divisao":
                if b == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
                resultado = a / b
            
            # Exibição do resultado
            print(f"\nResultado da operação: {resultado}")
            
            # Verificação de precisão (para divisões)
            if operacao == "divisao" and a % b != 0:
                print("Nota: O resultado é uma divisão com casas decimais.")
                precisao = input("Deseja ajustar a precisão decimal? (s/n): ").lower()
                if precisao == 's':
                    try:
                        casas = int(input("Digite o número de casas decimais: "))
                        if casas < 0:
                            print("Erro: O número de casas decimais deve ser positivo.")
                        else:
                            print(f"Resultado com {casas} casas decimais: {resultado:.{casas}f}")
                    except ValueError:
                        print("Erro: O número de casas decimais deve ser um inteiro.")
            
            # Operação bem-sucedida
            print("\nOperação realizada com sucesso!")
            
            # Pergunta se deseja realizar outra operação
            nova_operacao = input("Deseja realizar outra operação? (s/n): ").lower()
            if nova_operacao != 's':
                return True
            
        except Exception as e:
            print(f"\nErro inesperado: {str(e)}")
            
            if tentativa < MAX_TENTATIVAS:
                print("Tentando recuperar e continuar...")
            else:
                print("\nNúmero máximo de tentativas excedido.")
                print("Sugestões de recuperação:")
                print("1. Verifique se os valores de entrada são válidos.")
                print("2. Certifique-se de escolher uma operação válida.")
                print("3. Para divisão, certifique-se de que o divisor não é zero.")
                return False
    
    return True