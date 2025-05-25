# arquivo: utils/validadores.py
"""Funções de validação reutilizáveis."""

import re
from typing import Optional


def validar_isbn(isbn: str) -> bool:
    """
    Valida um ISBN-10 ou ISBN-13.

    Args:
        isbn: String contendo o ISBN

    Returns:
        True se válido, False caso contrário
    """
    # Remove hífens e espaços
    isbn = isbn.replace("-", "").replace(" ", "")

    # ISBN-10
    if len(isbn) == 10:
        if not isbn[:-1].isdigit():
            return False

        soma = sum(int(isbn[i]) * (10 - i) for i in range(9))
        check = 11 - (soma % 11)

        if check == 10:
            return isbn[-1].upper() == 'X'
        elif check == 11:
            return isbn[-1] == '0'
        else:
            return isbn[-1] == str(check)

    # ISBN-13
    elif len(isbn) == 13:
        if not isbn.isdigit():
            return False

        soma = sum(
            int(isbn[i]) * (3 if i % 2 else 1)
            for i in range(12)
        )
        check = (10 - (soma % 10)) % 10

        return int(isbn[-1]) == check

    return False


# arquivo: main.py
"""Ponto de entrada da aplicação."""

import sys
from repositories.livro_repository import LivroRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.emprestimo_repository import EmprestimoRepository
from services.biblioteca_service import BibliotecaService
from ui.menu_principal import MenuPrincipal


def main():
    """Função principal da aplicação."""
    # Inicializar repositórios
    livro_repo = LivroRepository()
    usuario_repo = UsuarioRepository()
    emprestimo_repo = EmprestimoRepository()

    # Inicializar serviço
    biblioteca_service = BibliotecaService(
        livro_repo,
        usuario_repo,
        emprestimo_repo
    )

    # Carregar dados iniciais (se existirem)
    try:
        livro_repo.carregar_de_arquivo("data/livros.json")
        usuario_repo.carregar_de_arquivo("data/usuarios.json")
        emprestimo_repo.carregar_de_arquivo("data/emprestimos.json")
    except FileNotFoundError:
        print("Iniciando com banco de dados vazio.")

    # Iniciar interface
    menu = MenuPrincipal(biblioteca_service)

    try:
        menu.executar()
    except KeyboardInterrupt:
        print("\nEncerrando aplicação...")
    finally:
        # Salvar dados
        livro_repo.salvar_em_arquivo("data/livros.json")
        usuario_repo.salvar_em_arquivo("data/usuarios.json")
        emprestimo_repo.salvar_em_arquivo("data/emprestimos.json")
        print("Dados salvos com sucesso!")


if __name__ == "__main__":
    main()