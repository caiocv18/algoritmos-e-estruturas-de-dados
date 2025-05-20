def sistema_recomendacao():
    """Sistema simples de recomendação de produtos."""
    
    # Banco de dados simulado de produtos
    produtos = [
        {"id": 1, "nome": "Smartphone XYZ", "categoria": "eletrônicos", "preco": 1500.0, 
         "tags": ["tecnologia", "smartphone", "android"], "avaliacao": 4.5},
        {"id": 2, "nome": "Notebook Ultra", "categoria": "eletrônicos", "preco": 4200.0, 
         "tags": ["tecnologia", "computador", "trabalho"], "avaliacao": 4.8},
        {"id": 3, "nome": "Tênis Runner", "categoria": "esportes", "preco": 280.0, 
         "tags": ["esporte", "corrida", "casual"], "avaliacao": 4.3},
        {"id": 4, "nome": "Smart TV 50\"", "categoria": "eletrônicos", "preco": 3200.0, 
         "tags": ["tecnologia", "entretenimento", "casa"], "avaliacao": 4.6},
        {"id": 5, "nome": "Livro: Python Essencial", "categoria": "livros", "preco": 85.0, 
         "tags": ["educação", "programação", "tecnologia"], "avaliacao": 4.9},
        {"id": 6, "nome": "Bicicleta Mountain", "categoria": "esportes", "preco": 1800.0, 
         "tags": ["esporte", "lazer", "aventura"], "avaliacao": 4.7},
        {"id": 7, "nome": "Fone Bluetooth", "categoria": "eletrônicos", "preco": 150.0, 
         "tags": ["tecnologia", "música", "acessório"], "avaliacao": 4.2},
        {"id": 8, "nome": "Camisa Polo", "categoria": "vestuário", "preco": 120.0, 
         "tags": ["casual", "moda", "conforto"], "avaliacao": 4.0},
        {"id": 9, "nome": "Cafeteira Express", "categoria": "eletrodomésticos", "preco": 350.0, 
         "tags": ["casa", "bebida", "cozinha"], "avaliacao": 4.4},
        {"id": 10, "nome": "Mochila Travel", "categoria": "acessórios", "preco": 200.0, 
         "tags": ["viagem", "organização", "casual"], "avaliacao": 4.3},
    ]
    
    print("\n===== SISTEMA DE RECOMENDAÇÃO =====")
    print("Bem-vindo ao nosso sistema de recomendação personalizada!")
    
    # 1. Coleta de dados do perfil
    perfil = coletar_perfil()
    if not perfil:
        return
    
    # 2. Obtenção de preferências
    preferencias = obter_preferencias()
    if not preferencias:
        return
    
    # 3. Simulação de histórico de compras
    historico = simular_historico()
    
    # 4. Geração de recomendações
    recomendacoes = gerar_recomendacoes(perfil, preferencias, historico, produtos)
    
    # 5. Apresentação dos resultados
    exibir_recomendacoes(recomendacoes)

def coletar_perfil():
    """Coleta e valida os dados do perfil do usuário."""
    print("\n-- Perfil do Usuário --")
    
    try:
        # Coleta básica de dados
        nome = input("Nome: ")
        if not nome.strip():
            print("Erro: Nome não pode estar vazio.")
            return None
        
        idade_str = input("Idade: ")
        try:
            idade = int(idade_str)
            if idade < 18 or idade > 100:
                print("Aviso: Idade fora do intervalo comum (18-100).")
                confirmacao = input("Deseja continuar mesmo assim? (s/n): ").lower()
                if confirmacao != 's':
                    return None
        except ValueError:
            print("Erro: Idade deve ser um número inteiro.")
            return None
        
        print("\nFaixa de Renda:")
        print("1. Até R$ 2.000")
        print("2. R$ 2.001 a R$ 5.000")
        print("3. R$ 5.001 a R$ 10.000")
        print("4. Acima de R$ 10.000")
        
        renda_opcao = input("Selecione sua faixa de renda (1-4): ")
        if not renda_opcao.isdigit() or int(renda_opcao) not in range(1, 5):
            print("Erro: Opção inválida.")
            return None
        
        faixas_renda = ["Até R$ 2.000", "R$ 2.001 a R$ 5.000", "R$ 5.001 a R$ 10.000", "Acima de R$ 10.000"]
        renda = faixas_renda[int(renda_opcao) - 1]
        
        # Construção e retorno do perfil
        perfil = {
            "nome": nome,
            "idade": idade,
            "renda": renda
        }
        
        return perfil
        
    except Exception as e:
        print(f"Erro ao coletar perfil: {e}")
        return None

