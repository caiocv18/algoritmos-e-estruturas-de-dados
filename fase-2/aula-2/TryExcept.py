def ler_arquivo_json(caminho_arquivo):
    """
    Lê um arquivo JSON com tratamento de erros completo.

    Returns:
        dict: Dados do arquivo ou None se houver erro
    """
    import json

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print(f"✅ Arquivo '{caminho_arquivo}' lido com sucesso")
            return dados

    except FileNotFoundError:
        print(f"❌ Arquivo '{caminho_arquivo}' não encontrado")
        return None

    except json.JSONDecodeError as e:
        print(f"❌ Erro ao decodificar JSON: {e}")
        return None

    except PermissionError:
        print(f"❌ Sem permissão para ler '{caminho_arquivo}'")
        return None

    except Exception as e:
        print(f"❌ Erro inesperado: {type(e).__name__}: {e}")
        return None

# Exemplo prático - Calculadora robusta
def calculadora_robusta():
    """Calculadora com tratamento completo de erros."""
    while True:
        try:
# Menu
            print("\n=== CALCULADORA ===")
            print("1. Somar")
            print("2. Subtrair")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "5":
                print("Encerrando...")
                break

# Validar opção
            if opcao not in ["1", "2", "3", "4"]:
                raise ValueError("Opção inválida")

# Obter números
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))

# Operações
            if opcao == "1":
                resultado = num1 + num2
                operacao = "+"
            elif opcao == "2":
                resultado = num1 - num2
                operacao = "-"
            elif opcao == "3":
                resultado = num1 * num2
                operacao = "*"
            elif opcao == "4":
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não permitida")
                resultado = num1 / num2
                operacao = "/"

            print(f"\nResultado: {num1} {operacao} {num2} = {resultado:.2f}")

        except ValueError as e:
            if "could not convert" in str(e):
                print("❌ Por favor, digite apenas números")
            else:
                print(f"❌ Erro: {e}")

        except ZeroDivisionError as e:
            print(f"❌ Erro matemático: {e}")

        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário")
            break

        except Exception as e:
            print(f"❌ Erro inesperado: {type(e).__name__}: {e}")

# Função com limpeza garantida (finally)
def processar_arquivo_com_backup(arquivo_origem):
    """
    Processa arquivo com backup e limpeza garantida.
    """
    import shutil
    import tempfile
    import os

    arquivo_backup = None

    try:
# Criar backup
        arquivo_backup = tempfile.mktemp(suffix='.bak')
        shutil.copy2(arquivo_origem, arquivo_backup)
        print(f"✅ Backup criado: {arquivo_backup}")

# Processar arquivo (simulação)
        with open(arquivo_origem, 'r') as f:
            conteudo = f.read()

# Simular processamento
        conteudo_processado = conteudo.upper()

# Salvar alterações
        with open(arquivo_origem, 'w') as f:
            f.write(conteudo_processado)

        print("✅ Arquivo processado com sucesso")

    except Exception as e:
        print(f"❌ Erro durante processamento: {e}")

# Restaurar backup se houver erro
        if arquivo_backup and os.path.exists(arquivo_backup):
            shutil.copy2(arquivo_backup, arquivo_origem)
            print("✅ Backup restaurado")

        raise# Re-lança a exceção

    finally:
# Limpeza sempre executada
        if arquivo_backup and os.path.exists(arquivo_backup):
            os.remove(arquivo_backup)
            print("🧹 Arquivo temporário removido")

# Para testar (cuidado - modifica arquivo!):# processar_arquivo_com_backup("teste.txt")