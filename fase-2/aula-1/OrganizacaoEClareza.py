def validar_cpf(cpf):
    """Valida um número de CPF."""
# Implementação da validação
    pass

def formatar_cpf(cpf):
    """Formata um CPF para exibição."""
# Implementação da formatação
    pass

def processar_cliente(nome, cpf):
    """Processa dados de um novo cliente."""
    if validar_cpf(cpf):
        cpf_formatado = formatar_cpf(cpf)
        print(f"Cliente {nome} cadastrado com CPF {cpf_formatado}")
    else:
        print("CPF inválido!")