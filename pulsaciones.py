#las variables de obtoner los datos del usuario
nombre=input("escriba su nombre ")
sexo=input("masculinno o femenino ")
edad=int(input("cuantos años tienes "))
#defenir los valores de los datos de usuarios para calcular sus pulsaciones
if sexo == "masculino":
    numPulsaciones=(210-edad)/10
elif sexo == "femenino":
    numPulsaciones=(220-edad)/10
#impresion de los datos de usuarios
print("el nombre es: {0} sexo es {1} su edad {2} años y el numero de sus pulsaciones son :{3}".format(nombre.capitalize(),sexo.capitalize(), edad,num_pulsaciones))