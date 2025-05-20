def saida_contextual():
    """Demonstra saída contextual, que adapta o formato e detalhamento conforme o contexto."""
    
    # Dados de exemplo
    dados = {
        "nome": "Maria Silva",
        "idade": 35,
        "profissao": "Engenheira",
        "salario": 8500.0,
        "dependentes": 2,
        "ferias_acumuladas": 15,
        "nivel_acesso": "gerente"
    }
    
    # Contexto 1: Exibição para o próprio funcionário
    print("\n-- Visualização para o próprio funcionário --")
    exibir_dados_funcionario(dados, "proprio")
    
    # Contexto 2: Exibição para outro funcionário
    print("\n-- Visualização para outro funcionário --")
    exibir_dados_funcionario(dados, "colega")
    
    # Contexto 3: Exibição para o RH
    print("\n-- Visualização para o RH --")
    exibir_dados_funcionario(dados, "rh")
    
    # Contexto 4: Exibição para o diretor
    print("\n-- Visualização para o diretor --")
    exibir_dados_funcionario(dados, "diretor")

def exibir_dados_funcionario(dados, contexto):
    """Exibe dados do funcionário adaptados ao contexto do visualizador."""
    print(f"Funcionário: {dados['nome']}")
    
    # Dados básicos visíveis em todos os contextos
    print(f"Cargo: {dados['profissao']}")
    
    # Dados condicionais baseados no contexto
    if contexto in ["proprio", "rh", "diretor"]:
        print(f"Idade: {dados['idade']} anos")
        print(f"Dependentes: {dados['dependentes']}")
    
    if contexto in ["proprio", "rh", "diretor"]:
        print(f"Férias acumuladas: {dados['ferias_acumuladas']} dias")
    
    # Dados sensíveis - Salário
    if contexto == "proprio":
        print(f"Salário: R$ {dados['salario']:.2f}")
    elif contexto == "rh":
        print(f"Faixa salarial: R$ {dados['salario']:.2f} (Confidencial)")
    elif contexto == "diretor":
        print(f"Salário: R$ {dados['salario']:.2f}")
        if dados['salario'] > 7000:
            print("Observação: Salário acima da média para o cargo")
    
    # Informações adicionais conforme o contexto
    if contexto == "proprio":
        print("\nInformações adicionais:")
        print(f"- Você tem {dados['ferias_acumuladas']} dias de férias disponíveis")
        if dados['ferias_acumuladas'] > 10:
            print("- Recomendamos que você programe suas férias em breve")
    
    elif contexto == "rh":
        print("\nObservações para RH:")
        if dados['ferias_acumuladas'] > 10:
            print("- Funcionário com férias acumuladas (alerta)")
        if dados['dependentes'] > 0:
            print(f"- Possui {dados['dependentes']} dependentes (verificar benefícios)")
    
    elif contexto == "diretor":
        print("\nInformações gerenciais:")
        print(f"- Nível de acesso: {dados['nivel_acesso']}")
        print(f"- Custo mensal total: R$ {dados['salario'] * 1.8:.2f} (incluindo encargos)")