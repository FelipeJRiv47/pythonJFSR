#lista de las boletas
descuentosBoletas = [
    {"color": "rojo", "descuento": 0.15},
    {"color": "verde", "descuento": 0.20}
]
#datos de la compra hechas por el usuario para la lista
totalCompra=float(input('total_compra: '))
#datos del color de la boleta para el descuento del usuario
colorDelaboleta=input("ingrese el color de la boleta (rojo, verde, otro color: )").strip().lower()
#defenir los valores de los colores para el descuento
if colorDelaboleta=='rojo': 
    porcentajeDeldescuento=0.15
    
elif colorDelaboleta=='verde':
    porcentajeDeldescuento=0.20
else:
    porcentajeDeldescuento=0.00
#la varibale para calcular el descuento
descuento=totalCompra*porcentajeDeldescuento
#la variable del total de la compra con del descuento
totalCondescuento=totalCompra-descuento
#imprimir los resultados
print(f"total de la compra  ${totalCompra:.2f}")
print(f"el color de la boleta: {colorDelaboleta.capitalize()}")
print(f"el valor del descuento ${descuento:.2f}")
print(f"el total con descuento es ${totalCondescuento:.2f}")