#Podemos crear modulos
#Podemos descargarlos desde Internet
#Utilizar las librerias que PYTHON maneja 

import mymath
import datetime
from colorama import Fore, Style, init
init(convert=True)

#Utilizando las librerias en este apartado....
print("---------------------------------------")

print(datetime.date.today())

print(datetime.timedelta(minutes=75))

mymath.suma(8, 9)
mymath.restar(4, 2)

print(Fore.BLUE + "Hola Mundo")