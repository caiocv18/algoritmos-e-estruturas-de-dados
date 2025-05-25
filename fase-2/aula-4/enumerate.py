frutas = ["maçã", "banana", "laranja"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")
# 0: maçã
# 1: banana
# 2: laranja

# Começando de índice diferente
for num, item in enumerate(frutas, start=1):
    print(f"{num}º item: {item}")
