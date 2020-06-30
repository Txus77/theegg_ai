
Remolque= int(input("Introduce peso remolque:  "))
numVacas=int(input("Introduce numero de vacas a la venta:  "))

Pesos=[]
Produccion=[]

while numVacas>0:
 	
		peso=(int(input("Introduce peso vaca:  ")))

		if peso>Remolque:
			print("Introduzca un peso menor que el peso que soporta el remolque")
		
			continue
		Pesos.append (peso)


		Vol=(int(input("Introduce produccion vaca:  ")))

		
		Produccion.append (Vol)

		
	
		numVacas=numVacas-1



from itertools import  combinations



Listaordenada= sorted (list(zip(Produccion, Pesos)), reverse=True)


ListaPesosOrdenada=[]
ListaVolOrdenada=[]


for i in Listaordenada:
		ListaPesosOrdenada.append(i[1])
		ListaVolOrdenada.append(i[0])
	


pesosCombinados=sum([list(map(list, combinations(ListaPesosOrdenada, i))) for i in range(len(ListaPesosOrdenada) + 1)], [])

volCombinados=sum([list(map(list, combinations(ListaVolOrdenada, i))) for i in range(len(ListaVolOrdenada) + 1)], [])

ProduccionMax=0


for j in range(len(pesosCombinados)):
	
	

	if sum(pesosCombinados[j])>Remolque:
	 continue

	if sum(volCombinados[j])>ProduccionMax:
		ProduccionMax=sum(volCombinados[j])
print(ProduccionMax)