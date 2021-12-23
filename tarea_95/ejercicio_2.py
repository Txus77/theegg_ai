cadena = input ("Introduzca una cadena de texto que se componga sólo de letras y números: ")

if  cadena.isalnum():#condicional para establecer que sólo sea válido introducir caracteres alfanumericas

	if 10 > len (cadena) >= 5:#Nos indica longitud de cadena según lo establecido en el enunciado
		print ("la cadena tiene una longitud de mayor o igual a 5 caracteres y a su vez es menor de 10  caracteres")

	elif len (cadena) < 5:
		print ("La cadena tiene una longitud  de menos de 5 caracteres")

	else:
		print ("La cadena tiene una longitud  mayor o igual a 10 caracteres")

else:#en caso de no cumplir con el filtro establecido (introducir caracteres alfanumericos) obliga a reiniciar el programa
	print ("No ha introducido una cadena de texto válida \nReinicialice el programa e introduzca una cadena de texto válida")