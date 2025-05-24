def configurar_aplicacao(modo="producao", *middlewares, **configs):
    """
    Configura uma aplicação com middlewares e configurações flexíveis.

    Args:
        modo: Modo de execução (producao, desenvolvimento, teste)
        *middlewares: Middlewares a serem carregados
        **configs: Configurações específicas da aplicação
    """
    print(f"=== CONFIGURANDO APLICAÇÃO EM MODO {modo.upper()} ===\n")

# Configurações padrão por modo
    configs_padrao = {
        "producao": {"debug": False, "cache": True, "logs": "arquivo"},
        "desenvolvimento": {"debug": True, "cache": False, "logs": "console"},
        "teste": {"debug": True, "cache": False, "logs": "memoria"}
    }

# Mescla configurações padrão com as fornecidas
    config_final = configs_padrao.get(modo, {})
    config_final.update(configs)

    print("Configurações finais:")
    for chave, valor in config_final.items():
        print(f"  {chave}: {valor}")

# Carregando middlewares
    if middlewares:
        print(f"\nMiddlewares ativos ({len(middlewares)}):")
        for middleware in middlewares:
            print(f"  ✓ {middleware}")
    else:
        print("\nNenhum middleware configurado")

    return config_final

# Exemplos de uso
configurar_aplicacao()# Usa padrões

configurar_aplicacao(
    "desenvolvimento",
    "autenticacao", "cors", "rate_limit",
    porta=5000,
    database="postgresql://localhost/dev",
    secret_key="dev-secret-123"
)

configurar_aplicacao(
    "producao",
    "autenticacao", "cors", "compressao", "cache",
    porta=80,
    database="postgresql://prod-server/app",
    workers=4,
    ssl=True
)