# Ejercicio5: Dibuja un ordinograma que lea dos números, calcule y muestre 
# el valor de sus suma, resta,producto y división.

# Entrada de datos
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Cálculos
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

# Validación para evitar división por cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

# Salida de resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")
print(f"División: {division}")