def obter_dados_compra():
    """Função responsável apenas pela entrada de dados."""
    valor = float(input("Valor da compra: R$ "))
    categoria = input("Categoria do produto (A/B/C): ").upper()
    tipo_cliente = input("Tipo de cliente (comum/premium): ").lower()
    return valor, categoria, tipo_cliente

def validar_dados(valor, categoria, tipo_cliente):
    """Função responsável apenas pela validação."""
    if valor <= 0:
        return False, "Valor da compra deve ser positivo."
    if categoria not in ["A", "B", "C"]:
        return False, "Categoria inválida. Use A, B ou C."
    if tipo_cliente not in ["comum", "premium"]:
        return False, "Tipo de cliente inválido. Use comum ou premium."
    return True, "Dados válidos."

# Cada função resolve uma subtarefa específica, tornando o código mais modular