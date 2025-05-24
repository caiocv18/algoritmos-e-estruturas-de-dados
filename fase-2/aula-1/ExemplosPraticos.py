# Sistema de notas - código repetitivo
print("=== Aluno 1 ===")
nota1_aluno1 = 7.5
nota2_aluno1 = 8.0
nota3_aluno1 = 6.5
media_aluno1 = (nota1_aluno1 + nota2_aluno1 + nota3_aluno1) / 3
if media_aluno1 >= 7:
    situacao_aluno1 = "Aprovado"
elif media_aluno1 >= 5:
    situacao_aluno1 = "Recuperação"
else:
    situacao_aluno1 = "Reprovado"
print(f"Média: {media_aluno1:.2f}")
print(f"Situação: {situacao_aluno1}")

print("\n=== Aluno 2 ===")
nota1_aluno2 = 9.0
nota2_aluno2 = 8.5
nota3_aluno2 = 9.5
media_aluno2 = (nota1_aluno2 + nota2_aluno2 + nota3_aluno2) / 3
if media_aluno2 >= 7:
    situacao_aluno2 = "Aprovado"
elif media_aluno2 >= 5:
    situacao_aluno2 = "Recuperação"
else:
    situacao_aluno2 = "Reprovado"
print(f"Média: {media_aluno2:.2f}")
print(f"Situação: {situacao_aluno2}")

# ... repetido para cada aluno