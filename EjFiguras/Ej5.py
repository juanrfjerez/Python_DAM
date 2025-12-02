"""
Ejercicio 5: Cruz con borde punteado
Enunciado:

Imprime una cruz en una matriz de tamaño n x n con puntos en el borde, asteriscos en las líneas vertical y horizontal centrales, y espacios en el resto.

Figura para n=7:

. . . . . . .
. * . * . * .
. . * . * . .
* * * * * * *
. . * . * . .
. * . * . * .
. . . . . . .
"""

n = int(input("Introduce el tamaño de la matriz (n impar): "))

for i in range(n):
    fila = ""
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            fila += ". "
        elif i == n // 2 or j == n // 2:
            fila += "* "
        else:
            fila += "* " if (i % 2 == j % 2) else ". "
    print(fila)