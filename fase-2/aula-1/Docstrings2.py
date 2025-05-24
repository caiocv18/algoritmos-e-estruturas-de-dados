def processar_pagamento(valor, metodo, parcelas=1):
    """
    Processa um pagamento no sistema.

    Args:
        valor (float): Valor total do pagamento
        metodo (str): Método de pagamento ('cartao', 'boleto', 'pix')
        parcelas (int): Número de parcelas (padrão: 1)

    Returns:
        dict: Dicionário com os detalhes do pagamento processado

    Raises:
        ValueError: Se o valor for negativo ou método inválido

    Example:
        >>> processar_pagamento(100.0, 'pix')
        {'status': 'aprovado', 'valor': 100.0, 'metodo': 'pix'}
    """
# Implementação da função
    pass