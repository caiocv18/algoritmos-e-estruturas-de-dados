def gerar_relatorio(titulo, formato="PDF", incluir_graficos=True, idioma="pt-BR"):
    """
    Gera um relatório com configurações customizáveis.

    Args:
        titulo: Título do relatório (obrigatório)
        formato: Formato de saída (padrão: PDF)
        incluir_graficos: Se deve incluir gráficos (padrão: True)
        idioma: Idioma do relatório (padrão: pt-BR)
    """
    print(f"Gerando relatório: '{titulo}'")
    print(f"Formato: {formato}")
    print(f"Incluir gráficos: {'Sim' if incluir_graficos else 'Não'}")
    print(f"Idioma: {idioma}")
    print("-" * 40)

# Diferentes formas de chamar a função
gerar_relatorio("Vendas Mensais")# Usa todos os padrões
gerar_relatorio("Análise Trimestral", "Excel")# Sobrescreve formato
gerar_relatorio("Balanço Anual", "PDF", False)# Sem gráficos
gerar_relatorio("Report", "HTML", True, "en-US")# Todos personalizados