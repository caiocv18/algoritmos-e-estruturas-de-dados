import re

# Validação de email (simplificada)
padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
email = "usuario@exemplo.com"
if re.match(padrao_email, email):
    print("Email válido")