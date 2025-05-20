# Atribuições simples
mensagem = "Aprovado" if nota >= 6 else "Reprovado"

# Retornos de função
def verificar_paridade(n):
    return "Par" if n % 2 == 0 else "Ímpar"

# Em compreensões de lista
numeros = [1, 2, 3, 4, 5]
resultado = [n if n % 2 == 0 else n * 2 for n in numeros]
# resultado: [2, 2, 6, 4, 10]