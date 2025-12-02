"""
Ejercicio 13:
Leer una cadena y eliminar todos los espacios, construyendo una cadena continua.
"""

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Nueva cadena vacía
nueva_cadena = ""

# Recorrer la cadena carácter por carácter
for i in range(len(cadena)):
    caracter = cadena[i]
    if caracter != " ":
        nueva_cadena = nueva_cadena + caracter

print("La nueva cadena continua es:", nueva_cadena)