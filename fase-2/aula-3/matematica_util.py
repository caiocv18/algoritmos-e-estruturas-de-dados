# arquivo: matematica_util.py
"""
Módulo com funções matemáticas utilitárias.
Este módulo fornece operações matemáticas avançadas.
"""

import math

def area_circulo(raio):
    """Calcula a área de um círculo dado seu raio."""
    return math.pi * raio ** 2

def volume_esfera(raio):
    """Calcula o volume de uma esfera dado seu raio."""
    return (4/3) * math.pi * raio ** 3

def fatorial(n):
    """Calcula o fatorial de um número usando recursão."""
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

# Variável do módulo
PI_APROXIMADO = 3.14159