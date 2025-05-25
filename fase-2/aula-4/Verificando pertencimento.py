frutas = ["maçã", "banana", "laranja", "uva"]

# Verificação simples
print("banana" in frutas)  # True
print("pera" in frutas)  # False
print("maçã" not in frutas)  # False

# Uso em condicionais
if "laranja" in frutas:
    print("Temos laranja disponível!")

# Verificação antes de operações
item = "manga"
if item not in frutas:
    frutas.append(item)