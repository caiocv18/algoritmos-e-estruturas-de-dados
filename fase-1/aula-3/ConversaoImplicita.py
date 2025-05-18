# Valores que são considerados False:
print(bool(0))# False
print(bool(""))# False (string vazia)
print(bool([]))# False (lista vazia)
print(bool({}))# False (dicionário vazio)
print(bool(None))# False
print(bool(0.0))# False# Valores que são considerados True:
print(bool(1))# True (qualquer número não-zero)
print(bool("texto"))# True (string não vazia)
print(bool([1, 2]))# True (lista não vazia)
print(bool({1: 2}))# True (dicionário não vazio)# Uso em condicionais
lista = []
if lista:
    print("Lista tem elementos")
else:
    print("Lista está vazia")# Esta será a saída