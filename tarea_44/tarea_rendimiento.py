import time

def suma_lineal (n):
	suma=0
	for i in range(n+1):
		suma = suma+i
	

	return (suma)
		
print(suma_lineal(1100))

def suma_constante(n):

	suma = n/2*(n+1)


	return (suma)

print(suma_constante (1100))

cantidad = 1000000

for j in range(4):

	t0 = time.time()

	suma1 = suma_lineal(cantidad)

	t1 = time.time()

	suma2 = suma_constante(cantidad)

	t2 = time.time()

	print( "{} - {}".format(suma1, t1-t0))
	print( "{} - {}".format(suma2, t2-t1))
	cantidad *= 10
