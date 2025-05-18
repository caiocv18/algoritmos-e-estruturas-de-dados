# Conversão de outros tipos para int
inteiro1 = int(5.7)# 5 (trunca, não arredonda)
inteiro2 = int("42")# 42
inteiro3 = int(True)# 1
inteiro4 = int("0b101", 2)# 5 (binário para decimal)
inteiro5 = int("1A", 16)# 26 (hexadecimal para decimal)
# Conversão de outros tipos para float
float1 = float(5)# 5.0
float2 = float("3.14")# 3.14
float3 = float("-inf")# -infinito# Conversão de outros tipos para str
texto1 = str(42)# "42"
texto2 = str(3.14159)# "3.14159"
texto3 = str(True)# "True"
texto4 = str([1, 2, 3])# "[1, 2, 3]"
# Conversão de outros tipos para bool
bool1 = bool(1)# True
bool2 = bool(0)# False
bool3 = bool("Texto")# True
bool4 = bool("")# False# Conversão para list, tuple
lista = list("Python")# ['P', 'y', 't', 'h', 'o', 'n']
tupla = tuple([1, 2, 3])# (1, 2, 3)