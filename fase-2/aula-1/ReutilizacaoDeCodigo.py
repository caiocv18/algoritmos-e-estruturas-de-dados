def calcular_media(numeros):
    """Calcula a média de uma lista de números."""
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Reutilizando em diferentes contextos
notas_matematica = [8.5, 7.0, 9.2, 6.8]
notas_portugues = [7.5, 8.0, 8.5, 9.0]
temperaturas_semana = [28, 31, 27, 32, 29, 30, 26]

print(f"Média Matemática: {calcular_media(notas_matematica):.2f}")
print(f"Média Português: {calcular_media(notas_portugues):.2f}")
print(f"Temperatura média: {calcular_media(temperaturas_semana):.1f}°C")