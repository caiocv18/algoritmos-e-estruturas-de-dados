import pdb

def funcao_problematica():
    a = 5
    b = 0
    
    pdb.set_trace()  # O programa para aqui e entra no modo de depuração
    
    c = a / b  # Isso causará um erro
    return c

funcao_problematica()