"""
Ejercicio 18:
Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes 
(sin listas, usando condiciones y concatenación).
"""

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Nueva cadena vacía
nueva_cadena = ""

# Recorrer la cadena carácter por carácter
for i in range(len(cadena)):
    if cadena[i].isalpha() and cadena[i].lower() not in "aeiou":
        nueva_cadena = nueva_cadena + cadena[i]
print("La nueva cadena es:", nueva_cadena)
     