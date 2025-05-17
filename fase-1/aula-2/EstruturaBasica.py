#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Descrição do programa: Este script demonstra a estrutura básica de um programa Python.
Autor: Seu Nome
Data: 01/04/2023
Versão: 1.0
"""

# Importações
import math
import datetime

# Constantes
PI = math.pi
GRAVIDADE = 9.81

# Funções
def calcular_area_circulo(raio):
    """Calcula a área de um círculo dado o raio."""
    return PI * raio ** 2

def saudacao(nome):
    """Retorna uma saudação personalizada."""
    hora_atual = datetime.datetime.now().hour
    
    if hora_atual < 12:
        periodo = "bom dia"
    elif hora_atual < 18:
        periodo = "boa tarde"
    else:
        periodo = "boa noite"
    
    return f"Olá, {nome}! Tenha um {periodo}!"

# Código principal
if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    print(saudacao(nome))
    
    raio = float(input("Digite o raio de um círculo: "))
    area = calcular_area_circulo(raio)
    print(f"A área do círculo com raio {raio} é {area:.2f} unidades quadradas.")