idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
    tem_carteira = input("Possui carteira de motorista? (s/n): ").lower()

    if tem_carteira == "s":
        print("Você pode dirigir.")
    else:
        print("Você não pode dirigir até obter a carteira.")
else:
    print("Você é menor de idade.")
    acompanhado = input("Está acompanhado dos pais? (s/n): ").lower()

    if acompanhado == "s":
        print("Você pode entrar acompanhado.")
    else:
        print("Você não pode entrar sem acompanhamento.")