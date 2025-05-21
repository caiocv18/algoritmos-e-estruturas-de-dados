# Sintaxe: [expressão_if if condição else expressão_else for item in iterável]

# Classifica números como 'par' ou 'ímpar'
números = [1, 2, 3, 4, 5]
paridade = ["par" if n % 2 == 0 else "ímpar" for n in números]
print(paridade)  # ['ímpar', 'par', 'ímpar', 'par', 'ímpar']