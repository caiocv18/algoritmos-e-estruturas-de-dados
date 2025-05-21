# Extraindo informações específicas de textos
textos = [
    "ID: 1001, Nome: Ana Silva, Idade: 25",
    "ID: 1002, Nome: Bruno Costa, Idade: 31",
    "ID: 1003, Nome: Carlos Lima, Idade: 42"
]

# Extraindo apenas IDs e nomes
resultados = []
for texto in textos:
    partes = texto.split(", ")
    id_valor = partes[0].split(": ")[1]
    nome_valor = partes[1].split(": ")[1]
    
    resultados.append({"id": id_valor, "nome": nome_valor})

print(resultados)

# Versão com compreensão
resultados = [
    {"id": t.split(", ")[0].split(": ")[1], 
     "nome": t.split(", ")[1].split(": ")[1]}
    for t in textos
]