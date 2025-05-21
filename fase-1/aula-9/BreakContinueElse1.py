# break - sai do loop completamente
for i in range(1, 11):
    if i == 5:
        print("Encontrei o 5, saindo...")
        break
    print(i)

# continue - pula para a próxima iteração
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Pula números pares
    print(i)  # Imprime apenas ímpares