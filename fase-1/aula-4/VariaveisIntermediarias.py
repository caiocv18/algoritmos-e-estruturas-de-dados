# Cálculo direto (difícil de entender e depurar)
pagamento = principal * (taxa_mensal * (1 + taxa_mensal) ** prazo) / ((1 + taxa_mensal) ** prazo - 1)

# Cálculo com variáveis intermediárias (claro e fácil de depurar)
fator_composto = (1 + taxa_mensal) ** prazo
numerador = taxa_mensal * fator_composto
denominador = fator_composto - 1
pagamento = principal * numerador / denominador