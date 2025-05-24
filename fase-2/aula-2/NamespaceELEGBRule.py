# Demonstrando LEGB
nome = "Global"# Global

def funcao_externa():
    nome = "Enclosing"# Enclosing para funcao_interna

    def funcao_interna():
        nome = "Local"# Local
        print(f"Dentro de funcao_interna: {nome}")

# Acessando built-in
        print(f"Função len é: {len}")# Built-in

    funcao_interna()
    print(f"Dentro de funcao_externa: {nome}")

funcao_externa()
print(f"No escopo global: {nome}")

# Exemplo prático - Configurador aninhado
def criar_configurador(ambiente):
    """Cria um configurador para ambiente específico."""
# Enclosing scope
    configuracoes_base = {
        "desenvolvimento": {"debug": True, "cache": False},
        "producao": {"debug": False, "cache": True}
    }

    def configurar(chave, valor=None):
        """Função interna que acessa escopo envolvente."""
# Acessa variável do escopo envolvente
        config = configuracoes_base.get(ambiente, {})

        if valor is None:
# Modo leitura
            return config.get(chave, "Configuração não encontrada")
        else:
# Modo escrita
            config[chave] = valor
            return f"Configurado: {chave} = {valor}"

    return configurar

# Usando closures
config_dev = criar_configurador("desenvolvimento")
config_prod = criar_configurador("producao")

print(config_dev("debug"))# True
print(config_prod("debug"))# False
print(config_dev("cache"))# False
print(config_prod("cache"))# True