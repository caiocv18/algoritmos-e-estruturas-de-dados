contador_global = 0 # Variável global

def incrementar_contador():
    contador_local = 10 # Variável local
    print(f"Dentro da função - Global: {contador_global}, Local: {contador_local}")

    def funcao_interna():
				# Pode acessar contador_local da função externa
        contador_mais_interno = contador_local + 5
        return contador_mais_interno

    return funcao_interna()

resultado = incrementar_contador()
print(f"Resultado: {resultado}")
# print(contador_local)  
# Erro! Variável local não existe fora da função