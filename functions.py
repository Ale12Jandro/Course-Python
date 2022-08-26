#Vamos a declarar funciones 

def hello():
    print("Hola mundo")

hello()

print("----------------------")

#Se puede asignar un elemento a la función creada

def hola(name):
    print("Hola " + name)

hola("Alejandro")

#Se puede hacer cualquier cantidad de cosas
def suma(n1, n2):
    return n1 + n2

print(suma(10, 23))
print(suma(45, 2))
print("----------------------")
#Tambien se pueden crear funciones con un LAMBDA y retornar valores

sum = lambda num1, num2: num1 + num2

print(sum(12, 13))
print(sum(3, 43))