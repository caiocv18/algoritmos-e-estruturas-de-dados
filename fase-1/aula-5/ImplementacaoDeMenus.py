print("===== CALCULADORA SIMPLES =====")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Sair")

opcao = input("Escolha uma opção (1-5): ")

if opcao == "1":
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    resultado = a + b
    print(f"Resultado: {resultado}")
elif opcao == "2":
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    resultado = a - b
    print(f"Resultado: {resultado}")
elif opcao == "3":
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    resultado = a * b
    print(f"Resultado: {resultado}")
elif opcao == "4":
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    if b == 0:
        print("Erro: Divisão por zero")
    else:
        resultado = a / b
        print(f"Resultado: {resultado}")
elif opcao == "5":
    print("Encerrando o programa...")
else:
    print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")