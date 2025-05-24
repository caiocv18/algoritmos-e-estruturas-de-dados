def funcao_sem_return():
    """Esta função não tem return explícito."""
    x = 10
    y = 20
    z = x + y
# Implicitamente retorna None

resultado = funcao_sem_return()
print(f"Resultado: {resultado}")# None
print(f"Tipo: {type(resultado)}")# <class 'NoneType'># Usando None como valor significativo
def buscar_usuario(id_usuario):
    """
    Busca usuário por ID.

    Returns:
        dict ou None: Dados do usuário ou None se não encontrado
    """
# Simulando banco de dados
    usuarios = {
        1: {"nome": "Ana", "email": "ana@email.com"},
        2: {"nome": "Bruno", "email": "bruno@email.com"},
        3: {"nome": "Carlos", "email": "carlos@email.com"}
    }

    return usuarios.get(id_usuario)# Retorna None se ID não existir# Verificando None
usuario = buscar_usuario(5)
if usuario is None:
    print("Usuário não encontrado")
else:
    print(f"Usuário encontrado: {usuario['nome']}")

# Padrão comum: retorno antecipado
def dividir_com_seguranca(a, b):
    """Divide dois números com verificação de segurança."""
    if b == 0:
        print("Erro: Divisão por zero!")
        return None

    return a / b

# Testando
resultado = dividir_com_seguranca(10, 0)
if resultado is not None:
    print(f"Resultado: {resultado}")