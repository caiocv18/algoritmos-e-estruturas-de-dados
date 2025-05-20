# Encadeamento (difícil de ler)
categoria = "Infantil" if idade < 12 else "Jovem" if idade < 18 else "Adulto"

# Alternativa mais legível com if-elif-else
if idade < 12:
    categoria = "Infantil"
elif idade < 18:
    categoria = "Jovem"
else:
    categoria = "Adulto"