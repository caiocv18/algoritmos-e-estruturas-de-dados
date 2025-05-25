# arquivo: usando_imports.py

# Importação básica
import string_utils

texto = "  Olá   Mundo  Python  "
texto_limpo = string_utils.limpar_espacos(texto)
print(f"Texto limpo: '{texto_limpo}'")

# Importação com alias
import string_utils as su

palavras = su.contar_palavras("Python é uma linguagem incrível")
print(f"Número de palavras: {palavras}")

# Importação específica
from string_utils import eh_palindromo, extrair_numeros

print(f"'arara' é palíndromo? {eh_palindromo('arara')}")
print(f"'Python' é palíndromo? {eh_palindromo('Python')}")

numeros = extrair_numeros("Tenho 25 anos e R$ 1500.50 no banco")
print(f"Números encontrados: {numeros}")

# Importação múltipla
from string_utils import (
    truncar,
    censurar_palavras,
    VOGAIS,
    CONSOANTES
)

texto_longo = "Este é um texto muito longo que precisa ser truncado"
print(truncar(texto_longo, 20))

# Importação de tudo (evitar em produção)
from string_utils import *

texto_censurado = censurar_palavras(
    "Python e Java são linguagens populares",
    ["Java", "populares"]
)
print(f"Texto censurado: {texto_censurado}")