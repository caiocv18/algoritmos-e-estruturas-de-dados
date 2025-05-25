# Módulo simples: calculadora.py
"""Um módulo simples de calculadora."""

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

# Pacote: calculadora_avancada/
# calculadora_avancada/
#   ├── __init__.py
#   ├── basico.py
#   ├── cientifico.py
#   └── financeiro.py

# arquivo: calculadora_avancada/__init__.py
"""Pacote de calculadora avançada com múltiplas funcionalidades."""

from .basico import somar, subtrair, multiplicar, dividir
from .cientifico import seno, cosseno, logaritmo
from .financeiro import juros_simples, juros_compostos

__version__ = '2.0.0'

# arquivo: calculadora_avancada/basico.py
"""Operações matemáticas básicas."""

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna o produto de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de dois números."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

# arquivo: calculadora_avancada/cientifico.py
"""Operações matemáticas científicas."""

import math

def seno(angulo_graus):
    """Calcula o seno de um ângulo em graus."""
    radianos = math.radians(angulo_graus)
    return math.sin(radianos)

def cosseno(angulo_graus):
    """Calcula o cosseno de um ângulo em graus."""
    radianos = math.radians(angulo_graus)
    return math.cos(radianos)

def logaritmo(x, base=10):
    """Calcula o logaritmo de x na base especificada."""
    if base == 10:
        return math.log10(x)
    elif base == math.e:
        return math.log(x)
    else:
        return math.log(x, base)