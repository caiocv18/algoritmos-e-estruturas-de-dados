# arquivo: convencoes_exemplo.py
"""Demonstração das convenções de nomenclatura em Python (PEP 8)."""

# Módulos e pacotes: snake_case minúsculo
# Bom: math_utils.py, data_processing.py
# Ruim: MathUtils.py, dataProcessing.py

# Classes: PascalCase (CamelCase com primeira letra maiúscula)
class MinhaClasseExemplo:
    """Exemplo de nomenclatura de classe."""
    pass


class ProcessadorDeDados:
    """Outro exemplo seguindo a convenção."""
    pass


# Funções e variáveis: snake_case minúsculo
def calcular_media_ponderada(valores, pesos):
    """Exemplo de nomenclatura de função."""
    numero_total = len(valores)
    soma_ponderada = sum(v * p for v, p in zip(valores, pesos))
    return soma_ponderada / sum(pesos)


# Constantes: SNAKE_CASE maiúsculo
TAXA_MAXIMA = 0.15
NUMERO_MAXIMO_TENTATIVAS = 3
CAMINHO_PADRAO = "/home/usuario/dados"


# Métodos privados: começam com underscore
class ExemploPrivado:
    def __init__(self):
        self._atributo_interno = 42  # Atributo "privado"

    def _metodo_interno(self):
        """Método destinado ao uso interno da classe."""
        return self._atributo_interno * 2

    def metodo_publico(self):
        """Método público que usa o método interno."""
        return self._metodo_interno() + 10


# Métodos especiais (dunder methods): dois underscores
class MinhaLista:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        """Permite usar len() com objetos desta classe."""
        return len(self.items)

    def __str__(self):
        """Representação em string do objeto."""
        return f"MinhaLista({self.items})"