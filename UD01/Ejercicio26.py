# Ejercicio26: Dibuja un ordinograma que calcula el salario neto semanal de un trabajador en función del
# número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
# Las primeras 35 horas se pagan a tarifa normal.
# Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
# Las tasas de impuesto son:
# Los primeros 500€ son libres de impuestos.
# Los siguientes 400€ tiene un 25% de impuesto.
# Los restantes un 45% de impuesto.

# Solicita las horas trabajadas y la tarifa por hora
horas_trabajadas = float(input("Introduce el número de horas trabajadas esta semana: "))
tarifa_normal = float(input("Introduce la tarifa por hora (€): "))

# Calcula el salario bruto
if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * tarifa_normal
else:
    horas_extra = horas_trabajadas - 35
    salario_bruto = (35 * tarifa_normal) + (horas_extra * tarifa_normal * 1.5)

# Calcula los impuestos según tramos
if salario_bruto <= 500:
    impuestos = 0
elif salario_bruto <= 900:
    impuestos = (salario_bruto - 500) * 0.25
else:
    impuestos = (400 * 0.25) + ((salario_bruto - 900) * 0.45)

# Calcula el salario neto
salario_neto = salario_bruto - impuestos

# Muestra los resultados
print(f"Salario bruto: {salario_bruto:.2f} €")
print(f"Impuestos: {impuestos:.2f} €")
print(f"Salario neto: {salario_neto:.2f} €")