import random

# Simulação simplificada de crescimento populacional
populacao_inicial = 1000
taxa_crescimento = 0.05  # 5% ao ano
anos_simulados = 0
populacao = populacao_inicial
limite_populacional = 10000

print(f"Simulação de crescimento populacional")
print(f"População inicial: {populacao_inicial}")
print(f"Taxa de crescimento: {taxa_crescimento * 100:.1f}% ao ano")
print(f"Limite populacional: {limite_populacional}")

while populacao < limite_populacional:
    # Variação aleatória na taxa de crescimento (entre 0.8 e 1.2 vezes a taxa base)
    variacao = random.uniform(0.8, 1.2)
    taxa_efetiva = taxa_crescimento * variacao
    
    # Crescimento populacional
    populacao_antiga = populacao
    populacao = int(populacao * (1 + taxa_efetiva))
    anos_simulados += 1
    
    # Output com formatação
    print(f"Ano {anos_simulados}: {populacao_antiga} → {populacao} " +
          f"(crescimento de {taxa_efetiva * 100:.2f}%)")
    
    # Condição de parada adicional para evitar loops muito longos
    if anos_simulados >= 1000:
        print("Simulação interrompida após 1000 anos.")
        break

print(f"\nA população atingiu {populacao} após {anos_simulados} anos.")
print(f"Taxa média de crescimento anual: {(((populacao/populacao_inicial)**(1/anos_simulados))-1)*100:.2f}%")