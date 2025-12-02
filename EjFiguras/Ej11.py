"""
Tablero alternado con bloques 3x3:
- Casillas vacías: espacios
- Casillas activas: bloque 3x3 de asteriscos
- Alternancia tipo ajedrez
"""

bloques = 8          # número de casillas por fila
tamaño = 3           # cada casilla es de 3x3
simbolo = "*"
espacio = " "

for fila in range(bloques):
    for subfila in range(tamaño):
        linea = ""
        for columna in range(bloques):
            if (fila + columna) % 2 == 0:
                linea += espacio * tamaño
            else:
                linea += simbolo * tamaño
        print(linea)