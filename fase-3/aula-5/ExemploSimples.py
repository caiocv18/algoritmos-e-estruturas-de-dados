from collections import deque

# Criando uma fila
fila_atendimento = deque()

# Pessoas chegando na fila (enqueue)
fila_atendimento.append("Cliente A")
fila_atendimento.append("Cliente B")
fila_atendimento.append("Cliente C")
print(f"Fila atual: {list(fila_atendimento)}") # Convertemos para lista só para imprimir bonito

# Espiando o próximo a ser atendido (peek/front)
if fila_atendimento:
    print(f"Próximo a ser atendido: {fila_atendimento[0]}")

# Atendendo uma pessoa (dequeue)
if fila_atendimento:
    cliente_atendido = fila_atendimento.popleft()
    print(f"Cliente atendido: {cliente_atendido}")
print(f"Fila após atendimento: {list(fila_atendimento)}")

# Verificando se a fila está vazia
if not fila_atendimento:
    print("A fila de atendimento está vazia.")