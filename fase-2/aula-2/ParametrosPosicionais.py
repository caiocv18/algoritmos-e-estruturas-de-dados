def criar_perfil_usuario(nome, idade, cidade):
    """
    Cria um perfil de usuário com informações básicas.

    Args:
        nome: Nome completo do usuário
        idade: Idade em anos
        cidade: Cidade de residência
    """
    print(f"=== PERFIL DO USUÁRIO ===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Cidade: {cidade}")
    print("=" * 25)

# Chamando com argumentos posicionais (ordem importa!)
criar_perfil_usuario("Ana Silva", 28, "São Paulo")
criar_perfil_usuario("Carlos Santos", 35, "Rio de Janeiro")

# ERRO comum: argumentos na ordem errada
# criar_perfil_usuario(25, "João", "Brasília")  # Idade e nome trocados!