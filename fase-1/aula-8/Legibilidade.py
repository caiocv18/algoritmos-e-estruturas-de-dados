# Calculando a soma de uma lista com while
   numeros = [5, 10, 15, 20, 25]
   soma = 0
   i = 0
   while i < len(numeros):
       soma += numeros[i]
       i += 1
   print(f"Soma: {soma}")