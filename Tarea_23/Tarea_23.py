
TextoOriginal=input("introduce el mensaje a cifrar:  ")
def PrevCodMens (texto):#primera parte  establezco una funcion para preparar el mensaje para ser codificado ya que me servirá también para establecer el numero de cracteres del mismo para generar la clave
		
	 #El parametro que introduzco será el mensaje a cifrar
	mensMinus=texto.lower() #lo paso a minusculas
	mensajesinesp=[]
	for i in mensMinus:#Elimino los espacios en blanco
		if i==" ":
			continue
		mensajesinesp.append (i)
	l=[]
	for i in range (0,len(mensajesinesp),5):#Agrupo los caracteres de 5 en 5
		l.append(mensajesinesp[i:i+5])
	Ultlista=(l[(len(l)-1)])       #esta variable es el último elemento de la lista que es el único que puede no tener 5 caracteres
	
	if len(Ultlista)!=5: #Si el último elemnto no tiene 5 caracteres lo completo con x hasta que tenga 5 caracteres
		resta=5-(len(Ultlista))
		for m in range(resta):
			Ultlista.append("x")
	
	ls1=[]
	for x in range(len(l)):   #constituyo una lista con todos los elementos de 5 caracteres
		ls="".join(l[x])#funcion join me permite coger los elementos de una lista y ponerlos consecutivamente como una cadena
		ls1.append(ls)
		ls2="".join(ls1)#de la lista anterior formo una cadena con todos los caracteres seguidos sin espacios 
	return (ls2)
MensPrep=PrevCodMens(TextoOriginal)

