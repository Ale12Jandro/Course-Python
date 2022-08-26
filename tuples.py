#No se pueden cambiar esto quiere decir que son inmutables

tupla = ( 1, 2 , 3)
print(tupla)
print(type(tupla))

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'Octuber', 'November', 'December')
print(months)

#Nota: No sé puede considerar una sola tupla con un solo elemento tienen que ser más de dos. 
print("---------------------------")
print(months[5]) #Nos permite visualizar el elemento en esa posición de la tupla

#Ejemplo donde podemos usar las tuplas 

locations = {
    (35.12145, 39.65548):"Tokyo",
    (-89.45612, -47.8569):"New York"
}

print(locations)
print(type(locations))