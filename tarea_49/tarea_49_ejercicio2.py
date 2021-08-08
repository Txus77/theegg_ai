class Cuenta:

	def __init__(self):#constructor con los atributos titular y cantidad. Ambos son privados. 

			self.__titular=input("Introduzca nombre de titular: ")
			self.__cantidad=0
			

	def set_titular_modificar(self):#metodo para modificar el titular en caso de habernos equivocado
		self.__titular=input("Modifique el nombre de usuario: ")
		

	def get_titular(self):#metodo para obtener el titular
		print(self.__titular)


	def get_cantidad(self):#metodo para obtener la cantidad. Con la funcion round se establece que el resultado tenga como máximo 3 decimales

		print("El saldo de la cuenta es ", round(self.__cantidad, 3))	

		
	def ingreso(self):#metodo para ingresar dinero en la cuenta

		importe=round((float(input("ingrese una cantidad: "))),3)

		if importe>0:
			self.__cantidad+=importe
		return print(f'se han ingresado {importe} €')

	def retirar(self):#metodo para retirar dinero de la cuenta

		extraccion=round((float(input("Retire una cantidad: "))),3)

		if extraccion>0:
			self.__cantidad-=extraccion

		return print(f'se han retirado {extraccion} €') 


	def mostrar(self):#metodo que muestra los datos de la cuenta
		print(f"La cuenta del titular: {self.__titular} tiene un saldo de {round(self.__cantidad,3)} €")

usuario=Cuenta()
usuario.ingreso()
usuario.get_cantidad()
usuario.retirar()
usuario.get_cantidad()
usuario.mostrar()