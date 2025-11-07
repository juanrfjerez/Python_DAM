# Ejercicio28: Dibuja un ordinograma de un programa que suma independientemente los pares y los
# impares de los números comprendidos entre 100 y 200, y luego muestre por pantalla ambas sumas

# Inicializa las sumas
suma_pares = 0
suma_impares = 0

# Recorre los números del 100 al 200 incluido
for numero in range(100, 201):
    if numero % 2 == 0:
        suma_pares = suma_pares + numero  # Suma directa sin usar +=
    else:
        suma_impares = suma_impares + numero  # Suma directa sin usar +=

# Muestra los resultados
print("Suma de pares entre 100 y 200:", suma_pares)
print("Suma de impares entre 100 y 200:", suma_impares)