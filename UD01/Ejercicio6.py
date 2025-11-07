# Ejercicio6: Dibuja un ordinograma que dado el precio de un artículo y el precio de venta real nos
# muestre el porcentaje de descuento realizadoSolicita el precio original y el precio de venta

precio_original = float(input("Introduce el precio original del artículo: "))
precio_venta = float(input("Introduce el precio de venta real: "))

# Calcula el porcentaje de descuento
descuento = ((precio_original - precio_venta) / precio_original) * 100

# Muestra el resultado
print(f"El descuento aplicado es del {descuento:.2f}%")