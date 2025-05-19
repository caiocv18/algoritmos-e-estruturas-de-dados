# RUIM: Define o valor do desconto
desconto = total * 0.1

# BOM: Aplica desconto de 10% para compras acima de R$ 1000
if total > 1000:
    desconto = total * 0.1  # 10% de desconto
else:
    desconto = 0