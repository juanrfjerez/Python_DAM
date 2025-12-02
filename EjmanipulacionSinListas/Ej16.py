"""
Ejercicio 16:
Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación
(concatenar carácter a carácter con un ciclo usando .join()).
"""

# Pedir al usuario dos cadenas
cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

# Nueva cadena vacía
nueva_cadena = ""

# Concatenar carácter a carácter de la primera cadena
for i in range(len(cadena1)):
    nueva_cadena = "".join([nueva_cadena, cadena1[i]])

# Concatenar carácter a carácter de la segunda cadena
for i in range(len(cadena2)):
    nueva_cadena = "".join([nueva_cadena, cadena2[i]])

print("La nueva cadena concatenada es:", nueva_cadena)