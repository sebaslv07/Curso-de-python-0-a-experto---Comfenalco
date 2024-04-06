# Pide al usuario que ingrese su edad y calcula el año de nacimiento, luego muéstralo en pantalla. (el año actual es 2024) 

edad = int(input("Ingresa tu edad: "))
anio_actual = 2024
anio_nacimiento = anio_actual - edad

print("Tu año de nacimiento es", anio_nacimiento)

# Solicita al usuario que ingrese su edad y verifica si es elegible para conducir un auto en su país (generalmente a partir de los 16 años). Imprime un mensaje que indique si es elegible o no. 

edad = int(input("Ingresa tu edad: "))

if edad >= 16:
    print("Eres elegible para conducir un auto")
else:
    print("No eres elegible para conducir un auto")

# del ejercicio anterior agregar una validación si la persona no está habilitada para conducir si es mayor de edad 85 años 

edad2 = int(input("Ingresa tu edad: "))

if edad2 >= 16:
    if edad2 <= 85:
        print("Eres elegible para conducir un auto")
    else:
        print("No eres elegible para conducir un auto debido a que tienes más de 85 años")
else:
    print("No eres elegible para conducir un auto")