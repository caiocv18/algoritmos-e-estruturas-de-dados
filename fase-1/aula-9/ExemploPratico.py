# Convertendo temperaturas de Celsius para Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(9/5) * temp + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]