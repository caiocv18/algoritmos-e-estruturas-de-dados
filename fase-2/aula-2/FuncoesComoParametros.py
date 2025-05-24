def executar_operacao(func, a, b):
    """
    Executa uma operação usando a função fornecida.

    Args:
        func: Função que realiza a operação
        a, b: Operandos
    """
    resultado = func(a, b)
    print(f"Executando {func.__name__}({a}, {b}) = {resultado}")
    return resultado

# Definindo operações
def somar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

def potencia(x, y):
    return x ** y

# Passando funções como argumentos
executar_operacao(somar, 10, 5)
executar_operacao(multiplicar, 10, 5)
executar_operacao(potencia, 2, 8)

# Exemplo prático - Sistema de validação flexível
def validar_dados(dados, *validadores):
    """
    Valida dados usando múltiplas funções validadoras.

    Args:
        dados: Dados a serem validados
        *validadores: Funções de validação
    """
    erros = []

    for validador in validadores:
        resultado = validador(dados)
        if resultado is not True:
            erros.append(resultado)

    if erros:
        print("❌ Validação falhou:")
        for erro in erros:
            print(f"  - {erro}")
        return False

    print("✅ Dados válidos!")
    return True

# Validadores específicos
def validar_comprimento_minimo(dados):
    if len(str(dados)) < 3:
        return "Comprimento mínimo de 3 caracteres"
    return True

def validar_apenas_letras(dados):
    if not str(dados).replace(" ", "").isalpha():
        return "Deve conter apenas letras"
    return True

def validar_sem_espacos(dados):
    if " " in str(dados):
        return "Não pode conter espaços"
    return True

# Testando
validar_dados("João Silva", validar_comprimento_minimo, validar_apenas_letras)
validar_dados("A1", validar_comprimento_minimo, validar_apenas_letras)
validar_dados("usuario", validar_comprimento_minimo, validar_sem_espacos)