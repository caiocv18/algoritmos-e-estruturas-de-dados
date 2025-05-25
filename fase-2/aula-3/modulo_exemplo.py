# arquivo: modulo_exemplo.py (destinado a ser importado)
def saudar(nome):
    """Função para saudar um usuário."""
    return f"Olá, {nome}!"

def calcular_idade(ano_nascimento, ano_atual=2024):
    """Calcula a idade baseada no ano de nascimento."""
    return ano_atual - ano_nascimento

# Teste do módulo (só executa se rodado diretamente)
if __name__ == "__main__":
    print("Testando o módulo...")
    print(saudar("Python"))
    print(f"Idade: {calcular_idade(2000)}")