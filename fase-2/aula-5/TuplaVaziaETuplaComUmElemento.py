# Tupla vazia
tupla_vazia1 = ()
tupla_vazia2 = tuple()
print(f"Tupla vazia: {tupla_vazia1}, Tipo: {type(tupla_vazia1)}")

# Tupla com um elemento - A VÍRGULA É ESSENCIAL!
# Sem a vírgula, Python interpreta como um valor entre parênteses
nao_e_tupla = (42)  # Isso é um int
e_tupla = (42,)  # Isso é uma tupla
tambem_e_tupla = 42,  # Isso também é uma tupla

print(f"Não é tupla: {nao_e_tupla}, Tipo: {type(nao_e_tupla)}")
print(f"É tupla: {e_tupla}, Tipo: {type(e_tupla)}")

# Verificando se é tupla
def criar_tupla_segura(elemento):
    """Cria uma tupla com um único elemento de forma segura"""
    if isinstance(elemento, tuple):
        return elemento
    return (elemento,)

print(criar_tupla_segura(5))  # (5,)
print(criar_tupla_segura((5, 6)))  # (5, 6)
