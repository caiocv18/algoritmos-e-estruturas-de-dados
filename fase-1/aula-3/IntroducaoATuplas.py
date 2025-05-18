# Criação de tuplas
coordenadas = (10, 20)
pessoa = ("João", 30, "Engenheiro")
tupla_singleton = (42,)# Tupla com um elemento (note a vírgula)
tupla_vazia = ()

# Empacotamento e desempacotamento
nome, idade, profissao = pessoa# desempacotamento
ponto = 3, 4# empacotamento implícito# Acessando elementos (similar a listas)
x = coordenadas[0]# 10
y = coordenadas[1]# 20

# Tentando modificar (gera erro)
# coordenadas[0] = 15  

# TypeError: 'tuple' object does not support item assignment
# Métodos de tupla (poucos, comparado a listas)
print(coordenadas.count(10))# Conta ocorrências: 1
print(coordenadas.index(20))# Encontra índice: 1# Concatenação
nova_tupla = coordenadas + (30, 40)
print(nova_tupla)# (10, 20, 30, 40)