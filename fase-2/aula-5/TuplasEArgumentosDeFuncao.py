# Função com número variável de argumentos
def somar(*numeros):
    """Soma qualquer quantidade de números"""
    print(f"Tipo de 'numeros': {type(numeros)}")  # <class 'tuple'>
    return sum(numeros)

print(somar(1, 2, 3))  # 6
print(somar(10, 20, 30, 40))  # 100
print(somar())  # 0

# Combinando argumentos normais com *args
def criar_relatorio(titulo, *dados, formato="simples"):
    """Cria relatório com título e dados variáveis"""
    print(f"\n{titulo}")
    print("-" * len(titulo))

    if formato == "simples":
        for item in dados:
            print(f"• {item}")
    elif formato == "numerado":
        for i, item in enumerate(dados, 1):
            print(f"{i}. {item}")

criar_relatorio("Vendas do Mês", "Janeiro: R$ 10.000", "Fevereiro: R$ 12.000")
criar_relatorio("Tarefas", "Estudar Python", "Fazer exercícios",
                "Revisar código", formato="numerado")

# Desempacotando tuplas como argumentos
def calcular_distancia(x1, y1, x2, y2):
    """Calcula distância entre dois pontos"""
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Usando tuplas para os pontos
ponto_a = (0, 0)
ponto_b = (3, 4)

# Desempacotando com *
distancia = calcular_distancia(*ponto_a, *ponto_b)
print(f"\nDistância entre {ponto_a} e {ponto_b}: {distancia}")

# Função que retorna e recebe tuplas
def processar_coordenadas(*pontos):
    """Processa múltiplas coordenadas"""
    if not pontos:
        return None

    # Calcula centroide
    soma_x = sum(p[0] for p in pontos)
    soma_y = sum(p[1] for p in pontos)
    n = len(pontos)

    centroide = (soma_x / n, soma_y / n)

    # Calcula distâncias do centroide
    distancias = []
    for ponto in pontos:
        dist = calcular_distancia(*centroide, *ponto)
        distancias.append((ponto, dist))

    return centroide, distancias

pontos = [(0, 0), (4, 0), (4, 3), (0, 3)]
centro, dists = processar_coordenadas(*pontos)
print(f"\nCentroide: {centro}")
for ponto, dist in dists:
    print(f"Distância de {ponto} ao centro: {dist:.2f}")
