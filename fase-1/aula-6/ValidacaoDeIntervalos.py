def validar_data(dia, mes, ano):
    # Validação básica de intervalos
    if not (1 <= mes <= 12):
        return False, "Mês deve estar entre 1 e 12"
    
    # Determinação do número de dias no mês
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verificação de ano bissexto
    if mes == 2 and (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
        dias_no_mes = 29
    else:
        dias_no_mes = dias_por_mes[mes]
    
    # Validação do dia com base no mês e ano
    if not (1 <= dia <= dias_no_mes):
        return False, f"Dia deve estar entre 1 e {dias_no_mes} para o mês {mes}"
    
    return True, "Data válida"