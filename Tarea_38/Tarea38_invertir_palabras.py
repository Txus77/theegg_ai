
def invertir (cadena):
	list1=cadena.split()
	list1.reverse()
	invertir_cadena = " ".join(list1)
	return invertir_cadena


def comprobar(cad):
	list2 = cad.split()

	for i in range(0, len(list2)):
	 	if list2[i].isalpha()==False:	
	 		return False

	return True


while True:
	try:
		num_casos=int(input("Inserte numero de casos a resolver: "))
		break
	except:
		print("Error: Introduce un número por favor")


i = 0
lista = []
while i < num_casos:
	var = input("introduce palabras:  ")
	if comprobar(var):
		lista.append(var)
		i += 1
	else:
		print("Error. Introduce letras y espacios")
		continue


for i in range (0, len(lista)):
	print()
	print("Case #" + str(i+1) + ": ", invertir(lista[i]))
	




