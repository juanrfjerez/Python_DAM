"""
Ejercicio 9: Cuadrado con borde, diagonales y cuadro interno hueco
Enunciado:

Imprime un cuadrado de lado n con borde y diagonales en asteriscos, y un cuadro hueco centrado dentro.

Figura para n=9:

*********
* *   * *
*  * *  *
*   *   *
*       *
*   *   *
*  * *  *
* *   * *
*********
"""
n = int(input("Introduce el tamaño del cuadrado (n impar): "))

for i in range(n):
    fila = ""
    for j in range(n):
        if i == 0 or i == n - 1:
            fila += "*"
        elif i == n // 2:
            if j == 0 or j == n - 1:
                fila += "*"
            else:
                fila += " "
        elif i == j or i + j == n - 1:
            fila += "*"
        elif j == 0 or j == n - 1:
            fila += "*"
        else:
            fila += " "
    print(fila)