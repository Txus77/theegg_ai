class Persona:

	def __init__ (self):#constructor clase persona con 3 atributos

		self.__nombre="dato sin introducir"
		self.__edad="dato sin introducir"
		self.__dni="dato sin introducir"


	def set_edad (self):#metodo para establecer la edad

		while True:#ciclo indeterminado que se acaba cuando el dato se introduce correctamente
			try:
				edad=int(input ("Introduzca su edad " ))
				if edad>0 and edad<150:#condición que se establece como edad válida
					self.__edad=edad
					break
				else:
					print("dato introducido incorrecto. Por favor introduzca una edad correcta entre 0 y 150 años")
			except:
				print ("dato introducido incorrecto. Por favor introduzca una edad correcta entre 0 y 150 años")

	def get_edad (self):

		print("Edad: ", self.__edad)


	def set_nombre(self):#metodo para establecer el nombre

		while True:#ciclo indeterminado que se acaba cuando el dato se introduce correctamente
			nombre=input("introduzca su nombre ")
			if nombre.isalpha():#condición que establece que para que un nombre sea valido se tiene que componer solo de letras
				self.__nombre=nombre
				break
			else:
				print("Dato no valido. Introduzca el nombre otra vez")


	def get_nombre(self):
		return self.__nombre

	
	def set_dni(self):#metodo para establecer el DNI

		while True:#ciclo indeterminado que se acaba cuando el dato se introduce correctamente
			dni=input("Introduzca su DNI ")
			if len(dni)==9 and dni[0:8].isdigit() and dni[-1].isalpha():#condición que estblece que para que un dni sea valido se tiene que componer 9 elementos de los cuales los 8 primeros tienen que ser numeros y el ultimo letra
				self.__dni=dni
				break
			else:
				print("Dato no valido. El DNI debe tener 8 números y una letra al final. Introduzca el dato otra vez")

	def get_dni(self):

		print("DNI: ",self.__dni)


	def esMayorDeEdad(self):

		if self.__edad>=18:
			print (True)
		else:
			print(False)

	def mostrar(self):

		datos="Nombre: " + str(self.__nombre) + "\nEdad: " + str(self.__edad) + "\nDNI: " + str (self.__dni)
		return print(datos)


usuario=Persona()

usuario.set_dni()
usuario.set_edad()
usuario.set_nombre()

usuario.mostrar()

