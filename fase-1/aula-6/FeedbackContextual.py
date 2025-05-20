def cadastrar_usuario():
    # Coleta de dados
    nome = input("Nome completo: ")
    email = input("Email: ")
    senha = input("Senha: ")
    confirma_senha = input("Confirme a senha: ")
    
    # Validação com feedback contextual
    if not nome.strip():
        print("Erro: O nome não pode estar em branco.")
        return False
    
    if len(nome.split()) < 2:
        print("Erro: Por favor, insira seu nome completo (nome e sobrenome).")
        return False
    
    if "@" not in email or "." not in email:
        print("Erro: Email inválido. Certifique-se de incluir '@' e '.'")
        return False
    
    if len(senha) < 8:
        print("Erro: A senha deve ter pelo menos 8 caracteres.")
        return False
    
    if senha != confirma_senha:
        print("Erro: As senhas não correspondem. Por favor, verifique.")
        return False
    
    # Cadastro bem-sucedido
    print(f"\nSucesso! Usuário {nome} cadastrado com o email {email}.")
    print("Um email de confirmação foi enviado. Por favor, verifique sua caixa de entrada.")
    return True