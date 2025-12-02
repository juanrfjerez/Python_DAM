"""
Ejercicio 14:
Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.
"""

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Contador de caracteres numéricos
contador = 0

# Recorrer la cadena carácter por carácter
for i in range(len(cadena)):
    caracter = cadena[i]
    if caracter in "0123456789":
        contador = contador + 1

# Mostrar el resultado
print("La cadena contiene", contador, "carácter(es) numérico(s).")