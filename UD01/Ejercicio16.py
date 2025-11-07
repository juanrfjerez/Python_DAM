# Ejercicio16: Dibuja un ordinograma de un programa que lea un número y dice si es
# positivo o negativo, consideramos el cero como positivo

# Solicita un número al usuario
numero = float(input("Introduce un número: "))

# Verifica si el número es positivo o negativo
if numero >= 0:
    print("El número es positivo")
else:
    print("El número es negativo")