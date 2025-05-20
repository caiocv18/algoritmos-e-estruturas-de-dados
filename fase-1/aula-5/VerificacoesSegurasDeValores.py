# Verificação de None
def processa_dados(dados):
    if dados is None:# Use 'is None', não '== None'
        print("Dados não fornecidos")
        return

# Agora é seguro processar os dados
    print(f"Processando {len(dados)} itens")

# Verificação de tipo
def calcular_area(largura, altura):
    if not isinstance(largura, (int, float)) or not isinstance(altura, (int, float)):
        print("Dimensões devem ser numéricas")
        return None

    if largura <= 0 or altura <= 0:
        print("Dimensões devem ser positivas")
        return None

    return largura * altura

# Verificação de atributos (útil para objetos)
def imprimir_nome(objeto):
    if hasattr(objeto, 'nome'):
        print(f"Nome: {objeto.nome}")
    else:
        print("Objeto não possui um atributo 'nome'")