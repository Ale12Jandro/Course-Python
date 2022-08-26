#Nos permite hacer condiciones con nuestras variables o elementos

from turtle import color


x = 10

if x < 30:
    print("X es menor que 30")

y = 10

if y > 2:
    print("Y es mayor que 2")

c = 5

if c == 5:
    print("C es identico a 5")

print("---------------------------------------------------------")
#Comparar dato por consola
Juan = input("Edad de Juan: ")
Edad = int(Juan)  #Convierte la edad en número entero

if Edad > 10:
    print("Juan es mayor que su hermano")
else:
    print("Juan es menor que su hermano")

 #Comparar valores con condicionales dentro de elif
print("----------------------------------------------------------")
Color = input("Inserta el color: ")

if Color == "Azul":
    print("El color es Azul")
elif Color == "Rojo":
    print("El color es Rojo")
else:
    print("El color es otro")


    #Comparar valores con if aninados

    name = "John"
    lastname = "Carter"

    if name == "John":
        if lastname == "Carter":
            print("You are John Carter")
        else:
            print("You are not John Carter")
