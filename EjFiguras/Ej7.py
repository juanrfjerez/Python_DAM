"""
Ejercicio 7: Triángulo invertido con borde y relleno alternado
Enunciado:

Imprime un triángulo invertido de altura n con asteriscos en el borde, y líneas internas de relleno alternadas entre espacios y asteriscos.

Figura para n=6:

******
* * * *
*     *
* * * *
*     *
******
"""

n = int(input("Introduce la altura del triángulo invertido: "))

for i in range(n):
    if i == 0 or i == n - 1:         
        print("*" * n)
    else:
        if i % 2 == 1:               
            linea = "*"
            for j in range(1, n-1):
                if j % 2 == 1:
                    linea += " "
                else:
                    linea += "*"
            linea += "*"
            print(linea)
        else:                         
            print("*" + " " * (n-2) + "*")
