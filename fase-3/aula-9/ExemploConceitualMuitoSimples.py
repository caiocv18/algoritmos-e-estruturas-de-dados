# Dados de exemplo
meses = ['Jan', 'Fev', 'Mar', 'Abr']
vendas = [100, 120, 90, 150]

# Criando o gráfico de linha
plt.plot(meses, vendas, marker='o') # marker='o' adiciona bolinhas nos pontos

# Adicionando títulos e rótulos
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Unidades Vendidas')

# Exibindo o gráfico
plt.show()