def exibir_menu():
    print("\n===== MENU =====")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar itens")
    print("4. Sair")
    return input("Escolha uma opção (1-4): ")

itens = []
opcao = ""

while opcao != "4":
    opcao = exibir_menu()
    
    if opcao == "1":
        item = input("Digite o nome do item: ")
        itens.append(item)
        print(f"Item '{item}' adicionado com sucesso!")
    
    elif opcao == "2":
        if not itens:
            print("Não há itens para remover.")
        else:
            for i, item in enumerate(itens):
                print(f"{i+1}. {item}")
            try:
                indice = int(input("Digite o número do item a remover: ")) - 1
                if 0 <= indice < len(itens):
                    item_removido = itens.pop(indice)
                    print(f"Item '{item_removido}' removido com sucesso!")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")
    
    elif opcao == "3":
        if not itens:
            print("A lista está vazia.")
        else:
            print("\n===== ITENS =====")
            for i, item in enumerate(itens):
                print(f"{i+1}. {item}")
    
    elif opcao == "4":
        print("Encerrando o programa...")
    
    else:
        print("Opção inválida. Por favor, tente novamente.")

print("Programa encerrado. Obrigado por utilizar!")