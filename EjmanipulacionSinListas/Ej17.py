"""
Ejercicio 17:
Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez.
"""

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Nueva cadena vacía
nueva_cadena = ""

# Recorrer la cadena carácter por carácter
for i in range(len(cadena)):
    caracter = cadena[i]
    # Contamos cuántas veces aparece ese carácter en la cadena
    if cadena.count(caracter) > 1 and caracter not in nueva_cadena:
        nueva_cadena = nueva_cadena + caracter

print("La nueva cadena es:", nueva_cadena)