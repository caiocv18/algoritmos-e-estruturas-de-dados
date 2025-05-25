# Demonstrando a imutabilidade
lista = [1, 2, 3]
tupla = (1, 2, 3)

# Com lista, podemos modificar
lista[0] = 10
print(f"Lista após modificação: {lista}")  # [10, 2, 3]

# Com tupla, isso gera erro
try:
    tupla[0] = 10
except TypeError as e:
    print(f"Erro ao tentar modificar tupla: {e}")
    # 'tuple' object does not support item assignment
