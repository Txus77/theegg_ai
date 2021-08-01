import sys
from operator import itemgetter



def indicesrep(i,cadenabuscar,buffer):
	"""funcion para obtener los indices de las repeticiones del caracter que señala el cursor
	 en la porcion de cadena que ya ha recorrido el cursor"""
	listaindices=[]#obtengo lista de indices donde se repite el caracter donde está situado el cursor
	for j in range(0,len(buffer)):#recorro la porcion de cadena ya recorrida por el cursor
					
		if cadenabuscar[i]==buffer[j]:
			listaindices.append(j)
			
	return listaindices

def coincidencias (i,indices, cadenabuscar, buffer):
	"""funcion que sirve para obtener todas las posibles coincidencias de la cadena que se inicia en el cursor,
	 en la porcion de la cadena ya recorrida por el cursor"""
	listacoincidencias="" #cadena con las cadenas repetidas en la porcion de cadena recorrida
	for m in indices:
		p=m 
		l=i
		
		listacoincidencias+="/" #simbolo utilizado como separador para que al tener una cadena con espacios estos queden dentro de la cadena y no se supriman. En caso de que este simbolo formara parte de la cadena habría que cambiar este separador
		while buffer[p]==cadenabuscar[l]: #ciclo indeterminado para buscar todas las porciones de cadena repetidas
			listacoincidencias+=buffer[p]
			p+=1
			l+=1
			if p > len (buffer)-1 or l > len (cadenabuscar)-1:
				break
				
	return listacoincidencias[1:] #se coge la cadena desde el segundo caracter porque se ha añadido "/" como primer caracter y si no se suprime da error de sobrepasar el rango de cadena


def procesadolista (i,listacoincidencias, listaindices):
		"""funcion donde se procesa la lista de indices y la cadena de porciones repetidas para obtener una
		tupla con la ubicación y la longitud de la repetición más larga obtenida en la porcion de cadena recorrida"""
		listacaract=listacoincidencias.split(sep="/") # variable para generar una lista de la cadena de coincidencias obetenidas. Si la cadena original contiene este simbolo hay que cambiarlo por otro que no este en la cadena
		combinada=dict(zip(listaindices, listacaract)) #diccionario donde la clave es el indice del primer caracter repetido y el valor las porciones de caracteres repetidas
		final=dict(sorted(combinada.items(),reverse=True))#se ordena el diccionerio en orden inverso para coger siempre la repticion más próxima al cursor
		coincidef=max(final.items(), key=itemgetter(1))#se coge la repetición con la cadena más larga y se genera una tupla con el primer valor que corresponde al indice de la cadena más larga y el segundo valor la cadena obtenida
		ubicacion=i-coincidef[0] #obtengo la ubicación tomando como referencia donde esta el cursor
		longcad=len(coincidef[1]) #obtengo la longitud de la cadena repetida

		return (ubicacion, longcad)


def compresion(cadena):
	"""funcion con la que se obtiene el diccionario que no es mas que la salida codificada 
	 de la cadena que queremos comprimir"""
	diccionario=[]
	i=0 #posicion inicial del cursor inicializado 
	while i < len (cadena):
		
		listamenor=cadena[0:i] #porcion de cadena que se va recorriendo
		busqueda=cadena[i:] #porcion de cadena a recorrer
		
		if cadena[i] in listamenor: #condicion que indica True si el caracter donde se encuentra el cursor está en la cadena recorrida
			
			if busqueda in listamenor: #condicion que comprueba si la parte de la cdena que queda por recorrer se encuentra en la cadena recorrida
					longcad=len(busqueda)#en este caso la longitud de la cadena repetida será igual a la parte de la cadena que queda por recorrer
					listaindices=indicesrep(0,busqueda,listamenor)
					listacoincidencias=coincidencias(0, listaindices, busqueda, listamenor)
					tuplas=procesadolista (i,listacoincidencias,listaindices)
					ubicacion=tuplas[0]#localización del primer caracter repetido contado desde el cursor hacia atrás
					fin="<eoc>"#se indica cuando la parte de la cadena que queda por recorrer coincide completamente con otra cadean que esta en la cadena recorrida
					tupla1=str(ubicacion)+","+str(longcad)+","+str(fin)+"-"
					diccionario.append(tupla1)
					i+=longcad+1 #se mueve el cursor la longitud de la cadena repetida mas el caracter sin repetir 
				
			else:			
				listaindices=indicesrep(i,cadena,listamenor)
				
				listacoincidencias=coincidencias(i,listaindices, cadena, listamenor)
				tuplas=procesadolista (i,listacoincidencias,listaindices)
				
				longcad=tuplas[1]#longitud cadena repetida
				ubicacion=tuplas[0]#localización del primer caracter repetido contado desde el cursor hacia atrás
				tupla1=str(ubicacion)+","+str(longcad)+","+str(cadena[i+longcad])+"-"
				diccionario.append(tupla1)
				i+=longcad+1
			
		else:#condicion que comprueba que el caracter no está en la cadena recorrida
				tupla=str(0)+","+str(0)+","+str(cadena[i])+"-"	
				diccionario.append(tupla)
				i+=1

	cadena_dict="".join(diccionario[:])#se comvierte la salida a una cadena para que ocupe menos memoria

	cadena_comprimida=cadena_dict[:-1]

	return cadena_comprimida[:]


def descompresion(cadena_comprimida):

	diccionario=cadena_comprimida.split(sep="-")#convierto la cadena resultante de la compresión a una lista 

	diccionariotupla=[]#cada lemento de la lista que es una cadena lo convierto en tuplas cuyos elementos son (ubicación, longitudcadenarepetida, caracter diferente)
	for l in range (len(diccionario)):
		tupladic=tuple(diccionario[l].split(sep=","))
		diccionariotupla.append(tupladic)
	
	descomprimido=""
	for c in range (len(diccionariotupla)):#recorre los elemntos de la tupla para localizar los caracteres que formaran la cadena descomprimida
		
		if int(diccionariotupla[c][0])==0:
			descomprimido+=diccionariotupla[c][2]
		else:
			j=len(descomprimido)-int(diccionariotupla[c][0])
			suma=j+int(diccionariotupla[c][1])
			descomprimido+=descomprimido[j:suma]+diccionariotupla[c][2]
		
	if descomprimido [-5:]=="<eoc>":
		descomprimido=descomprimido[:-5]

	return descomprimido

cadena = "abracadabraarrayabracadabraarray"

diccionario=compresion(cadena)

original_descomprimido=descompresion(diccionario)

print("la cadena original es: ", cadena)

print("la cadena tiene ", len (cadena), "caracteres")

print("la cadena descomprimida es: ", original_descomprimido)

print("el archivo comprimdo es: ",diccionario)

print("la cadena comprimida tiene", len(diccionario), "caracteres")

print ("el tamaño de la cadena original es: ", sys.getsizeof (cadena), "bytes")

print ("el tamaño del archivo comprimido es: ", sys.getsizeof (diccionario), "bytes")	