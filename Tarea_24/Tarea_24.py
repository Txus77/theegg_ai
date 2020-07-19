
def convertidorDec_Bin(num): #función para convertir un número de base decimal a otro de base binaria
	i=num
	lista=[] #lista donde se van almacenando los 0 y 1 que se obtienen de la división continua entre 2. 
	while i>0: 
		resto=i%2#los elementos que vamos incorporando a la lista son los restos de las divisiones que se van realizando
		i=i//2#se obtiene la parte entera de la división realizada que es la que se va dividiendo continuamente entre 2. Se utiliza el operador // porque si no con números grandes phyton no da los resultados que se esperan 

		lista.append(str(resto))
		
	listainvertida=lista[::-1]#la lista que se genera es la inversa de la que se necesita para generar el número binario por lo que se invierte
	numerobinario=" ".join(listainvertida)#sacamos los elementos de la lista y se genera una lista  de ceros y unos que es el núemro decimal convertido en bianrio
	return (numerobinario)
while True: #bucle infinito hasta que se introduce un número correcto
	try:
		num=int(input("Introduce un número entero en base decimal: "))
		
		break
	except:
		print("Valor introducido incorrecto. Introduce un número entero de base decimal")
if num==0: #el convertidor no tiene en cuenta el 0 por lo que con este ocndicional lo ttenemos en cuenta
	print(num)
else:
	print(convertidorDec_Bin(num))







