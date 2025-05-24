def somar_numeros(*args):
    """
    Soma qualquer quantidade de números.
    *args coleta argumentos posicionais em uma tupla.
    """
    print(f"Argumentos recebidos: {args}")
    print(f"Tipo: {type(args)}")

    total = sum(args)
    print(f"Soma: {total}")
    return total

# Testando com diferentes quantidades de argumentos
somar_numeros(10, 20)
somar_numeros(1, 2, 3, 4, 5)
somar_numeros(100)
somar_numeros()# Tupla vazia