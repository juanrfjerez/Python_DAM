"""
Ejercicio 11:
Construir una nueva cadena con todos los caracteres de la cadena original,
pero duplicando cada vocal.
"""

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Nueva cadena donde iremos acumulando el resultado
nueva_cadena = ""

# Recorrer la cadena carácter por carácter
for i in range(len(cadena)):
    caracter = cadena[i]
    if caracter.lower() in "aeiou":
        nueva_cadena = nueva_cadena + caracter + caracter
    else:
        nueva_cadena = nueva_cadena + caracter

print("La nueva cadena es:", nueva_cadena)