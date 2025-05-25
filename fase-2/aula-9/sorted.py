outra_lista = [5, 1, 4, 2, 8]
print(f"Lista original: {outra_lista}")
lista_nova_ordenada = sorted(outra_lista)
print(f"Nova lista ordenada com sorted(): {lista_nova_ordenada}") # Saída: [1, 2, 4, 5, 8]
print(f"Lista original após sorted(): {outra_lista}") # Saída: [5, 1, 4, 2, 8] (permanece igual)