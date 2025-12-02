"""
Ejercicio 5:
Verificar si un carácter específico está en la cadena con un ciclo y comparaciones.
"""

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Pedir al usuario el carácter que desea verificar
caracter = input("Ingrese el carácter a verificar: ")

# Variable booleana para indicar si el carácter fue encontrado
encontrado = False

# Recorrer la cadena carácter por carácter
for i in range(len(cadena)):
    if cadena[i] == caracter:
        encontrado = True 
        break             

if encontrado:
    print("El carácter", caracter, "sí está en la cadena.")
else:
    print("El carácter", caracter, "no está en la cadena.")