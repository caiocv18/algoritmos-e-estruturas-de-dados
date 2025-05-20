def processar_arquivo():
    """Demonstra tratamento de erros robusto ao processar um arquivo."""
    
    while True:
        nome_arquivo = input("Digite o nome do arquivo CSV a processar: ")
        
        # Validação básica do nome do arquivo
        if not nome_arquivo:
            print("Erro: Nome do arquivo não pode estar vazio.")
            continue
        
        # Verificação da extensão
        if not nome_arquivo.lower().endswith('.csv'):
            resposta = input("O arquivo não tem extensão .csv. Deseja continuar mesmo assim? (s/n): ")
            if resposta.lower() != 's':
                continue
        
        try:
            # Tentativa de abrir o arquivo
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                
                # Verificação se o arquivo está vazio
                if not linhas:
                    print("Aviso: O arquivo está vazio.")
                    return None
                
                # Verificação do cabeçalho
                cabecalho = linhas[0].strip().split(',')
                colunas_esperadas = ["nome", "idade", "cidade"]
                
                # Validação das colunas necessárias
                colunas_faltantes = [col for col in colunas_esperadas if col not in cabecalho]
                if colunas_faltantes:
                    print(f"Erro: Colunas necessárias não encontradas: {', '.join(colunas_faltantes)}")
                    continuar = input("Deseja tentar outro arquivo? (s/n): ")
                    if continuar.lower() == 's':
                        continue
                    else:
                        return None
                
                # Processamento das linhas de dados
                dados = []
                for i, linha in enumerate(linhas[1:], 2):  # Começa do índice 2 para exibir número da linha correta
                    try:
                        valores = linha.strip().split(',')
                        
                        # Verificação do número de colunas
                        if len(valores) != len(cabecalho):
                            print(f"Aviso: Linha {i} possui {len(valores)} valores, mas eram esperados {len(cabecalho)}.")
                            continue
                        
                        # Mapeamento dos valores
                        registro = dict(zip(cabecalho, valores))
                        
                        # Validação dos tipos de dados
                        try:
                            if "idade" in registro:
                                registro["idade"] = int(registro["idade"])
                        except ValueError:
                            print(f"Aviso: Linha {i} - Valor inválido para idade: '{registro['idade']}'. Usando 0.")
                            registro["idade"] = 0
                        
                        dados.append(registro)
                        
                    except Exception as e:
                        print(f"Erro ao processar linha {i}: {e}")
                
                print(f"\nProcessamento concluído. {len(dados)} registros válidos encontrados.")
                return dados
                
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
            continuar = input("Deseja tentar outro arquivo? (s/n): ")
            if continuar.lower() != 's':
                return None
                
        except PermissionError:
            print(f"Erro: Sem permissão para acessar o arquivo '{nome_arquivo}'.")
            continuar = input("Deseja tentar outro arquivo? (s/n): ")
            if continuar.lower() != 's':
                return None
                
        except Exception as e:
            print(f"Erro inesperado: {e}")
            continuar = input("Deseja tentar outro arquivo? (s/n): ")
            if continuar.lower() != 's':
                return None