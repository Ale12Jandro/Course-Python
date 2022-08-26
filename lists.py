demo_list = [1, 'Hola', 1.34, False, [1, 34, 5]]

print(demo_list)

colors = ["red", "blue", "green", "yellow", "purple"]
#Podemos declarar listas a tráves de un constructor

numbers_list = ((1,2,3,4))
#print(numbers_list)

rango = list (range(1,10))
print(rango)

#print(dir(colors)) Saber el métodos que contiene las listas con "dir"
 
#colors.extend(['violet' , 'black']) Insertar valores a una lista 
#colors.insert(1, 'Violet') #Inserta valores después de Red tu eliges la posición
colors.insert(len(colors), 'black') #Agregar elementos al final de la lista de colores
print(colors)

#colors.pop() #Ruemueve el último elemento agregado en la lista

#Ordenar las listas
colors.sort() #Ordena la lista de manera alfabetica A-Z
print(colors)

colors.sort(reverse=True) #Ordena la lista de manera alfabetica pero de forma inverza Z-A
print(colors)

print(colors.index('green')) #Nos permite conocer la posición en la que se encuentra el color 