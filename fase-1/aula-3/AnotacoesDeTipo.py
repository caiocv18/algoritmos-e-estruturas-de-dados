# Anotações de tipo básicas
nome: str = "Maria"
idade: int = 30
altura: float = 1.75
ativo: bool = True

# Anotações para coleções
numeros: list[int] = [1, 2, 3, 4]
coordenadas: tuple[float, float] = (10.5, 20.3)
valores_opcionais: list[int | None] = [1, None, 3]# Union type (Python 3.10+)# Anotações em funções
def saudacao(nome: str, idade: int) -> str:
    return f"Olá {nome}, você tem {idade} anos"

# Tipos mais complexos
from typing import Dict, List, Tuple, Optional, Union, Any

# Para versões Python < 3.9
usuarios: Dict[str, int] = {"Ana": 25, "Bruno": 30}
matriz: List[List[int]] = [[1, 2], [3, 4]]
registro: Tuple[str, int, float] = ("Carlos", 42, 1.83)
valor: Optional[int] = None# int ou None
item: Union[int, str] = "texto"# int ou str (Python 3.10+: int | str)
algo: Any = [1, "texto", True]# Qualquer tipo