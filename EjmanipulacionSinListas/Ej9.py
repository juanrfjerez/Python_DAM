"""
Ejercicio 9:
Leer una cadena y contar cuántas vocales contiene.
"""
# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Contador de vocales
contador = 0

# Recorrer la cadena carácter por carácter
for i in range (len(cadena)):
    if cadena[i].lower() in 'aeiou':
        contador = contador + 1
        
print("La cadena contiene", contador, "vocales.")
