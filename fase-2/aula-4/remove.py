frutas = ["maçã", "banana", "laranja", "banana"]
frutas.remove("banana")
print(frutas)  # ["maçã", "laranja", "banana"]

# Cuidado: gera erro se o elemento não existir
try:
    frutas.remove("pera")
except ValueError:
    print("Elemento não encontrado")