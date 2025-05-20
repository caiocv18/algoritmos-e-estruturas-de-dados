def classificar_desempenho():
    """
    Sistema de classificação de desempenho acadêmico.
    Calcula média, determina situação e fornece feedback personalizado.
    """
    print("\n===== SISTEMA DE CLASSIFICAÇÃO ACADÊMICA =====\n")

# Entrada e validação de dados
    try:
        nome = input("Nome do aluno: ").strip()
        if not nome:
            print("Erro: Nome não pode estar vazio.")
            return

# Coletando notas com validação
        notas = []
        for i in range(3):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i+1} (0-10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Erro: A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Erro: Digite um valor numérico válido.")

# Verificação de frequência
        while True:
            try:
                frequencia = int(input("Frequência do aluno (0-100%): "))
                if 0 <= frequencia <= 100:
                    break
                else:
                    print("Erro: A frequência deve estar entre 0 e 100%.")
            except ValueError:
                print("Erro: Digite um valor numérico válido.")

    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        return

# Processamento dos dados
    media = sum(notas) / len(notas)

# Determinação da situação
    if frequencia < 75:
        situacao = "Reprovado por Falta"
        feedback = "O aluno não atingiu a frequência mínima necessária de 75%."
    elif media < 3:
        situacao = "Reprovado"
        feedback = "Desempenho muito abaixo do esperado. Recomenda-se refazer a disciplina."
    elif media < 6:
        situacao = "Recuperação"
        nota_necessaria = 12 - media
        feedback = f"O aluno precisa de nota {nota_necessaria:.1f} na recuperação para ser aprovado."
    elif media < 8:
        situacao = "Aprovado"
        feedback = "Desempenho satisfatório."
    else:
        situacao = "Aprovado com Distinção"
        feedback = "Excelente desempenho!"

# Determinação do conceito
    if situacao == "Reprovado por Falta":
        conceito = "F"
    else:
# Usando operador ternário aninhado (apenas para demonstração)
        conceito = "A" if media >= 9 else "B" if media >= 8 else "C" if media >= 6 else "D" if media >= 3 else "E"

# Saída formatada
    print("\n" + "=" * 40)
    print(f"RELATÓRIO DE DESEMPENHO - {nome.upper()}")
    print("=" * 40)

    for i, nota in enumerate(notas):
        print(f"Nota {i+1}: {nota:.1f}")

    print(f"Média: {media:.1f}")
    print(f"Frequência: {frequencia}%")
    print(f"Situação: {situacao}")
    print(f"Conceito: {conceito}")
    print("-" * 40)
    print(f"Feedback: {feedback}")
    print("=" * 40)

# Recomendações condicionais
    if situacao == "Aprovado" or situacao == "Aprovado com Distinção":
        print("\nRECOMENDAÇÕES:")

        if conceito == "A":
            print("- Considere participar do programa de monitoria")
            print("- Veja as opções de iniciação científica disponíveis")

        if frequencia < 90:
            print("- Procure melhorar sua frequência nas próximas disciplinas")

        if min(notas) < media - 2:
            print("- Seu desempenho foi inconsistente. Busque manter regularidade.")

    elif situacao == "Recuperação":
        print("\nORIENTAÇÕES PARA RECUPERAÇÃO:")
        print("- Foque nos tópicos das avaliações com menor nota")
        print(f"- Você precisa de pelo menos {nota_necessaria:.1f} na recuperação")
        print("- Procure o professor para esclarecimento de dúvidas")

    return situacao, media

# Execução do programa
if __name__ == "__main__":
    classificar_desempenho()