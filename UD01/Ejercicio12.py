# Ejercicio12: Dibuja un ordinograma de un programa que muestre los números pares comprendidos
# entre el 1 y el 200. Esta vez utiliza un contador sumando de 1 en 1

# Inicializamos el contador en 1
contador = 1

# Recorremos del 1 al 200 sumando de 1 en 1
while contador <= 200:
    # Si el número es par, lo mostramos
    if contador % 2 == 0:
        print(contador)
    contador += 1