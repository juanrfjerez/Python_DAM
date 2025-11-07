# Ejercicio21: Dibuja un ordinograma de un programa que lea 100 números no nulos
# y luego muestre un mensaje de si ha leído número negativo o no

# Variable para registrar si se ha leído algún número negativo
hay_negativo = False

# Bucle para leer 100 números
for i in range(1, 101):
    numero = float(input(f"Introduce el número {i} (no nulo): "))
    
    # Verifica que el número no sea cero
    while numero == 0:
        numero = float(input("El número no puede ser cero. Introduce otro: "))
    
    # Si el número es negativo, actualiza la variable
    if numero < 0:
        hay_negativo = True

# Muestra el mensaje final
if hay_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")