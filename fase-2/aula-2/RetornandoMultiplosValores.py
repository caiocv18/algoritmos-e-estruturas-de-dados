def analisar_texto(texto):
    """
    Analisa um texto e retorna várias estatísticas.

    Returns:
        tuple: (num_palavras, num_caracteres, num_linhas, palavras_unicas)
    """
# Análises
    num_caracteres = len(texto)
    num_linhas = texto.count('\n') + 1 if texto else 0
    palavras = texto.lower().split()
    num_palavras = len(palavras)
    palavras_unicas = len(set(palavras))

    return num_palavras, num_caracteres, num_linhas, palavras_unicas

# Desempacotamento de múltiplos valores
texto = """Python é uma linguagem incrível.
Python é usado em muitas áreas.
Aprender Python é muito útil."""

palavras, caracteres, linhas, unicas = analisar_texto(texto)
print(f"Palavras: {palavras}")
print(f"Caracteres: {caracteres}")
print(f"Linhas: {linhas}")
print(f"Palavras únicas: {unicas}")

# Também podemos capturar como tupla
resultado = analisar_texto(texto)
print(f"\nResultado completo: {resultado}")