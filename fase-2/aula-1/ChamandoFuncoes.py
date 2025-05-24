def obter_status_sistema():
    """Retorna o status atual do sistema."""
    print("Sistema operacional ✓")
    print("Conexão com banco de dados ✓")
    print("Serviços ativos ✓")

# 1. Chamada simples
obter_status_sistema()

# 2. Chamada dentro de estruturas condicionais
usuario_logado = True
if usuario_logado:
    obter_status_sistema()

# 3. Chamada dentro de loops
def processar_item():
    print("Item processado")

for i in range(3):
    print(f"Processamento {i+1}:")
    processar_item()

# 4. Chamada dentro de outras funções
def iniciar_sistema():
    """Inicia o sistema completo."""
    print("INICIANDO SISTEMA...")
    obter_status_sistema()
    exibir_menu()
    print("Sistema pronto para uso!")

iniciar_sistema()