def processador_transacoes_financeiras():
    """
    Sistema simplificado para processamento de transações financeiras.
    """
    print("\n===== PROCESSADOR DE TRANSAÇÕES FINANCEIRAS =====")
    
    # Inicialização de contas
    contas = {
        "12345": {"titular": "João Silva", "saldo": 1500.0, "limite": 2000.0, "tipo": "corrente"},
        "67890": {"titular": "Maria Santos", "saldo": 3500.0, "limite": 4000.0, "tipo": "corrente"},
        "54321": {"titular": "Pedro Oliveira", "saldo": 10000.0, "limite": 0.0, "tipo": "poupança"},
        "09876": {"titular": "Ana Pereira", "saldo": 5000.0, "limite": 3000.0, "tipo": "corrente"},
        "24680": {"titular": "Carlos Ferreira", "saldo": 7500.0, "limite": 0.0, "tipo": "poupança"}
    }
    
    # Histórico de transações
    transacoes = []
    
    while True:
        print("\nOpções:")
        print("1. Consultar saldo")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Transferência entre contas")
        print("5. Extrato de conta")
        print("6. Relatório de transações")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            consultar_saldo(contas)
        elif opcao == "2":
            realizar_deposito(contas, transacoes)
        elif opcao == "3":
            realizar_saque(contas, transacoes)
        elif opcao == "4":
            realizar_transferencia(contas, transacoes)
        elif opcao == "5":
            gerar_extrato(contas, transacoes)
        elif opcao == "6":
            relatorio_transacoes(transacoes)
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def consultar_saldo(contas):
    """Consulta o saldo de uma conta."""
    print("\n--- Consulta de Saldo ---")
    
    num_conta = input("Digite o número da conta: ")
    
    if num_conta in contas:
        conta = contas[num_conta]
        print(f"\nTitular: {conta['titular']}")
        print(f"Tipo de conta: {conta['tipo'].capitalize()}")
        print(f"Saldo atual: R$ {conta['saldo']:.2f}")
        
        if conta['tipo'] == "corrente" and conta['limite'] > 0:
            print(f"Limite de cheque especial: R$ {conta['limite']:.2f}")
            print(f"Disponível para saque: R$ {conta['saldo'] + conta['limite']:.2f}")
    else:
        print("Erro: Conta não encontrada.")

def realizar_deposito(contas, transacoes):
    """Realiza um depósito em uma conta."""
    print("\n--- Depósito ---")
    
    num_conta = input("Digite o número da conta para depósito: ")
    
    if num_conta not in contas:
        print("Erro: Conta não encontrada.")
        return
    
    try:
        valor = float(input("Digite o valor do depósito: R$ "))
        
        if valor <= 0:
            print("Erro: O valor do depósito deve ser positivo.")
            return
        
    except ValueError:
        print("Erro: Valor inválido.")
        return
    
    # Processamento do depósito
    saldo_anterior = contas[num_conta]["saldo"]
    contas[num_conta]["saldo"] += valor
    
    # Registro da transação
    transacao = {
        "tipo": "depósito",
        "conta": num_conta,
        "valor": valor,
        "saldo_anterior": saldo_anterior,
        "saldo_atual": contas[num_conta]["saldo"],
        "data": "2023-07-10"  # Em uma aplicação real, usaríamos a data atual
    }
    
    transacoes.append(transacao)
    
    print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
    print(f"Novo saldo: R$ {contas[num_conta]['saldo']:.2f}")

