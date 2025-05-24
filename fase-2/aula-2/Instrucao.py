def calcular_area_circulo(raio):
    """
    Calcula a área de um círculo dado seu raio.

    Args:
        raio: Raio do círculo

    Returns:
        float: Área calculada
    """
    import math

    if raio <= 0:
        print("Erro: Raio deve ser positivo")
        return None

    area = math.pi * raio ** 2
    return area

# Usando o valor retornado
raio = 5
area = calcular_area_circulo(raio)
if area:
    print(f"A área do círculo com raio {raio} é {area:.2f}")

# Return pode aparecer em qualquer ponto da função
def validar_idade(idade):
    """Valida se a idade está em um intervalo aceitável."""
    if idade < 0:
        return False, "Idade não pode ser negativa"

    if idade > 150:
        return False, "Idade improvável"

    if idade < 18:
        return True, "Menor de idade"

    return True, "Maior de idade"

# Testando
valido, mensagem = validar_idade(25)
print(f"Válido: {valido}, Mensagem: {mensagem}")