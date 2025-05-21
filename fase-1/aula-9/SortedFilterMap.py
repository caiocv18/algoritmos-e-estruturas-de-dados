números = [5, 2, 8, 1, 7]

# sorted() - retorna uma nova lista ordenada
for n in sorted(números):
    print(n)  # 1, 2, 5, 7, 8

# filter() - filtra elementos com base em uma função
for n in filter(lambda x: x % 2 == 0, números):
    print(n)  # 2, 8

# map() - aplica uma função a cada elemento
for n in map(lambda x: x * 2, números):
    print(n)  # 10, 4, 16, 2, 14