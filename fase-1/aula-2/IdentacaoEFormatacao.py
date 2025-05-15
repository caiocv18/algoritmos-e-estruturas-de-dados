def saudacao(nome):
    # Este bloco pertence à função saudacao
    mensagem = f"Olá, {nome}!"
    print(mensagem)

    if len(nome) > 5:
        # Este bloco pertence ao if
        print("Seu nome é relativamente longo.")
    else:
        # Este bloco pertence ao else
        print("Seu nome é relativamente curto.")

# Este código não está mais indentado, então não pertence à função
print("Fim do programa.")