print ("Introduzca dos números: \n")

while True: #ciclo indeterminado para comprobar que los valores introducidos con correctos, es decir, números reales

	try:
		numero_1 = float(input ("Introduce el primer número: "))
		numero_2 = float(input ("Introduce el segundo número: "))
		break
	except:
		print ("El valor introducido no es un número. \n Introduzca un valor correcto:")


def diferentes(num_1,num_2):
	"""función que establece si los números son diferentes y, en tal caso,  indica cual es mayor"""

	if num_1 != num_2 and num_1 > num_2:
	 	return print ("El primer número introducido: "+ str(num_1) + " es mayor que el segundo número introducido: "+ str(num_2) + "\n")
	else:
		return	print("El segundo número introducido: "+ str(num_2) + " es mayor o igual que el primer número introducido: "+ str(num_1) + "\n")


def iguales (num_1,num_2):
	"""función que establece si los números son iguales"""

	if num_1 == num_2:
		return print ("\nLos números introducidos son iguales \n")
	else:
		return print ("\nlos números introducidos son diferentes \n")

iguales(numero_1,numero_2)
diferentes(numero_1,numero_2)

	
	

