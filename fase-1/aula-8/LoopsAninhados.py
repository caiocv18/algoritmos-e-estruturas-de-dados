# Estrutura básica de loops aninhados
i = 1
while i <= 3:
    print(f"Loop externo: iteração {i}")
    
    j = 1
    while j <= 4:
        print(f"  Loop interno: iteração {j}")
        j += 1
    
    i += 1