def obter_preferencias():
    """Coleta preferências do usuário para recomendações."""
    print("\n-- Preferências --")
    
    try:
        # Lista de categorias disponíveis
        categorias = ["eletrônicos", "esportes", "livros", "vestuário", "eletrodomésticos", "acessórios"]
        
        print("Categorias de interesse (selecione pelo menos uma):")
        for i, categoria in enumerate(categorias, 1):
            print(f"{i}. {categoria.capitalize()}")
        
        selecao = input("Digite os números das categorias separados por vírgula: ")
        indices = [int(i.strip()) for i in selecao.split(",") if i.strip().isdigit()]
        
        if not indices or not all(1 <= i <= len(categorias) for i in indices):
            print("Erro: Seleção inválida.")
            return None
        
        categorias_selecionadas = [categorias[i-1] for i in indices]
        
        # Coleta de faixa de preço
        print("\nFaixa de preço preferida:")
        print("1. Econômico (até R$ 200)")
        print("2. Intermediário (R$ 201 a R$ 1.000)")
        print("3. Premium (acima de R$ 1.000)")
        print("4. Sem preferência")
        
        preco_opcao = input("Selecione uma opção (1-4): ")
        if not preco_opcao.isdigit() or int(preco_opcao) not in range(1, 5):
            print("Erro: Opção inválida. Usando 'Sem preferência'.")
            preco_opcao = "4"
        
        faixas_preco = ["econômico", "intermediário", "premium", "qualquer"]
        faixa_preco = faixas_preco[int(preco_opcao) - 1]
        
        # Coleta de palavras-chave de interesse
        print("\nDigite algumas palavras-chave de seu interesse (separadas por vírgula):")
        tags_input = input("Tags: ")
        tags = [tag.strip().lower() for tag in tags_input.split(",") if tag.strip()]
        
        # Construção e retorno das preferências
        preferencias = {
            "categorias": categorias_selecionadas,
            "faixa_preco": faixa_preco,
            "tags": tags
        }
        
        return preferencias
        
    except Exception as e:
        print(f"Erro ao coletar preferências: {e}")
        return None

def simular_historico():
    """Simula um histórico de compras para fins de demonstração."""
    return [
        {"produto_id": 3, "data": "10/04/2023", "avaliacao": 5},
        {"produto_id": 7, "data": "22/05/2023", "avaliacao": 4},
        {"produto_id": 2, "data": "15/06/2023", "avaliacao": 5}
    ]

