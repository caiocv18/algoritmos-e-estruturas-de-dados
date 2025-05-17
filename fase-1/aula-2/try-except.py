try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"10 dividido por {numero} é {resultado}")
except ValueError:
    print("Erro: Você não digitou um número válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except Exception as e:
    print(f"Erro inesperado: {e}")