# Lista global para armazenar cadastros (veremos melhores formas na próxima aula)
cadastros = []

def adicionar_cadastro():
    """Adiciona um novo cadastro ao sistema."""
    print("\n=== NOVO CADASTRO ===")
    nome = input("Nome completo: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

# Criar dicionário com os dados
    novo_cadastro = {
        "nome": nome,
        "email": email,
        "telefone": telefone
    }

    cadastros.append(novo_cadastro)
    print("✓ Cadastro realizado com sucesso!")

def listar_cadastros():
    """Lista todos os cadastros do sistema."""
    print("\n=== CADASTROS NO SISTEMA ===")

    if not cadastros:
        print("Nenhum cadastro encontrado.")
        return

    for i, cadastro in enumerate(cadastros, 1):
        print(f"\nCadastro #{i}")
        print(f"Nome: {cadastro['nome']}")
        print(f"Email: {cadastro['email']}")
        print(f"Telefone: {cadastro['telefone']}")
        print("-" * 30)

def buscar_cadastro():
    """Busca um cadastro por nome."""
    nome_busca = input("Digite o nome para buscar: ").lower()
    encontrados = []

    for cadastro in cadastros:
        if nome_busca in cadastro['nome'].lower():
            encontrados.append(cadastro)

    if encontrados:
        print(f"\n{len(encontrados)} cadastro(s) encontrado(s):")
        for cadastro in encontrados:
            print(f"- {cadastro['nome']} ({cadastro['email']})")
    else:
        print("Nenhum cadastro encontrado com esse nome.")

def menu_principal():
    """Exibe o menu principal do sistema."""
    print("\n=== SISTEMA DE CADASTRO ===")
    print("1. Adicionar cadastro")
    print("2. Listar cadastros")
    print("3. Buscar cadastro")
    print("4. Sair")
    print("=" * 27)

def executar_sistema():
    """Executa o sistema de cadastro."""
    print("Bem-vindo ao Sistema de Cadastro!")

    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_cadastro()
        elif opcao == "2":
            listar_cadastros()
        elif opcao == "3":
            buscar_cadastro()
        elif opcao == "4":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Para executar: executar_sistema()