"""
Ejercicio 15:
Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'.
"""

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Nueva cadena vacía
nueva_cadena = ""

# Recorrer la cadena carácter por carácter
for i in range(len(cadena)):
    caracter = cadena[i]
    # Comprobamos directamente si el carácter en minúscula es una vocal
    if caracter.lower() in "aeiou":
        nueva_cadena = nueva_cadena + "*"
    else:
        nueva_cadena = nueva_cadena + caracter

print("La nueva cadena es:", nueva_cadena)