def realizar_saque(contas, transacoes):
    """Realiza um saque de uma conta."""
    print("\n--- Saque ---")
    
    num_conta = input("Digite o número da conta para saque: ")
    
    if num_conta not in contas:
        print("Erro: Conta não encontrada.")
        return
    
    try:
        valor = float(input("Digite o valor do saque: R$ "))
        
        if valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")
            return
        
    except ValueError:
        print("Erro: Valor inválido.")
        return
    
    conta = contas[num_conta]
    saldo_anterior = conta["saldo"]
    
    # Verificação de saldo disponível (considerando limite para contas correntes)
    saldo_disponivel = conta["saldo"]
    if conta["tipo"] == "corrente":
        saldo_disponivel += conta["limite"]
    
    if valor > saldo_disponivel:
        print("Erro: Saldo insuficiente para este saque.")
        print(f"Saldo disponível para saque: R$ {saldo_disponivel:.2f}")
        return
    
    # Processamento do saque
    contas[num_conta]["saldo"] -= valor
    
    # Verificação de uso de cheque especial
    cheque_especial_usado = False
    if conta["tipo"] == "corrente" and contas[num_conta]["saldo"] < 0:
        cheque_especial_usado = True
    
    # Registro da transação
    transacao = {
        "tipo": "saque",
        "conta": num_conta,
        "valor": valor,
        "saldo_anterior": saldo_anterior,
        "saldo_atual": contas[num_conta]["saldo"],
        "cheque_especial_usado": cheque_especial_usado,
        "data": "2023-07-10"  # Em uma aplicação real, usaríamos a data atual
    }
    
    transacoes.append(transacao)
    
    print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")
    print(f"Novo saldo: R$ {contas[num_conta]['saldo']:.2f}")
    
    if cheque_especial_usado:
        print("Atenção: Você está utilizando seu limite de cheque especial.")

def realizar_transferencia(contas, transacoes):
    """Realiza uma transferência entre contas."""
    print("\n--- Transferência ---")
    
    num_conta_origem = input("Digite o número da conta de origem: ")
    
    if num_conta_origem not in contas:
        print("Erro: Conta de origem não encontrada.")
        return
    
    num_conta_destino = input("Digite o número da conta de destino: ")
    
    if num_conta_destino not in contas:
        print("Erro: Conta de destino não encontrada.")
        return
    
    if num_conta_origem == num_conta_destino:
        print("Erro: As contas de origem e destino não podem ser a mesma.")
        return
    
    try:
        valor = float(input("Digite o valor da transferência: R$ "))
        
        if valor <= 0:
            print("Erro: O valor da transferência deve ser positivo.")
            return
        
    except ValueError:
        print("Erro: Valor inválido.")
        return
    
    conta_origem = contas[num_conta_origem]
    saldo_anterior_origem = conta_origem["saldo"]
    
    # Verificação de saldo disponível (considerando limite para contas correntes)
    saldo_disponivel = conta_origem["saldo"]
    if conta_origem["tipo"] == "corrente":
        saldo_disponivel += conta_origem["limite"]
    
    if valor > saldo_disponivel:
        print("Erro: Saldo insuficiente para esta transferência.")
        print(f"Saldo disponível: R$ {saldo_disponivel:.2f}")
        return
    
    conta_destino = contas[num_conta_destino]
    saldo_anterior_destino = conta_destino["saldo"]
    
    # Processamento da transferência
    contas[num_conta_origem]["saldo"] -= valor
    contas[num_conta_destino]["saldo"] += valor
    
    # Verificação de uso de cheque especial
    cheque_especial_usado = False
    if conta_origem["tipo"] == "corrente" and contas[num_conta_origem]["saldo"] < 0:
        cheque_especial_usado = True
    
    # Registro da transação (origem)
    transacao_origem = {
        "tipo": "transferência (saída)",
        "conta": num_conta_origem,
        "conta_destino": num_conta_destino,
        "valor": valor,
        "saldo_anterior": saldo_anterior_origem,
        "saldo_atual": contas[num_conta_origem]["saldo"],
        "cheque_especial_usado": cheque_especial_usado,
        "data": "2023-07-10"  # Em uma aplicação real, usaríamos a data atual
    }
    
    # Registro da transação (destino)
    transacao_destino = {
        "tipo": "transferência (entrada)",
        "conta": num_conta_destino,
        "conta_origem": num_conta_origem,
        "valor": valor,
        "saldo_anterior": saldo_anterior_destino,
        "saldo_atual": contas[num_conta_destino]["saldo"],
        "data": "2023-07-10"  # Em uma aplicação real, usaríamos a data atual
    }
    
    transacoes.append(transacao_origem)
    transacoes.append(transacao_destino)
    
    print(f"\nTransferência de R$ {valor:.2f} realizada com sucesso.")
    print(f"Novo saldo na conta de origem: R$ {contas[num_conta_origem]['saldo']:.2f}")
    
    if cheque_especial_usado:
        print("Atenção: Você está utilizando seu limite de cheque especial.")

