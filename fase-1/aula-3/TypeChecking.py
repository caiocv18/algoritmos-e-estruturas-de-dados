valor = 42

# Verificando o tipo
print(isinstance(valor, int))# True
print(isinstance(valor, float))# False
print(isinstance(valor, (int, float)))# True (múltiplos tipos)
# Na prática
def processar_numero(valor):
    if not isinstance(valor, (int, float)):
        raise TypeError("Esperado um número (int ou float)")
    return valor * 2

# Verificando subclasses
print(issubclass(bool, int))# True (bool é subclasse de int)