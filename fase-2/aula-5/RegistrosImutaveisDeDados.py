from datetime import datetime
from collections import namedtuple

# Definindo estrutura de registro imutável
RegistroVenda = namedtuple('RegistroVenda',
    ['id', 'data', 'cliente', 'produto', 'quantidade', 'preco_unitario'])

# Sistema de vendas com registros imutáveis
class SistemaVendas:
    def __init__(self):
        self.vendas = []
        self.proximo_id = 1

    def registrar_venda(self, cliente, produto, quantidade, preco_unitario):
        """Cria registro imutável de venda"""
        venda = RegistroVenda(
            id=self.proximo_id,
            data=datetime.now(),
            cliente=cliente,
            produto=produto,
            quantidade=quantidade,
            preco_unitario=preco_unitario
        )
        self.vendas.append(venda)
        self.proximo_id += 1
        return venda

    def calcular_total_venda(self, venda):
        """Calcula total de uma venda"""
        return venda.quantidade * venda.preco_unitario

    def relatorio_vendas(self):
        """Gera relatório de vendas"""
        print("\n=== RELATÓRIO DE VENDAS ===")
        print(f"{'ID':>4} {'Data':>20} {'Cliente':>15} {'Produto':>20} {'Qtd':>5} {'Unit':>10} {'Total':>10}")
        print("-" * 95)

        total_geral = 0
        for venda in self.vendas:
            total_venda = self.calcular_total_venda(venda)
            total_geral += total_venda

            print(f"{venda.id:>4} {venda.data.strftime('%Y-%m-%d %H:%M'):>20} "
                  f"{venda.cliente:>15} {venda.produto:>20} "
                  f"{venda.quantidade:>5} {venda.preco_unitario:>10.2f} "
                  f"{total_venda:>10.2f}")

        print("-" * 95)
        print(f"{'TOTAL GERAL':>75} {total_geral:>10.2f}")

# Exemplo de uso
sistema = SistemaVendas()
sistema.registrar_venda("João Silva", "Notebook", 1, 3500.00)
sistema.registrar_venda("Maria Santos", "Mouse", 2, 50.00)
sistema.registrar_venda("Pedro Costa", "Teclado", 1, 200.00)
sistema.registrar_venda("Ana Lima", "Monitor", 2, 800.00)

sistema.relatorio_vendas()

# Tentativa de modificar registro (falha)
venda = sistema.vendas[0]
print(f"\nVenda original: {venda}")
try:
    venda.quantidade = 10  # Erro! NamedTuple é imutável
except AttributeError as e:
    print(f"Erro ao tentar modificar: {e}")