def gerar_extrato(contas, transacoes):
    """Gera um extrato de uma conta."""
    print("\n--- Extrato ---")
    
    num_conta = input("Digite o número da conta: ")
    
    if num_conta not in contas:
        print("Erro: Conta não encontrada.")
        return
    
    # Filtrar transações da conta
    transacoes_conta = [t for t in transacoes if t["conta"] == num_conta]
    
    if not transacoes_conta:
        print("Não há transações registradas para esta conta.")
        return
    
    # Exibição do extrato
    conta = contas[num_conta]
    print(f"\nEXTRATO DE CONTA - {conta['titular']}")
    print(f"Conta: {num_conta} ({conta['tipo'].capitalize()})")
    print(f"Data: 2023-07-10")  # Em uma aplicação real, usaríamos a data atual
    print("\n" + "-" * 60)
    print(f"{'Data':<12} {'Tipo':<20} {'Valor':<12} {'Saldo':<12}")
    print("-" * 60)
    
    for t in transacoes_conta:
        tipo = t["tipo"]
        valor_texto = f"R$ {t['valor']:.2f}"
        
        # Formatação diferente baseada no tipo de transação
        if "saída" in tipo:
            valor_texto = f"-{valor_texto}"
        elif "entrada" in tipo or tipo == "depósito":
            valor_texto = f"+{valor_texto}"
        
        print(f"{t['data']:<12} {tipo:<20} {valor_texto:<12} R$ {t['saldo_atual']:.2f}")
    
    print("-" * 60)
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    
    if conta['tipo'] == "corrente" and conta['limite'] > 0:
        disponivel = conta['saldo'] + conta['limite']
        print(f"Limite de cheque especial: R$ {conta['limite']:.2f}")
        print(f"Total disponível para saque: R$ {disponivel:.2f}")
        
        if conta['saldo'] < 0:
            print(f"Atenção: Você está utilizando R$ {-conta['saldo']:.2f} do seu limite.")

def relatorio_transacoes(transacoes):
    """Gera um relatório de transações."""
    print("\n--- Relatório de Transações ---")
    
    if not transacoes:
        print("Não há transações registradas.")
        return
    
    total_depositos = 0
    total_saques = 0
    total_transferencias = 0
    
    for t in transacoes:
        if t["tipo"] == "depósito":
            total_depositos += t["valor"]
        elif t["tipo"] == "saque":
            total_saques += t["valor"]
        elif t["tipo"] == "transferência (saída)":
            total_transferencias += t["valor"]
    
    print(f"\nResumo de transações:")
    print(f"Total de transações: {len(transacoes)}")
    print(f"Volume total de depósitos: R$ {total_depositos:.2f}")
    print(f"Volume total de saques: R$ {total_saques:.2f}")
    print(f"Volume total de transferências: R$ {total_transferencias:.2f}")
    
    # Análise de padrões
    print("\nAnálise de padrões:")
    
    # Contas mais ativas
    contas_frequencia = {}
    for t in transacoes:
        conta = t["conta"]
        contas_frequencia[conta] = contas_frequencia.get(conta, 0) + 1
    
    if contas_frequencia:
        conta_mais_ativa = max(contas_frequencia, key=contas_frequencia.get)
        print(f"Conta mais ativa: {conta_mais_ativa} ({contas_frequencia[conta_mais_ativa]} transações)")
    
    # Transações com uso de cheque especial
    transacoes_cheque_especial = [t for t in transacoes if t.get("cheque_especial_usado", False)]
    if transacoes_cheque_especial:
        print(f"Transações com uso de cheque especial: {len(transacoes_cheque_especial)}")
    
    # Ranking de tipos de transação
    tipos_transacao = {}
    for t in transacoes:
        tipo = t["tipo"]
        tipos_transacao[tipo] = tipos_transacao.get(tipo, 0) + 1
    
    print("\nRanking de tipos de transação:")
    for tipo, count in sorted(tipos_transacao.items(), key=lambda x: x[1], reverse=True):
        print(f"- {tipo}: {count} ocorrências")

# Execução do exemplo
if __name__ == "__main__":
    processador_transacoes_financeiras()