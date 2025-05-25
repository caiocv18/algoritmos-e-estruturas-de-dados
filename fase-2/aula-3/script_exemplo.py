# arquivo: script_exemplo.py (destinado a ser executado diretamente)
import sys

def processar_argumentos():
    """Processa argumentos da linha de comando."""
    if len(sys.argv) < 2:
        print("Uso: python script_exemplo.py <argumento>")
        return

    print(f"Processando: {sys.argv[1]}")

# Este código só executa quando o arquivo é rodado diretamente
if __name__ == "__main__":
    processar_argumentos()