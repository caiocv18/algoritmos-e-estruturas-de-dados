def is_elegivel(idade, nacionalidade, possui_restricoes):
    maior_idade = idade >= 18
    nacionalidade_elegivel = nacionalidade in ["brasileira", "portuguesa"]
    sem_restricoes = not possui_restricoes
    return maior_idade and nacionalidade_elegivel and sem_restricoes

if is_elegivel(idade, nacionalidade, possui_restricoes):
    print("Elegível para o cargo")