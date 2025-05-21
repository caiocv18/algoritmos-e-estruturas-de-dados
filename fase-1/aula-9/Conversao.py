# Loop for convertido para while
# Original
for i in range(1, 6):
    print(i)

# Equivalente com while
i = 1
while i <= 5:
    print(i)
    i += 1

# Loop while convertido para for
# Original
contador = 0
total = 0
while contador < 10:
    total += contador
    contador += 1

# Equivalente com for
total = 0
for contador in range(10):
    total += contador