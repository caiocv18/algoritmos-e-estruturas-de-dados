def calcular_investimento(principal, taxa_anual, anos):
    """
    Calcula o montante final de um investimento com juros compostos.

    Args:
        principal: Valor inicial investido
        taxa_anual: Taxa de juros anual (em decimal, ex: 0.10 para 10%)
        anos: Período do investimento em anos
    """
    montante = principal * (1 + taxa_anual) ** anos
    lucro = montante - principal

    print(f"Investimento inicial: R$ {principal:,.2f}")
    print(f"Taxa anual: {taxa_anual * 100:.1f}%")
    print(f"Período: {anos} anos")
    print(f"Montante final: R$ {montante:,.2f}")
    print(f"Lucro: R$ {lucro:,.2f}")
    return montante

# Usando a função
valor_final = calcular_investimento(10000, 0.12, 5)
print(f"\nValor retornado: R$ {valor_final:,.2f}")