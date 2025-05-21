# Bom uso de compreensão
nomes = ["Ana", "BRUNO", "Carlos", "DIANA"]
nomes_formatados = [nome.capitalize() for nome in nomes]

# Melhor com loop tradicional
resultados = []
for valor in dados:
    try:
        resultado = processar_complexo(valor)
        validar_resultado(resultado)
        resultados.append(resultado)
    except ValueError:
        registrar_erro(valor)
        resultados.append(valor_padrão)