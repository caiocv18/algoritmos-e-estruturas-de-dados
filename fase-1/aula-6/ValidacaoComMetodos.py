def validar_formulario(email, telefone, cpf):
    # Validação de email (simplificada)
    if not "@" in email or not "." in email:
        return False, "Email inválido"
    
    # Validação de telefone (somente dígitos, tamanho correto)
    telefone_digitos = ''.join(c for c in telefone if c.isdigit())
    if len(telefone_digitos) not in [10, 11]:
        return False, "Telefone deve ter 10 ou 11 dígitos"
    
    # Validação de CPF (somente verificação básica)
    cpf_digitos = ''.join(c for c in cpf if c.isdigit())
    if len(cpf_digitos) != 11:
        return False, "CPF deve ter 11 dígitos"
    
    return True, "Formulário válido"