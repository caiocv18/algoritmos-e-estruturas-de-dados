# Verificando se um número é primo
def é_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} é divisível por {i}")
            break
    else:  # Executa se nenhum break foi acionado
        return True
    return False

print(é_primo(17))  # True
print(é_primo(15))  # False