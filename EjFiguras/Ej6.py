"""
Ejercicio 6: Letra M mayúscula con asteriscos
Enunciado:

Imprime la letra M mayúscula usando asteriscos en una matriz cuadrada de tamaño impar n.
Las líneas de la M deben visualizarse usando asteriscos, con espacios en el resto.

Figura para n=7:

*     *
**   **
* * * *
*  *  *
*     *
*     *
*     *
"""

n = int(input("Introduce el tamaño de la matriz (n impar): "))

for i in range(n):
    fila = ""
    for j in range(n):
        if j == 0 or j == n - 1:
            fila += "*"
        elif i == j and i <= n // 2:
            fila += "*"
        elif i + j == n - 1 and i <= n // 2:
            fila += "*"
        else:
            fila += " "
    print(fila)