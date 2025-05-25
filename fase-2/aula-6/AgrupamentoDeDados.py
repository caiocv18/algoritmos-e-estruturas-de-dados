# Agrupando pessoas por idade
pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "João", "idade": 30},
    {"nome": "Maria", "idade": 25}
]

grupos = {}
for pessoa in pessoas:
    idade = pessoa["idade"]
    if idade not in grupos:
        grupos[idade] = []
    grupos[idade].append(pessoa["nome"])
