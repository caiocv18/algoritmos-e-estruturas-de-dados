
# Operações aritméticas entre int e float
resultado1 = 5 + 3.14# 8.14 (float)
# Operações com bool e números
resultado2 = 10 + True# 11 (True é tratado como 1)
resultado3 = 10 * False# 0 (False é tratado como 0)
# Concatenação de strings
resultado4 = "Python" + " 3"# "Python 3"
# Multiplicação de string e int
resultado5 = "Python" * 3# "PythonPythonPython"
# Operações com listas
resultado6 = [1, 2] + [3, 4]# [1, 2, 3, 4]
resultado7 = [0] * 5# [0, 0, 0, 0, 0]

# Erro: tipos incompatíveis
try:
    resultado_erro = "5" + 5# TypeError
except TypeError as e:
    print(f"Erro: {e}")