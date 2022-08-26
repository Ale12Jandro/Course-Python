myStr = "Hola mundo"

#print(dir(myStr)) --> nos permite visualizar lo que podemos hacer con  las cadenas

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hola', 'Adios')) #Remplaza el texto
print(myStr.count('o')) #Cuenta cuantas veces se repite el caracter o

print(myStr.startswith('Hello')) #Analiza si la primera palabra empieza con ese texto y regresa un valor Verdadero o Falso.

print(myStr.split()) #Lo que hace es separar el texto 
