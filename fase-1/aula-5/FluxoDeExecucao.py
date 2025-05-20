print("Início do programa")

nota = float(input("Digite sua nota: "))

if nota >= 6.0:
    print("Aprovado")
    situacao = "aprovado"
else:
    print("Reprovado")
    situacao = "reprovado"

print(f"O aluno está {situacao}.")
print("Fim do programa")