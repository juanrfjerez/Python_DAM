"""
Ejercicio 4: Cuadrado con diagonales y borde relleno
Enunciado:

Imprime un cuadrado de lado n con bordes de asteriscos y las dos diagonales marcadas, dejando espacios en el resto.

Figura para n=7:

*******
* *   *
*  *  *
*   * *
*  *  *
* *   *
*******
"""

n = int(input("Introduce el tamaño del cuadrado: "))

for i in range(n):
    fila = ""
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            fila += "*"
        else:
            centro = n // 2
            if i <= centro:          
                pos_flecha = i
            else:                     
                pos_flecha = n - i - 1

            if j == pos_flecha:
                fila += "*"
            else:
                fila += " "
    print(fila)