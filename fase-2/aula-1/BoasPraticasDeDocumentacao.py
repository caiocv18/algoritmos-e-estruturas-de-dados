# EXEMPLO DE BOA DOCUMENTAÇÃO
def validar_cpf(cpf):
    """
    Valida um número de CPF brasileiro.

    Args:
        cpf (str): CPF a ser validado (com ou sem formatação)

    Returns:
        bool: True se o CPF é válido, False caso contrário

    Examples:
        >>> validar_cpf("123.456.789-10")
        True
        >>> validar_cpf("00000000000")
        False

    Note:
        Esta função remove automaticamente pontos e hífens
        antes da validação.
    """
# Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

# Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False

# Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

# Validação do algoritmo do CPF# ... implementação ...
    return True

# EXEMPLO DE DOCUMENTAÇÃO RUIM
def calc(x):
    """Calcula algo"""# Vago e não informativo# faz uns cálculos aí
    return x * 2