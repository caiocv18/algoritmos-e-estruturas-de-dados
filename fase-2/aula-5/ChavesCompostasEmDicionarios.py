# Sistema de cache com chaves compostas
class CacheMatriz:
    """Cache para operações de matriz usando tuplas como chaves"""
    def __init__(self):
        self.cache = {}

    def multiplicar_matrizes(self, matriz_a, matriz_b):
        """Multiplica matrizes com cache"""
        # Converte matrizes para tuplas (hashable)
        chave = (tuple(map(tuple, matriz_a)), tuple(map(tuple, matriz_b)))

        if chave in self.cache:
            print("Resultado obtido do cache!")
            return self.cache[chave]

        # Calcula multiplicação
        resultado = self._multiplicar(matriz_a, matriz_b)

        # Armazena no cache
        self.cache[chave] = resultado
        return resultado

    def _multiplicar(self, a, b):
        """Multiplicação real de matrizes"""
        print("Calculando multiplicação...")
        linhas_a, colunas_a = len(a), len(a[0])
        linhas_b, colunas_b = len(b), len(b[0])

        if colunas_a != linhas_b:
            raise ValueError("Dimensões incompatíveis")

        resultado = [[0] * colunas_b for _ in range(linhas_a)]

        for i in range(linhas_a):
            for j in range(colunas_b):
                for k in range(colunas_a):
                    resultado[i][j] += a[i][k] * b[k][j]

        return resultado

# Exemplo de uso
cache = CacheMatriz()

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Primeira chamada - calcula
resultado1 = cache.multiplicar_matrizes(A, B)
print(f"Resultado: {resultado1}")

# Segunda chamada - usa cache
resultado2 = cache.multiplicar_matrizes(A, B)
print(f"Resultado (cache): {resultado2}")

# Mapeamento geográfico com coordenadas
mapa_locais = {
    # (latitude, longitude): informações do local
    (-23.5505, -46.6333): {
        "cidade": "São Paulo",
        "tipo": "Metrópole",
        "população": 12325232
    },
    (-22.9068, -43.1729): {
        "cidade": "Rio de Janeiro",
        "tipo": "Metrópole",
        "população": 6747815
    },
    (-15.7942, -47.8822): {
        "cidade": "Brasília",
        "tipo": "Capital Federal",
        "população": 3055149
    }
}

# Busca por proximidade
def encontrar_cidade_proxima(lat, lon, mapa, tolerancia=0.1):
    """Encontra cidade próxima às coordenadas"""
    for (lat_cidade, lon_cidade), info in mapa.items():
        if abs(lat - lat_cidade) < tolerancia and abs(lon - lon_cidade) < tolerancia:
            return info
    return None

# Teste
coord_busca = (-23.55, -46.63)
cidade = encontrar_cidade_proxima(*coord_busca, mapa_locais)
if cidade:
    print(f"\nCidade encontrada: {cidade['cidade']}")
