def criar_pessoa(**kwargs):
    """
    Cria um perfil de pessoa com atributos variáveis.
    **kwargs coleta argumentos nomeados em um dicionário.
    """
    print("Criando perfil com os seguintes dados:")
    print(f"Tipo de kwargs: {type(kwargs)}")

    for chave, valor in kwargs.items():
        print(f"  {chave}: {valor}")

# Acessando valores específicos com segurança
    nome = kwargs.get('nome', 'Não informado')
    idade = kwargs.get('idade', 'Não informada')

    print(f"\nResumo: {nome}, {idade} anos")
    return kwargs

# Exemplos de uso
pessoa1 = criar_pessoa(nome="Maria", idade=30, cidade="SP", profissao="Médica")
pessoa2 = criar_pessoa(nome="João", email="joao@email.com", telefone="11999999999")