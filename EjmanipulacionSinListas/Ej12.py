"""
Ejercicio 12:
Leer una cadena y construir una nueva cadena con los caracteres en orden inverso.
"""

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Nueva cadena vacía
nueva_cadena = ""

# Recorrer la cadena desde el final hacia el inicio
for i in range(len(cadena) - 1, -1, -1):
    nueva_cadena = nueva_cadena + cadena[i]

print("La nueva cadena en orden inverso es:", nueva_cadena)