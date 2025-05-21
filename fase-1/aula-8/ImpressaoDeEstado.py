contador = 1
soma = 0

while contador <= 5:
    print(f"--- Iteração {contador} ---")
    print(f"  Antes: contador = {contador}, soma = {soma}")
    
    soma += contador
    contador += 1
    
    print(f"  Depois: contador = {contador}, soma = {soma}")