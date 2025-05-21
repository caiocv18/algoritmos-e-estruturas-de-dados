# Processando uma lista de alunos
alunos = [
    {"nome": "Ana", "notas": [8.5, 9.0, 7.5], "faltas": 2},
    {"nome": "Bruno", "notas": [7.0, 8.5, 9.5], "faltas": 0},
    {"nome": "Carla", "notas": [9.0, 9.5, 10.0], "faltas": 1},
    {"nome": "Diego", "notas": [6.5, 7.0, 8.0], "faltas": 5}
]

# Calculando médias e situação
for aluno in alunos:
    média = sum(aluno["notas"]) / len(aluno["notas"])
    aluno["média"] = média
    
    if aluno["faltas"] > 4:
        situação = "Reprovado por faltas"
    elif média >= 7.0:
        situação = "Aprovado"
    elif média >= 5.0:
        situação = "Recuperação"
    else:
        situação = "Reprovado"
    
    aluno["situação"] = situação
    
    print(f"Nome: {aluno['nome']}")
    print(f"Média: {média:.1f}")
    print(f"Faltas: {aluno['faltas']}")
    print(f"Situação: {situação}")
    print("-" * 30)