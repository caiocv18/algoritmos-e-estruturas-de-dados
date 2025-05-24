def configurar_servidor(host, porta=8000, debug=False, workers=4, timeout=30):
    """
    Configura um servidor web com parâmetros específicos.
    """
    print("Configuração do Servidor:")
    print(f"  Host: {host}")
    print(f"  Porta: {porta}")
    print(f"  Modo Debug: {'Ativado' if debug else 'Desativado'}")
    print(f"  Workers: {workers}")
    print(f"  Timeout: {timeout}s")

# Argumentos nomeados tornam a chamada mais clara
configurar_servidor(host="localhost", debug=True)
configurar_servidor(host="0.0.0.0", porta=5000, workers=8)
configurar_servidor(host="api.exemplo.com", timeout=60, debug=True, porta=443)

# Misturando posicionais e nomeados (posicionais devem vir primeiro)
configurar_servidor("192.168.1.100", debug=True, workers=2)