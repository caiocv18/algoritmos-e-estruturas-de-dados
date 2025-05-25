import math

# Sistema de coordenadas 2D
class SistemaCoordenadas2D:
    def __init__(self):
        self.pontos = {}

    def adicionar_ponto(self, nome, coordenadas):
        """Adiciona um ponto nomeado ao sistema"""
        if not isinstance(coordenadas, tuple) or len(coordenadas) != 2:
            raise ValueError("Coordenadas devem ser tupla (x, y)")
        self.pontos[nome] = coordenadas

    def distancia(self, ponto1, ponto2):
        """Calcula distância euclidiana entre dois pontos"""
        x1, y1 = self.pontos[ponto1]
        x2, y2 = self.pontos[ponto2]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def ponto_medio(self, ponto1, ponto2):
        """Calcula o ponto médio entre dois pontos"""
        x1, y1 = self.pontos[ponto1]
        x2, y2 = self.pontos[ponto2]
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    def area_triangulo(self, p1, p2, p3):
        """Calcula área de triângulo usando coordenadas"""
        x1, y1 = self.pontos[p1]
        x2, y2 = self.pontos[p2]
        x3, y3 = self.pontos[p3]
        
        # Fórmula da área usando determinante
        area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
        return area

# Exemplo de uso
sistema = SistemaCoordenadas2D()
sistema.adicionar_ponto("A", (0, 0))
sistema.adicionar_ponto("B", (3, 4))
sistema.adicionar_ponto("C", (6, 0))

print(f"Distância A-B: {sistema.distancia('A', 'B'):.2f}")
print(f"Ponto médio A-C: {sistema.ponto_medio('A', 'C')}")
print(f"Área do triângulo ABC: {sistema.area_triangulo('A', 'B', 'C'):.2f}")

# Trabalhando com coordenadas 3D
def vetor_3d(p1, p2):
    """Calcula vetor entre dois pontos 3D"""
    return tuple(b - a for a, b in zip(p1, p2))

def produto_escalar_3d(v1, v2):
    """Calcula produto escalar de dois vetores 3D"""
    return sum(a * b for a, b in zip(v1, v2))

def magnitude_3d(vetor):
    """Calcula magnitude de vetor 3D"""
    return math.sqrt(sum(x**2 for x in vetor))

# Exemplo 3D
p1_3d = (1, 2, 3)
p2_3d = (4, 6, 8)
vetor = vetor_3d(p1_3d, p2_3d)
print(f"\nVetor de {p1_3d} para {p2_3d}: {vetor}")
print(f"Magnitude: {magnitude_3d(vetor):.2f}")
