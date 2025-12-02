"""
Ejercicio 7:
Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.
"""

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Pedir al usuario el carácter que desea reemplazar
caracter_original = input("Ingrese el carácter a reemplazar: ")

# Pedir al usuario el nuevo carácter
caracter_nuevo = input("Ingrese el nuevo carácter: ")

# Inicializar la nueva cadena vacía
nueva_cadena = ""

# Recorrer la cadena carácter por carácter
for i in range(len(cadena)):
    if cadena[i] == caracter_original:
        nueva_cadena = nueva_cadena + caracter_nuevo 
    else:
        nueva_cadena = nueva_cadena + cadena[i]

print("La nueva cadena es:", nueva_cadena)