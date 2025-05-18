lista = [10, 20, 30, 40, 50]
tupla = ('a', 'b', 'c', 'd', 'e')

# Acesso por índice positivo (do início)
print(lista[0])# 10
print(tupla[2])# 'c'# Acesso por índice negativo (do final)
print(lista[-1])# 50
print(tupla[-2])# 'd'# Acesso a elementos aninhados
matriz = [[1, 2], [3, 4]]
print(matriz[0][1])# 2 (segundo elemento da primeira lista)

# Tratando erros de índice
try:
    print(lista[10])# Gera IndexError
except IndexError:
    print("Índice fora do intervalo!")

# Método mais seguro com get (para listas)
indice = 10
elemento = lista[indice] if indice < len(lista) else None
print(elemento)# None