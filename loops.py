#Realizar recorridos con for o while (bucles)

foods = ["apples", "bread", "cheese", "milk", "cherries"]

for food in foods:
    if food == "cheese":
        print("Tienes que comprar queso")
    print(food)

print("---------------------------")
#Imprimir un rango 

for number in range (1, 8):
    print(number)

print("---------------------------")

for letra in  "Hola":
    print(letra)
print("---------------------------")
#También podemos usar un bucle WHILE 

count = 4

while count <= 10:
    print(count)
    count = count + 1