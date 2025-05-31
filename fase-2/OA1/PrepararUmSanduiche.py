def verificar_ingredientes_sanduiche(ingredientes_disponiveis, ingredientes_necessarios):
    """Verifica se todos os ingredientes necessários estão disponíveis."""
    # Lógica aqui...
    return True # ou False, ou lista de faltantes

def montar_sanduiche(tipo_pao, recheio_principal, adicionais):
    """Simula a montagem do sanduíche."""
    # Lógica aqui...
    return f"Sanduíche de {recheio_principal} em pão {tipo_pao} com {', '.join(adicionais)} pronto!"

# Script principal
meus_ingredientes = ["pão forma", "queijo", "presunto", "alface"]
preciso_para_misto = ["pão forma", "queijo", "presunto"]

if verificar_ingredientes_sanduiche(meus_ingredientes, preciso_para_misto):
    print(montar_sanduiche("forma", "queijo e presunto", ["alface"]))
else:
    print("Faltam ingredientes para o misto!")