# Exemplos de outras automações com while:

def monitorar_sistema(intervalo=5, max_verificacoes=100):
    """Monitora um sistema em intervalos regulares."""
    verificacoes = 0
    
    while verificacoes < max_verificacoes:
        status = verificar_status_sistema()
        registrar_log(status)
        
        if status == "CRÍTICO":
            enviar_alerta("Sistema em estado crítico!")
            break
        
        verificacoes += 1
        time.sleep(intervalo)

def sincronizar_dados(origem, destino, max_tentativas=3):
    """Sincroniza dados entre dois sistemas com tentativas em caso de falha."""
    dados = carregar_dados(origem)
    indice = 0
    
    while indice < len(dados):
        item = dados[indice]
        tentativas = 0
        sucesso = False
        
        while tentativas < max_tentativas and not sucesso:
            try:
                enviar_para_destino(destino, item)
                sucesso = True
            except:
                tentativas += 1
                time.sleep(1)  # Espera antes de tentar novamente
        
        if sucesso:
            indice += 1
        else:
            registrar_erro(f"Falha ao sincronizar item {item['id']}")
            indice += 1  # Ou pular o item