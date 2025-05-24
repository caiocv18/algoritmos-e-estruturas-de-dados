def gerar_codigo_produto():
    """Gera um código único para produto."""
    import random
    prefixo = "PROD"
    numero = random.randint(1000, 9999)
    codigo = f"{prefixo}-{numero}"
    print(f"Código gerado: {codigo}")
    return codigo

def exibir_boas_vindas():
    """Exibe mensagem de boas-vindas personalizada."""
    import datetime
    hora = datetime.datetime.now().hour

    if 5 <= hora < 12:
        periodo = "Bom dia"
    elif 12 <= hora < 18:
        periodo = "Boa tarde"
    else:
        periodo = "Boa noite"

    print(f"{periodo}! Bem-vindo ao sistema.")
    print("Como posso ajudá-lo hoje?")

def calcular_tempo_execucao():
    """Calcula e exibe o tempo de execução."""
    import time
    inicio = time.time()

# Simula processamento
    print("Processando...")
    time.sleep(2)# Pausa de 2 segundos

    fim = time.time()
    tempo_total = fim - inicio
    print(f"Tempo de execução: {tempo_total:.2f} segundos")

# Executando as funções
exibir_boas_vindas()
print()
gerar_codigo_produto()
print()
calcular_tempo_execucao()