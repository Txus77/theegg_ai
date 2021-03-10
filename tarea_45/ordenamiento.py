"""algoritmo Quitsort. En este algoritmo se realiza la ordenación aplicando recursión. El caso base se establece como una lista de 0 o 1 elemento que ya está ordenada
En listas mayores de un elemento se escoje un pivote y se establece los valores superiores e inferiores creando 2 sublistas, una de valores superiores y otra inferiores
se aplica tantas veces como sea necesario hasta llegar al caso base. El rendimeinto de este algoritmo depende del pivote que se coja.Este algoritmo es O(n2) para el peor 
caso de tener una lista ya ordenada y coger como pivote siempre el primer elemento. En el mejor caso su rendimiento es O(log n) que es cuando en una lista ordenada se coge 
como pivote siempre el elemento que está en mitad de la listaEl caso promedio será O (n logn) ya que en cada ivel de la pila de llamadas siempre hay que tocar todos los 
elementos para ordenarlo. El número de niveles e la pila de llamadas dependerá del pivote escogido y oscila, como ya se ha indicado, entre n y log n"""
def ordenar_quicksort (lista):
	if len (lista) < 2:
		return lista

	else:
		pivote = lista [0] 
		menores = [i for i in lista [1:] if i <= pivote]
		mayores = [j for j in lista [1:] if j > pivote]

		return ordenar_quicksort(menores) + [pivote] + ordenar_quicksort(mayores)


"""ordenar por selección lo componen 2 funciones: la primera sirve para hallar el índice el menor valor de la lista. 
En la segunda se establece un ciclo for para que realice tantas iteraciones como elementos tiene la lista y en cada iteracción 
a la lista ordenada el menor valor de la lista. Observese que en cada iteracción extrae el elemneto añadido con la función pop. 
La eficiencia de este algoritmo es O(n2)"""

def menor(lista):
	menor = lista[0]
	menor_indice = 0
	for i in range (1, len(lista)):
		if menor > lista [i]:
			menor = lista [i]
			menor_indice = i 
	return menor_indice


def ordenar_seleccion (lista):
	lista_ordenada = []
	for i in range (len(lista)):
		indice_menor = menor(lista)
		lista_ordenada.append(lista.pop(indice_menor))#tener en cuenta que al ser las listas objetos mutables si la modficamos en el ambito de la función lo mismo ocurre fuera. En este caso al aplicar el metodo pop estamos vaciando la lista 
	return lista_ordenada							 #de la variable a por lo que tras aplicar esta función a será una lista vacia
	

#A continuación otra forma de ordenar por selección

def mayor (lista):
	mayor = 0
	for i in lista:
		if i > mayor:
			mayor = i
	return mayor

def ordenar_selc_mayor_menor (lista1):
	listaord = []
	for i in range (len(lista1)):
		mayor1 = mayor(lista1)
		listaord.append (mayor1)
		lista1.remove(mayor1)
		
	return listaord [::-1]



"""ordenar por mergesort: Se ordena an 2 funciones: la primera sirve para ordenar los elementos de 2 listas entre ellos y que el resultado salga en una sola lista. En la segunda función uso recursividad
Divido la lista en mitades hasta que quedan los elementos individuales (caso base). Luego se va aplicando la primera función a esas mitades desde las de menos elementoa a las de más elementos de forma
que vamos uniedno las mitades ordenándolas hasta tener una única lista con elemntos ordenados. El rendimiento es O (n logn) en todos los casos ya que el número de niveles de la pila de llamadas es log n
aunque en cada nivel siempre haya que tocar todos los elementos para ordenarlos."""


def merge(lista1, lista2):
	"""ordena elementos de 2 listas entre ellos de menor a mayor y el resultado el una lista con los elementos de las 2 listas ordenados"""
	i = 0
	j = 0
	lista_resultado = []
 
	while i < len(lista1) and j < len(lista2):

	 	if lista1[i]  < lista2 [j]:
	 		lista_resultado.append(lista1[i])
	 		i+=1
	 	else:
	 		lista_resultado.append(lista2[j])
	 		j+=1

	lista_resultado += lista1 [i:]
	lista_resultado += lista2 [j:]

	return lista_resultado

def mergesort(lista):
	"""divide una lista en mitades hasta llegar a una lista de 1 elemento. Retorna una lista con los elementos ordenados resultado de ir aplicando a cada par de sublistas que se generan el metodo merge"""
	if len (lista) <2:
		return lista
	else:
		indice_medio = len(lista)//2
		lista_menor = mergesort(lista[:indice_medio])
		lista_mayor = mergesort(lista[indice_medio:])
		return merge (lista_menor, lista_mayor)


if __name__ == "__main__":
	lista= [3,5,78,23,454,6778,466,33]
	print(ordenar_seleccion(lista))

