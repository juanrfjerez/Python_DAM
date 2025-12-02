"""
Ejercicio 8:
Convertir todas las letras a mayúsculas usando ciclos y un diccionario de conversión (sin usar upper()).
"""

# Diccionario de conversión de minúsculas a mayúsculas
conversion_mayus = {
    'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J',
    'k':'K','l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R','s':'S','t':'T',
    'u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'
}

# Pedir al usuario una cadena
cadena = input("Ingrese una cadena: ")

# Construir la nueva cadena en MAYÚSCULAS
mayusculas = ""
for i in range(len(cadena)):
    caracter = cadena[i]
    if caracter in conversion_mayus:
        mayusculas = mayusculas + conversion_mayus[caracter]
    else:
        mayusculas = mayusculas + caracter

print("Cadena en MAYÚSCULAS:", mayusculas)