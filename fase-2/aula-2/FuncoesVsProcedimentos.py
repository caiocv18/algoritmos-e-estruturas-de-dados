# Procedimento (não retorna valor útil, apenas executa ações)
def exibir_mensagem_boas_vindas(nome):
    """Procedimento que apenas exibe mensagem."""
    print(f"{'=' * 40}")
    print(f"Bem-vindo(a), {nome}!")
    print(f"{'=' * 40}")
# Implicitamente retorna None# Função (retorna valor útil)
def formatar_mensagem_boas_vindas(nome):
    """Função que retorna mensagem formatada."""
    linha = "=" * 40
    mensagem = f"{linha}\nBem-vindo(a), {nome}!\n{linha}"
    return mensagem

# Comparando uso
resultado1 = exibir_mensagem_boas_vindas("Ana")
print(f"Procedimento retornou: {resultado1}")# None

resultado2 = formatar_mensagem_boas_vindas("Ana")
print(f"Função retornou:\n{resultado2}")

# Exemplo prático - Logging
def registrar_erro(mensagem):
    """Procedimento: registra erro mas não retorna nada útil."""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[ERRO] {timestamp}: {mensagem}")

def validar_email(email):
    """Função: valida email e retorna resultado."""
    import re
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(padrao, email))

# Uso combinado
email = "usuario@exemplo.com"
if not validar_email(email):# Função retorna valor útil
    registrar_erro(f"Email inválido: {email}")# Procedimento apenas executa