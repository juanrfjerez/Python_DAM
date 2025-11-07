# Ejercicio22: Dibuja un ordinograma de un programa que lea 100 números no nulos
# y luego muestre un mensaje indicando cuántos son positivos y cuantos negativos

# Inicializa contadores
positivos = 0
negativos = 0

# Bucle para leer 100 números
for i in range(1, 101):
    numero = float(input(f"Introduce el número {i} (no nulo): "))
    
    # Verifica que el número no sea cero
    while numero == 0:
        numero = float(input("El número no puede ser cero. Introduce otro: "))
    
    # Clasifica el número como positivo o negativo
    if numero > 0:
        positivos += 1
    else:
        negativos += 1

# Muestra los resultados
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")