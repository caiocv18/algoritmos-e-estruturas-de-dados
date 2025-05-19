#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculadora de Empréstimos

Este programa calcula pagamentos de empréstimos, incluindo amortização,
juros totais e gera uma tabela de amortização completa.

Autor: Professor Caio Vinícius
Data: 25/04/2025
"""

import math

def calcular_pagamento_mensal(principal, taxa_anual, anos):
    """
    Calcula o pagamento mensal de um empréstimo.

    Args:
        principal: Valor do empréstimo
        taxa_anual: Taxa de juros anual (em percentual)
        anos: Prazo do empréstimo em anos

    Returns:
        Valor do pagamento mensal
    """
    # Converter taxa anual para mensal (decimal)
    taxa_mensal = taxa_anual / 100 / 12

    # Número total de pagamentos
    num_pagamentos = anos * 12

    # Cálculo do pagamento mensal
    if taxa_mensal == 0:
        # Caso especial: taxa zero
        return principal / num_pagamentos

    # Fórmula: P = principal * (r * (1+r)^n) / ((1+r)^n - 1)
    fator = (1 + taxa_mensal) ** num_pagamentos
    pagamento = principal * (taxa_mensal * fator) / (fator - 1)

    return pagamento

def gerar_tabela_amortizacao(principal, taxa_anual, anos):
    """
    Gera uma tabela de amortização completa.

    Args:
        principal: Valor do empréstimo
        taxa_anual: Taxa de juros anual (em percentual)
        anos: Prazo do empréstimo em anos

    Returns:
        Lista de dicionários com informações de cada pagamento
    """
    taxa_mensal = taxa_anual / 100 / 12
    num_pagamentos = anos * 12
    pagamento_mensal = calcular_pagamento_mensal(principal, taxa_anual, anos)

    tabela = []
    saldo_restante = principal

    for mes in range(1, num_pagamentos + 1):
        juros = saldo_restante * taxa_mensal
        amortizacao = pagamento_mensal - juros
        saldo_restante -= amortizacao

        # Correção para evitar saldo negativo no último pagamento
        if mes == num_pagamentos:
            amortizacao += saldo_restante
            saldo_restante = 0

        tabela.append({
            "mes": mes,
            "pagamento": pagamento_mensal,
            "juros": juros,
            "amortizacao": amortizacao,
            "saldo_restante": saldo_restante
        })

    return tabela

def formatar_moeda(valor, simbolo="R$"):
    """Formata um valor como moeda."""
    return f"{simbolo} {valor:,.2f}"

def mostrar_resumo_emprestimo(principal, taxa_anual, anos):
    """Exibe um resumo do empréstimo."""
    pagamento_mensal = calcular_pagamento_mensal(principal, taxa_anual, anos)
    num_pagamentos = anos * 12
    total_pago = pagamento_mensal * num_pagamentos
    total_juros = total_pago - principal

    print("\n=== RESUMO DO EMPRÉSTIMO ===")
    print(f"Valor do empréstimo: {formatar_moeda(principal)}")
    print(f"Taxa de juros anual: {taxa_anual:.2f}%")
    print(f"Prazo: {anos} anos ({num_pagamentos} meses)")
    print(f"Pagamento mensal: {formatar_moeda(pagamento_mensal)}")
    print(f"Total pago: {formatar_moeda(total_pago)}")
    print(f"Total em juros: {formatar_moeda(total_juros)}")

def mostrar_tabela_amortizacao(tabela, mostrar_todos=False):
    """
    Mostra a tabela de amortização formatada.

    Args:
        tabela: Lista de dicionários com informações de cada pagamento
        mostrar_todos: Se True, mostra todos os meses, caso contrário
                      mostra apenas os 3 primeiros, 3 últimos e a cada ano
    """
    print("\n=== TABELA DE AMORTIZAÇÃO ===")
    print(f"{'Mês':^5}|{'Pagamento':^15}|{'Juros':^15}|{'Amortização':^15}|{'Saldo Restante':^18}")
    print("-" * 72)

    for i, linha in enumerate(tabela):
        # Se não mostrar todos, exibe apenas os 3 primeiros e 3 últimos meses,
        # e um mês a cada 12 (para mostrar a evolução anual)
        if (mostrar_todos or
            i < 3 or
            i >= len(tabela) - 3 or
            linha["mes"] % 12 == 0):

            print(f"{linha['mes']:5d}|"
                  f"{formatar_moeda(linha['pagamento']):^15}|"
                  f"{formatar_moeda(linha['juros']):^15}|"
                  f"{formatar_moeda(linha['amortizacao']):^15}|"
                  f"{formatar_moeda(linha['saldo_restante']):^18}")

            if i == 2 and not mostrar_todos and len(tabela) > 6:
                print(f"{'...':^5}|{'...':^15}|{'...':^15}|{'...':^15}|{'...':^18}")

def obter_dados_emprestimo():
    """Solicita e valida os dados do empréstimo junto ao usuário."""
    while True:
        try:
            principal = float(input("Digite o valor do empréstimo: "))
            if principal <= 0:
                print("O valor do empréstimo deve ser positivo.")
                continue

            taxa_anual = float(input("Digite a taxa de juros anual (%): "))
            if taxa_anual < 0:
                print("A taxa de juros não pode ser negativa.")
                continue

            anos = int(input("Digite o prazo em anos: "))
            if anos <= 0:
                print("O prazo deve ser positivo.")
                continue

            return principal, taxa_anual, anos

        except ValueError:
            print("Entrada inválida. Digite apenas números.")

def simular_cenarios(principal, taxa_anual, anos):
    """Simula diferentes cenários de empréstimo."""
    print("\n=== SIMULAÇÃO DE CENÁRIOS ===")

    # Cenário 1: Aumentar o prazo em 5 anos
    novo_prazo = anos + 5
    pagamento_original = calcular_pagamento_mensal(principal, taxa_anual, anos)
    pagamento_prazo_maior = calcular_pagamento_mensal(principal, taxa_anual, novo_prazo)
    diferenca_mensal = pagamento_original - pagamento_prazo_maior

    print(f"\nCenário 1: Aumentar prazo para {novo_prazo} anos")
    print(f"Pagamento mensal atual: {formatar_moeda(pagamento_original)}")
    print(f"Pagamento com prazo maior: {formatar_moeda(pagamento_prazo_maior)}")
    print(f"Economia mensal: {formatar_moeda(diferenca_mensal)}")
    print(f"Custo total adicional: {formatar_moeda(pagamento_prazo_maior * novo_prazo * 12 - pagamento_original * anos * 12)}")

    # Cenário 2: Reduzir a taxa de juros em 1%
    nova_taxa = max(0, taxa_anual - 1)
    pagamento_taxa_menor = calcular_pagamento_mensal(principal, nova_taxa, anos)
    diferenca_mensal = pagamento_original - pagamento_taxa_menor

    print(f"\nCenário 2: Reduzir taxa para {nova_taxa:.2f}%")
    print(f"Pagamento mensal atual: {formatar_moeda(pagamento_original)}")
    print(f"Pagamento com taxa menor: {formatar_moeda(pagamento_taxa_menor)}")
    print(f"Economia mensal: {formatar_moeda(diferenca_mensal)}")
    print(f"Economia total: {formatar_moeda(pagamento_original * anos * 12 - pagamento_taxa_menor * anos * 12)}")

def main():
    """Função principal do programa."""
    print("=== CALCULADORA DE EMPRÉSTIMOS ===")
    print("Este programa calcula detalhes sobre empréstimos e financiamentos.")

    # Obter dados do empréstimo
    principal, taxa_anual, anos = obter_dados_emprestimo()

    # Mostrar resumo
    mostrar_resumo_emprestimo(principal, taxa_anual, anos)

    # Gerar tabela de amortização
    tabela = gerar_tabela_amortizacao(principal, taxa_anual, anos)

    # Perguntar se usuário quer ver tabela completa
    ver_completa = input("\nDeseja ver a tabela de amortização completa? (s/n): ").lower() == 's'
    mostrar_tabela_amortizacao(tabela, mostrar_todos=ver_completa)

    # Simular cenários
    simular = input("\nDeseja simular cenários diferentes? (s/n): ").lower() == 's'
    if simular:
        simular_cenarios(principal, taxa_anual, anos)

    print("\nObrigado por utilizar a Calculadora de Empréstimos!")

if __name__ == "__main__":
    main()