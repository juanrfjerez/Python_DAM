# Ejercicio23: Dibuja un ordinograma de un programa que lea una secuencia de números
# no nulos hasta que se introduzca un 0, y luego muestre si ha leído
#  algún número negativo, cuantos positivos y cuantos negativos

# Inicializamos los contadores
positivos = 0
negativos = 0

# Bucle para leer números hasta que se introduzca un 0
while True:
    numero = float(input("Introduce un número (0 para terminar): "))
    
    # Si el número es 0, se termina la lectura
    if numero == 0:
        break
    
    # Clasifica el número como positivo o negativo
    if numero > 0:
        positivos += 1
    else:
        negativos += 1

# Muestra los resultados
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

# Verifica si se leyó algún número negativo
if negativos > 0:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")