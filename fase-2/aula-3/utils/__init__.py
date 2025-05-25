# arquivo: utils/__init__.py
"""
Pacote de utilitários do projeto.

Este pacote contém funções auxiliares para:
- Validação de dados
- Formatação de strings
- Operações matemáticas
"""

# Importações convenientes
from .validacao import validar_email, validar_cpf
from .formatacao import formatar_moeda, formatar_data
from .matematica import calcular_media, calcular_desvio_padrao

# Define o que é exportado com "from utils import *"
__all__ = [
    'validar_email',
    'validar_cpf',
    'formatar_moeda',
    'formatar_data',
    'calcular_media',
    'calcular_desvio_padrao'
]

# Metadados do pacote
__version__ = '1.0.0'
__author__ = 'Seu Nome'