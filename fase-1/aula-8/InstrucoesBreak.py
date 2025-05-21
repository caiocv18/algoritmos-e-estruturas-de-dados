# Demonstração de break
contador = 1
while contador <= 10:
    print(contador, end=" ")
    if contador == 5:
        print("\nEncontrado o valor 5, interrompendo o loop!")
        break
    contador += 1
print("Loop encerrado.")

# Demonstração de continue
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:  # Se for par
        continue  # Pula para a próxima iteração
    print(contador, end=" ")  # Imprime apenas ímpares