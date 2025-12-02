"""
Ejercicio 10:
Leer una cadena y contar cuántos caracteres son letras mayúsculas.
"""

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Variable con todas las letras mayúsculas
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Contador de mayúsculas
contador = 0

# Recorrer la cadena carácter por carácter
for i in range(len(cadena)):
    caracter = cadena[i]
    if caracter in mayusculas:
        contador = contador + 1

print("La cadena contiene", contador, "letra(s) mayúscula(s).")