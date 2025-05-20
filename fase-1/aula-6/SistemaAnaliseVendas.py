def sistema_analise_vendas():
    # Simulação de base de dados de vendas
    vendas = []
    
    while True:
        print("\n==== SISTEMA DE ANÁLISE DE VENDAS ====")
        print("1. Cadastrar nova venda")
        print("2. Visualizar vendas")
        print("3. Análise por categoria")
        print("4. Análise por região")
        print("5. Relatório personalizado")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            nova_venda = cadastrar_venda()
            if nova_venda:
                vendas.append(nova_venda)
                print("Venda cadastrada com sucesso!")
        
        elif opcao == "2":
            visualizar_vendas(vendas)
        
        elif opcao == "3":
            analise_por_categoria(vendas)
        
        elif opcao == "4":
            analise_por_regiao(vendas)
        
        elif opcao == "5":
            relatorio_personalizado(vendas)
        
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

def cadastrar_venda():
    print("\n-- Cadastro de Nova Venda --")
    
    # Entrada de dados
    try:
        produto = input("Nome do produto: ")
        valor = float(input("Valor da venda: R$ "))
        
        print("\nCategorias disponíveis:")
        print("1. Eletrônicos")
        print("2. Vestuário")
        print("3. Alimentos")
        print("4. Móveis")
        
        categoria_opcao = input("Selecione a categoria (1-4): ")
        categorias = ["", "Eletrônicos", "Vestuário", "Alimentos", "Móveis"]
        if not categoria_opcao.isdigit() or int(categoria_opcao) not in range(1, 5):
            print("Erro: Categoria inválida.")
            return None
        categoria = categorias[int(categoria_opcao)]
        
        print("\nRegiões disponíveis:")
        print("1. Norte")
        print("2. Nordeste")
        print("3. Centro-Oeste")
        print("4. Sudeste")
        print("5. Sul")
        
        regiao_opcao = input("Selecione a região (1-5): ")
        regioes = ["", "Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
        if not regiao_opcao.isdigit() or int(regiao_opcao) not in range(1, 6):
            print("Erro: Região inválida.")
            return None
        regiao = regioes[int(regiao_opcao)]
        
        data = input("Data da venda (DD/MM/AAAA): ")
        # Validação simples de data
        if len(data.split('/')) != 3:
            print("Erro: Formato de data inválido. Use DD/MM/AAAA.")
            return None
    
    except ValueError:
        print("Erro: Valor inválido.")
        return None
    
    # Validação dos dados
    if not produto.strip():
        print("Erro: Nome do produto é obrigatório.")
        return None
    
    if valor <= 0:
        print("Erro: Valor da venda deve ser maior que zero.")
        return None
    
    # Criação do registro de venda
    venda = {
        "produto": produto,
        "valor": valor,
        "categoria": categoria,
        "regiao": regiao,
        "data": data
    }
    
    return venda

def visualizar_vendas(vendas):
    if not vendas:
        print("\nNenhuma venda cadastrada.")
        return
    
    print("\n-- Lista de Vendas --")
    print(f"{'Produto':<20} {'Valor':<10} {'Categoria':<15} {'Região':<15} {'Data':<12}")
    print("-" * 75)
    
    for venda in vendas:
        print(f"{venda['produto']:<20} R$ {venda['valor']:<8.2f} {venda['categoria']:<15} {venda['regiao']:<15} {venda['data']:<12}")
    
    print("-" * 75)
    print(f"Total de vendas: {len(vendas)}")
    total_valor = sum(venda['valor'] for venda in vendas)
    print(f"Valor total: R$ {total_valor:.2f}")

def analise_por_categoria(vendas):
    if not vendas:
        print("\nNenhuma venda cadastrada.")
        return
    
    # Agregação por categoria
    categorias = {}
    for venda in vendas:
        categoria = venda['categoria']
        if categoria in categorias:
            categorias[categoria]['total'] += venda['valor']
            categorias[categoria]['quantidade'] += 1
        else:
            categorias[categoria] = {
                'total': venda['valor'],
                'quantidade': 1
            }
    
    # Exibição dos resultados
    print("\n-- Análise por Categoria --")
    print(f"{'Categoria':<15} {'Quantidade':<12} {'Total':<15} {'Média':<10}")
    print("-" * 55)
    
    for categoria, dados in categorias.items():
        media = dados['total'] / dados['quantidade']
        print(f"{categoria:<15} {dados['quantidade']:<12} R$ {dados['total']:<12.2f} R$ {media:.2f}")
    
    # Identificação da categoria com maior venda total
    if categorias:
        cat_maior_venda = max(categorias, key=lambda k: categorias[k]['total'])
        print("\nCategoria com maior venda total:", cat_maior_venda)
        print(f"Total: R$ {categorias[cat_maior_venda]['total']:.2f}")

def analise_por_regiao(vendas):
    if not vendas:
        print("\nNenhuma venda cadastrada.")
        return
    
    # Agregação por região
    regioes = {}
    for venda in vendas:
        regiao = venda['regiao']
        if regiao in regioes:
            regioes[regiao]['total'] += venda['valor']
            regioes[regiao]['quantidade'] += 1
        else:
            regioes[regiao] = {
                'total': venda['valor'],
                'quantidade': 1
            }
    
    # Exibição dos resultados
    print("\n-- Análise por Região --")
    print(f"{'Região':<15} {'Quantidade':<12} {'Total':<15} {'Média':<10}")
    print("-" * 55)
    
    for regiao, dados in regioes.items():
        media = dados['total'] / dados['quantidade']
        print(f"{regiao:<15} {dados['quantidade']:<12} R$ {dados['total']:<12.2f} R$ {media:.2f}")
    
    # Identificação da região com maior venda total
    if regioes:
        reg_maior_venda = max(regioes, key=lambda k: regioes[k]['total'])
        print("\nRegião com maior venda total:", reg_maior_venda)
        print(f"Total: R$ {regioes[reg_maior_venda]['total']:.2f}")

def relatorio_personalizado(vendas):
    if not vendas:
        print("\nNenhuma venda cadastrada.")
        return
    
    print("\n-- Relatório Personalizado --")
    print("Selecione os filtros desejados:")
    
    # Seleção de categoria
    print("\nCategorias disponíveis:")
    print("0. Todas")
    print("1. Eletrônicos")
    print("2. Vestuário")
    print("3. Alimentos")
    print("4. Móveis")
    
    categoria_opcao = input("Selecione a categoria (0-4): ")
    categorias = ["Todas", "Eletrônicos", "Vestuário", "Alimentos", "Móveis"]
    if not categoria_opcao.isdigit() or int(categoria_opcao) not in range(0, 5):
        print("Erro: Opção inválida. Usando 'Todas'.")
        categoria_opcao = "0"
    
    # Seleção de região
    print("\nRegiões disponíveis:")
    print("0. Todas")
    print("1. Norte")
    print("2. Nordeste")
    print("3. Centro-Oeste")
    print("4. Sudeste")
    print("5. Sul")
    
    regiao_opcao = input("Selecione a região (0-5): ")
    regioes = ["Todas", "Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
    if not regiao_opcao.isdigit() or int(regiao_opcao) not in range(0, 6):
        print("Erro: Opção inválida. Usando 'Todas'.")
        regiao_opcao = "0"
    
    # Seleção de valor mínimo
    try:
        valor_min = input("Valor mínimo (ou Enter para ignorar): ")
        valor_min = float(valor_min) if valor_min else 0
    except ValueError:
        print("Erro: Valor inválido. Usando 0.")
        valor_min = 0
    
    # Aplicação dos filtros
    vendas_filtradas = []
    for venda in vendas:
        include = True
        
        # Filtro de categoria
        if categoria_opcao != "0" and venda['categoria'] != categorias[int(categoria_opcao)]:
            include = False
        
        # Filtro de região
        if regiao_opcao != "0" and venda['regiao'] != regioes[int(regiao_opcao)]:
            include = False
        
        # Filtro de valor mínimo
        if venda['valor'] < valor_min:
            include = False
        
        if include:
            vendas_filtradas.append(venda)
    
    # Exibição dos resultados
    if not vendas_filtradas:
        print("\nNenhuma venda encontrada com os filtros selecionados.")
        return
    
    print("\n-- Resultado do Relatório --")
    print(f"Categoria: {categorias[int(categoria_opcao)]}")
    print(f"Região: {regioes[int(regiao_opcao)]}")
    print(f"Valor mínimo: R$ {valor_min:.2f}")
    print(f"Total de vendas encontradas: {len(vendas_filtradas)}")
    
    # Resumo
    total_valor = sum(venda['valor'] for venda in vendas_filtradas)
    media_valor = total_valor / len(vendas_filtradas)
    
    print(f"\nValor total das vendas: R$ {total_valor:.2f}")
    print(f"Valor médio por venda: R$ {media_valor:.2f}")
    
    # Detalhamento (opcional)
    mostrar_detalhes = input("\nDeseja ver os detalhes das vendas? (s/n): ").lower() == 's'
    
    if mostrar_detalhes:
        print("\nDetalhes das vendas:")
        print(f"{'Produto':<20} {'Valor':<10} {'Categoria':<15} {'Região':<15} {'Data':<12}")
        print("-" * 75)
        
        for venda in vendas_filtradas:
            print(f"{venda['produto']:<20} R$ {venda['valor']:<8.2f} {venda['categoria']:<15} {venda['regiao']:<15} {venda['data']:<12}")

# Execução do sistema
if __name__ == "__main__":
    sistema_analise_vendas()