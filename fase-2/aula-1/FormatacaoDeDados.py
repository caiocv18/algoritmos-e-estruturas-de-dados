def formatar_telefone(telefone):
    """Formata número de telefone para exibição."""
# Remove caracteres não numéricos
    numeros = ''.join(filter(str.isdigit, telefone))

    if len(numeros) == 11:# Celular com DDD
        return f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
    elif len(numeros) == 10:# Fixo com DDD
        return f"({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}"
    else:
        return "Número inválido"

def formatar_moeda(valor):
    """Formata valor para moeda brasileira."""
    return f"R$ {valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")

# Exemplos
print(formatar_telefone("11987654321"))
print(formatar_telefone("1134567890"))
print(formatar_moeda(1234.56))
print(formatar_moeda(1000000.00))