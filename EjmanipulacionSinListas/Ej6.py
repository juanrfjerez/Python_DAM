"""
Ejercicio 6:
Extraer subcadenas usando slicing (rebanado de cadenas sin usar listas).
"""

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Pedir al usuario los índices de inicio y fin
inicio = int(input("Ingrese el índice de inicio: "))
fin = int(input("Ingrese el índice de fin: "))

# Extraer la subcadena directamente con slicing
subcadena = cadena[inicio:fin]

print("La subcadena extraída es:", subcadena)