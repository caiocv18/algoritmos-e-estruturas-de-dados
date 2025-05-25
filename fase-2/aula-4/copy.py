original = [1, 2, 3, [4, 5]]
copia = original.copy()
copia[0] = 10
copia[3][0] = 40# Cuidado: objetos internos são compartilhados!

print(original)# [1, 2, 3, [40, 5]]
print(copia)# [10, 2, 3, [40, 5]]# Para cópia profunda
import copy
copia_profunda = copy.deepcopy(original)