# Programa para calcular el precio final de un producto con descuentos

precio = int(input("Ingrese el precio del producto: "))
tarjeta = input("¿Tiene tarjeta de fidelidad? (s/n): ").lower()

descuento = 0
try:
		
	if precio > 100000:
		descuento += 0.15
	elif 50000 <= precio <= 100000:
		descuento += 0.10
	elif 10000 <= precio <= 49999:
		descuento += 0.05

	if tarjeta == 's':
		descuento += 0.05

	precio_final = precio * (1 - descuento)

	print("El precio final después de descuentos es", precio_final)



	print("888888")                                
	print("8    8 eeeee  eeeee eeee e  eeeee eeeee")
	print("8e     8   8  8   8 8  8 8  8   8 8   ")
	print("88  ee 8eee8e 8eee8 8e   8e 8eee8 8eeee")
	print("88   8 88   8 88  8 88   88 88  8    88")
	print("88eee8 88   8 88  8 88e8 88 88  8 8ee88")
except ValueError:
	print("entrada invalida ")
