def calculadora_financeira():
    """Sistema de calculadora financeira com múltiplas funcionalidades."""
    
    while True:
        print("\n===== CALCULADORA FINANCEIRA =====")
        print("1. Juros Simples")
        print("2. Juros Compostos")
        print("3. Amortização")
        print("4. Valor Futuro de Investimento")
        print("5. Tempo para Atingir Valor")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            calcular_juros_simples()
        elif opcao == "2":
            calcular_juros_compostos()
        elif opcao == "3":
            calcular_amortizacao()
        elif opcao == "4":
            calcular_valor_futuro()
        elif opcao == "5":
            calcular_tempo_para_valor()
        elif opcao == "0":
            print("Encerrando a calculadora...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def obter_entrada_numerica(mensagem, minimo=None, maximo=None):
    """Solicita e valida entrada numérica dentro de um intervalo."""
    while True:
        try:
            valor = float(input(mensagem))
            
            if minimo is not None and valor < minimo:
                print(f"Erro: O valor deve ser maior ou igual a {minimo}.")
                continue
                
            if maximo is not None and valor > maximo:
                print(f"Erro: O valor deve ser menor ou igual a {maximo}.")
                continue
                
            return valor
        except ValueError:
            print("Erro: Por favor, digite um valor numérico válido.")

def formatar_moeda(valor):
    """Formata um valor como moeda."""
    return f"R$ {valor:,.2f}"

def calcular_juros_simples():
    """Calcula juros simples com base no principal, taxa e tempo."""
    print("\n-- Calculadora de Juros Simples --")
    
    try:
        principal = obter_entrada_numerica("Principal (valor inicial): R$ ", minimo=0)
        taxa_anual = obter_entrada_numerica("Taxa de juros anual (%): ", minimo=0)
        anos = obter_entrada_numerica("Período (anos): ", minimo=0)
        
        # Conversão da taxa percentual para decimal
        taxa_decimal = taxa_anual / 100
        
        # Cálculo de juros simples
        juros = principal * taxa_decimal * anos
        montante = principal + juros
        
        # Exibição dos resultados
        print("\nResultados:")
        print(f"Principal: {formatar_moeda(principal)}")
        print(f"Taxa de juros anual: {taxa_anual:.2f}%")
        print(f"Período: {anos:.2f} anos")
        print(f"Juros: {formatar_moeda(juros)}")
        print(f"Montante final: {formatar_moeda(montante)}")
        
    except Exception as e:
        print(f"Erro ao calcular juros simples: {e}")

def calcular_juros_compostos():
    """Calcula juros compostos com base no principal, taxa, tempo e periodicidade."""
    print("\n-- Calculadora de Juros Compostos --")
    
    try:
        principal = obter_entrada_numerica("Principal (valor inicial): R$ ", minimo=0)
        taxa_anual = obter_entrada_numerica("Taxa de juros anual (%): ", minimo=0)
        anos = obter_entrada_numerica("Período (anos): ", minimo=0)
        
        print("\nPeriodicidade de capitalização:")
        print("1. Anual")
        print("2. Semestral")
        print("3. Trimestral")
        print("4. Mensal")
        print("5. Diária")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        # Determinação da periodicidade
        if opcao == "1":
            periodicidade = 1
            desc_periodicidade = "anual"
        elif opcao == "2":
            periodicidade = 2
            desc_periodicidade = "semestral"
        elif opcao == "3":
            periodicidade = 4
            desc_periodicidade = "trimestral"
        elif opcao == "4":
            periodicidade = 12
            desc_periodicidade = "mensal"
        elif opcao == "5":
            periodicidade = 365
            desc_periodicidade = "diária"
        else:
            print("Opção inválida. Usando capitalização anual.")
            periodicidade = 1
            desc_periodicidade = "anual"
        
        # Conversão da taxa anual para a taxa por período
        taxa_periodo = (taxa_anual / 100) / periodicidade
        
        # Cálculo de juros compostos
        periodos = anos * periodicidade
        montante = principal * (1 + taxa_periodo) ** periodos
        juros = montante - principal
        
        # Exibição dos resultados
        print("\nResultados:")
        print(f"Principal: {formatar_moeda(principal)}")
        print(f"Taxa de juros anual: {taxa_anual:.2f}%")
        print(f"Capitalização: {desc_periodicidade}")
        print(f"Período: {anos:.2f} anos ({periodos:.0f} períodos)")
        print(f"Juros: {formatar_moeda(juros)}")
        print(f"Montante final: {formatar_moeda(montante)}")
        
        # Demonstração anual
        print("\nDemonstração de crescimento:")
        print(f"{'Ano':<6} {'Principal':<15} {'Juros':<15} {'Montante':<15}")
        print("-" * 55)
        
        valor_atual = principal
        for ano in range(1, min(int(anos) + 1, 11)):  # Limita a 10 anos para não ficar muito extenso
            montante_ano = principal * (1 + taxa_periodo) ** (ano * periodicidade)
            juros_ano = montante_ano - principal
            print(f"{ano:<6} {formatar_moeda(principal):<15} {formatar_moeda(juros_ano):<15} {formatar_moeda(montante_ano):<15}")
        
        if anos > 10:
            print("...(anos omitidos para brevidade)...")
            montante_final = principal * (1 + taxa_periodo) ** periodos
            juros_final = montante_final - principal
            print(f"{int(anos):<6} {formatar_moeda(principal):<15} {formatar_moeda(juros_final):<15} {formatar_moeda(montante_final):<15}")
        
    except Exception as e:
        print(f"Erro ao calcular juros compostos: {e}")

def calcular_amortizacao():
    """Calcula tabela de amortização para empréstimos."""
    print("\n-- Calculadora de Amortização --")
    
    try:
        principal = obter_entrada_numerica("Valor do empréstimo: R$ ", minimo=0)
        taxa_anual = obter_entrada_numerica("Taxa de juros anual (%): ", minimo=0)
        anos = obter_entrada_numerica("Prazo (anos): ", minimo=0)
        
        # Conversão para taxa mensal
        taxa_mensal = (taxa_anual / 100) / 12
        meses = int(anos * 12)
        
        # Cálculo da parcela mensal
        if taxa_mensal == 0:
            parcela = principal / meses
        else:
            parcela = principal * (taxa_mensal * (1 + taxa_mensal) ** meses) / ((1 + taxa_mensal) ** meses - 1)
        
        # Exibição dos detalhes do empréstimo
        print("\nDetalhes do Empréstimo:")
        print(f"Valor do empréstimo: {formatar_moeda(principal)}")
        print(f"Taxa de juros anual: {taxa_anual:.2f}%")
        print(f"Taxa de juros mensal: {taxa_mensal*100:.4f}%")
        print(f"Prazo: {anos:.1f} anos ({meses} meses)")
        print(f"Parcela mensal: {formatar_moeda(parcela)}")
        
        # Cálculo do total pago e juros totais
        total_pago = parcela * meses
        total_juros = total_pago - principal
        
        print(f"Total pago: {formatar_moeda(total_pago)}")
        print(f"Total de juros: {formatar_moeda(total_juros)}")
        
        # Perguntar se o usuário quer ver a tabela de amortização
        ver_tabela = input("\nDeseja ver a tabela de amortização? (s/n): ").lower() == 's'
        
        if ver_tabela:
            print("\nTabela de Amortização:")
            print(f"{'Mês':<5} {'Parcela':<15} {'Juros':<15} {'Amortização':<15} {'Saldo Devedor':<15}")
            print("-" * 70)
            
            saldo = principal
            for mes in range(1, meses + 1):
                # Mostrar apenas os primeiros 12 meses e os últimos 3 para não ficar muito extenso
                if mes <= 12 or mes > meses - 3:
                    juros_mes = saldo * taxa_mensal
                    amortizacao = parcela - juros_mes
                    saldo -= amortizacao
                    
                    print(f"{mes:<5} {formatar_moeda(parcela):<15} {formatar_moeda(juros_mes):<15} {formatar_moeda(amortizacao):<15} {formatar_moeda(max(0, saldo)):<15}")
                elif mes == 13:
                    print("...(meses omitidos para brevidade)...")
        
    except Exception as e:
        print(f"Erro ao calcular amortização: {e}")

def calcular_valor_futuro():
    """Calcula o valor futuro de um investimento com aportes regulares."""
    print("\n-- Calculadora de Valor Futuro --")
    
    try:
        aporte_inicial = obter_entrada_numerica("Aporte inicial: R$ ", minimo=0)
        aporte_mensal = obter_entrada_numerica("Aporte mensal: R$ ", minimo=0)
        taxa_anual = obter_entrada_numerica("Taxa de juros anual (%): ", minimo=0)
        anos = obter_entrada_numerica("Período (anos): ", minimo=0)
        
        # Conversão para taxa mensal
        taxa_mensal = (taxa_anual / 100) / 12
        meses = int(anos * 12)
        
        # Cálculo do valor futuro
        valor_futuro_aporte_inicial = aporte_inicial * (1 + taxa_mensal) ** meses
        
        # Cálculo dos aportes mensais (usando fórmula de soma de PG)
        if taxa_mensal > 0:
            valor_futuro_aportes = aporte_mensal * ((1 + taxa_mensal) ** meses - 1) / taxa_mensal
        else:
            valor_futuro_aportes = aporte_mensal * meses
        
        valor_futuro_total = valor_futuro_aporte_inicial + valor_futuro_aportes
        total_investido = aporte_inicial + (aporte_mensal * meses)
        juros_ganhos = valor_futuro_total - total_investido
        
        # Exibição dos resultados
        print("\nResultados:")
        print(f"Aporte inicial: {formatar_moeda(aporte_inicial)}")
        print(f"Aporte mensal: {formatar_moeda(aporte_mensal)}")
        print(f"Taxa de juros anual: {taxa_anual:.2f}%")
        print(f"Taxa de juros mensal: {taxa_mensal*100:.4f}%")
        print(f"Período: {anos:.1f} anos ({meses} meses)")
        print(f"Valor futuro do aporte inicial: {formatar_moeda(valor_futuro_aporte_inicial)}")
        print(f"Valor futuro dos aportes mensais: {formatar_moeda(valor_futuro_aportes)}")
        print(f"Valor futuro total: {formatar_moeda(valor_futuro_total)}")
        print(f"Total investido: {formatar_moeda(total_investido)}")
        print(f"Juros ganhos: {formatar_moeda(juros_ganhos)}")
        print(f"Rentabilidade: {(valor_futuro_total / total_investido - 1) * 100:.2f}%")
        
        # Demonstração da evolução anual
        print("\nEvolução do investimento:")
        print(f"{'Ano':<5} {'Saldo':<15} {'Total Investido':<20} {'Juros Acumulados':<20}")
        print("-" * 65)
        
        saldo = aporte_inicial
        investido = aporte_inicial
        
        for ano in range(1, int(anos) + 1):
            for mes in range(1, 13):
                if ano * 12 + mes <= meses:
                    saldo = saldo * (1 + taxa_mensal) + aporte_mensal
                    investido += aporte_mensal
            
            juros = saldo - investido
            print(f"{ano:<5} {formatar_moeda(saldo):<15} {formatar_moeda(investido):<20} {formatar_moeda(juros):<20}")
        
    except Exception as e:
        print(f"Erro ao calcular valor futuro: {e}")

def calcular_tempo_para_valor():
    """Calcula quanto tempo levará para atingir um valor alvo com investimentos regulares."""
    print("\n-- Calculadora de Tempo para Valor Alvo --")
    
    try:
        aporte_inicial = obter_entrada_numerica("Aporte inicial: R$ ", minimo=0)
        aporte_mensal = obter_entrada_numerica("Aporte mensal: R$ ", minimo=0)
        taxa_anual = obter_entrada_numerica("Taxa de juros anual (%): ", minimo=0)
        valor_alvo = obter_entrada_numerica("Valor alvo: R$ ", minimo=aporte_inicial)
        
        # Verificação se é possível atingir o valor alvo
        if aporte_mensal == 0 and (aporte_inicial >= valor_alvo or taxa_anual == 0):
            if aporte_inicial >= valor_alvo:
                print("\nO aporte inicial já é maior ou igual ao valor alvo.")
                return
            else:
                print("\nImpossível atingir o valor alvo sem aportes mensais e sem juros.")
                return
        
        # Conversão para taxa mensal
        taxa_mensal = (taxa_anual / 100) / 12
        
        # Cálculo do tempo necessário
        meses = 0
        saldo = aporte_inicial
        
        while saldo < valor_alvo and meses < 1200:  # Limite de 100 anos
            saldo = saldo * (1 + taxa_mensal) + aporte_mensal
            meses += 1
        
        if meses >= 1200:
            print("\nO tempo para atingir o valor alvo excede 100 anos ou é inatingível com os parâmetros fornecidos.")
            return
        
        anos = meses / 12
        total_investido = aporte_inicial + (aporte_mensal * meses)
        juros_ganhos = saldo - total_investido
        
        # Exibição dos resultados
        print("\nResultados:")
        print(f"Aporte inicial: {formatar_moeda(aporte_inicial)}")
        print(f"Aporte mensal: {formatar_moeda(aporte_mensal)}")
        print(f"Taxa de juros anual: {taxa_anual:.2f}%")
        print(f"Valor alvo: {formatar_moeda(valor_alvo)}")
        print(f"Tempo necessário: {anos:.2f} anos ({meses} meses)")
        print(f"Saldo final: {formatar_moeda(saldo)}")
        print(f"Total investido: {formatar_moeda(total_investido)}")
        print(f"Juros ganhos: {formatar_moeda(juros_ganhos)}")
        print(f"Participação dos juros: {(juros_ganhos / saldo) * 100:.2f}%")
        
    except Exception as e:
        print(f"Erro ao calcular tempo para valor: {e}")

# Execução da calculadora
if __name__ == "__main__":
    calculadora_financeira()