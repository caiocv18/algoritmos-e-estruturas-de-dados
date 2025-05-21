# main.py
from modelo import RepositorioDados
import processamento
import visualizacao

def main():
    """Função principal do sistema."""
    # Inicializar o repositório e carregar dados de exemplo
    repositorio = RepositorioDados()
    repositorio.carregar_dados_exemplo()

    while True:
        opcao = visualizacao.exibir_menu()

        if opcao == '0':
            print("\nEncerrando o sistema... Até logo!")
            break

        elif opcao == '1':
            # Total de Vendas
            total = processamento.calcular_total_vendas(repositorio)
            visualizacao.exibir_total_vendas(total)

        elif opcao == '2':
            # Vendas por Categoria
            vendas_por_categoria = processamento.calcular_vendas_por_categoria(repositorio)
            visualizacao.exibir_vendas_por_categoria(vendas_por_categoria)

        elif opcao == '3':
            # Produtos Mais Vendidos
            produtos_mais_vendidos = processamento.calcular_produtos_mais_vendidos(repositorio)
            visualizacao.exibir_produtos_mais_vendidos(produtos_mais_vendidos)

        elif opcao == '4':
            # Tendência de Vendas
            tendencia = processamento.analisar_tendencia_vendas(repositorio)
            visualizacao.exibir_tendencia_vendas(tendencia)

        elif opcao == '5':
            # Todas as Análises
            total = processamento.calcular_total_vendas(repositorio)
            visualizacao.exibir_total_vendas(total)

            vendas_por_categoria = processamento.calcular_vendas_por_categoria(repositorio)
            visualizacao.exibir_vendas_por_categoria(vendas_por_categoria)

            produtos_mais_vendidos = processamento.calcular_produtos_mais_vendidos(repositorio)
            visualizacao.exibir_produtos_mais_vendidos(produtos_mais_vendidos)

            tendencia = processamento.analisar_tendencia_vendas(repositorio)
            visualizacao.exibir_tendencia_vendas(tendencia)

        else:
            print("\nOpção inválida! Por favor, tente novamente.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
