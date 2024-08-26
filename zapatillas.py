#las variables de obtoner los datos del usuario
cantidadDeZapatillas=int(input("ingrese la cantidad de zapatillas"))
valordeCompras=float(input("ingrese valor de compras"))
valordelDescuento=float(input("ingrese valor de descuento de compras"))

#calculando el descuento   
descuento = (valordelDescuento * cantidadDeZapatillas) / 100
# Convertir el valor a decimal
descuentoDecimal = valordelDescuento / 100

#calculando el valor final
valorFinal = valordeCompras - descuento

#mostrando el resultado

print("El valor final de la compra es:", valorFinal)
print("La cantidad de zapatillas es:", cantidadDeZapatillas)
print("El valor de compras es:", valordeCompras)
print("El valor de descuento es:", valordelDescuento)