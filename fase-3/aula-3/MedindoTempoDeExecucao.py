import time

inicio = time.time() # Marca o tempo de início

# ... seu código que você quer medir ...
# Por exemplo, um loop longo ou uma função
for i in range(1000000):
    pass

fim = time.time() # Marca o tempo de fim

tempo_decorrido = fim - inicio
print(f"O código levou {tempo_decorrido:.4f} segundos para rodar.")