import re

def validar_senha(senha):
    # Pelo menos 8 caracteres
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres"
    
    # Pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula"
    
    # Pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False, "A senha deve conter pelo menos uma letra minúscula"
    
    # Pelo menos um número
    if not re.search(r'[0-9]', senha):
        return False, "A senha deve conter pelo menos um número"
    
    # Pelo menos um caractere especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return False, "A senha deve conter pelo menos um caractere especial"
    
    return True, "Senha válida"