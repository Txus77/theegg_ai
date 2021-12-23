while True: #ciclo indeterminado para obligar a introducir los datos correctos según un filtor establecido, es decir, números enteros en el intervalo del 0 al 99, ambos no incluidos

	try:
		num = int(input("Introduzca un número entero entre 0 y 99: "))

		if 0 < num < 99:
			break
		else:
			print ("El número introducido no está dentro del intervalo indicado\nVuelva a introducir un número entre 0 y 99")

	except:
		print ("El dato introducido no es un número entero. Introduzca un valor correcto")


print ("La tabla del " + str(num) + " es: ")


for i in range(1, 11): #ciclo determinado que genera una serie de números del 1 al 10, ambos inclusive
	
	prod=num*i #calcula el valor del número que hemos elegido por cada número generado del 1 al 10
	print (str(num) + " X "+ str(i) + " = " + str (prod)) # imprime los resultados



