# arquivo: tests/test_livro_repository.py
"""Testes para o repositório de livros."""

import unittest
from models.livro import Livro
from repositories.livro_repository import LivroRepository


class TestLivroRepository(unittest.TestCase):
    """Testa as operações do repositório de livros."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.repo = LivroRepository()
        self.livro_teste = Livro(
            titulo="1984",
            autor="George Orwell",
            isbn="978-0-452-28423-4"
        )

    def test_salvar_livro_novo(self):
        """Testa salvamento de um novo livro."""
        livro_salvo = self.repo.salvar(self.livro_teste)

        self.assertIsNotNone(livro_salvo.id)
        self.assertEqual(livro_salvo.id, 1)
        self.assertEqual(len(self.repo.listar_todos()), 1)

    def test_buscar_por_isbn(self):
        """Testa busca de livro por ISBN."""
        self.repo.salvar(self.livro_teste)

        livro_encontrado = self.repo.buscar_por_isbn("978-0-452-28423-4")
        self.assertIsNotNone(livro_encontrado)
        self.assertEqual(livro_encontrado.titulo, "1984")

        livro_nao_encontrado = self.repo.buscar_por_isbn("000-0-000-00000-0")
        self.assertIsNone(livro_nao_encontrado)

    def test_buscar_disponiveis(self):
        """Testa busca de livros disponíveis."""
        # Adicionar livros
        livro1 = Livro("Livro 1", "Autor 1", "111", disponivel=True)
        livro2 = Livro("Livro 2", "Autor 2", "222", disponivel=False)
        livro3 = Livro("Livro 3", "Autor 3", "333", disponivel=True)

        self.repo.salvar(livro1)
        self.repo.salvar(livro2)
        self.repo.salvar(livro3)

        disponiveis = self.repo.buscar_disponiveis()
        self.assertEqual(len(disponiveis), 2)
        self.assertTrue(all(l.disponivel for l in disponiveis))


if __name__ == "__main__":
    unittest.main()