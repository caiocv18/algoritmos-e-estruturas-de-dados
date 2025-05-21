# Continuar pedindo entrada até que seja válida
while True:
    entrada = input("Digite um número positivo: ")
    if entrada.isdigit() and int(entrada) > 0:
        break