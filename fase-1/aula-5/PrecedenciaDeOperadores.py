# Sem parênteses - avalia primeiro "idade > 18 and possui_documento"
if idade > 18 and possui_documento or acompanhado_responsavel:
    print("Pode entrar")

# Com parênteses - mudando a ordem de avaliação
if idade > 18 and (possui_documento or acompanhado_responsavel):
    print("Pode entrar")