def busca_binaria(lista, valor):
    """
    Implementação de busca binária com verificações explícitas
    de condições de entrada e saída.
    """
    # Verificação pré-loop
    if not lista:
        print("Lista vazia, busca impossível.")
        return -1
    
    # Verificação antes de entrar no loop
    print(f"Iniciando busca por {valor} em lista de {len(lista)} elementos")
    print(f"Limites iniciais: 0 a {len(lista)-1}")
    
    inicio = 0
    fim = len(lista) - 1
    iteracoes = 0
    
    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        
        # Verificações durante o loop
        print(f"Iteração {iteracoes}: Verificando posição {meio} (valor {lista[meio]})")
        
        if lista[meio] == valor:
            # Verificação pós-loop (sucesso)
            print(f"Valor {valor} encontrado na posição {meio} após {iteracoes} iterações")
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
            print(f"  Valor na posição {meio} é menor que {valor}. Novo início: {inicio}")
        else:
            fim = meio - 1
            print(f"  Valor na posição {meio} é maior que {valor}. Novo fim: {fim}")
    
    # Verificação pós-loop (não encontrado)
    print(f"Valor {valor} não encontrado após {iteracoes} iterações")
    return -1

# Teste com uma lista ordenada
numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
busca_binaria(numeros, 23)