def gerar_recomendacoes(perfil, preferencias, historico, produtos):
    """
    Gera recomendações personalizadas com base no perfil, preferências e histórico.
    Utiliza múltiplos critérios condicionais para pontuação dos produtos.
    """
    recomendacoes = []
    
    # Pontuação para cada produto
    for produto in produtos:
        # Inicializa pontuação
        pontuacao = 0
        motivos = []
        
        # Verifica se o produto já foi comprado
        ids_comprados = [item["produto_id"] for item in historico]
        if produto["id"] in ids_comprados:
            continue  # Pula produtos já comprados
        
        # Pontuação por categoria
        if produto["categoria"] in preferencias["categorias"]:
            pontuacao += 30
            motivos.append(f"Categoria {produto['categoria']} de interesse")
        
        # Pontuação por faixa de preço
        if preferencias["faixa_preco"] == "econômico" and produto["preco"] <= 200:
            pontuacao += 20
            motivos.append("Preço econômico")
        elif preferencias["faixa_preco"] == "intermediário" and 200 < produto["preco"] <= 1000:
            pontuacao += 20
            motivos.append("Preço intermediário")
        elif preferencias["faixa_preco"] == "premium" and produto["preco"] > 1000:
            pontuacao += 20
            motivos.append("Produto premium")
        elif preferencias["faixa_preco"] == "qualquer":
            pontuacao += 10
        
        # Pontuação por tags
        tags_coincidentes = [tag for tag in produto["tags"] if tag in preferencias["tags"]]
        if tags_coincidentes:
            pontuacao += 5 * len(tags_coincidentes)
            motivos.append(f"Tags coincidentes: {', '.join(tags_coincidentes)}")
        
        # Pontuação por avaliação
        if produto["avaliacao"] >= 4.5:
            pontuacao += 15
            motivos.append("Produto muito bem avaliado")
        elif produto["avaliacao"] >= 4.0:
            pontuacao += 10
            motivos.append("Produto bem avaliado")
        
        # Ajuste com base no perfil e histórico
        # Se o usuário comprou produtos de tecnologia e este é de tecnologia
        tecnologia_no_historico = any(
            "tecnologia" in produtos[item["produto_id"]-1]["tags"] 
            for item in historico if 1 <= item["produto_id"] <= len(produtos)
        )
        if tecnologia_no_historico and "tecnologia" in produto["tags"]:
            pontuacao += 10
            motivos.append("Baseado em compras anteriores de tecnologia")
        
        # Ajuste com base na idade
        if perfil["idade"] < 30 and "tecnologia" in produto["tags"]:
            pontuacao += 5
            motivos.append("Popular entre jovens adultos")
        
        # Ajuste com base na renda
        if "Acima de R$ 10.000" in perfil["renda"] and produto["preco"] > 1000:
            pontuacao += 10
            motivos.append("Compatível com sua faixa de renda")
        elif "R$ 2.001 a R$ 5.000" in perfil["renda"] and 200 < produto["preco"] < 500:
            pontuacao += 5
            motivos.append("Bom custo-benefício para sua faixa de renda")
        
        # Adiciona à lista de recomendações se tiver pontuação mínima
        if pontuacao >= 30:
            recomendacoes.append({
                "produto": produto,
                "pontuacao": pontuacao,
                "motivos": motivos
            })
    
    # Ordena pela pontuação, maior primeiro
    recomendacoes.sort(key=lambda x: x["pontuacao"], reverse=True)
    
    # Limita a 5 recomendações
    return recomendacoes[:5]

def exibir_recomendacoes(recomendacoes):
    """Exibe as recomendações geradas de forma formatada."""
    if not recomendacoes:
        print("\nNão foi possível encontrar recomendações adequadas ao seu perfil.")
        print("Sugestões:")
        print("- Tente selecionar mais categorias de interesse")
        print("- Adicione mais tags/palavras-chave")
        print("- Altere suas preferências de preço")
        return
    
    print("\n===== RECOMENDAÇÕES PERSONALIZADAS =====")
    print(f"Encontramos {len(recomendacoes)} produtos que podem te interessar:\n")
    
    for i, rec in enumerate(recomendacoes, 1):
        produto = rec["produto"]
        print(f"--- Recomendação {i} ---")
        print(f"Produto: {produto['nome']}")
        print(f"Categoria: {produto['categoria'].capitalize()}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Avaliação: {produto['avaliacao']:.1f}/5.0")
        print(f"Tags: {', '.join(produto['tags'])}")
        print(f"Por que recomendamos: {'; '.join(rec['motivos'])}")
        print()
    
    print("Estas recomendações foram geradas com base no seu perfil, preferências e padrões de compra.")
    print("A ordem leva em consideração a relevância estimada para você.")

# Execução do sistema
if __name__ == "__main__":
    sistema_recomendacao()