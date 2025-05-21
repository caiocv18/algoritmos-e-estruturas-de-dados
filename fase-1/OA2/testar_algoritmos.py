def testar_algoritmos():
    """Executa testes automáticos para validar os algoritmos implementados."""
    # Testes para converter_temperatura
    assert abs(converter_temperatura(0, 'C', 'F') - 32.0) < 0.01
    assert abs(converter_temperatura(100, 'C', 'K') - 373.15) < 0.01
    assert abs(converter_temperatura(32, 'F', 'C') - 0.0) < 0.01
    assert abs(converter_temperatura(273.15, 'K', 'C') - 0.0) < 0.01

    # Testes para verificar_primo
    assert verificar_primo(2) == True
    assert verificar_primo(17) == True
    assert verificar_primo(4) == False
    assert verificar_primo(1) == False
    assert verificar_primo(0) == False
    assert verificar_primo(-5) == False

    # Testes para calcular_estatisticas
    estatisticas = calcular_estatisticas([1, 2, 3, 4, 5])
    assert abs(estatisticas['media'] - 3.0) < 0.01
    assert abs(estatisticas['mediana'] - 3.0) < 0.01
    assert estatisticas['moda'] is None  # Todos aparecem uma vez

    estatisticas = calcular_estatisticas([1, 2, 2, 3, 4, 4, 4, 5])
    assert abs(estatisticas['media'] - 3.125) < 0.01
    assert abs(estatisticas['mediana'] - 3.5) < 0.01
    assert estatisticas['moda'] == 4

    print("Todos os testes passaram com sucesso!")
