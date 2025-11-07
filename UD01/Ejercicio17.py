# Ejercicio17: Dibuja un ordinograma de un programa que lea dos números
# y lo visualiza en orden ascendente

# Solicita dos números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Muestra los números en orden ascendente
if num1 < num2:
    print(f"Orden ascendente: {num1}, {num2}")
elif num2 < num1:
    print(f"Orden ascendente: {num2}, {num1}")
else:
    print("Ambos números son iguales")