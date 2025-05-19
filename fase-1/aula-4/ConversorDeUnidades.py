#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Conversor de Unidades

Este programa permite converter valores entre diferentes unidades de medida,
incluindo comprimento, peso e temperatura.

Autor: Professor Caio Vinícius
Data: 25/04/2025
"""

# Definição de fatores de conversão (em relação à unidade base)
COMPRIMENTO = {
    "mm": 0.001,      # milímetro (em metros)
    "cm": 0.01,       # centímetro
    "m": 1.0,         # metro (unidade base)
    "km": 1000.0,     # quilômetro
    "in": 0.0254,     # polegada
    "ft": 0.3048,     # pé
    "yd": 0.9144,     # jarda
    "mi": 1609.344    # milha
}

PESO = {
    "mg": 0.000001,   # miligrama (em kg)
    "g": 0.001,       # grama
    "kg": 1.0,        # quilograma (unidade base)
    "ton": 1000.0,    # tonelada
    "oz": 0.028349523125,  # onça
    "lb": 0.45359237       # libra
}

# Para temperatura, usamos funções de conversão em vez de fatores simples
def celsius_para_kelvin(c):
    """Converte Celsius para Kelvin."""
    return c + 273.15

def kelvin_para_celsius(k):
    """Converte Kelvin para Celsius."""
    return k - 273.15

def celsius_para_fahrenheit(c):
    """Converte Celsius para Fahrenheit."""
    return c * 9/5 + 32

def fahrenheit_para_celsius(f):
    """Converte Fahrenheit para Celsius."""
    return (f - 32) * 5/9

# Funções para conversão
def converter_unidade(valor, unidade_origem, unidade_destino, conversoes):
    """
    Converte um valor entre duas unidades do mesmo tipo de medida.

    Args:
        valor: Valor a ser convertido
        unidade_origem: Unidade de origem
        unidade_destino: Unidade de destino
        conversoes: Dicionário com fatores de conversão

    Returns:
        Valor convertido para a unidade de destino
    """
    if unidade_origem not in conversoes or unidade_destino not in conversoes:
        raise ValueError("Unidade não reconhecida")

    # Converter para a unidade base
    valor_base = valor * conversoes[unidade_origem]

    # Converter da unidade base para a unidade de destino
    return valor_base / conversoes[unidade_destino]

def converter_temperatura(valor, unidade_origem, unidade_destino):
    """Converte temperatura entre diferentes unidades."""
    # Primeiro converter para Celsius (nossa unidade intermediária)
    if unidade_origem == "K":
        celsius = kelvin_para_celsius(valor)
    elif unidade_origem == "F":
        celsius = fahrenheit_para_celsius(valor)
    else:  # C
        celsius = valor

    # Depois converter de Celsius para a unidade de destino
    if unidade_destino == "K":
        return celsius_para_kelvin(celsius)
    elif unidade_destino == "F":
        return celsius_para_fahrenheit(celsius)
    else:  # C
        return celsius

def obter_opcao_menu(opcoes, prompt):
    """
    Apresenta um menu de opções e retorna a escolha do usuário.

    Args:
        opcoes: Lista de opções a serem exibidas
        prompt: Mensagem a ser exibida para o usuário

    Returns:
        Índice da opção escolhida
    """
    while True:
        print("\n" + prompt)
        for i, opcao in enumerate(opcoes, 1):
            print(f"{i}. {opcao}")

        try:
            escolha = int(input("\nEscolha uma opção (número): "))
            if 1 <= escolha <= len(opcoes):
                return escolha - 1
            print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Digite apenas números.")

def obter_valor_numerico(prompt):
    """Solicita e valida um valor numérico."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Valor inválido. Digite apenas números.")

def mostrar_categoria_comprimento():
    """Gerencia conversões de comprimento."""
    unidades = list(COMPRIMENTO.keys())
    unidades_formatadas = ["Milímetros (mm)", "Centímetros (cm)", "Metros (m)",
                          "Quilômetros (km)", "Polegadas (in)", "Pés (ft)",
                          "Jardas (yd)", "Milhas (mi)"]

    print("\n=== Conversão de Comprimento ===")
    idx_origem = obter_opcao_menu(unidades_formatadas, "Escolha a unidade de origem:")
    idx_destino = obter_opcao_menu(unidades_formatadas, "Escolha a unidade de destino:")

    unidade_origem = unidades[idx_origem]
    unidade_destino = unidades[idx_destino]

    valor = obter_valor_numerico(f"Digite o valor em {unidades_formatadas[idx_origem]}: ")
    resultado = converter_unidade(valor, unidade_origem, unidade_destino, COMPRIMENTO)

    print(f"\nResultado: {valor} {unidade_origem} = {resultado:.6g} {unidade_destino}")

def mostrar_categoria_peso():
    """Gerencia conversões de peso."""
    unidades = list(PESO.keys())
    unidades_formatadas = ["Miligramas (mg)", "Gramas (g)", "Quilogramas (kg)",
                          "Toneladas (ton)", "Onças (oz)", "Libras (lb)"]

    print("\n=== Conversão de Peso ===")
    idx_origem = obter_opcao_menu(unidades_formatadas, "Escolha a unidade de origem:")
    idx_destino = obter_opcao_menu(unidades_formatadas, "Escolha a unidade de destino:")

    unidade_origem = unidades[idx_origem]
    unidade_destino = unidades[idx_destino]

    valor = obter_valor_numerico(f"Digite o valor em {unidades_formatadas[idx_origem]}: ")
    resultado = converter_unidade(valor, unidade_origem, unidade_destino, PESO)

    print(f"\nResultado: {valor} {unidade_origem} = {resultado:.6g} {unidade_destino}")

def mostrar_categoria_temperatura():
    """Gerencia conversões de temperatura."""
    unidades = ["C", "F", "K"]
    unidades_formatadas = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]

    print("\n=== Conversão de Temperatura ===")
    idx_origem = obter_opcao_menu(unidades_formatadas, "Escolha a unidade de origem:")
    idx_destino = obter_opcao_menu(unidades_formatadas, "Escolha a unidade de destino:")

    unidade_origem = unidades[idx_origem]
    unidade_destino = unidades[idx_destino]

    valor = obter_valor_numerico(f"Digite o valor em {unidades_formatadas[idx_origem]}: ")
    resultado = converter_temperatura(valor, unidade_origem, unidade_destino)

    print(f"\nResultado: {valor} °{unidade_origem} = {resultado:.2f} °{unidade_destino}")

def main():
    """Função principal do programa."""
    categorias = ["Comprimento", "Peso", "Temperatura", "Sair"]

    print("=== CONVERSOR DE UNIDADES ===")
    print("Este programa permite converter entre diferentes unidades de medida.")

    while True:
        escolha = obter_opcao_menu(categorias, "Escolha uma categoria:")

        if escolha == 0:  # Comprimento
            mostrar_categoria_comprimento()
        elif escolha == 1:  # Peso
            mostrar_categoria_peso()
        elif escolha == 2:  # Temperatura
            mostrar_categoria_temperatura()
        else:  # Sair
            print("\nObrigado por utilizar o Conversor de Unidades!")
            break

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()