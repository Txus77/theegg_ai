def comprobar(Cadena):
	for k in Cadena:
		if k!="A" and k!="G" and k!="T" and k!="C":
			return False
	return True

def intoducirdatos(dato):
	cadenamayusculas=dato.upper()
	while comprobar(cadenamayusculas)==False:
		print("Introduce una secuencia que unicamente tenga la combinación de una o más de las siguientes bases. adenina (abreviado A), citosina (C), guanina (G) y timina (T)")
		print("La secuencia debe ir sin espacios y permite introducir mayúsculas o minúsculas")
		dato=input("Introduce la primera secuencia de ADN a comparar: ")
		cadenamayusculas=dato.upper()
	return cadenamayusculas
	

def juntarcaracteres(lista):
	secuencias="".join(lista)
	caracteresunidos=secuencias.split()
	return caracteresunidos


def establecerlongcadenas(cadena1,cadena2):
	if len(cadena1)>len(cadena2):
		cadenamayor=cadena1
		cadenamenor=cadena2
	else:
		cadenamayor=cadena2
		cadenamenor=cadena1
	return cadenamayor, cadenamenor


cadena1=input("Introduce la primera secuencia de ADN a comparar: ")
cadena1mayusculas=intoducirdatos(cadena1)


cadena2=input("Introduce la segunda secuencia de ADN a comparar: ")
cadena2mayusculas=intoducirdatos(cadena2)


print ("El resultado se dará en mayúsculas")
print("En caso de varias secuencias de igual tamaño el resultado se dará representando cada una de las secuencias separadas con un espacio entre si")


listacadenasordlong= establecerlongcadenas(cadena1mayusculas, cadena2mayusculas)
cadenamayor=listacadenasordlong[0]
cadenamenor=listacadenasordlong[1]


lista=[]
for i in range(0, len(cadenamayor)):
	if cadenamayor[i] in cadenamenor:
		for j in range (0, len(cadenamenor)):
			if cadenamayor [i]==cadenamenor [j]:
				m=i
				l=j
				lista.append(" ")
				while cadenamayor[m]==cadenamenor[l]:
					lista.append(cadenamayor[m])
					m+=1
					l+=1
					if m > len(cadenamayor)-1 or l >len(cadenamenor)-1:
						lista.append(" ")
						break
			else:
				lista.append(" ")	
		lista.append(" ")
	else:
		lista.append(" ")

listasecuencias=juntarcaracteres(lista)

	
if len(listasecuencias)==0:
	print("no hay secuencias iguales")
else:
	mejorsecuencia=listasecuencias[0]
	for m in range (0, len(listasecuencias)):
	 	if len(listasecuencias [m])>len(mejorsecuencia):
	 		mejorsecuencia=listasecuencias[m]
	listamejorsec=[]
	for s in range (0, len(listasecuencias)):  
		if len(listasecuencias[s])==len(mejorsecuencia):
			listamejorsec.append(listasecuencias[s])
			mejoressec=" ".join(listamejorsec)
	print ("Las secuencias coincidentes de mayor tamaño son: ",mejoressec)

