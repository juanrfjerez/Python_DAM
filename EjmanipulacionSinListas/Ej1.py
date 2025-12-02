"""
Ejercicio 1:
Leer una cadena desde teclado y mostrarla carácter por carácter usando un ciclo for y el índice.
"""

# Leer una cadena desde teclado
cadena = input("Ingrese una cadena: ")

for i in range(len(cadena)):
    print("Índice:", i, "Carácter:", cadena[i])