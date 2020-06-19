num = float(input())
denominador=10000
numerador=int(num*10000)
for i in [4, 3, 2, 1, 0]:
	if numerador%2**i==0 and denominador%2**i==0:
		numerador=numerador/2**i
		denominador=denominador/2**i
	
for j in [4, 3, 2, 1, 0]:

	if numerador%5**j==0 and denominador%5**j==0:
		numerador=numerador/5**j
		denominador=denominador/5**j

print ("%d/%d" %(numerador, denominador))