def solitario():
	
	
	cadena=len(MensPrep) #Variable que me da el número de caracteres del mensaje a cifrar
	
	#A partir de aqui se procede con el metodo del solitario para hallar la clave que luego se utilizará para cifrar y descifrar el mensaje
	Treboles=["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12", "T13"]
	Diamantes=["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13"]
	Corazones=["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13"]
	Picas=["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11", "P12", "P13"]
	Comodines=["A", "B"]
	Baraja=Treboles+Diamantes+Corazones+Picas+Comodines
	ListaNum=[]
	for i in range(1,53):
		ListaNum.append(i)
	listanumCom=ListaNum+Comodines
	BarajaNum=dict(zip(Baraja, listanumCom)) #Diccionario que tiene como clave cada una de las cartas y como valor el número que les corresponde empezando desde el 1 hasta el 52. Los comodines no tienen valor numérico
	
	ValorBaraja=BarajaNum.values()
	ValorBaraja1=[]
	for i in ValorBaraja:
		ValorBaraja1.append(i)
	
	import random
	Barajeada=random.sample(ValorBaraja1,54) #esta función se utiliza para barajear las cartas cada vez que queramos cifrar un mensaje de forma que para cada mensaje haya una clave diferente
	
	m=Barajeada#estado inicial de la baraja
	print ("Esta es la posicion inical de la baraja y, por tanto, la clave: ", Barajeada)	
	k=0
	RitraNum=[] #lista de números que serán la clave resultante después de aplicar el  solitario
	while k<cadena: #Bucle para generar un número por cada caracter del mensaje
		A="A"
		B="B"
		
		
		OrdenA=m.index(A) #establezco la posición del comodin A
		
		OrdenB=m.index(B)#establezco la posición del comodin B
		
		#primero contemplo los casos excepcionales que se originan como resultado de considerar la baraja como un ciclo, es decir, que cuando los comodines están al final al moverlos 1 o 2 posiciones pasan al principio de la baraja
		if OrdenA==53: #el primer caso excepcional si el comdin A está en la última posición tiene qye pasar a ser la segunda carta de la baraja
			m.remove("A")
			m.insert(1, A)
			if OrdenB>51:#dentro del caso dado puede suceder que el comodin B este en la  posición anterior. Entonces al mover el comodin A a la segunda posición queda el B en la última por lo que al moverlo 2 posiciones tendrá que ir como tercera carta
				m.remove("B")
				m.insert(2, B)
			
				
		elif OrdenB>51:#segundo caso que el comodin B este la última o la penultima carta
			if OrdenA==OrdenB-1:#variante dentro de la anterior caso con el comodin A delante. Al mover el comodin A el comodin B se desplaza una posicion hacia atrás
				m.remove("A")
				m.insert(OrdenA+1, A)
				if m.index(B)>51: #opcion si el comodin B queda en la última o penultima posición tras mover el A
					m.remove("B")
					m.insert(53-(OrdenB-1), B)
					
				else:#opcion si el comodin B queda en la fuera de las 2 ultimas posiciones, es decir, en la tercera posición si se empieza a contar desde la última carta
					m.remove("B")
					m.insert(53,B)
			else:#variante donde el comodin A no está entre las 3 última cartas
				m.remove("B")
				m.insert(OrdenB-51, B)
			

		elif OrdenA==OrdenB-1: #variante cundo el comodin A está delante del B en cualquier lugar de la baraja
			m.pop(OrdenA)
			m.insert((OrdenA+1), A)
			m.insert((OrdenB+2), B)
			m.pop(OrdenB-1)
		
			
		else: #cualquier otro caso fuera de los casos excepcionales
			m.pop(OrdenA)
			m.insert((OrdenA+1), A)
			m.insert((OrdenB+3), B)
			m.pop(OrdenB)
		#A partir de este punto teniendo en  cuenta donde han quedado los comodines A y B tras moverlos y se tienen en cuenta todas las posibilidades
		OrdenewA=m.index(A)#establezco la nueva posición del comodin A
		OrdenewB=m.index(B)#establezco la nueva posición del comodin B
		
		if OrdenewA<OrdenewB:#caso en el que el comodin A ha quedado delante del B
			#Se realizan los movimientos que se indican en el algoritmo del solitario
			sl=m[:(m.index(A))] #cojo la porcion de baraja desde el inicio hasta el comodin A
			g=m[(m.index(A)):(m.index(B)+1)] #parte de la baraja entre los dos comodines
			sl2=m[(m.index(B)+1):]#cojo la porcion de baraja desde el comodin B hasta el final
			
			Barajeada1=sl2+g+sl#nueva baraja cambiando el orden, es decir, poniendo al final la porcion de baraja hasta el comodin A y al principio la porcion de baraja desde el comodin B
			
			L=Barajeada1[53]#Establezco el valor de la última carta
			
			if L==A or L==B:#En caso de que sea un comodin el valor es 53 y la baraja queda como está
				L=53
				m=Barajeada1
					

			else:#en caso de no ser un comodin la última carta se cuenta el valor obtenido desde la primera carta 
				listapaso4=[]#lista obtenida de sacar las cartas obtenidas del anterior conteo
				for i in Barajeada1 [0:L]:
					listapaso4.append(i)
				
				
				Barajeada1[0:L]=[]
				m=Barajeada1[0:(53-L)]+listapaso4+[Barajeada1.pop(Barajeada1.index(L))]#nuvea posicion de la baraja tras añadir la porcion anterior al final conservando la última carta
				

			if A==m[0] or B==m[0]:#si la primera carta resultante es un comodin se cuenta 53
					
					numero=m[53]
					if numero==A or numero==B: #si la carta obtenida tras el conteo es un comodin se vuelve a empezar el bucle sin variar el orden de las cartas y sin que cuente el ciclo
						continue
					else:#se contemplan las diferentes posibilidades si la carta obtenida tras el conteo no es un comodin y se añaden a la lista de la clave
						if numero >26 and numero<40:
							clave1=numero-13
							
							RitraNum.append(clave1)
					
						elif numero>39 and numero<53:
							clave2=numero-26
							
							RitraNum.append(clave2)
					
						else:
							
							RitraNum.append(numero)
			else:#si la primera carta resultante no es un comodin  se cuenta desde empezando en la carta con posición 1 y se tienen en cunta las diferentes posiblidades para incluir el número resultante en la lista de la clave
			
				numero=m[m[0]]
				
				if numero==A or numero==B:
							continue
				else:
					if numero >26 and numero<40:
						clave1=numero-13
						
						RitraNum.append(clave1)
					
					elif numero>39 and numero<53:
						clave2=numero-26
						
						RitraNum.append(clave2)
						
					else:
					
						RitraNum.append(numero)
			


		else:#caso en el que el comodin B ha quedado delante del A. Se procede de forma analoga a lo anterior cambiando A por B
			sl=m[:(m.index(B))]
			g=m[(m.index(B)):(m.index(A)+1)]
			sl2=m[(m.index(A)+1):]
			Barajeada1=sl2+g+sl
			
			L=Barajeada1[53]
			
			if L==A or L==B:
				L=53
				m=Barajeada1
				
			else:
				listapaso4=[]
				for i in Barajeada1 [0:L]:
					listapaso4.append(i)
				
				Barajeada1[0:L]=[]
				m=Barajeada1[0:(53-L)]+listapaso4+[Barajeada1.pop(Barajeada1.index(L))]
				

			if A==m[0] or B==m[0]:
					
					numero=m[53]
					if numero==A or numero==B:
						continue
					else:
						if numero >26 and numero<40:
							clave1=numero-13
							
							RitraNum.append(clave1)
					
						elif numero>39 and numero<53:
							clave2=numero-26
							
							RitraNum.append(clave2)
					
						else:
							
							RitraNum.append(numero)
			else:
				numero=m[m[0]]
				if numero==A or numero==B:
							continue
				else:
					if numero >26 and numero<40:
						clave1=numero-26
						
						RitraNum.append(clave1)
					
					elif numero>39 and numero<53:
						clave2=numero-39
						
						RitraNum.append(clave2)
					
					else:
						
						RitraNum.append(numero)

		k=k+1
	return (RitraNum)

