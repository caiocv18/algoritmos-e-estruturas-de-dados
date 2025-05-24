def gerar_senha_simples():
    """Gera uma senha aleatória simples."""
    import random
    import string

# Componentes da senha
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits

# Garantir pelo menos um de cada tipo
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(digitos)
    ]

# Completar com caracteres aleatórios
    todos_caracteres = letras_maiusculas + letras_minusculas + digitos
    for _ in range(5):# Mais 5 caracteres
        senha.append(random.choice(todos_caracteres))

# Embaralhar
    random.shuffle(senha)

# Converter para string
    senha_final = ''.join(senha)
    print(f"Senha gerada: {senha_final}")

def verificar_forca_senha():
    """Verifica a força de uma senha."""
    senha = input("Digite a senha para verificar: ")

    criterios = {
        "Comprimento mínimo (8 caracteres)": len(senha) >= 8,
        "Contém letra maiúscula": any(c.isupper() for c in senha),
        "Contém letra minúscula": any(c.islower() for c in senha),
        "Contém número": any(c.isdigit() for c in senha),
        "Contém caractere especial": any(c in "!@#$%^&*" for c in senha)
    }

    print("\n=== ANÁLISE DA SENHA ===")
    pontos = 0
    for criterio, atende in criterios.items():
        status = "✓" if atende else "✗"
        print(f"{status} {criterio}")
        if atende:
            pontos += 1

# Classificação
    if pontos <= 2:
        forca = "FRACA"
    elif pontos <= 4:
        forca = "MÉDIA"
    else:
        forca = "FORTE"

    print(f"\nForça da senha: {forca} ({pontos}/5 critérios)")

# Testando
gerar_senha_simples()
gerar_senha_simples()
verificar_forca_senha()