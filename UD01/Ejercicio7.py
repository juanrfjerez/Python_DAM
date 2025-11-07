# Ejercicio7: Dibuja un ordinograma que lea un valor correspondiente a una distancia en millas marinas
# y escriba la distancia en metros. Sabiendo que una milla marina equivale a 1.852 metros.

METROS_POR_MILLA_MARINA = 1852

# Solicita la distancia en millas marinas
millas = float(input("Introduce la distancia en millas marinas: "))

# Convierte a metros
metros = millas * METROS_POR_MILLA_MARINA

# Muestra el resultado
print(f"{millas} millas marinas equivalen a {metros:.2f} metros")