# Evitar constantes "mágicas" no código
# RUIM:
if temperatura > 37.5:
    print("Febre detectada")

# BOM:
LIMITE_FEBRE = 37.5
if temperatura > LIMITE_FEBRE:
    print("Febre detectada")

# Evitar repetição de código
# RUIM:
area_quadrado = lado * lado
area_circulo = math.pi * raio * raio

# BOM:
def calcular_area_quadrado(lado):
    return lado ** 2

def calcular_area_circulo(raio):
    return math.pi * raio ** 2

area_quadrado = calcular_area_quadrado(lado)
area_circulo = calcular_area_circulo(raio)

# Usar nomes de variáveis significativos
# RUIM:
x = a * b / 2

# BOM:
area_triangulo = base * altura / 2