listaUnica=solitario()#lista de números generada con el solitario
print("Esta es la lista de números que derivan de la clave: ", listaUnica)


def cifrado():#funcion para cifrar el mensaje
	#esta primera parte es igual a la que se seguía en la funcion solitario para ver los caracteres del mensaje

	
	MensCod=[]#Esta lista esta compuesta por números que surgen de transformar el abecedario en número por sustitución a=1, b=2.... con la función 
	for a in MensPrep:
		num = ord(a) - 96 #función que transforma un caracter en su valor numérico ASCII. Restandole 96 la a minuscula es igual a 1.
		MensCod.append(num)
			
	#A partir de aqui empieza el cifrado propiamente dicho	

	ristra=listaUnica #clave obtenida en el solitario
	
	sumacifrada=[]#lista que es el resultado de sumar la lista obtenida de transformar los caracteres a números + la clave. Para sumar se siguen las reglas del solitario
	for i in range (len(MensCod)):
		lasuma=ristra[i]+MensCod[i]
		if lasuma>26:
			lasuma=lasuma-26
		sumacifrada.append (lasuma)
	
	cifradoletras=[] #lista con los números obtenidos de la suma transformado a letras
	for i in sumacifrada:
		let=chr(i+96)
		cifradoletras.append(let)
	
	cifradoletras1=[] #lista anterior haciendo sublistas con 5 elementos uno por cada caracter
	for i in range(0,len(cifradoletras),5):
		cifradoletras1.append (cifradoletras[i:i+5])
	

	ls4=[]#transformo la lista anterior en otra lista donde cada elemento tiene 5 caracteres, es decir, las sublistas de cifradoletras1 las transformo en un único elemento de 5 caracteres
	for x in range(len(cifradoletras1)):
		
		ls3="".join(cifradoletras1[x])
		ls4.append(ls3)
		
		ls5=" ".join(ls4) #transformo la lista anterior en una sucesión de caracteres agrupados de 5 en 5 
	return (ls5)

print("Este es el texto cifrado: ", (cifrado()))



def descifrado(mens1): #funcion de descifrado procedo de forma inverse a la fucnción de cifrado
	Mensajecifrado=mens1
	lisMensajeCifr=Mensajecifrado.split()#con la función split transformo una sucesión de caracteres agrupados de 5 en 5 en una lista con elemntos de 5 caracteres
	
	lista=[]#lista con el mensaje cifrado transformado a números con la funcion ord que me permite transformar cada caracter a un numero que constituye un elemento unico en la lista
	for i in range(len(lisMensajeCifr)):
		for m in lisMensajeCifr[i]:
			num=ord(m)-96
			lista.append(num)

	ristra=listaUnica
	RestaMen=[]#lista con el resultado de restar el mensaje cifrado transformado a numeros y la clave
	for i in range(len(lista)):
		
		if lista[i]<=ristra[i]:
			lista[i]=lista[i]+26
		ll=lista[i]-ristra[i]
		RestaMen.append(ll)
	
	menDesc=[] #lista con la lista RestaMen transformada a letras con la funcion chr
	for i in RestaMen:
		letras=chr(i+96)
		menDesc.append(letras)
	
	listafracc=[]#lista formada por sublistas de 5 elemntos de números
	for i in range(0, len(menDesc), 5):
		listafracc.append(menDesc[i:i+5])
	
	listafinal=[]#lista donde se eliminan las sublistas y quedan elementos de 5 caracteres.
	for x in range(len(listafracc)):
		listafinal.append("".join(listafracc[x]))
	
	listafinal1=" ".join(listafinal) #sucesión de caracteres agrupados de 5 en 5 que es nuevamente el mensaje original
	return (listafinal1)
print("Este es el mensaje descifrado: ", descifrado((cifrado())))