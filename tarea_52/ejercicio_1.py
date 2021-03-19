def introducir_numero():
	"""funcion que sirve para controlar que los datos que se introducen son correctos, es decir,
	si se introduce un dato que no sea un número entero pide que se introduzca otra vez el dato"""
	
	while True:
		try:
			num = int(input ("Ingrese un número entero ",))
			return num
			
		except:
			print("El dato introducido no es un número entero. Vuelva a intentarlo")


print("Introduzca un 0 para que el programa no le pida introducir más datos")

def sumatorio(lista):
	"""funciónde determina el sumatorio de una lista de números"""
	suma=0
	for i in range(len(lista)):
		suma+=lista[i]
	return suma

num=introducir_numero()

# Resolución primra parte del ejercicio
lista = []

while num != 0:
	lista.append (num)
	num=introducir_numero()

print (lista)	


# Resolución segunda parte del ejercicio

print("El próximo número que introduzca será eliminado")

num2 = introducir_numero()

if num2 in lista:
	lista.remove (num2) #se elimina la primra ocurrencia del valor indicado
else:
	print ("El número no esta en la lista")

print(lista)

print ("El sumatorio es ", sumatorio(lista))

# Resolución tercera parte del ejercicio

print("El próximo número que introduzca acotará la lista por arriba con el fin de generar una nueva \nlista con los elementos de la nueva lista y el número de ocurrencias en la misma")

# Resolución cuarta parte del ejercicio. 

num3 = introducir_numero()

lista2 =[x for x in lista if x < num3] #lista con los elementos menores de un número determinado

for i in lista2:
	print (i)
# Resolución quinta parte del ejercicio. 
#A partir de aquí se indican diferentes formas de resolver la última parte del ejercicio. Únicamente se deja una sin comentar

# Primera:Creando un diccionario en el que la clave sea cada elemento de la lista y el valor el número de repeticiones
result={}

for i in lista2:
	if i not in result.keys():
		result[i] = 1
	else:
		result[i] += 1

lista_definitiva = result.items()

print (lista_definitiva)

#Segunda: Creando una lista con valores únicos y luego toamndo esa lista como referencia, crear una nueva lista de tuplas 
#con los valores, como elemento inicial de cada tupla, y el número de veces que aparece repetido como segundo valor de cada tupla

"""lista_valores1 = []
for i in lista2:
	print (i)
	if i not in lista_valores1:
		lista_valores1.append(i)

lista3 =[]
for j in lista_valores1:
	a = (j, lista2.count(j))
	lista3.append(a)

print(lista3)"""

#Tercera: igual que en el caso anterior pero la lista de valores que no se repiten la creo con la funcion set () que me da un conjunto con los valores que forman la lista

"""lista_valores = sorted(list(set(lista2)))
lista3=[]
for j in lista_valores:
	a = (j, lista2.count(j))
	lista3.append(a)

print(lista3)"""

