# Exemplo conceitual
def calcular_variacao_percentual(valor_atual, valor_anterior):
  if valor_anterior == 0: # Evita divisão por zero
    return float('inf') # Ou outra forma de indicar crescimento "infinito" ou erro
  variacao = ((valor_atual - valor_anterior) / valor_anterior) * 100
  return variacao

# Uso:
# vendas_fev = 120
# vendas_jan = 100
# crescimento_fev_vs_jan = calcular_variacao_percentual(vendas_fev, vendas_jan)
# print(f"Crescimento percentual: {crescimento_fev_vs_jan:.2f}%") # Saída: 20.00%