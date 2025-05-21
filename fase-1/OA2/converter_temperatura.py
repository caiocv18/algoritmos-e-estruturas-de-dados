def converter_temperatura(valor, unidade_origem, unidade_destino):
    """
    Converte temperaturas entre diferentes unidades.

    Parâmetros:
        valor (float): O valor da temperatura a ser convertida
        unidade_origem (str): A unidade de origem ('C', 'F' ou 'K')
        unidade_destino (str): A unidade de destino ('C', 'F' ou 'K')

    Retorno:
        float: O valor convertido para a unidade de destino
    """
    # Primeiro, converter para Celsius como unidade intermediária
    if unidade_origem == 'C':
        celsius = valor
    elif unidade_origem == 'F':
        celsius = (valor - 32) * 5/9
    elif unidade_origem == 'K':
        celsius = valor - 273.15
    else:
        raise ValueError("Unidade de origem inválida. Use 'C', 'F' ou 'K'.")

    # Depois, converter de Celsius para a unidade de destino
    if unidade_destino == 'C':
        return celsius
    elif unidade_destino == 'F':
        return (celsius * 9/5) + 32
    elif unidade_destino == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Unidade de destino inválida. Use 'C', 'F' ou 'K'.")
