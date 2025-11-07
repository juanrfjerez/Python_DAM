# Ejercicio20: Dibuja un ordinograma de un programa que lea un número positivo N
# y calcule y visualice su factura N! siendo el factorial

# Solicita un número positivo al usuario
N = int(input("Introduce un número positivo: "))

# Verifica que el número sea positivo
if N < 0:
    print("El número debe ser positivo")
else:
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i  # Multiplica acumulativamente
    print(f"El factorial de {N} es: {factorial}")