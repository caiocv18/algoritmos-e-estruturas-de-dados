# Explorando alguns módulos da biblioteca padrão
import os# Operações do sistema operacional
import datetime# Manipulação de datas e horas
import json# Trabalho com JSON
import random# Geração de números aleatórios
import re# Expressões regulares# Exemplo prático usando múltiplos módulos
def exemplo_biblioteca_padrao():
# os - informações do sistema
    print(f"Sistema Operacional: {os.name}")
    print(f"Diretório atual: {os.getcwd()}")

# datetime - trabalhando com datas
    agora = datetime.datetime.now()
    print(f"Data e hora atual: {agora.strftime('%d/%m/%Y %H:%M')}")

# json - serialização de dados
    dados = {"nome": "Python", "versao": 3.9, "modulos": ["os", "json"]}
    json_string = json.dumps(dados, indent=2)
    print(f"JSON:\n{json_string}")

# random - números aleatórios
    numeros = [random.randint(1, 100) for _ in range(5)]
    print(f"Números aleatórios: {numeros}")

# re - expressões regulares
    texto = "Contato: email@example.com ou telefone: (11) 98765-4321"
    emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', texto)
    print(f"Emails encontrados: {emails}")