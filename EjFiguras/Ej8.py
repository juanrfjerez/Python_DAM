"""
Ejercicio 8: Rombo sólido
Enunciado:

Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos.

Figura para n=4:

   *
  ***
 *****
*******
 *****
  ***
   *
"""
n = int(input("Introduce la altura del rombo: "))

for i in range(1, n + 1):
    espacios = n - i
    estrellas = 2 * i - 1
    print(" " * espacios + "*" * estrellas)

for i in range(n - 1, 0, -1):
    espacios = n - i
    estrellas = 2 * i - 1
    print(" " * espacios + "*" * estrellas)