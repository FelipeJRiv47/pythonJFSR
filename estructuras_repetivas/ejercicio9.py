# Defino las variables
totaledadHombres = 0
totaledadMujeres = 0
edadTotal = 0
cantidadHombres = 0
cantidadMujeres = 0
cantidadTotal = 0
# Número total de alumnos
numeroAlumnos = int(input("Ingrese el número total de alumnos: "))
# Se inicia el bucle
for i in range(numeroAlumnos):
    # Solicitar la edad y el género del alumno
    edad = int(input(f"Ingrese la edad del alumno {i + 1}: "))
    genero = input(f"Ingrese el género del alumno {i + 1} (M/F): ")
    edadTotal += edad
    edadTotal += 1
    if genero == 'M':
        totaledadHombres += edad
        cantidadHombres += 1
    elif genero == 'F':
        totaledadMujeres += edad
        cantidadMujeres += 1
        # Cálculo de promedios
if cantidadHombres > 0:
    promedio_hombres = totaledadHombres / cantidadHombres
else:
    promedio_hombres = 0
if cantidadMujeres > 0:
    promedio_mujeres = totaledadMujeres / cantidadMujeres
else:
    promedio_mujeres = 0
if cantidadTotal > 0:
    promedio_total = edadTotal / cantidadTotal
else:
    promedio_total = 0
# Imprimir resultados
print(f"Promedio de edad de los hombres: {promedio_hombres:.2f}")
print(f"Promedio de edad de las mujeres: {promedio_mujeres:.2f}")
print(f"Promedio de edad del grupo total: {promedio_total:.2f}")