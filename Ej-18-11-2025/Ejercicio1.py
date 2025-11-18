altura = int(input("Introduce la altura de la pirámide: "))

for i in range(1, altura + 1):
    espacios = altura - i
    if i == 1:
        print(" " * espacios + "*")
    else:
        print(" " * espacios + "*" + " " * (i - 2) + "*")

for i in range(altura - 1, 0, -1):
    espacios = altura - i
    if i == 1:
        print(" " * espacios + "*")
    else:
        print(" " * espacios + "*" + " " * (i - 2) + "*")
        