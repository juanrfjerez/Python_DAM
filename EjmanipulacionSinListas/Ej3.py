"""
Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.
"""

cadena = input("Ingrese una cadena: ")
caracter_a_contar = input("Ingrese el carácter a contar: ")
contador = 0

for i in range(len(cadena)):
    if cadena[i] == caracter_a_contar:
        contador = contador + 1
print("El carácter ",caracter_a_contar," aparece ", contador," veces en la cadena.")