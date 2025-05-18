texto = "Python"

# Indexação (começa em 0)
print(texto[0]) # 'P'
print(texto[1]) # 'y'
print(texto[-1]) # 'n' (indexação negativa começa do final)# Fatiamento [início:fim:passo]
print(texto[0:3]) # 'Pyt' (caracteres de 0 a 2)
print(texto[2:]) # 'thon' (do índice 2 até o final)
print(texto[:4]) # 'Pyth' (do início até o índice 3)
print(texto[::2]) # 'Pto' (do início ao fim, pegando a cada 2 caracteres)
print(texto[::-1]) # 'nohtyP' (reverso)