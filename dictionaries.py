#Estos diccionarios nos permiten utilizarlas para tener claves y que estas tengan algún valor

from itertools import product


productos = {
    "Libro": "Cenicienta",
    "Cantidad": 3,
    "Precio": 175.50
}

print(productos)
print(type(productos))

#Ejemplo para utilizar los diccionarios

persona = {
    "Nombre": "Alejandro",
    "Edad": 23,
    "Peso": 62,
    "Altura": 168
}

print(persona)

print(persona.keys()) #Nos permite visualizar solamente las llaves 
print(persona.items()) #Nos permite visualizar los items 

#Se puede tener una lista con dos diccionarios 

product = [
    {"Celular": "Samsung A52", "Precio": 7599},
    {"Laptop": "Dell Inspiron 3500", "Precio": 19399}
]

print(product)