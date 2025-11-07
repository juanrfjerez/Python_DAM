# Ejercicio27: Dibuja un ordinograma de un programa que lea una secuencia de notas (con valores que
# van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10.add()

# Variable para registrar si se ha leído alguna nota con valor 10
hay_diez = False

# Bucle para leer notas hasta que se introduzca -1
while True:
    nota = float(input("Introduce una nota entre 0 y 10 (-1 para terminar): "))
    
    # Verifica si se debe terminar
    if nota == -1:
        break
    
    # Verifica que la nota esté en el rango válido
    if 0 <= nota <= 10:
        if nota == 10:
            hay_diez = True
    else:
        print("Nota fuera de rango. Introduce un valor entre 0 y 10 o -1 para terminar.")

# Muestra el resultado final
if hay_diez:
    print("Se ha introducido al menos una nota con valor 10.")
else:
    print("No se ha introducido ninguna nota con valor 10.")