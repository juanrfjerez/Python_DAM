"""
Figura de estrellas alternadas:
- Fila 0, 2, 4, ...: completa con símbolos
- Fila 1, 3, 5, ...: símbolos intercalados con espacios
- Sin última columna
"""

filas = 10         # total teórico
columnas = 20      # número exacto de columnas visibles
simbolo = "*"

# Imprimir hasta la penúltima fila
for i in range(filas - 1):
    fila = ""

    if i % 2 == 0:
        # Fila completa: símbolo en todas las columnas menos la última
        for j in range(columnas - 1):
            if j == columnas - 2:
                fila = fila + simbolo
            else:
                fila = fila + simbolo + " "
    else:
        # Fila intercalada: símbolo en pares
        for j in range(columnas - 1):
            if j % 2 == 0:
                if j == columnas - 2:
                    fila = fila + simbolo
                else:
                    fila = fila + simbolo + " "
            else:
                if j == columnas - 2:
                    fila = fila + " "
                else:
                    fila = fila + "  "

    print(fila)