# Validação de entrada numérica
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0 or idade > 120:
            print("Idade inválida. Digite um valor entre 0 e 120.")
            continue
        break  # Sai do loop se a entrada for válida
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

print(f"Idade registrada: {idade} anos")