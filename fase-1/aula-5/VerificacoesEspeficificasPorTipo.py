# Strings
nome = "Python"
if nome.startswith("Py"):
    print("Começa com Py")
if "th" in nome:
    print("Contém 'th'")
if nome.isalpha():
    print("Contém apenas letras")

# Listas
numeros = [1, 2, 3, 4, 5]
if 3 in numeros:
    print("A lista contém o número 3")
if len(numeros) > 3:
    print("A lista tem mais de 3 elementos")
if numeros[0] > numeros[-1]:
    print("O primeiro elemento é maior que o último")

# Dicionários
pessoa = {"nome": "Carlos", "idade": 30}
if "nome" in pessoa:
    print("A chave 'nome' existe no dicionário")
if pessoa.get("profissao") is None:
    print("A chave 'profissao' não existe ou é None")
if pessoa.get("idade", 0) >= 18:
    print("A pessoa é maior de idade (se existir idade)")