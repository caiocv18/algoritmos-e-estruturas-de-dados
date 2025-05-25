import timeit
import sys

# Comparando tempo de criação
tempo_lista = timeit.timeit('lista = [1, 2, 3, 4, 5]', number=1000000)
tempo_tupla = timeit.timeit('tupla = (1, 2, 3, 4, 5)', number=1000000)

print(f"Tempo criação lista: {tempo_lista:.4f}s")
print(f"Tempo criação tupla: {tempo_tupla:.4f}s")
print(f"Tupla é {tempo_lista/tempo_tupla:.2f}x mais rápida na criação")

# Comparando tempo de acesso
lista_grande = list(range(1000))
tupla_grande = tuple(range(1000))

tempo_acesso_lista = timeit.timeit(
    'x = lista[500]',
    globals={'lista': lista_grande},
    number=1000000
)
tempo_acesso_tupla = timeit.timeit(
    'x = tupla[500]',
    globals={'tupla': tupla_grande},
    number=1000000
)

print(f"\nTempo acesso lista: {tempo_acesso_lista:.4f}s")
print(f"Tempo acesso tupla: {tempo_acesso_tupla:.4f}s")
