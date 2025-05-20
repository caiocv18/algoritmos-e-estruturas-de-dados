def testar_condiciones_extremas():
    """
    Realiza testes com valores extremos para verificar o comportamento
    do sistema em situações limítrofes.
    """
    print("\n=== Teste de Condições Extremas ===")
    
    # Casos de teste para valores limítrofes
    casos_teste = [
        {
            "nome": "Caso 1: Valores mínimos",
            "idade": 18,
            "renda": 3000,
            "score": 700
        },
        {
            "nome": "Caso 2: Valores máximos",
            "idade": 65,
            "renda": 50000,
            "score": 1000
        },
        {
            "nome": "Caso 3: Idade abaixo do mínimo",
            "idade": 17,
            "renda": 5000,
            "score": 800
        },
        {
            "nome": "Caso 4: Idade acima do máximo",
            "idade": 66,
            "renda": 5000,
            "score": 800
        },
        {
            "nome": "Caso 5: Renda abaixo do mínimo",
            "idade": 30,
            "renda": 2999,
            "score": 800
        },
        {
            "nome": "Caso 6: Score abaixo do mínimo",
            "idade": 30,
            "renda": 5000,
            "score": 699
        },
        {
            "nome": "Caso 7: Caso extremo - valores muito altos",
            "idade": 25,
            "renda": 1000000,
            "score": 950
        },
        {
            "nome": "Caso 8: Caso extremo - valores na fronteira",
            "idade": 21,
            "renda": 3000,
            "score": 700
        }
    ]
    
    # Execução dos casos de teste
    for caso in casos_teste:
        print(f"\n{caso['nome']}")
        try:
            resultado = rastrear_fluxo_execucao(caso["idade"], caso["renda"], caso["score"])
            print(f"Resultado: {'Aprovado' if resultado else 'Reprovado'}")
        except Exception as e:
            print(f"Erro durante execução: {e}")