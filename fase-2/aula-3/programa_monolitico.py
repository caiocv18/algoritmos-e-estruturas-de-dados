"""
Sistema de gerenciamento de biblioteca - versão monolítica.

Este módulo implementa um sistema simples de gerenciamento de biblioteca
com funcionalidades básicas de cadastro de livros, usuários e empréstimos.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional


# Armazenamento em memória
livros: List[Dict] = []
usuarios: List[Dict] = []
emprestimos: List[Dict] = []


def adicionar_livro(titulo: str, autor: str, isbn: str) -> None:
    """
    Adiciona um novo livro ao sistema.
    
    Args:
        titulo: Título do livro
        autor: Nome do autor
        isbn: Código ISBN do livro
    """
    livro = {
        "id": len(livros) + 1,
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "disponivel": True
    }
    livros.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")


def adicionar_usuario(nome: str, cpf: str, email: str) -> None:
    """
    Cadastra um novo usuário no sistema.
    
    Args:
        nome: Nome completo do usuário
        cpf: CPF do usuário
        email: Email do usuário
    """
    usuario = {
        "id": len(usuarios) + 1,
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "ativo": True
    }
    usuarios.append(usuario)
    print(f"Usuário '{nome}' cadastrado com sucesso!")


def emprestar_livro(livro_id: int, usuario_id: int) -> None:
    """
    Realiza o empréstimo de um livro para um usuário.
    
    Args:
        livro_id: ID do livro a ser emprestado
        usuario_id: ID do usuário que está pegando o livro
    """
    livro = next((l for l in livros if l["id"] == livro_id), None)
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)

    if not livro:
        print("Livro não encontrado!")
        return

    if not usuario:
        print("Usuário não encontrado!")
        return

    if not livro["disponivel"]:
        print("Livro não está disponível!")
        return

    emprestimo = {
        "id": len(emprestimos) + 1,
        "livro_id": livro_id,
        "usuario_id": usuario_id,
        "data_emprestimo": datetime.now(),
        "data_devolucao": datetime.now() + timedelta(days=14),
        "devolvido": False
    }

    emprestimos.append(emprestimo)
    livro["disponivel"] = False

    print(f"Livro '{livro['titulo']}' emprestado para '{usuario['nome']}'")

# ... mais 500 linhas de código misturado ...