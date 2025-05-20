def validacao_contextual():
    """Demonstra validação contextual, que se adapta conforme a natureza dos dados."""
    
    # Exemplo 1: Validação de data
    print("\n-- Validação de Data --")
    while True:
        data = input("Digite uma data (DD/MM/AAAA): ")
        valido, feedback = validar_data(data)
        
        if valido:
            print(f"Data válida: {feedback}")
            break
        else:
            print(f"Erro: {feedback}")
    
    # Exemplo 2: Validação de email
    print("\n-- Validação de Email --")
    while True:
        email = input("Digite um email: ")
        valido, feedback = validar_email(email)
        
        if valido:
            print(f"Email válido: {feedback}")
            break
        else:
            print(f"Erro: {feedback}")
    
    # Exemplo 3: Validação de CPF
    print("\n-- Validação de CPF --")
    while True:
        cpf = input("Digite um CPF: ")
        valido, feedback = validar_cpf(cpf)
        
        if valido:
            print(f"CPF válido: {feedback}")
            break
        else:
            print(f"Erro: {feedback}")

def validar_data(data):
    """Valida uma data no formato DD/MM/AAAA."""
    # Verificação do formato
    if not isinstance(data, str) or len(data) != 10 or data[2] != '/' or data[5] != '/':
        return False, "Formato inválido. Use DD/MM/AAAA."
    
    try:
        dia, mes, ano = map(int, data.split('/'))
    except ValueError:
        return False, "A data deve conter apenas números e barras."
    
    # Validação básica dos valores
    if not (1 <= mes <= 12):
        return False, "Mês deve estar entre 1 e 12."
    
    # Validação de dias conforme o mês
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verificação de ano bissexto
    if mes == 2 and (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
        dias_no_mes = 29
    else:
        dias_no_mes = dias_por_mes[mes]
    
    if not (1 <= dia <= dias_no_mes):
        return False, f"Dia deve estar entre 1 e {dias_no_mes} para o mês {mes}."
    
    # Outras verificações contextuais
    if ano < 1900:
        return False, "O ano não deve ser anterior a 1900."
    
    # Data validada com sucesso
    data_formatada = f"{dia:02d}/{mes:02d}/{ano:04d}"
    return True, data_formatada

def validar_email(email):
    """Valida um endereço de email."""
    if not isinstance(email, str) or not email:
        return False, "Email não pode estar vazio."
    
    # Verificação de formato básico
    if '@' not in email or '.' not in email or email.count('@') > 1:
        return False, "Email deve conter um único @ e pelo menos um ponto."
    
    # Verificação de nome de usuário
    nome, dominio = email.split('@', 1)
    if not nome:
        return False, "Nome de usuário não pode estar vazio."
    
    # Verificação de domínio
    if '.' not in dominio:
        return False, "Domínio inválido. Deve conter pelo menos um ponto."
    
    # Verificação da extensão
    partes_dominio = dominio.split('.')
    if len(partes_dominio[-1]) < 2:
        return False, "Extensão de domínio inválida."
    
    for parte in partes_dominio:
        if not parte:
            return False, "O domínio contém partes vazias."
    
    # Email validado com sucesso
    return True, email

def validar_cpf(cpf):
    """Valida um CPF (implementação simplificada)."""
    # Remover caracteres não numéricos
    cpf_limpo = ''.join(c for c in cpf if c.isdigit())
    
    # Verificação de tamanho
    if len(cpf_limpo) != 11:
        return False, "CPF deve conter 11 dígitos."
    
    # Verificação de dígitos repetidos
    if cpf_limpo == cpf_limpo[0] * 11:
        return False, "CPF inválido (dígitos repetidos)."
    
    # Validação do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf_limpo[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        dv1 = 0
    else:
        dv1 = 11 - resto
    
    if int(cpf_limpo[9]) != dv1:
        return False, "CPF inválido (primeiro dígito verificador)."
    
    # Validação do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf_limpo[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        dv2 = 0
    else:
        dv2 = 11 - resto
    
    if int(cpf_limpo[10]) != dv2:
        return False, "CPF inválido (segundo dígito verificador)."
    
    # CPF validado com sucesso
    cpf_formatado = f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
    return True, cpf_formatado