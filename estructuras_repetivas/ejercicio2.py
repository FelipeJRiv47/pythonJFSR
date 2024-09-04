#Leer 10 numeros negativos a positivos
#Iniciando suma
sumaPositivos = 0
#leer 10 números negativos
for i in range (10):
    numero = float(input("Ingrese el numero negativo: "))
    if numero < 0:
        sumaPositivos += abs(numero)
# Imprimir la suma de los números que se van a convertir
print(f"La suma de los números convertidos a positivos es: {sumaPositivos}")