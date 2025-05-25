# arquivo: utils/decoradores.py
"""Decoradores reutilizáveis para diversas situações."""

import time
import functools
import logging
from typing import Callable, Any


def medir_tempo(func: Callable) -> Callable:
    """Decorador que mede o tempo de execução de uma função."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"{func.__name__} levou {tempo_execucao:.4f} segundos")
        return resultado
    return wrapper


def cache_resultado(func: Callable) -> Callable:
    """Decorador que cacheia resultados de funções."""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Retornando resultado cacheado para {args}")
            return cache[args]

        resultado = func(*args)
        cache[args] = resultado
        return resultado

    return wrapper


def validar_tipos(**tipos_esperados):
    """Decorador que valida tipos de argumentos."""
    def decorador(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Obter nomes dos parâmetros da função
            nomes_params = func.__code__.co_varnames[:func.__code__.co_argcount]

            # Criar dicionário de argumentos
            todos_args = dict(zip(nomes_params, args))
            todos_args.update(kwargs)

            # Validar tipos
            for nome, valor in todos_args.items():
                if nome in tipos_esperados:
                    tipo_esperado = tipos_esperados[nome]
                    if not isinstance(valor, tipo_esperado):
                        raise TypeError(
                            f"{nome} deve ser {tipo_esperado.__name__}, "
                            f"recebido {type(valor).__name__}"
                        )

            return func(*args, **kwargs)
        return wrapper
    return decorador


def tentar_novamente(max_tentativas: int = 3, delay: float = 1.0):
    """Decorador que tenta executar função múltiplas vezes em caso de erro."""
    def decorador(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for tentativa in range(max_tentativas):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if tentativa == max_tentativas - 1:
                        raise
                    print(f"Tentativa {tentativa + 1} falhou: {e}")
                    time.sleep(delay)

        return wrapper
    return decorador


# Exemplo de uso dos decoradores
@medir_tempo
@cache_resultado
def fibonacci(n: int) -> int:
    """Calcula o n-ésimo número de Fibonacci."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


@validar_tipos(nome=str, idade=int, salario=float)
def criar_funcionario(nome, idade, salario):
    """Cria um registro de funcionário."""
    return {
        "nome": nome,
        "idade": idade,
        "salario": salario
    }


@tentar_novamente(max_tentativas=3, delay=0.5)
def operacao_instavel():
    """Simula uma operação que pode falhar."""
    import random
    if random.random() < 0.7:  # 70% de chance de falhar
        raise ConnectionError("Falha na conexão")
    return "Sucesso!"