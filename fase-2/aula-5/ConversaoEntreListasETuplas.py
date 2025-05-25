# Lista para tupla
lista_original = [1, 2, 3, 4, 5]
tupla_convertida = tuple(lista_original)
print(f"Lista: {lista_original} -> Tupla: {tupla_convertida}")

# Tupla para lista (quando precisamos modificar)
tupla_original = (10, 20, 30, 40, 50)
lista_convertida = list(tupla_original)
lista_convertida.append(60)  # Agora podemos modificar
print(f"Tupla: {tupla_original} -> Lista modificada: {lista_convertida}")

# Padrão comum: converter para lista, modificar, converter de volta
def adicionar_elemento_tupla(tupla, elemento):
    """Retorna uma nova tupla com o elemento adicionado"""
    lista_temp = list(tupla)
    lista_temp.append(elemento)
    return tuple(lista_temp)

tupla_inicial = (1, 2, 3)
tupla_final = adicionar_elemento_tupla(tupla_inicial, 4)
print(f"Tupla inicial: {tupla_inicial}")
print(f"Tupla final: {tupla_final}")

# Forma mais eficiente usando concatenação
tupla_final2 = tupla_inicial + (4,)
print(f"Tupla final (concatenação): {tupla_final2}")
