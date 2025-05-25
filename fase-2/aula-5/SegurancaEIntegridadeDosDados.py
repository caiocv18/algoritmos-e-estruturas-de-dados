# Exemplo de problema com mutabilidade
def processar_lista_perigoso(lista):
    """Esta função modifica a lista original!"""
    lista.append(999)
    return sum(lista)

minha_lista = [1, 2, 3]
resultado = processar_lista_perigoso(minha_lista)
print(f"Lista após processamento: {minha_lista}")  # [1, 2, 3, 999] - Modificada!

# Com tuplas, isso não é possível
def processar_tupla_seguro(tupla):
    """Esta função não pode modificar a tupla original"""
    # tupla.append(999)  # Isso geraria erro
    return sum(tupla)

minha_tupla = (1, 2, 3)
resultado = processar_tupla_seguro(minha_tupla)
print(f"Tupla após processamento: {minha_tupla}")  # (1, 2, 3) - Inalterada!

# Garantindo integridade em estruturas de dados
class Ponto2D:
    def __init__(self, x, y):
        # Usando tupla para garantir imutabilidade
        self._coordenadas = (x, y)

    @property
    def coordenadas(self):
        return self._coordenadas

    @property
    def x(self):
        return self._coordenadas[0]

    @property
    def y(self):
        return self._coordenadas[1]

    def __repr__(self):
        return f"Ponto2D{self._coordenadas}"

# Uso
p = Ponto2D(10, 20)
print(p)  # Ponto2D(10, 20)
# p.coordenadas[0] = 30  # Erro! Não pode modificar
