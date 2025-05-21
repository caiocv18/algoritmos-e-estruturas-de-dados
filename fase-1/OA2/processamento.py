# processamento.py
from typing import Dict, List, Tuple
from datetime import datetime
from modelo import RepositorioDados, Produto, Venda

def calcular_total_vendas(repositorio: RepositorioDados) -> float:
    """
    Calcula o valor total de todas as vendas.

    Args:
        repositorio: Repositório contendo produtos e vendas

    Returns:
        float: Valor total das vendas
    """
    total = 0.0
    for venda in repositorio.vendas:
        produto = repositorio.buscar_produto_por_id(venda.produto_id)
        if produto:
            total += produto.preco * venda.quantidade
    return total

def calcular_vendas_por_categoria(repositorio: RepositorioDados) -> Dict[str, float]:
    """
    Calcula o total de vendas por categoria.

    Args:
        repositorio: Repositório contendo produtos e vendas

    Returns:
        Dict[str, float]: Dicionário mapeando categorias para valores totais
    """
    vendas_por_categoria = {}

    for venda in repositorio.vendas:
        produto = repositorio.buscar_produto_por_id(venda.produto_id)
        if produto:
            valor_venda = produto.preco * venda.quantidade
            if produto.categoria in vendas_por_categoria:
                vendas_por_categoria[produto.categoria] += valor_venda
            else:
                vendas_por_categoria[produto.categoria] = valor_venda

    return vendas_por_categoria

def calcular_produtos_mais_vendidos(repositorio: RepositorioDados, top_n: int = 3) -> List[Tuple[Produto, int]]:
    """
    Determina os produtos mais vendidos em quantidade.

    Args:
        repositorio: Repositório contendo produtos e vendas
        top_n: Número de produtos para retornar

    Returns:
        List[Tuple[Produto, int]]: Lista de tuplas (produto, quantidade total vendida)
    """
    vendas_por_produto = {}

    for venda in repositorio.vendas:
        if venda.produto_id in vendas_por_produto:
            vendas_por_produto[venda.produto_id] += venda.quantidade
        else:
            vendas_por_produto[venda.produto_id] = venda.quantidade

    # Converter ids para objetos Produto
    resultado = []
    for produto_id, quantidade in vendas_por_produto.items():
        produto = repositorio.buscar_produto_por_id(produto_id)
        if produto:
            resultado.append((produto, quantidade))

    # Ordenar por quantidade (decrescente) e limitar ao top_n
    resultado.sort(key=lambda x: x[1], reverse=True)
    return resultado[:top_n]

def analisar_tendencia_vendas(repositorio: RepositorioDados, dias: int = 7) -> List[Tuple[datetime, float]]:
    """
    Analisa a tendência de vendas nos últimos dias.

    Args:
        repositorio: Repositório contendo produtos e vendas
        dias: Número de dias para analisar

    Returns:
        List[Tuple[datetime, float]]: Lista de tuplas (data, valor total)
    """
    from datetime import datetime, timedelta

    # Inicializar dicionário com os últimos 'dias' dias
    hoje = datetime.now()
    vendas_diarias = {}
    for i in range(dias):
        data = hoje - timedelta(days=i)
        data_apenas = datetime(data.year, data.month, data.day)
        vendas_diarias[data_apenas] = 0.0

    # Somar vendas por dia
    for venda in repositorio.vendas:
        data_venda = datetime(venda.data.year, venda.data.month, venda.data.day)
        if data_venda in vendas_diarias:
            produto = repositorio.buscar_produto_por_id(venda.produto_id)
            if produto:
                vendas_diarias[data_venda] += produto.preco * venda.quantidade

    # Converter para lista de tuplas e ordenar por data
    resultado = [(data, valor) for data, valor in vendas_diarias.items()]
    resultado.sort(key=lambda x: x[0])
    return resultado
