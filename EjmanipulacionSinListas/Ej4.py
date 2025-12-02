"""
Ejercicio 4:
Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas).
"""
cadena = input("Ingrese una cadena: ")

# Construir una nueva cadena filtrando solo las vocales
solo_vocales = ""
for i in range(len(cadena)):
    if cadena[i].lower() in "aeiou":  # comprobamos si el carácter es una vocal
        solo_vocales = solo_vocales + cadena[i]  # añadimos el carácter a la nueva cadena

print("Cadena con solo vocales:", solo_vocales)