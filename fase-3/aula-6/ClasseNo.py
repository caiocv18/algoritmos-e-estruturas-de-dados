class No:
    def __init__(self, valor):
        self.valor = valor          # O dado armazenado no nó
        self.esquerda = None      # Referência para o filho da esquerda (inicialmente None)
        self.direita = None       # Referência para o filho da direita (inicialmente None)

    def __str__(self): # Para imprimir o valor do nó de forma legível
        return str(self.valor)