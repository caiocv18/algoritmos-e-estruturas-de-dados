# modelo.py
from typing import List, Dict, Union, Tuple
from datetime import datetime

class Produto:
    """Representa um produto no sistema."""

    def __init__(self, id: int, nome: str, categoria: str, preco: float):
        """
        Inicializa um novo produto.

        Args:
            id: Identificador único do produto
            nome: Nome do produto
            categoria: Categoria à qual o produto pertence
            preco: Preço unitário do produto
        """
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco

    def __str__(self) -> str:
        """Retorna uma representação em string do produto."""
        return f"Produto(id={self.id}, nome={self.nome}, categoria={self.categoria}, preço={self.preco:.2f})"


class Venda:
    """Representa uma transação de venda."""

    def __init__(self, id: int, data: datetime, produto_id: int, quantidade: int):
        """
        Inicializa uma nova venda.

        Args:
            id: Identificador único da venda
            data: Data e hora da venda
            produto_id: ID do produto vendido
            quantidade: Quantidade vendida
        """
        self.id = id
        self.data = data
        self.produto_id = produto_id
        self.quantidade = quantidade

    def __str__(self) -> str:
        """Retorna uma representação em string da venda."""
        data_formatada = self.data.strftime("%d/%m/%Y %H:%M")
        return f"Venda(id={self.id}, data={data_formatada}, produto_id={self.produto_id}, quantidade={self.quantidade})"


class RepositorioDados:
    """Gerencia o armazenamento de produtos e vendas."""

    def __init__(self):
        """Inicializa o repositório com listas vazias."""
        self.produtos: List[Produto] = []
        self.vendas: List[Venda] = []

    def adicionar_produto(self, produto: Produto) -> None:
        """Adiciona um produto ao repositório."""
        self.produtos.append(produto)

    def adicionar_venda(self, venda: Venda) -> None:
        """Adiciona uma venda ao repositório."""
        self.vendas.append(venda)

    def buscar_produto_por_id(self, produto_id: int) -> Union[Produto, None]:
        """Busca um produto pelo ID."""
        for produto in self.produtos:
            if produto.id == produto_id:
                return produto
        return None

    def buscar_vendas_por_periodo(self, data_inicio: datetime, data_fim: datetime) -> List[Venda]:
        """Retorna vendas realizadas em um período específico."""
        return [v for v in self.vendas if data_inicio <= v.data <= data_fim]

    def carregar_dados_exemplo(self) -> None:
        """Carrega dados de exemplo para testes."""
        # Produtos
        produtos = [
            Produto(1, "Notebook", "Eletrônicos", 3500.00),
            Produto(2, "Mouse", "Periféricos", 120.00),
            Produto(3, "Teclado", "Periféricos", 200.00),
            Produto(4, "Monitor", "Eletrônicos", 1200.00),
            Produto(5, "Headset", "Periféricos", 300.00)
        ]

        for produto in produtos:
            self.adicionar_produto(produto)

        # Vendas (últimos 30 dias)
        import random
        from datetime import timedelta

        hoje = datetime.now()
        for i in range(1, 31):
            # Gerar entre 1 e 5 vendas por dia
            for j in range(random.randint(1, 5)):
                venda_id = (i - 1) * 5 + j + 1
                data = hoje - timedelta(days=30-i,
                                       hours=random.randint(0, 23),
                                       minutes=random.randint(0, 59))
                produto_id = random.randint(1, 5)
                quantidade = random.randint(1, 3)

                self.adicionar_venda(Venda(venda_id, data, produto_id, quantidade))
