nombre = input("Nombre del vendedor: ")
venta = input("Digite el total de sus ventas en pesos: ")
totalVenta = float(venta);
comision = round(totalVenta * 0.13, 2);
print(f"El vendedor {nombre}, tuvo un total de ventas equivalentes a ${totalVenta}")
print(f"Por lo tanto le corresponde una comisión de ${comision}")