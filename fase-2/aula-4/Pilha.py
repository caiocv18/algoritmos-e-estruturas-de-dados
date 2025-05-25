class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.items.pop()
        return None

    def topo(self):
        if not self.vazia():
            return self.items[-1]
        return None

    def vazia(self):
        return len(self.items) == 0

    def tamanho(self):
        return len(self.items)

# Uso da pilha
pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
print(pilha.desempilhar())# 3
print(pilha.topo())# 2