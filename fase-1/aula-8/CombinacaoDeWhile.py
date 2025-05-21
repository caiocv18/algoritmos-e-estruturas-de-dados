# Programa para encontrar números primos até um limite
limite = int(input("Encontrar números primos até: "))
numero = 2

print(f"Números primos até {limite}:")
while numero <= limite:
    eh_primo = True
    divisor = 2
    
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1
    
    if eh_primo:
        print(numero, end=" ")
    
    numero += 1