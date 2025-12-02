"""
Enunciado:

Imprime un diamante hueco de altura total 2n - 1, 
centrado con asteriscos, donde solo se imprimen los bordes y el centro.

Figura para n=5:

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""
altura = int(input("Introduce la altura del rombo: "))

for i in range (1, altura + 1):
    espacios = altura - i
    if i == 1:
        print (" " * espacios + "*")
    else:
        print(" " * espacios + "*" + " " * (2*i - 3) + "*")

for i in range (altura -1,0, -1):
    espacios = altura - i
    if i == 1:
        print (" " * espacios + "*")
    else:
        print (" " * espacios + "*" + " " * (2*i - 3) + "*")