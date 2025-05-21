# Gerando todas as combinações de 3 letras e 2 dígitos
letras = ["A", "B", "C"]
dígitos = [1, 2]

for letra in letras:
    for dígito in dígitos:
        print(f"{letra}{dígito}")