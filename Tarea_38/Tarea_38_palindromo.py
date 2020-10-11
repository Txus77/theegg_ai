#numero primo

import math


def primo(num):
	i = 2

	while i <= math.sqrt(num):
		if num % i == 0:
			return False
		i += 1	
		
	if num==1:
		return False
	return True


def palindromo(num1):
	var=str(num1)

	if var[:] == var[::-1]:
			return True
		
	return False


def comprobar(num3):

	if num3 < 1 or num3 > 1000000:
		return False
	return True


while True:
	try:
		numero=int(input("Introduce un número entero  mayor o igual que 1 y menor o igual que 1000000: "))
		comprobarnumero=comprobar(numero)
		if comprobarnumero:
			break
	except:
		print("El valor introducido no es correcto. Intentelo de nuevo")



def buscar(num2):
	
	while palindromo(num2)==False or primo(num2)==False:
		num2+=1
	return num2

print(buscar(numero))


