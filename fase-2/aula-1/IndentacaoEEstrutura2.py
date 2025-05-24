def verificar_estoque_critico():
    """Verifica produtos com estoque baixo."""
    produtos = {
        "Notebook": 5,
        "Mouse": 2,
        "Teclado": 15,
        "Monitor": 1
    }

    estoque_minimo = 3
    produtos_criticos = []

    for produto, quantidade in produtos.items():
        if quantidade <= estoque_minimo:
            produtos_criticos.append(produto)
            print(f"⚠️  ALERTA: {produto} com apenas {quantidade} unidades!")

    if produtos_criticos:
        print(f"\nTotal de produtos em situação crítica: {len(produtos_criticos)}")
    else:
        print("✓ Todos os produtos têm estoque adequado.")

verificar_estoque_critico()