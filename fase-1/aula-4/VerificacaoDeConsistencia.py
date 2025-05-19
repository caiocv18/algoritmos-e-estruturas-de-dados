# Correção para evitar saldo negativo no último pagamento
if mes == num_pagamentos:
    amortizacao += saldo_restante
    saldo_restante = 0