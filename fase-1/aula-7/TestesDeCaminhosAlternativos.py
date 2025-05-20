def validar_formulario(dados):
    """
    Valida um formulário com múltiplos campos e regras.
    Inclui verificação de caminhos alternativos para depuração.
    """
    print("\n=== Validação de Formulário ===")
    print("Iniciando validação com os seguintes dados:")
    for campo, valor in dados.items():
        print(f"- {campo}: {valor}")
    
    erros = []
    caminho = []  # Para rastrear o fluxo de execução
    
    # Validação de campos obrigatórios
    campos_obrigatorios = ["nome", "email", "telefone", "cpf"]
    for campo in campos_obrigatorios:
        caminho.append(f"Verificando campo obrigatório: {campo}")
        
        if campo not in dados or not dados[campo]:
            erros.append(f"Campo '{campo}' é obrigatório")
            caminho.append(f"Erro: campo '{campo}' ausente ou vazio")
    
    # Validação específica de email
    if "email" in dados and dados["email"]:
        caminho.append("Validando formato de email")
        
        email = dados["email"]
        if "@" not in email or "." not in email:
            erros.append("Email inválido")
            caminho.append("Erro: formato de email inválido")
        elif email.count("@") > 1:
            erros.append("Email inválido (múltiplos @)")
            caminho.append("Erro: email contém múltiplos @")
        elif email.split("@")[0] == "":
            erros.append("Email inválido (nome de usuário vazio)")
            caminho.append("Erro: nome de usuário vazio")
        elif "." not in email.split("@")[1]:
            erros.append("Email inválido (domínio sem ponto)")
            caminho.append("Erro: domínio sem ponto")
        else:
            caminho.append("Email válido")
    
    # Validação de idade
    if "idade" in dados:
        caminho.append("Validando idade")
        
        try:
            idade = int(dados["idade"])
            if idade < 18:
                erros.append("Idade deve ser maior ou igual a 18 anos")
                caminho.append("Erro: idade menor que 18")
            elif idade > 120:
                erros.append("Idade inválida")
                caminho.append("Erro: idade acima de 120")
            else:
                caminho.append("Idade válida")
        except ValueError:
            erros.append("Idade deve ser um número inteiro")
            caminho.append("Erro: idade não é um número inteiro")
    
    # Validação de senha e confirmação
    if "senha" in dados and "confirma_senha" in dados:
        caminho.append("Validando senha e confirmação")
        
        senha = dados["senha"]
        confirma = dados["confirma_senha"]
        
        if senha != confirma:
            erros.append("Senha e confirmação não correspondem")
            caminho.append("Erro: senha e confirmação diferentes")
        elif len(senha) < 6:
            erros.append("Senha deve ter pelo menos 6 caracteres")
            caminho.append("Erro: senha muito curta")
        else:
            tem_letra = any(c.isalpha() for c in senha)
            tem_numero = any(c.isdigit() for c in senha)
            
            if not (tem_letra and tem_numero):
                erros.append("Senha deve conter letras e números")
                caminho.append("Erro: senha sem letras ou números")
            else:
                caminho.append("Senha válida")
    
    # Validação de termos
    if "aceita_termos" in dados:
        caminho.append("Verificando aceitação de termos")
        
        if not dados["aceita_termos"]:
            erros.append("Você deve aceitar os termos de uso")
            caminho.append("Erro: termos não aceitos")
        else:
            caminho.append("Termos aceitos")
    
    # Resultado da validação
    print("\nCaminho de execução:")
    for i, passo in enumerate(caminho, 1):
        print(f"{i}. {passo}")
    
    print("\nResultado da validação:")
    if erros:
        print(f"Formulário inválido. {len(erros)} erro(s) encontrado(s):")
        for erro in erros:
            print(f"- {erro}")
        return False
    else:
        print("Formulário válido!")
        return True