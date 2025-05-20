def menu_adaptativo():
    # Estado inicial do usuário
    usuario = {
        "logado": False,
        "nivel": "visitante",
        "permissoes": [],
        "ultima_acao": None
    }
    
    while True:
        # Menu adapta-se ao estado do usuário
        print("\n===== SISTEMA ADAPTATIVO =====")
        
        if not usuario["logado"]:
            print("1. Login")
            print("2. Cadastro")
            print("3. Sobre o sistema")
            print("0. Sair")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                usuario = fazer_login(usuario)
            elif opcao == "2":
                usuario = fazer_cadastro(usuario)
            elif opcao == "3":
                mostrar_sobre()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")
        
        else:
            # Menu para usuários logados (adapta-se ao nível)
            print(f"Usuário: {usuario['nome']} ({usuario['nivel']})")
            
            # Opções comuns a todos os usuários
            print("1. Ver perfil")
            print("2. Alterar senha")
            
            # Opções específicas por nível
            if usuario["nivel"] == "admin":
                print("3. Gerenciar usuários")
                print("4. Configurações do sistema")
                print("5. Logs do sistema")
            elif usuario["nivel"] == "gerente":
                print("3. Relatórios")
                print("4. Gerenciar equipe")
            elif usuario["nivel"] == "operador":
                print("3. Registrar operação")
            
            print("9. Logout")
            print("0. Sair")
            
            opcao = input("\nEscolha uma opção: ")
            
            # Processamento da opção escolhida
            if opcao == "1":
                ver_perfil(usuario)
            elif opcao == "2":
                usuario = alterar_senha(usuario)
            elif opcao == "3":
                if usuario["nivel"] == "admin":
                    gerenciar_usuarios()
                elif usuario["nivel"] == "gerente":
                    gerar_relatorios()
                elif usuario["nivel"] == "operador":
                    registrar_operacao()
            # Continuar com as demais opções...
            elif opcao == "9":
                print("Logout realizado com sucesso.")
                usuario = {
                    "logado": False,
                    "nivel": "visitante",
                    "permissoes": [],
                    "ultima_acao": "logout"
                }
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

def fazer_login(usuario):
    print("\n-- Login --")
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    
    # Simulação de autenticação
    if nome == "admin" and senha == "admin":
        print("Login realizado com sucesso! Bem-vindo, Administrador.")
        return {
            "logado": True,
            "nome": "Administrador",
            "nivel": "admin",
            "permissoes": ["ler", "escrever", "gerenciar"],
            "ultima_acao": "login"
        }
    elif nome == "gerente" and senha == "gerente":
        print("Login realizado com sucesso! Bem-vindo, Gerente.")
        return {
            "logado": True,
            "nome": "Gerente",
            "nivel": "gerente",
            "permissoes": ["ler", "escrever"],
            "ultima_acao": "login"
        }
    elif nome == "operador" and senha == "operador":
        print("Login realizado com sucesso! Bem-vindo, Operador.")
        return {
            "logado": True,
            "nome": "Operador",
            "nivel": "operador",
            "permissoes": ["ler"],
            "ultima_acao": "login"
        }
    else:
        print("Credenciais inválidas. Tente novamente.")
        return usuario

# Outras funções do sistema seriam implementadas aqui...

def mostrar_sobre():
    print("\n-- Sobre o Sistema --")
    print("Sistema Adaptativo v1.0")
    print("Desenvolvido como exemplo para a aula de Algoritmos e Estrutura de Dados")
    print("Este sistema demonstra interfaces adaptativas baseadas no estado do usuário.")
    
    input("\nPressione Enter para voltar ao menu...")