def processar_pedido(*itens, **informacoes):
    """
    Processa um pedido com múltiplos itens e informações adicionais.

    Args:
        *itens: Itens do pedido (quantidade variável)
        **informacoes: Informações adicionais (cliente, endereço, etc)
    """
    print("=== PROCESSANDO PEDIDO ===")

# Processando itens
    print(f"\nItens do pedido ({len(itens)}):")
    total = 0
    for i, item in enumerate(itens, 1):
        print(f"  {i}. {item}")
# Simulando preço
        preco = len(item) * 10# Preço fictício baseado no nome
        total += preco

    print(f"\nTotal dos itens: R$ {total:.2f}")

# Processando informações
    print("\nInformações do pedido:")
    for chave, valor in informacoes.items():
        print(f"  {chave.replace('_', ' ').title()}: {valor}")

# Aplicando desconto se for cliente VIP
    if informacoes.get('cliente_vip', False):
        desconto = total * 0.1
        total -= desconto
        print(f"\nDesconto VIP aplicado: -R$ {desconto:.2f}")
        print(f"Total final: R$ {total:.2f}")

    return total

# Usando a função
processar_pedido(
    "Notebook", "Mouse", "Teclado",
    cliente="Ana Silva",
    endereco="Rua das Flores, 123",
    cliente_vip=True,
    observacoes="Entregar após 14h"
)