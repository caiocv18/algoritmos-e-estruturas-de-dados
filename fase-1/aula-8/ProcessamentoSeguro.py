# Usando uma condição de segurança para evitar loops infinitos
def processamento_seguro(dados, max_iteracoes=1000):
    iteracoes = 0
    
    while condição_de_processamento(dados):
        # Processamento normal
        processar_dados(dados)
        iteracoes += 1
        
        # Condição de segurança
        if iteracoes >= max_iteracoes:
            print(f"Aviso: Número máximo de iterações ({max_iteracoes}) atingido.")
            print("O loop foi interrompido por segurança.")
            break