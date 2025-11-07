# Ejercicio8: Dibuja un ordinograma de un programa que pide la edad por teclado y nos muestra el
# mensaje de “Eres mayor de edad”, si y solamente si lo somos.

# Solicita la edad
edad = int(input("Introduce tu edad: "))

# Verifica si es mayor de edad
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")