# Retorno múltiplo básico
def dividir_com_resto(dividendo, divisor):
    """Retorna quociente e resto da divisão"""
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto  # Implicitamente retorna uma tupla

q, r = dividir_com_resto(17, 5)
print(f"17 ÷ 5 = {q} resto {r}")

# Retornando status e resultado
def buscar_usuario(user_id):
    """Retorna (sucesso, dados) ou (falha, mensagem_erro)"""
    usuarios = {1: "Ana", 2: "Bruno", 3: "Carlos"}
    
    if user_id in usuarios:
        return True, usuarios[user_id]
    else:
        return False, f"Usuário {user_id} não encontrado"

# Uso com desempacotamento
sucesso, resultado = buscar_usuario(2)
if sucesso:
    print(f"Usuário encontrado: {resultado}")
else:
    print(f"Erro: {resultado}")

# Retornando estatísticas complexas
def analisar_vendas(vendas):
    """Análise completa de vendas"""
    if not vendas:
        return None
    
    total = sum(vendas)
    media = total / len(vendas)
    minima = min(vendas)
    maxima = max(vendas)
    amplitude = maxima - minima
    
    # Retorna tupla nomeada para melhor legibilidade
    from collections import namedtuple
    Estatisticas = namedtuple('Estatisticas',
                             'total media minima maxima amplitude')
    
    return Estatisticas(total, media, minima, maxima, amplitude)

vendas_mes = [1200, 1500, 800, 2000, 1800, 900, 1600]
stats = analisar_vendas(vendas_mes)
print(f"Análise de vendas:")
print(f"  Total: R$ {stats.total:,.2f}")
print(f"  Média: R$ {stats.media:,.2f}")
print(f"  Amplitude: R$ {stats.amplitude:,.2f}")
