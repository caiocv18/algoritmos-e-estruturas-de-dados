# DEPOIS: Estrutura modular
# biblioteca/
#   ├── __init__.py
#   ├── main.py
#   ├── models/
#   │   ├── __init__.py
#   │   ├── livro.py
#   │   ├── usuario.py
#   │   └── emprestimo.py
#   ├── repositories/
#   │   ├── __init__.py
#   │   ├── base.py
#   │   ├── livro_repository.py
#   │   ├── usuario_repository.py
#   │   └── emprestimo_repository.py
#   ├── services/
#   │   ├── __init__.py
#   │   ├── biblioteca_service.py
#   │   └── notificacao_service.py
#   └── utils/
#       ├── __init__.py
#       ├── validadores.py
#       └── formatadores.py

# arquivo: models/livro.py
"""Modelo de dados para Livro."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Livro:
    """Representa um livro na biblioteca."""
    titulo: str
    autor: str
    isbn: str
    id: Optional[int] = None
    disponivel: bool = True
    data_cadastro: datetime = field(default_factory=datetime.now)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


# arquivo: repositories/base.py
"""Repositório base com funcionalidades comuns."""

from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')


class RepositoryBase(ABC, Generic[T]):
    """Classe base para todos os repositórios."""

    def __init__(self):
        self._items: List[T] = []
        self._proximo_id = 1

    @abstractmethod
    def _set_id(self, item: T, id_value: int) -> T:
        """Define o ID de um item."""
        pass

    def salvar(self, item: T) -> T:
        """Salva ou atualiza um item."""
        if not hasattr(item, 'id') or item.id is None:
            item = self._set_id(item, self._proximo_id)
            self._proximo_id += 1
            self._items.append(item)
        else:
            # Atualizar item existente
            for i, existing in enumerate(self._items):
                if existing.id == item.id:
                    self._items[i] = item
                    break
        return item

    def buscar_por_id(self, item_id: int) -> Optional[T]:
        """Busca um item pelo ID."""
        for item in self._items:
            if hasattr(item, 'id') and item.id == item_id:
                return item
        return None

    def listar_todos(self) -> List[T]:
        """Retorna todos os items."""
        return self._items.copy()

    def remover(self, item_id: int) -> bool:
        """Remove um item pelo ID."""
        for i, item in enumerate(self._items):
            if hasattr(item, 'id') and item.id == item_id:
                del self._items[i]
                return True
        return False


# arquivo: repositories/livro_repository.py
"""Repositório para livros."""

from typing import List, Optional
from models.livro import Livro
from .base import RepositoryBase


class LivroRepository(RepositoryBase[Livro]):
    """Gerencia a persistência de livros."""

    def _set_id(self, item: Livro, id_value: int) -> Livro:
        """Define o ID de um livro."""
        item.id = id_value
        return item

    def buscar_por_isbn(self, isbn: str) -> Optional[Livro]:
        """Busca um livro pelo ISBN."""
        for livro in self._items:
            if livro.isbn == isbn:
                return livro
        return None

    def buscar_disponiveis(self) -> List[Livro]:
        """Retorna apenas livros disponíveis."""
        return [livro for livro in self._items if livro.disponivel]

    def buscar_por_autor(self, autor: str) -> List[Livro]:
        """Busca livros de um autor específico."""
        autor_lower = autor.lower()
        return [
            livro for livro in self._items
            if autor_lower in livro.autor.lower()
        ]


# arquivo: services/biblioteca_service.py
"""Serviço principal da biblioteca."""

from datetime import datetime, timedelta
from typing import Optional, List
from models.livro import Livro
from models.usuario import Usuario
from models.emprestimo import Emprestimo
from repositories.livro_repository import LivroRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.emprestimo_repository import EmprestimoRepository


class BibliotecaService:
    """Gerencia as operações principais da biblioteca."""

    def __init__(
        self,
        livro_repo: LivroRepository,
        usuario_repo: UsuarioRepository,
        emprestimo_repo: EmprestimoRepository
    ):
        self.livro_repo = livro_repo
        self.usuario_repo = usuario_repo
        self.emprestimo_repo = emprestimo_repo

    def emprestar_livro(
        self,
        livro_id: int,
        usuario_id: int,
        dias_emprestimo: int = 14
    ) -> Optional[Emprestimo]:
        """
        Realiza o empréstimo de um livro.

        Args:
            livro_id: ID do livro
            usuario_id: ID do usuário
            dias_emprestimo: Número de dias do empréstimo

        Returns:
            Emprestimo se bem-sucedido, None caso contrário
        """
        # Validações
        livro = self.livro_repo.buscar_por_id(livro_id)
        if not livro:
            raise ValueError("Livro não encontrado")

        if not livro.disponivel:
            raise ValueError("Livro não está disponível")

        usuario = self.usuario_repo.buscar_por_id(usuario_id)
        if not usuario:
            raise ValueError("Usuário não encontrado")

        if not usuario.ativo:
            raise ValueError("Usuário não está ativo")

        # Verificar se usuário tem empréstimos pendentes
        emprestimos_pendentes = self.emprestimo_repo.buscar_por_usuario(
            usuario_id, apenas_ativos=True
        )

        if len(emprestimos_pendentes) >= 3:
            raise ValueError("Usuário já possui o máximo de empréstimos ativos")

        # Criar empréstimo
        emprestimo = Emprestimo(
            livro_id=livro_id,
            usuario_id=usuario_id,
            data_emprestimo=datetime.now(),
            data_devolucao_prevista=datetime.now() + timedelta(days=dias_emprestimo)
        )

        # Atualizar disponibilidade do livro
        livro.disponivel = False
        self.livro_repo.salvar(livro)

        # Salvar empréstimo
        return self.emprestimo_repo.salvar(emprestimo)
