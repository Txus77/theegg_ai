while True: #ciclo indeterminado para obligar al ususario a introducir un valor que se ajuste a lo pedido. 

	try:
		impar = int(input("Introduce un numero impar: " ))

		if (impar % 2) != 0: #condición de que un números sea impar
			
			break
		else:
			print (f'El valor {impar} no es impar')
	except:

		print ("Introduce un valor correcto")

print (f'El valor introducido: {impar} es impar')



