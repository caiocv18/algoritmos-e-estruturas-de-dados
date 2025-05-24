def calcular_frete(peso, distancia):
    """
    Calcula o valor do frete baseado no peso e distância.

    Esta função implementa uma fórmula simples para cálculo
    de frete, considerando um valor base por quilograma
    e um adicional por quilômetro de distância.

    Fórmula: frete = (peso * 2) + (distancia * 0.5)
    """
    valor_por_kg = 2.0
    valor_por_km = 0.5
    frete = (peso * valor_por_kg) + (distancia * valor_por_km)
    return frete

# Acessando a documentação
print(calcular_frete.__doc__)
help(calcular_frete)