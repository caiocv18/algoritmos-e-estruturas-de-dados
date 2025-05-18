import sys

# Tamanho de diferentes tipos em memória
print(f"Inteiro: {sys.getsizeof(42)} bytes")
print(f"Float: {sys.getsizeof(3.14)} bytes")
print(f"String pequena: {sys.getsizeof('a')} bytes")
print(f"String maior: {sys.getsizeof('Python')} bytes")
print(f"Lista vazia: {sys.getsizeof([])} bytes")
print(f"Lista com 5 inteiros: {sys.getsizeof([1, 2, 3, 4, 5])} bytes")
print(f"Tupla vazia: {sys.getsizeof(())} bytes")
print(f"Tupla com 5 inteiros: {sys.getsizeof((1, 2, 3, 4, 5))} bytes")

# Identificador único de um objeto (endereço de memória)
a = [1, 2, 3]
b = a# b referencia o mesmo objeto que a
c = [1, 2, 3]# c é um novo objeto com o mesmo conteúdo

print(f"ID de a: {id(a)}")
print(f"ID de b: {id(b)}")# Mesmo ID que 'a'
print(f"ID de c: {id(c)}")# ID diferente

print(f"a is b: {a is b}")# True (mesmo objeto)
print(f"a is c: {a is c}")# False (objetos diferentes)
print(f"a == c: {a == c}")# True (mesmo conteúdo)