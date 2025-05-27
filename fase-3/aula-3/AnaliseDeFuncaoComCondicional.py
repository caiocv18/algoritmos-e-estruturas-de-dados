def processa_lista(lista_dados, alvo):
    for i, item in enumerate(lista_dados): # Loop O(n)
        if item == alvo:
            # Realiza 5 operações aqui (O(1))
            print(f"Alvo encontrado na posição {i}")
            return True # Melhor caso
    # Realiza 3 operações aqui se o loop terminar (O(1))
    print("Alvo não encontrado")
    return False # Pior caso