# Exemplo de loop infinito e sua correção
def loop_infinito_exemplo():
    # Loop infinito - a condição nunca muda
    contador = 1
    while contador <= 10:
        print(contador)
        # Esqueceu de incrementar contador!
    
    print("Este código nunca será alcançado")

def loop_corrigido():
    # Loop corrigido - agora conta até 10 e para
    contador = 1
    while contador <= 10:
        print(contador)
        contador += 1  # Incrementa o contador
    
    print("Loop concluído corretamente")