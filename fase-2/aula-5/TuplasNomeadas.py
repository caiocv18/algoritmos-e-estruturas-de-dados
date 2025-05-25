from collections import namedtuple

# Definindo uma namedtuple
Pessoa = namedtuple('Pessoa', ['nome', 'idade', 'cidade'])
Ponto3D = namedtuple('Ponto3D', 'x y z')  # Pode usar string com espaços

# Criando instâncias
pessoa1 = Pessoa('Ana', 28, 'São Paulo')
pessoa2 = Pessoa(nome='Carlos', idade=35, cidade='Rio de Janeiro')

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")
print(f"Acesso por índice também funciona: {pessoa1[0]}")

# Métodos especiais de namedtuple
print(f"Campos: {pessoa1._fields}")
print(f"Como dict: {pessoa1._asdict()}")

# Criando a partir de iterável
dados = ['Pedro', 42, 'Brasília']
pessoa3 = Pessoa._make(dados)
print(f"Pessoa 3: {pessoa3}")

# Substituindo valores (retorna nova namedtuple)
pessoa4 = pessoa1._replace(idade=29)
print(f"Original: {pessoa1}")
print(f"Nova: {pessoa4}")

# Exemplo prático: Representando dados estruturados
Produto = namedtuple('Produto', 'codigo nome preco estoque')
produtos = [
    Produto('001', 'Notebook', 3500.00, 10),
    Produto('002', 'Mouse', 50.00, 100),
    Produto('003', 'Teclado', 150.00, 50)
]

for produto in produtos:
    valor_total = produto.preco * produto.estoque
    print(f"{produto.nome}: R$ {valor_total:,.2f} em estoque")
