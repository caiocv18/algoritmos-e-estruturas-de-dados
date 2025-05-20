# A ordem importa!
idade = 15

# Versão correta
if idade < 12:
    valor = 10.0
    categoria = "Infantil"
elif idade < 18:
    valor = 15.0
    categoria = "Jovem"
else:
    valor = 20.0
    categoria = "Adulto"

# Versão incorreta - lógica falha
if idade < 18:
    valor = 15.0
    categoria = "Jovem"
elif idade < 12:# Nunca será avaliado para idade < 12!
    valor = 10.0
    categoria = "Infantil"
else:
    valor = 20.0
    categoria = "Adulto"