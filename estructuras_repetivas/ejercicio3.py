#Variables

sumarCalificaciones = 0
maximaCalificaciones = 100
minimmaCalificaciones = 50

for i in range (5):

    calificacion = int(input("Ingrese la calificacion del alumno: "))
    sumarCalificaciones += calificacion
    if calificacion > maximaCalificaciones:
        maximaCalificaciones = calificacion
    if calificacion < minimmaCalificaciones:
        minimmaCalificaciones = calificacion

promedio = sumarCalificaciones / 5
#Imprimir resultados
print(f"El promedio de las calificaciones es: {promedio}")
print(f"La calificación más alta es: {maximaCalificaciones}")
print(f"La calificación más baja es: {minimmaCalificaciones}")