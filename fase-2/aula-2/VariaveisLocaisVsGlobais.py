# Variável global
contador_global = 0
mensagem = "Olá do escopo global!"

def demonstrar_escopo():
    """Demonstra diferença entre escopo local e global."""
# Variável local
    contador_local = 10
    mensagem = "Olá do escopo local!"# Sombrea a global

    print(f"Dentro da função:")
    print(f"  contador_local = {contador_local}")
    print(f"  mensagem = {mensagem}")
    print(f"  contador_global = {contador_global}")# Lê a global# Chamando a função
demonstrar_escopo()

print(f"\nFora da função:")
print(f"  mensagem = {mensagem}")# Global não foi alterada
print(f"  contador_global = {contador_global}")
# print(f"  contador_local = {contador_local}")  # Erro! Não existe aqui# Exemplo prático - Sistema de configuração
configuracao = {
    "debug": False,
    "porta": 8080,
    "host": "localhost"
}

def ativar_modo_debug():
    """Tenta modificar configuração global (não funciona como esperado)."""
    configuracao = {"debug": True}# Cria variável local!
    print(f"Dentro da função: {configuracao}")

ativar_modo_debug()
print(f"Configuração global: {configuracao}")# Não foi alterada!