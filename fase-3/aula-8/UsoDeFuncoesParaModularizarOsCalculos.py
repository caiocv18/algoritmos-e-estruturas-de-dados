# Exemplo conceitual de função para um KPI simples
def calcular_media_vendas(lista_de_vendas):
  if not lista_de_vendas: # Verifica se a lista não está vazia
    return 0
  total_vendas = sum(lista_de_vendas)
  numero_de_registros = len(lista_de_vendas)
  media = total_vendas / numero_de_registros
  return media

# Uso:
# vendas_janeiro = [100, 150, 120, 130]
# media_jan = calcular_media_vendas(vendas_janeiro)
# print(f"Média de vendas em Janeiro: {media_jan}")