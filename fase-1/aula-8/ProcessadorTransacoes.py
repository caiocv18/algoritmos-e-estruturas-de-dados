import random
import time

class ProcessadorTransacoes:
    def __init__(self):
        self.transacoes_processadas = 0
        self.total_valor = 0
        self.transacoes_aprovadas = 0
        self.transacoes_rejeitadas = 0
        self.erros = 0
        self.tempo_inicio = None
        self.tempo_fim = None
    
    def gerar_transacoes_teste(self, quantidade):
        """Gera uma lista de transações de teste."""
        tipos = ["CREDITO", "DEBITO", "TRANSFERENCIA", "DEPOSITO"]
        transacoes = []
        
        for i in range(quantidade):
            tipo = random.choice(tipos)
            valor = round(random.uniform(10, 1000), 2)
            # 5% de chance de valor negativo (inválido)
            if random.random() < 0.05:
                valor = -valor
            
            # 10% de chance de transação com ID inválido
            id_invalido = random.random() < 0.1
            id_transacao = "" if id_invalido else f"TX{i+1000}"
            
            transacoes.append({
                "id": id_transacao,
                "tipo": tipo,
                "valor": valor,
                "timestamp": time.time() + i
            })
        
        return transacoes
    
    def validar_transacao(self, transacao):
        """Valida uma transação antes do processamento."""
        if not transacao.get("id"):
            print(f"Erro: ID de transação ausente")
            return False
        
        if transacao.get("valor", 0) <= 0:
            print(f"Erro: Valor inválido ({transacao.get('valor')})")
            return False
        
        if transacao.get("tipo") not in ["CREDITO", "DEBITO", "TRANSFERENCIA", "DEPOSITO"]:
            print(f"Erro: Tipo de transação inválido ({transacao.get('tipo')})")
            return False
        
        return True
    
    def processar_transacao(self, transacao):
        """Processa uma transação individual."""
        if not self.validar_transacao(transacao):
            self.transacoes_rejeitadas += 1
            return False
        
        # Simulação de processamento
        print(f"Processando {transacao['tipo']} de R$ {transacao['valor']:.2f} (ID: {transacao['id']})")
        
        # Simulação de aprovação/rejeição com base no tipo e valor
        aprovada = True
        if transacao['tipo'] == "CREDITO" and transacao['valor'] > 500:
            # Simula uma taxa de rejeição de 20% para transações de crédito altas
            aprovada = random.random() > 0.2
        
        if aprovada:
            self.transacoes_aprovadas += 1
            self.total_valor += transacao['valor']
            print(f"  ✅ Transação aprovada")
        else:
            self.transacoes_rejeitadas += 1
            print(f"  ❌ Transação rejeitada")
        
        self.transacoes_processadas += 1
        return aprovada
    
    def processar_lote(self, transacoes, max_erros=3):
        """Processa um lote de transações."""
        self.tempo_inicio = time.time()
        indice = 0
        erros_consecutivos = 0
        
        print(f"\n{'='*50}")
        print(f"INICIANDO PROCESSAMENTO DE {len(transacoes)} TRANSAÇÕES")
        print(f"{'='*50}\n")
        
        while indice < len(transacoes):
            try:
                transacao_atual = transacoes[indice]
                
                # Simulação de possível erro de sistema
                if random.random() < 0.03:  # 3% de chance de erro
                    raise Exception("Erro de sistema simulado")
                
                resultado = self.processar_transacao(transacao_atual)
                
                if resultado:
                    erros_consecutivos = 0
                else:
                    erros_consecutivos += 1
                
                # Verifica se atingiu limite de erros consecutivos
                if erros_consecutivos >= max_erros:
                    print(f"\nAlerta: {max_erros} erros consecutivos. Interrompendo processamento.")
                    break
                
                indice += 1
                
                # Pausa breve para simular tempo de processamento
                time.sleep(0.1)
                
            except Exception as e:
                self.erros += 1
                print(f"Erro no processamento: {e}")
                # Tenta novamente a mesma transação
                erros_consecutivos += 1
                
                if erros_consecutivos >= max_erros:
                    print(f"\nAlerta: {max_erros} erros consecutivos. Interrompendo processamento.")
                    break
        
        self.tempo_fim = time.time()
        self.exibir_relatorio()
    
    def exibir_relatorio(self):
        """Exibe um relatório do processamento."""
        duracao = self.tempo_fim - self.tempo_inicio if self.tempo_fim else 0
        
        print(f"\n{'='*50}")
        print(f"RELATÓRIO DE PROCESSAMENTO")
        print(f"{'='*50}")
        print(f"Transações processadas: {self.transacoes_processadas}")
        print(f"Aprovadas: {self.transacoes_aprovadas}")
        print(f"Rejeitadas: {self.transacoes_rejeitadas}")
        print(f"Erros de sistema: {self.erros}")
        print(f"Valor total processado: R$ {self.total_valor:.2f}")
        print(f"Tempo de processamento: {duracao:.2f} segundos")
        
        if self.transacoes_processadas > 0:
            taxa_aprovacao = (self.transacoes_aprovadas / self.transacoes_processadas) * 100
            print(f"Taxa de aprovação: {taxa_aprovacao:.1f}%")
            
            if duracao > 0:
                tps = self.transacoes_processadas / duracao
                print(f"Velocidade: {tps:.2f} transações por segundo")
        
        print(f"{'='*50}")

# Execução do sistema
if __name__ == "__main__":
    processador = ProcessadorTransacoes()
    transacoes_teste = processador.gerar_transacoes_teste(20)
    processador.processar_lote(transacoes_teste)