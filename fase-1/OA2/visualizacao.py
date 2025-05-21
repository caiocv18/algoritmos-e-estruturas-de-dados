# visualizacao.py
from typing import Dict, List, Tuple
from datetime import datetime
from modelo import Produto, RepositorioDados

def exibir_titulo(titulo: str) -> None:
    """Exibe um título formatado."""
    print("\n" + "=" * 50)
    print(f"{titulo.center(50)}")
    print("=" * 50)

def exibir_total_vendas(total: float) -> None:
    """Exibe o total de vendas formatado."""
    exibir_titulo("TOTAL DE VENDAS")
    print(f"Valor total: R$ {total:.2f}")

def exibir_vendas_por_categoria(vendas_por_categoria: Dict[str, float]) -> None:
    """Exibe o total de vendas por categoria."""
    exibir_titulo("VENDAS POR CATEGORIA")

    # Calcular o total geral para percentuais
    total_geral = sum(vendas_por_categoria.values())

    for categoria, valor in sorted(vendas_por_categoria.items(),
                                  key=lambda x: x[1], reverse=True):
        percentual = (valor / total_geral) * 100 if total_geral > 0 else 0
        print(f"{categoria}: R$ {valor:.2f} ({percentual:.1f}%)")

def exibir_produtos_mais_vendidos(produtos_mais_vendidos: List[Tuple[Produto, int]]) -> None:
    """Exibe os produtos mais vendidos."""
    exibir_titulo("PRODUTOS MAIS VENDIDOS")

    for i, (produto, quantidade) in enumerate(produtos_mais_vendidos, 1):
        print(f"{i}. {produto.nome} - {quantidade} unidades (R$ {produto.preco:.2f} cada)")

def exibir_tendencia_vendas(tendencia: List[Tuple[datetime, float]]) -> None:
    """Exibe a tendência de vendas dos últimos dias."""
    exibir_titulo("TENDÊNCIA DE VENDAS")

    # Determinar a largura máxima do gráfico
    max_valor = max([valor for _, valor in tendencia]) if tendencia else 0
    largura_max = 40

    for data, valor in tendencia:
        data_str = data.strftime("%d/%m/%Y")
        if max_valor > 0:
            barras = int((valor / max_valor) * largura_max)
        else:
            barras = 0
        print(f"{data_str}: {'█' * barras} R$ {valor:.2f}")

def exibir_menu() -> str:
    """Exibe o menu e retorna a opção escolhida."""
    exibir_titulo("SISTEMA DE ANÁLISE DE VENDAS")
    print("1. Mostrar Total de Vendas")
    print("2. Mostrar Vendas por Categoria")
    print("3. Mostrar Produtos Mais Vendidos")
    print("4. Mostrar Tendência de Vendas")
    print("5. Mostrar Todas as Análises")
    print("0. Sair")
    return input("\nEscolha uma opção: ")
