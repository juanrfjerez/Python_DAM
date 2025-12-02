"""
Ejercicio 2: Estrella de ocho puntas
Enunciado:

Imprime una estrella de ocho puntas combinando líneas verticales, horizontales y diagonales 
con asteriscos en una matriz de tamaño impar n x n (ej. 9x9).

Figura para n=9:

*   *   *
 *  *  *
  * * *
*********
  * * *
 *  *  *
*   *   *
"""

n = int(input("Introduce un número impar para el tamaño de la estrella: "))

for i in range(n):
    linea = ""
    for j in range(n):
        if i == j:       
            linea += "*"
        elif i + j == n - 1:         
            linea += "*"
        elif i == n // 2: 
            linea += "*"
        elif j == n // 2:                 
            linea += "*"
        else:
            linea += " "
    print(linea)
