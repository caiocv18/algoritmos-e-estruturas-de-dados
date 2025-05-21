# Depuração por amostragem
iteracoes_totais = 1000
amostra_frequencia = 100

contador = 1
while contador <= iteracoes_totais:
    # Mostrar apenas a primeira, última e a cada 'amostra_frequencia' iterações
    if contador == 1 or contador == iteracoes_totais or contador % amostra_frequencia == 0:
        print(f"Iteração {contador}: processando...")
    
    # Processamento normal
    # ...
    
    contador += 1