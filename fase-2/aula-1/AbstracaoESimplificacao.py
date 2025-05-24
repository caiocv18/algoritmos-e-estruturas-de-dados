def enviar_email_boas_vindas(usuario):
    """Envia email de boas-vindas para novo usuário."""
# Complexidade escondida dentro da função
    validar_email(usuario.email)
    gerar_token_confirmacao(usuario)
    criar_mensagem_personalizada(usuario)
    enviar_via_servidor_smtp(usuario.email, mensagem)
    registrar_log_envio(usuario)

# Uso simples
novo_usuario = criar_usuario("João", "joao@email.com")
enviar_email_boas_vindas(novo_usuario)# Simples de usar!