# Calculando π usando o método de Monte Carlo
import random

precisão_alvo = 0.0001  # Precisão desejada
max_iterações = 1000000  # Limite para evitar loop infinito
dentro_círculo = 0
total_pontos = 0
estimativa_anterior = 0

# while para controlar a precisão
while total_pontos < max_iterações:
    # for para gerar lotes de pontos
    for _ in range(10000):  # Processar em lotes
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:  # Ponto dentro do círculo
            dentro_círculo += 1
        total_pontos += 1
    
    # Calcular estimativa atual de π
    estimativa_atual = 4 * dentro_círculo / total_pontos
    
    # Verificar convergência
    if total_pontos > 10000 and abs(estimativa_atual - estimativa_anterior) < precisão_alvo:
        break
    
    estimativa_anterior = estimativa_atual
    
    # Reportar progresso a cada 100.000 pontos
    if total_pontos % 100000 == 0:
        print(f"Pontos: {total_pontos}, π ≈ {estimativa_atual}")

print(f"\nEstimativa final: π ≈ {estimativa_atual} (após {total_pontos} pontos)")
print(f"Valor real de π: 3.141592653589793...")