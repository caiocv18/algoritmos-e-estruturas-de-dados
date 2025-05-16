# Exemplos de formatação com f-strings
x = 10
y = 20
print(f"A soma de {x} e {y} é {x + y}")      # "A soma de 10 e 20 é 30"

pi = 3.14159
print(f"Pi com duas casas decimais: {pi:.2f}")  # "Pi com duas casas decimais: 3.14"

# Alinhamento de texto
nome = "Carlos"
print(f"{nome:>10}")  # "    Carlos" (alinhado à direita em 10 espaços)
print(f"{nome:<10}")  # "Carlos    " (alinhado à esquerda em 10 espaços)
print(f"{nome:^10}")  # "  Carlos  " (centralizado em 10 espaços)