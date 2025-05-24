# Sem funções - código repetitivo
print("=== Cálculo de Preço com Desconto - Cliente 1 ===")
preco_original_1 = 100.00
if preco_original_1 > 50:
    desconto_1 = preco_original_1 * 0.10
    preco_final_1 = preco_original_1 - desconto_1
    print(f"Preço original: R$ {preco_original_1:.2f}")
    print(f"Desconto aplicado: R$ {desconto_1:.2f}")
    print(f"Preço final: R$ {preco_final_1:.2f}")
else:
    print(f"Preço: R$ {preco_original_1:.2f} (sem desconto)")

print("\n=== Cálculo de Preço com Desconto - Cliente 2 ===")
preco_original_2 = 75.00
if preco_original_2 > 50:
    desconto_2 = preco_original_2 * 0.10
    preco_final_2 = preco_original_2 - desconto_2
    print(f"Preço original: R$ {preco_original_2:.2f}")
    print(f"Desconto aplicado: R$ {desconto_2:.2f}")
    print(f"Preço final: R$ {preco_final_2:.2f}")
else:
    print(f"Preço: R$ {preco_original_2:.2f} (sem desconto)")

print("\n=== Cálculo de Preço com Desconto - Cliente 3 ===")
preco_original_3 = 30.00
if preco_original_3 > 50:
    desconto_3 = preco_original_3 * 0.10
    preco_final_3 = preco_original_3 - desconto_3
    print(f"Preço original: R$ {preco_original_3:.2f}")
    print(f"Desconto aplicado: R$ {desconto_3:.2f}")
    print(f"Preço final: R$ {preco_final_3:.2f}")
else:
    print(f"Preço: R$ {preco_original_3:.2f} (sem desconto)")