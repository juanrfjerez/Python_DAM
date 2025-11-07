# Ejercicio14: Dibuja un ordinograma que lea dos números, calcule y muestre el valor de sus suma, resta,
# producto y división (Ten en cuenta la división por cero)

# Solicita dos números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Realiza las operaciones básicas
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

# Verifica si el segundo número es cero antes de dividir
if num2 != 0:
    division = num1 / num2
    print(f"División: {division}")
else:
    print("No se puede dividir entre cero.")

# Muestra los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")