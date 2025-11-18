altura = int(input("Introduce la altura del triángulo: "))

for i in range(1, altura + 1):
    if i == 1:
        print("*")
    elif i == 2:
        print("**")
    elif i == altura:
        print("*" * altura)
    else:
        print("*" + " " * (i - 2) + "*")