#Es una colección de datos de manera desordenada que no tiene un índice 

colors = {'Red', 'Green', 'Blue'}
print(colors)
print(type(colors))

print('Blue' in colors) #Verifica si el color está dentro del SET nos devuelve un valor boleano 
colors.add('Violet') #Agrega un elemento al SET 
print(colors)

#Limpiar los datos de un SET con clear()
#colors.clear()