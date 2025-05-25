class Fila:
    def __init__(self):
        self.items = []

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.vazia():
            return self.items.pop(0)# Menos eficiente que collections.deque
        return None

    def frente(self):
        if not self.vazia():
            return self.items[0]
        return None

    def vazia(self):
        return len(self.items) == 0

# Uso mais eficiente com deque
from collections import deque

fila = deque()
fila.append(1)# Enfileirar
fila.append(2)
fila.append(3)
print(fila.popleft())# 1 (Desenfileirar)