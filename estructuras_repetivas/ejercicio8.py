# Defino las variables
cal50 = 0
calificacion50 = 0
calificacion70 = 0
calificacion80 = 0
# se ejecuta el bucle
for i in range(23):
    # se solicita que ingrese una calificacion entre 1 a 100
    calificacion = int(input("Inserte la calificación del estudiante (entre 1 y 100): "))
# con esta funcion validamos que la calificacion este entre 1 y 100
    if calificacion >= 100 or calificacion <= 0:
        # si la calificacion no esta entre 1 y 100 imprimimos el siguiente mensaje hasta que ingresen una calificacion valida
        print("Inserte una calificación válida.")
        # pone la calificación en el rango correspondiente y suma uno al contador si esta en esta nota
    if calificacion < 50:
        cal50 += 1
    elif calificacion >= 50 or calificacion < 70:
        cal50 += 1
    elif calificacion >= 70 or calificacion < 80:
        calificacion70 += 1
    else:
        calificacion80 += 1
# Imprime el número total de estudiantes en cada rango de calificación
print(f"{cal50} Estudiantes obtuvieron una calificación menor a 50.")
print(f"{cal50} Estudiantes obtuvieron una calificación entre 50 y 70.")
print(f"{calificacion70} Estudiantes obtuvieron una calificación entre 70 y 80.")
print(f"{calificacion80} Estudiantes obtuvieron una calificación mayor a 80.")