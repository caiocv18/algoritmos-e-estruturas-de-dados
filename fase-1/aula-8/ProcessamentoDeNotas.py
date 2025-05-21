# Processamento de notas até que seja digitado -1
print("Digite as notas dos alunos. Digite -1 para encerrar.")
notas = []
soma = 0
contador = 0

while True:
    entrada = float(input("Digite uma nota: "))
    
    if entrada == -1:  # Valor sentinela
        break
    
    if 0 <= entrada <= 10:
        notas.append(entrada)
        soma += entrada
        contador += 1
    else:
        print("Nota inválida. Digite um valor entre 0 e 10.")

if contador > 0:
    media = soma / contador
    print(f"Notas digitadas: {notas}")
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota válida foi digitada.")