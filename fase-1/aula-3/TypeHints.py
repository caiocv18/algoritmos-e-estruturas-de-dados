# Sem type hints
def processa_dados(dados, filtro, valor_padrao):
    resultado = []
    for item in dados:
        if filtro(item):
            resultado.append(item)
    return resultado if resultado else valor_padrao

# Com type hints
from typing import TypeVar, Callable, List, Optional

T = TypeVar('T')# Define um tipo genérico

def processa_dados(
    dados: List[T],
    filtro: Callable[[T], bool],
    valor_padrao: Optional[List[T]] = None
) -> List[T]:
    """
    Filtra uma lista de acordo com o critério fornecido.

    Args:
        dados: Lista de elementos a serem filtrados
        filtro: Função que verifica se um elemento deve ser incluído
        valor_padrao: Valor a retornar se nenhum elemento passar no filtro

    Returns:
        Lista filtrada ou valor padrão se a lista filtrada estiver vazia
    """
    resultado = [item for item in dados if filtro(item)]
    return resultado if resultado else (valor_padrao or [])