suma = 0 #definimos la variable suma

for i in range (1, 116, 2):#ciclo determinado que genera una serie de números entre 1 y 115, ambos inclusive, de forma que cada uno se genera sumando 2 al anterior, es decir los impares entre 1 y 115
	suma += i	# calcula el resultado del valor que se obtiene en la variable suma en cada ciclo  más el nuevo impar que se genera

print (f"la suma de todos los impares entre 0 y 115, incluído el 115, es {suma}") 