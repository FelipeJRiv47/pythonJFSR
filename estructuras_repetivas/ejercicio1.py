#Leer 20 numeros
positivos=0
negativos=0
neutros=0
#Lee 20 numeros
for i in range(20):
        numero = float(input(f"Ingrese el numero {i + 1}: "))
        if numero > 0:
                positivos += 1
        elif numero < 0:
                negativos += 1
        else:
                neutros += 1
print(f" cantidad de numeros Positivos: {positivos}")
print(f"cantidad de numeros Negativos: {negativos}")
print(f"cantidad de numerosNeutros: {neutros}")
