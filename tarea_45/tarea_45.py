from ordenamiento import *

lista_num=[3, 56, 21, 33, 874, 123, 66, 1000,23, 45, 65, 56] 

def ordenar_quicksort (lista):
	if len (lista) < 2:
		return lista

	else:
		pivote = lista [0] 
		menores = [i for i in lista [1:] if i <= pivote]
		mayores = [j for j in lista [1:] if j > pivote]

		return ordenar_quicksort(menores) + [pivote] + ordenar_quicksort(mayores)

#Número a buscar

Num = 1000
#busqueda lineal
#i es el contador de iteracciones
for i in range(len(lista_num)):
	if lista_num[i] == Num:
		print ("número encontrado")
		break

print ("El algoritmo secuencial ha empleado,", i+1, "operaciones")	

#busqueda binaria

lista_ordenada = ordenar_quicksort(lista_num)
print(lista_ordenada)

def busqueda_binaria(lista, elemento):
	i=0 #inicializo el contador de iteracciones
	inicio = 0
	final = len(lista)-1
	
	while inicio <= final:	
		medio = (inicio+final)//2
		if lista [medio] == elemento:
			return print("el número ", lista[medio], " ha sido encontrado. Se han empleado", i,"operaciones")
		elif lista [medio] < elemento:
			inicio = medio+1
			print("es incio", inicio)
		elif lista [medio] > elemento:
			final = (medio)-1
			print("es final", final)
		i+=1
		print(i)
						
	return print("No coincide, el número de operaciones en busqueda binaria ha sido de: ", i)

busqueda_binaria (lista_ordenada,Num)
