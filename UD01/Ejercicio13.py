# Ejercicio13: Dibuja un ordinograma de un programa que muestre los números
# desde el 1 hasta el número N que se introducirá por teclado

# Solicita el número N
N = int(input("Introduce un número N: "))

# Muestra los números desde 1 hasta N
for numero in range(1, N + 1):
    print(numero)