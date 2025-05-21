# Implementação manual do comportamento do loop for
frutas = ["maçã", "banana", "laranja"]
iterador = iter(frutas)  # Cria um iterador

try:
    while True:
        fruta = next(iterador)  # Obtém o próximo item
        print(fruta)
except StopIteration:
    pass  # Fim da iteração