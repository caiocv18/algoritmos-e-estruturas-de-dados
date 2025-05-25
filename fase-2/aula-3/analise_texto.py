# arquivo: analise_texto.py
"""
Módulo de Análise de Texto
==========================

Este módulo fornece ferramentas para análise estatística e processamento
de textos em português.

Principais funcionalidades:
- Análise de frequência de palavras
- Cálculo de métricas de legibilidade
- Extração de palavras-chave
- Análise de sentimentos básica

Exemplo de uso:
    >>> from analise_texto import AnalisadorTexto
    >>> analisador = AnalisadorTexto()
    >>> resultado = analisador.analisar("Python é uma linguagem incrível!")
    >>> print(resultado.num_palavras)
    5

Autor: Seu Nome
Versão: 1.0.0
"""

from collections import Counter
from dataclasses import dataclass
from typing import List, Dict, Set
import re


@dataclass
class ResultadoAnalise:
    """
    Resultado da análise de um texto.

    Attributes:
        num_palavras: Número total de palavras
        num_caracteres: Número total de caracteres
        num_frases: Número estimado de frases
        palavras_unicas: Conjunto de palavras únicas
        frequencia_palavras: Dicionário com frequência de cada palavra
        complexidade: Índice de complexidade do texto (0-100)
    """
    num_palavras: int
    num_caracteres: int
    num_frases: int
    palavras_unicas: Set[str]
    frequencia_palavras: Dict[str, int]
    complexidade: float


class AnalisadorTexto:
    """
    Classe principal para análise de textos.

    Esta classe fornece métodos para analisar diversos aspectos
    de um texto, incluindo estatísticas básicas e métricas de
    complexidade.
    """

    def __init__(self, idioma: str = "pt"):
        """
        Inicializa o analisador.

        Args:
            idioma: Código do idioma (padrão: "pt" para português)
        """
        self.idioma = idioma
        self._palavras_comuns = self._carregar_palavras_comuns()

    def analisar(self, texto: str) -> ResultadoAnalise:
        """
        Realiza análise completa de um texto.

        Args:
            texto: O texto a ser analisado

        Returns:
            ResultadoAnalise contendo todas as métricas

        Raises:
            ValueError: Se o texto estiver vazio

        Example:
            >>> analisador = AnalisadorTexto()
            >>> resultado = analisador.analisar("Olá mundo!")
            >>> print(f"Palavras: {resultado.num_palavras}")
            Palavras: 2
        """
        if not texto:
            raise ValueError("Texto não pode estar vazio")

        palavras = self._extrair_palavras(texto)
        frases = self._contar_frases(texto)

        return ResultadoAnalise(
            num_palavras=len(palavras),
            num_caracteres=len(texto),
            num_frases=frases,
            palavras_unicas=set(palavras),
            frequencia_palavras=Counter(palavras),
            complexidade=self._calcular_complexidade(texto, palavras)
        )

    def _extrair_palavras(self, texto: str) -> List[str]:
        """Extrai palavras do texto (método interno)."""
        palavras = re.findall(r'\b\w+\b', texto.lower())
        return palavras

    def _contar_frases(self, texto: str) -> int:
        """Estima o número de frases no texto."""
        # Simplificado: conta pontos finais, exclamações e interrogações
        return len(re.findall(r'[.!?]+', texto))

    def _calcular_complexidade(self, texto: str, palavras: List[str]) -> float:
        """
        Calcula índice de complexidade do texto.

        Baseado em:
        - Comprimento médio das palavras
        - Variedade de vocabulário
        - Comprimento das frases
        """
        if not palavras:
            return 0.0

        # Comprimento médio das palavras
        comp_medio = sum(len(p) for p in palavras) / len(palavras)

        # Variedade de vocabulário
        variedade = len(set(palavras)) / len(palavras)

        # Complexidade estimada (0-100)
        complexidade = min(100, (comp_medio * 10) + (variedade * 50))

        return round(complexidade, 2)

    def _carregar_palavras_comuns(self) -> Set[str]:
        """Carrega lista de palavras comuns do idioma."""
        # Simulação - em produção, carregar de arquivo
        return {"o", "a", "de", "e", "do", "da", "em", "um", "uma", "os", "as"}