# Simulação de investimento com juros compostos
principal = 1000
taxa_anual = 0.05  # 5%
anos = 20

print(f"Investimento inicial: R${principal:.2f}")
print(f"Taxa anual: {taxa_anual:.2%}")
print(f"Período: {anos} anos")
print("Ano | Saldo")
print("-" * 15)

saldo = principal
for ano in range(1, anos + 1):
    saldo *= (1 + taxa_anual)
    print(f"{ano:3d} | R${saldo:.2f}")

ganho = saldo - principal
print(f"\nGanho total após {anos} anos: R${ganho:.2f}")
print(f"Rendimento total: {(ganho/principal)*100:.2f}%")