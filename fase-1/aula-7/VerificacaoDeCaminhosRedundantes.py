# Código original com redundâncias
def calcular_frete_original(peso, distancia, urgente, internacional):
    if internacional:
        if urgente:
            if peso <= 1:
                return 50 + distancia * 0.5
            elif peso <= 5:
                return 70 + distancia * 0.5
            else:
                return 100 + distancia * 0.5
        else:# não urgente
            if peso <= 1:
                return 30 + distancia * 0.3
            elif peso <= 5:
                return 50 + distancia * 0.3
            else:
                return 80 + distancia * 0.3
    else:# nacional
        if urgente:
            if peso <= 1:
                return 20 + distancia * 0.2
            elif peso <= 5:
                return 40 + distancia * 0.2
            else:
                return 60 + distancia * 0.2
        else:# não urgente
            if peso <= 1:
                return 10 + distancia * 0.1
            elif peso <= 5:
                return 20 + distancia * 0.1
            else:
                return 30 + distancia * 0.1

# Versão refatorada eliminando redundâncias
def calcular_frete_refatorado(peso, distancia, urgente, internacional):
# Determinação da taxa por distância
    if internacional:
        taxa_distancia = 0.5 if urgente else 0.3
    else:# nacional
        taxa_distancia = 0.2 if urgente else 0.1

# Determinação da taxa básica com base no peso
    if peso <= 1:
        if internacional:
            taxa_basica = 50 if urgente else 30
        else:
            taxa_basica = 20 if urgente else 10
    elif peso <= 5:
        if internacional:
            taxa_basica = 70 if urgente else 50
        else:
            taxa_basica = 40 if urgente else 20
    else:
        if internacional:
            taxa_basica = 100 if urgente else 80
        else:
            taxa_basica = 60 if urgente else 30

# Cálculo final
    return taxa_basica + distancia * taxa_distancia
