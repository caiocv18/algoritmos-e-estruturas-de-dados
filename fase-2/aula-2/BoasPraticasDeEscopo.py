# 1. EVITE usar global quando possível
# RUIM
total = 0

def adicionar_ruim(valor):
    global total
    total += valor

# BOM - Use retorno de valores
def adicionar_bom(total_atual, valor):
    return total_atual + valor

total = adicionar_bom(0, 10)
total = adicionar_bom(total, 20)

# 2. Use constantes em maiúsculas para valores globais
# Configurações globais (constantes)
TAXA_CONVERSAO = 5.25
LIMITE_TENTATIVAS = 3
URL_API = "https://api.exemplo.com"

def converter_moeda(valor_reais):
    """Usa constante global de forma apropriada."""
    return valor_reais / TAXA_CONVERSAO

# 3. Encapsule estado em classes ou closures
def criar_contador():
    """Cria um contador encapsulado."""
    contador = {"valor": 0}

    def incrementar(quantidade=1):
        contador["valor"] += quantidade
        return contador["valor"]

    def decrementar(quantidade=1):
        contador["valor"] -= quantidade
        return contador["valor"]

    def resetar():
        contador["valor"] = 0
        return contador["valor"]

    def obter_valor():
        return contador["valor"]

    # Retorna interface pública
    return {
        "incrementar": incrementar,
        "decrementar": decrementar,
        "resetar": resetar,
        "valor": obter_valor
    }

# Usando contador encapsulado
contador1 = criar_contador()
contador2 = criar_contador()  # Independente!

print(contador1["incrementar"]())  # 1
print(contador1["incrementar"](5))  # 6
print(contador2["incrementar"]())  # 1 (independente)
print(contador1["valor"]())  # 6

# 4. Use injeção de dependências
def processar_dados(dados, funcao_validacao, funcao_formatacao):
    """
    Processa dados usando funções injetadas.
    Evita dependências globais.
    """
    dados_validos = []

    for item in dados:
        if funcao_validacao(item):
            item_formatado = funcao_formatacao(item)
            dados_validos.append(item_formatado)

    return dados_validos

# Funções específicas
def validar_positivo(num):
    return num > 0

def formatar_moeda(num):
    return f"R$ {num:.2f}"

# Uso
numeros = [10, -5, 20, 0, 30, -10]
resultado = processar_dados(numeros, validar_positivo, formatar_moeda)
print(f"Valores processados: {resultado}")