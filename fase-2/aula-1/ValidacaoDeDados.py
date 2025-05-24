def validar_email(email):
    """Valida formato básico de email."""
    if "@" not in email:
        print("❌ Email inválido: falta @")
        return False

    partes = email.split("@")
    if len(partes) != 2:
        print("❌ Email inválido: múltiplos @")
        return False

    usuario, dominio = partes
    if not usuario or not dominio:
        print("❌ Email inválido: usuário ou domínio vazio")
        return False

    if "." not in dominio:
        print("❌ Email inválido: domínio sem ponto")
        return False

    print("✓ Email válido")
    return True

# Testando
validar_email("usuario@exemplo.com")
validar_email("invalido.com")
validar_email("@exemplo.com")