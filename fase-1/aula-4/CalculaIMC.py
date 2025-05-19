#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Descrição do programa: Este script calcula o IMC (Índice de Massa Corporal)
e fornece a classificação de acordo com a tabela da OMS.

Autor: Professor Caio Vinícius
Data: 25/04/2025
Versão: 1.0
"""

# Importações
import math

# Constantes
CLASSIFICACAO_IMC = {
    "Abaixo do peso": 18.5,
    "Peso normal": 25.0,
    "Sobrepeso": 30.0,
    "Obesidade grau I": 35.0,
    "Obesidade grau II": 40.0
}

# Funções
def calcular_imc(peso, altura):
    """Calcula o IMC baseado no peso (kg) e altura (m)."""
    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero")
    return peso / (altura ** 2)

def obter_classificacao(imc):
    """Retorna a classificação do IMC de acordo com a tabela da OMS."""
    for categoria, limite in sorted(CLASSIFICACAO_IMC.items()):
        if imc < limite:
            return categoria
    return "Obesidade grau III"

# Entrada de dados
def obter_dados_usuario():
    """Solicita e valida dados do usuário."""
    while True:
        try:
            peso = float(input("Digite seu peso em kg: "))
            if peso <= 0:
                print("O peso deve ser maior que zero.")
                continue

            altura = float(input("Digite sua altura em metros: "))
            if altura <= 0:
                print("A altura deve ser maior que zero.")
                continue

            return peso, altura
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

# Programa principal
def main():
    print("Calculadora de IMC - Índice de Massa Corporal\n")

    # Obter dados
    peso, altura = obter_dados_usuario()

    # Processar
    imc = calcular_imc(peso, altura)
    classificacao = obter_classificacao(imc)

    # Saída
    print("\nResultados:")
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

    # Informações adicionais
    if classificacao != "Peso normal":
        print("\nObservação: Consulte um profissional de saúde para uma avaliação completa.")

# Execução do programa
if __name__ == "__main__":
    main()
