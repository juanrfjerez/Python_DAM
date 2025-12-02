"""
Ejercicio 3: Pirámide con huecos internos (estructura tipo "reja")
Enunciado:

Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.

Figura para n=6:

     *
    * *
   *   *
  * * * *
 *       *
***********
"""

n = int(input("Introduce la altura de la pirámide: "))

for i in range(1, n + 1):
    espacios = n - i
    if i == 1:
        print(" " * espacios + "*")
    elif i == n:
        print("*" * (2 * n - 1))
    else:
        if i % 2 == 0:  
            linea = ""
            ancho = 2 * i - 1
            for j in range(ancho):
                if j % 2 == 0:
                    linea += "*"
                else:
                    linea += " "
            print(" " * espacios + linea)
        else:  
            print(" " * espacios + "*" + " " * (2 * i - 3) + "*")
