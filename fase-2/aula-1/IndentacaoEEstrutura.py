# CORRETO - indentação consistente
def calcular_bonus():
    salario_base = 3000
    percentual = 0.1
    bonus = salario_base * percentual
    print(f"Bônus calculado: R$ {bonus:.2f}")

# INCORRETO - erro de indentação
def calcular_bonus_errado():
salario_base = 3000# IndentationError!
    percentual = 0.1
    bonus = salario_base * percentual