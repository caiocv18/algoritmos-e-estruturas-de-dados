def calcular_imc():
    # 1. ENTRADA
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
    except ValueError:
        print("Erro: Por favor, digite valores numéricos.")
        return None
    
    # 2. VALIDAÇÃO
    if peso <= 0 or altura <= 0:
        print("Erro: Peso e altura devem ser valores positivos.")
        return None
    
    # 3. PROCESSAMENTO
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    
    # 4. SAÍDA
    print(f"\nResultados:")
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {categoria}")
    
    return imc, categoria