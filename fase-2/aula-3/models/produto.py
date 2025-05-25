# ESTRUTURA COM BOA SEPARAÇÃO DE RESPONSABILIDADES

# arquivo: models/produto.py
"""Modelo de dados do Produto - responsável apenas pela estrutura."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Produto:
    """Representa um produto no sistema."""
    id: Optional[int] = None
    nome: str = ""
    preco: float = 0.0
    estoque: int = 0
    criado_em: datetime = None

    def __post_init__(self):
        if self.criado_em is None:
            self.criado_em = datetime.now()


# arquivo: repositories/produto_repository.py
"""Repositório - responsável apenas por persistência de dados."""

from typing import List, Optional
from models.produto import Produto

class ProdutoRepository:
    """Gerencia a persistência de produtos."""

    def __init__(self):
        self._produtos = {}# Simulando um banco de dados
        self._proximo_id = 1

    def salvar(self, produto: Produto) -> Produto:
        """Salva ou atualiza um produto."""
        if produto.id is None:
            produto.id = self._proximo_id
            self._proximo_id += 1

        self._produtos[produto.id] = produto
        return produto

    def buscar_por_id(self, produto_id: int) -> Optional[Produto]:
        """Busca um produto pelo ID."""
        return self._produtos.get(produto_id)

    def listar_todos(self) -> List[Produto]:
        """Retorna todos os produtos."""
        return list(self._produtos.values())


# arquivo: services/produto_service.py
"""Serviço - responsável pela lógica de negócios."""

from typing import List, Optional
from models.produto import Produto
from repositories.produto_repository import ProdutoRepository

class ProdutoService:
    """Implementa a lógica de negócios para produtos."""

    def __init__(self, repository: ProdutoRepository):
        self.repository = repository

    def criar_produto(self, nome: str, preco: float, estoque: int) -> Produto:
        """Cria um novo produto com validação."""
        if not nome:
            raise ValueError("Nome do produto é obrigatório")
        if preco < 0:
            raise ValueError("Preço não pode ser negativo")
        if estoque < 0:
            raise ValueError("Estoque não pode ser negativo")

        produto = Produto(nome=nome, preco=preco, estoque=estoque)
        return self.repository.salvar(produto)

    def aplicar_desconto(self, produto_id: int, percentual: float) -> Optional[Produto]:
        """Aplica desconto a um produto."""
        if not 0 <= percentual <= 100:
            raise ValueError("Percentual deve estar entre 0 e 100")

        produto = self.repository.buscar_por_id(produto_id)
        if produto:
            produto.preco *= (1 - percentual / 100)
            return self.repository.salvar(produto)
        return None


# arquivo: controllers/produto_controller.py
"""Controller - responsável por coordenar a interação entre UI e serviços."""

from services.produto_service import ProdutoService

class ProdutoController:
    """Coordena as operações de produto."""

    def __init__(self, service: ProdutoService):
        self.service = service

    def processar_novo_produto(self, dados_formulario: dict):
        """Processa dados do formulário e cria produto."""
        try:
            produto = self.service.criar_produto(
                nome=dados_formulario.get('nome', ''),
                preco=float(dados_formulario.get('preco', 0)),
                estoque=int(dados_formulario.get('estoque', 0))
            )
            return {"sucesso": True, "produto_id": produto.id}
        except ValueError as e:
            return {"sucesso": False, "erro": str(e)}