# Usando if-elif: apenas um bloco será executado
numero = 15

if numero > 20:
    print("Maior que 20")
elif numero > 10:
    print("Maior que 10")
elif numero > 0:
    print("Maior que 0")

# Saída: "Maior que 10" (apenas um bloco é executado)

# Usando múltiplos if: todos os blocos com condições verdadeiras serão executados
if numero > 20:
    print("Maior que 20")
if numero > 10:
    print("Maior que 10")
if numero > 0:
    print("Maior que 0")

# Saída: "Maior que 10" e "Maior que 0" (todos os blocos com condições True são executados)