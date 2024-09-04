# Variables
cantidadHombres = 0
cantidadMujeres = 0
totalAltura = 0
cantidadAlturaMayor170 = 0
cantidadAlturaMenorIgual150 = 0
totalAlumnos = 0

# Bucle para ingresar datos de los alumnos
while True:
    # Solicitar datos del alumno
    sexo = input("Ingrese el sexo del alumno (H para hombre, M para mujer): ").upper()
    edad = int(input("Ingrese la edad del alumno: "))
    
    # Terminar el bucle si la edad es 0
    if edad == 0:
        break
    
    altura = float(input("Ingrese la altura del alumno en metros (por ejemplo, 1.75): "))
    
    # Actualizando contadores y acumuladores
    if sexo == 'H':
        cantidadHombres += 1
    elif sexo == 'M':
        cantidadMujeres += 1
    else:
        print("Sexo no reconocido. Debe ingresar 'H' para hombre o 'M' para mujer.")
        continue
    
    totalAltura += altura
    totalAlumnos += 1
    
    if altura > 1.70:
        cantidadAlturaMayor170 += 1
    if altura <= 1.50:
        cantidadAlturaMenorIgual150 += 1

# Calcular el promedio de altura
promedioAltura = totalAltura / totalAlumnos if totalAlumnos > 0 else 0

# Mostrar resultados
print(f"\nCantidad de hombres: {cantidadHombres}")
print(f"Cantidad de mujeres: {cantidadMujeres}")
print(f"Altura promedio: {promedioAltura:.2f} metros")
print(f"Cantidad de alumnos con altura mayor a 1.70 cm: {cantidadAlturaMayor170}")