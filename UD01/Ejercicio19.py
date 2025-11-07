# Ejercicio19: Dibuja un ordinograma de un programa que lea tres números
# y nos diga cual es mayor, cual menor y cuales son iguales

# Solicita tres números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Verifica si todos son iguales
if num1 == num2 == num3:
    print("Los tres números son iguales")
else:
    # Determina el mayor
    mayor = max(num1, num2, num3)
    # Determina el menor
    menor = min(num1, num2, num3)

    print(f"El mayor es: {mayor}")
    print(f"El menor es: {menor}")

    # Verifica si hay dos iguales
    if num1 == num2 or num1 == num3 or num2 == num3:
        print("Hay dos números iguales")