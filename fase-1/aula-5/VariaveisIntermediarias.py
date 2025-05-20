# Difícil de ler
if idade >= 18 and (nacionalidade == "brasileira" or nacionalidade == "portuguesa") and not possui_restricoes:
    print("Elegível para o cargo")

# Mais claro
maior_idade = idade >= 18
nacionalidade_elegivel = nacionalidade == "brasileira" or nacionalidade == "portuguesa"
sem_restricoes = not possui_restricoes

if maior_idade and nacionalidade_elegivel and sem_restricoes:
    print("Elegível para o cargo")