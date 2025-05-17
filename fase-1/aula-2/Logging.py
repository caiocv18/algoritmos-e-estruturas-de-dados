import logging

# Configuração básica
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def dividir(a, b):
    logging.debug(f"Tentando dividir {a} por {b}")
    if b == 0:
        logging.error("Tentativa de divisão por zero")
        return None
    
    return a / b

dividir(10, 0)