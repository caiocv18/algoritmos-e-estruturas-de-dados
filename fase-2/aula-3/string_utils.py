# arquivo: string_utils.py
"""
Módulo de utilitários para manipulação de strings.

Este módulo fornece funções para processar, validar e
transformar strings de várias formas.
"""

import re
from typing import List, Optional

def limpar_espacos(texto: str) -> str:
    """Remove espaços extras e espaços nas extremidades."""
    return ' '.join(texto.split())

def contar_palavras(texto: str) -> int:
    """Conta o número de palavras em um texto."""
    palavras = texto.split()
    return len(palavras)

def eh_palindromo(texto: str) -> bool:
    """Verifica se um texto é um palíndromo (ignora espaços e case)."""
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto.lower())
    return texto_limpo == texto_limpo[::-1]

def extrair_numeros(texto: str) -> List[float]:
    """Extrai todos os números de um texto."""
    padrao = r'-?\d+\.?\d*'
    numeros_str = re.findall(padrao, texto)
    return [float(num) for num in numeros_str]

def censurar_palavras(texto: str, palavras_proibidas: List[str]) -> str:
    """Substitui palavras proibidas por asteriscos."""
    for palavra in palavras_proibidas:
        padrao = re.compile(re.escape(palavra), re.IGNORECASE)
        censura = '*' * len(palavra)
        texto = padrao.sub(censura, texto)
    return texto

def truncar(texto: str, max_chars: int, sufixo: str = "...") -> str:
    """Trunca um texto para um número máximo de caracteres."""
    if len(texto) <= max_chars:
        return texto
    return texto[:max_chars - len(sufixo)] + sufixo

# Constantes do módulo
VOGAIS = "aeiouAEIOU"
CONSOANTES = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"