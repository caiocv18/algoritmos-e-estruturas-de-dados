def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("=" * 40)
    print("         SISTEMA DE VENDAS")
    print("=" * 40)
    print("1. Cadastrar produto")
    print("2. Realizar venda")
    print("3. Consultar estoque")
    print("4. Gerar relatório")
    print("5. Sair")
    print("=" * 40)

def limpar_tela():
    """Simula limpeza de tela."""
    print("\n" * 5)

def exibir_data_hora():
    """Exibe data e hora atuais."""
    from datetime import datetime
    agora = datetime.now()
    print(f"Data/Hora: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

# Usando as funções
exibir_data_hora()
exibir_menu()