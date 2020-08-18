Vida_pikachu=100
Vida_Jigglypuff=100

Ataque_pikachu=55
Ataque_Jigglypuff=45

Turno=1


while  Vida_Jigglypuff >= 0 and Vida_pikachu >=0:

	if Turno == 1:
		Vida_Jigglypuff=Vida_Jigglypuff-Ataque_pikachu
		Turno=0
		print ("vida Jiggly: ", Vida_Jigglypuff)

	else:
		Vida_pikachu=Vida_pikachu-Ataque_Jigglypuff
		Turno=1
		print("Vida Pikachu: ", Vida_pikachu)



if Vida_pikachu<=0:
	print("Jigglypuff gana")

else:
	print ("Pikachu gana")
	