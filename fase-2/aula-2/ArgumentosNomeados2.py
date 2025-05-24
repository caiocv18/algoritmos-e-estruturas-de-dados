from datetime import datetime

def registrar_log(mensagem, nivel="INFO", timestamp=None, usuario=None, detalhes=None):
    """
    Registra uma mensagem de log com informações contextuais.

    Args:
        mensagem: Mensagem principal do log
        nivel: Nível do log (INFO, WARNING, ERROR, DEBUG)
        timestamp: Data/hora do evento (usa atual se None)
        usuario: Usuário relacionado ao evento
        detalhes: Dicionário com detalhes adicionais
    """
# Define timestamp se não fornecido
    if timestamp is None:
        timestamp = datetime.now()

# Formata a saída
    niveis_cores = {
        "INFO": "\033[94m",# Azul
        "WARNING": "\033[93m",# Amarelo
        "ERROR": "\033[91m",# Vermelho
        "DEBUG": "\033[92m"# Verde
    }

    cor = niveis_cores.get(nivel, "\033[0m")
    reset = "\033[0m"

    print(f"{cor}[{nivel}]{reset} {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Mensagem: {mensagem}")

    if usuario:
        print(f"Usuário: {usuario}")

    if detalhes:
        print("Detalhes:")
        for chave, valor in detalhes.items():
            print(f"  - {chave}: {valor}")

    print("-" * 50)

# Usando argumentos nomeados para clareza
registrar_log("Sistema iniciado com sucesso")

registrar_log(
    mensagem="Falha na autenticação",
    nivel="ERROR",
    usuario="joao.silva",
    detalhes={"ip": "192.168.1.50", "tentativas": 3}
)

registrar_log(
    nivel="WARNING",
    mensagem="Uso de CPU acima de 80%",
    detalhes={"cpu_percent": 85.2, "memory_percent": 62.1}
)