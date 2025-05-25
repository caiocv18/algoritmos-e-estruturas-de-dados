# arquivo: explorando_paths.py
import sys
import os


def mostrar_caminhos_python():
    """Mostra onde Python procura por módulos."""
    print("Caminhos de busca do Python (sys.path):")
    for i, path in enumerate(sys.path, 1):
        print(f"{i}. {path}")


def adicionar_caminho_customizado(novo_caminho):
    """Adiciona um novo caminho para busca de módulos."""
    if os.path.exists(novo_caminho) and novo_caminho not in sys.path:
        sys.path.append(novo_caminho)
        print(f"Caminho '{novo_caminho}' adicionado com sucesso!")
    else:
        print(f"Caminho '{novo_caminho}' não existe ou já está na lista.")


# Importação relativa e absoluta
# Em um projeto estruturado:
# projeto/
#   ├── main.py
#   ├── utils/
#   │   ├── __init__.py
#   │   ├── math_utils.py
#   │   └── string_utils.py
#   └── models/
#       ├── __init__.py
#       └── user.py
#
# No arquivo main.py:
# from utils.math_utils import calcular_media
# from models.user import Usuario
#
# Dentro de utils/math_utils.py (importação relativa):
# from .string_utils import limpar_espacos