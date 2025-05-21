import os

# Criando múltiplos arquivos
for i in range(1, 6):
    nome_arquivo = f"arquivo_{i}.txt"
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(f"Este é o conteúdo do arquivo {i}\n")
        arquivo.write(f"Linha adicional para o arquivo {i}")
    print(f"Arquivo {nome_arquivo} criado com sucesso")

# Processando múltiplos arquivos
arquivos_txt = [f for f in os.listdir('.') if f.endswith('.txt')]
conteúdo_total = ""

for nome_arquivo in arquivos_txt:
    print(f"Processando {nome_arquivo}...")
    with open(nome_arquivo, "r") as arquivo:
        conteúdo = arquivo.read()
        conteúdo_total += conteúdo + "\n\n"

# Salvando conteúdo consolidado
with open("todos_arquivos.txt", "w") as arquivo_final:
    arquivo_final.write(conteúdo_total)