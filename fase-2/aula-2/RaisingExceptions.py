class SaldoInsuficienteError(Exception):
    """Exceção customizada para saldo insuficiente."""
    pass

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def sacar(self, valor):
        """
        Realiza saque da conta.

        Raises:
            ValueError: Se o valor for inválido
            SaldoInsuficienteError: Se não houver saldo suficiente
        """
        if valor <= 0:
            raise ValueError("Valor de saque deve ser positivo")

        if valor > self._saldo:
            raise SaldoInsuficienteError(
                f"Saldo insuficiente. Disponível: R$ {self._saldo:.2f}"
            )

        self._saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso")
        return self._saldo

    def depositar(self, valor):
        """Realiza depósito na conta."""
        if valor <= 0:
            raise ValueError("Valor de depósito deve ser positivo")

        self._saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso")
        return self._saldo

    @property
    def saldo(self):
        return self._saldo

# Usando a classe
conta = ContaBancaria("João Silva", 1000)

try:
    conta.sacar(500)
    print(f"Saldo atual: R$ {conta.saldo:.2f}")

    conta.sacar(600)# Vai gerar erro
except SaldoInsuficienteError as e:
    print(f"⚠️  {e}")
except ValueError as e:
    print(f"❌ Erro: {e}")

# Função com múltiplas validações
def conectar_api(url, timeout=30, tentativas=3):
    """
    Conecta a uma API com validações e retry.

    Raises:
        ValueError: Para parâmetros inválidos
        ConnectionError: Para falhas de conexão
    """
    import time

# Validações
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL deve começar com http:// ou https://")

    if timeout <= 0:
        raise ValueError("Timeout deve ser positivo")

    if tentativas < 1:
        raise ValueError("Deve haver pelo menos 1 tentativa")

# Simula tentativas de conexão
    for tentativa in range(1, tentativas + 1):
        print(f"Tentativa {tentativa}/{tentativas}: Conectando a {url}...")

# Simula possível falha (50% de chance)
        import random
        if random.random() > 0.5:
            print("✅ Conexão estabelecida!")
            return True

        if tentativa < tentativas:
            print("❌ Falha na conexão. Tentando novamente...")
            time.sleep(1)

# Se todas as tentativas falharam
    raise ConnectionError(f"Não foi possível conectar a {url} após {tentativas} tentativas")

# Testando
try:
    conectar_api("https://api.exemplo.com", timeout=10, tentativas=3)
except (ValueError, ConnectionError) as e:
    print(f"Erro: {e}")