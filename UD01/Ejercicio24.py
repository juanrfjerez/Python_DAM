# Ejercicio24: Dibuja un ordinograma de un programa que calcule y escriba la suma
# y el producto de los 10 primeros números naturales

# Inicializa las variables
suma = 0
producto = 1

# Recorre los 10 primeros números naturales
for numero in range(1, 11):
    suma += numero         # Acumula la suma
    producto *= numero     # Acumula el producto

# Muestra los resultados
print(f"Suma de los 10 primeros números naturales: {suma}")
print(f"Producto (factorial de 10): {producto}")