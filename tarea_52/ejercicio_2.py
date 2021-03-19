
def comprobar(cad):
	"""funcion para comprobar que sólo se introducen letras y espacios para 
	los nombres"""
	list2 = cad.split()
	if len (list2) > 0:
		for i in range(0, len(list2)):
		 	if list2[i].isalpha()==False:	
		 		return False

		return True
	else:
		return False

def introducir_alumno():
	"""funcion que permite introducir el nombre del alumno y
	procesa el dato introducido para que pueda ser utilizado por el resto de funciones"""
	lista = []
	alumno = ""
	print ("Si quiere finalizar de introducir nombres introduzca la secuencia: ?x?")
	while alumno != "?x?":
		alumno = input("Introduzca el nombre de un alumno ")
		alumno_sin_esp = alumno.strip() #elimina los espacios al inicio y al final de la cadena
		alumno_format = alumno_sin_esp.title() #este metodo hace que todos los nombres estén escritos de la mmisma forma (mayúscula al inicio de cada palabra y minusculas el resto) para que puedan ser comparados
		if comprobar(alumno_format):
			lista.append(alumno_format)
		else:
			continue
	return lista


def imprimir_nombres(lista):
	""" imprime las diferentes listas que se van generando"""
	print("\n".join(lista),"\n")


def informar_nombres (lista):
	"""genera una lista de nombres sin que aparezcan repeticiones en caso de que las hubiera"""
	listasinrep = [] #esta lista se podría generar de forma más sencilla aplicando la funcion set () pero los nombres aparecerían en orden aleatorio
	
	for i in lista:
		if i not in listasinrep:
			listasinrep.append(i)
		else:
			continue
	return listasinrep

def nombres_repetidos_nivel(lista1,lista2):
	"""genera una lista con los nombres repetidos dentro de un mismo nivel de enseñanza"""
	lista_rep=[]
	for i in lista1:
		if lista2.count(i)>1:
			lista_rep.append(i)
	return lista_rep


def nombres_repetidos_nivel_dif(lista1,lista2):
	"""genera una lista con los nombres repetidos dentro de 2 niveles de enseñanza diferentes"""
	listarepdif=[]
	for i in range (len(lista1)):
		for j in range (len(lista2)):
			if lista1[i] == lista2[j]:
				listarepdif.append(lista1[i])
			else:
				continue
	return listarepdif

def lista1_no_lista2(lista1, lista2):
	for i in lista1:
		if i not in lista2:
			print (i)
		else:
			continue


lista_primaria = introducir_alumno()
print ("\nNombres introducidos de primaria")
imprimir_nombres(lista_primaria)


lista_secundaria = introducir_alumno()
print ("\nNombres introducidos de secundaria")
imprimir_nombres (lista_secundaria)


print ("Nombres primaria sin repeticiones")
lista_sin_rep_primaria = informar_nombres(lista_primaria)
imprimir_nombres(lista_sin_rep_primaria)


print ("Nombres secundaria sin repeticiones")
lista_sin_rep_secundaria = informar_nombres(lista_secundaria)
imprimir_nombres(lista_sin_rep_secundaria)


print("Nombres repetidos en el nivel de primaria")
imprimir_nombres(nombres_repetidos_nivel(lista_sin_rep_primaria, lista_primaria))

print("Nombres repetidos en el nivel de secundaria")
imprimir_nombres(nombres_repetidos_nivel(lista_sin_rep_secundaria, lista_secundaria))


print("Nombres que se encuentran en el nivel de primaria y en el de secundaria")
imprimir_nombres(nombres_repetidos_nivel_dif(lista_sin_rep_primaria,lista_sin_rep_secundaria))

print("Nombres de nivel primario que no se repiten en los de nivel secundario")
lista1_no_lista2(lista_sin_rep_primaria, lista_sin_rep_secundaria)
