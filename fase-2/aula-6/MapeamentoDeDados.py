# Tradução de códigos
status_pedido = {
    "P": "Pendente",
    "A": "Aprovado",
    "E": "Enviado",
    "C": "Cancelado"
}

# Usando o mapeamento
codigo = "E"
print(f"Status: {status_pedido.get(codigo, 'Desconhecido')}")
