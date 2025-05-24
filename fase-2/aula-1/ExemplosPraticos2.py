def calcular_media(nota1, nota2, nota3):
    """Calcula a média de três notas."""
    return (nota1 + nota2 + nota3) / 3

def determinar_situacao(media):
    """Determina a situação do aluno baseada na média."""
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def processar_aluno(nome, nota1, nota2, nota3):
    """Processa as notas de um aluno e exibe o resultado."""
    print(f"=== {nome} ===")
    media = calcular_media(nota1, nota2, nota3)
    situacao = determinar_situacao(media)
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print()

# Agora é muito mais simples processar qualquer quantidade de alunos
processar_aluno("Aluno 1", 7.5, 8.0, 6.5)
processar_aluno("Aluno 2", 9.0, 8.5, 9.5)
processar_aluno("Aluno 3", 5.0, 6.0, 4.5)
processar_aluno("Maria Silva", 10.0, 9.5, 9.8)