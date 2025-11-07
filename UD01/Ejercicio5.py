# Ejercicio5: Dibuja un ordinograma que toma como dato de entrada un número que corresponde a la
# longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
# de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
# círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la
# esfera que corresponde con dicho radio.

import math

# Entrada del radio
radio = float(input("Introduce la longitud del radio: "))

# Cálculo del diámetro
diametro = 2 * radio

# Longitud de la circunferencia
longitud_circunferencia = math.pi * diametro

# Área del círculo
area_circulo = math.pi * radio ** 2

# Volumen de la esfera
volumen_esfera = (4/3) * math.pi * radio ** 3

# Resultados
print(f"Diámetro: {diametro}")
print(f"Longitud de la circunferencia: {longitud_circunferencia}")
print(f"Área del círculo: {area_circulo}")
print(f"Volumen de la esfera: {volumen_esfera}")