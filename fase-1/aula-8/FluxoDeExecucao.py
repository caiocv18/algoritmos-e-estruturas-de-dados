x = 1
while x <= 10:
    print(f"Valor atual: {x}")
    x += 5
    print(f"Valor após incremento: {x}")
    # Mesmo que x já seja > 10 aqui, o loop só verificará na próxima iteração

print(f"Valor final: {x}")