def calcular_idade(ano_nascimento):
    """
    Calcula idade baseada no ano de nascimento.

    Args:
        ano_nascimento: Ano de nascimento

    Returns:
        int: Idade calculada

    Raises:
        ValueError: Se o ano for inválido
    """
    from datetime import datetime

# Validações
    ano_atual = datetime.now().year

    if not isinstance(ano_nascimento, int):
        raise TypeError("Ano de nascimento deve ser um número inteiro")

    if ano_nascimento > ano_atual:
        raise ValueError("Ano de nascimento não pode ser no futuro")

    if ano_nascimento < 1900:
        raise ValueError("Ano de nascimento muito antigo (mínimo: 1900)")

    idade = ano_atual - ano_nascimento
    return idade

# Testando validações
try:
    idade = calcular_idade(1990)
    print(f"Idade: {idade} anos")

    idade = calcular_idade("1990")# TypeError
except TypeError as e:
    print(f"Erro de tipo: {e}")
except ValueError as e:
    print(f"Erro de valor: {e}")

# Exemplo completo - Processador de pagamentos
def processar_pagamento(valor, metodo, detalhes=None):
    """
    Processa um pagamento com validações robustas.

    Args:
        valor: Valor do pagamento
        metodo: Método de pagamento (cartao, pix, boleto)
        detalhes: Detalhes específicos do método
    """
# Validação do valor
    if not isinstance(valor, (int, float)):
        raise TypeError("Valor deve ser numérico")

    if valor <= 0:
        raise ValueError("Valor deve ser positivo")

    if valor > 10000:
        raise ValueError("Valor excede limite de R$ 10.000")

# Validação do método
    metodos_validos = ["cartao", "pix", "boleto"]
    if metodo not in metodos_validos:
        raise ValueError(f"Método inválido. Use: {', '.join(metodos_validos)}")

# Validações específicas por método
    if metodo == "cartao" and detalhes:
        if "numero" not in detalhes:
            raise ValueError("Número do cartão é obrigatório")

        if len(detalhes["numero"].replace(" ", "")) != 16:
            raise ValueError("Número do cartão deve ter 16 dígitos")

    print(f"✅ Pagamento de R$ {valor:.2f} via {metodo} processado!")
    return True

# Testando
try:
    processar_pagamento(100, "pix")
    processar_pagamento(500, "cartao", {"numero": "1234 5678 9012 3456"})
    processar_pagamento(-50, "pix")# Erro!
except (TypeError, ValueError) as e:
    print(f"❌ Erro no processamento: {e}")