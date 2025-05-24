def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal."""
    if altura <= 0 or peso <= 0:
        return None
    return peso / (altura ** 2)

# Fácil de testar isoladamente
print(calcular_imc(70, 1.75))# Teste 1
print(calcular_imc(0, 1.75))# Teste 2 - caso extremo
print(calcular_imc(80, 0))# Teste 3 - caso extremo