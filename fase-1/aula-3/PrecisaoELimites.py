import sys

# Maior e menor float representável
print(sys.float_info.max) # Aproximadamente 1.8 × 10^308
print(sys.float_info.min) # Aproximadamente 2.2 × 10^(-308)

# Precisão - geralmente 15-17 dígitos significativos
print(0.1234567890123456789) # Mostra aproximadamente 0.12345678901234568