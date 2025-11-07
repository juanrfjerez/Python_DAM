# Ejercicio15: Dibuja un ordinograma de un programa que lee dos números y muestra el mayor.

# Solicita dos números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Compara los dos números y muestra el mayor
if num1 > num2:
    print(f"El mayor es: {num1}")
elif num2 > num1:
    print(f"El mayor es: {num2}")
else:
    print("Ambos números son iguales")