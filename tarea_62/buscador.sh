#!/bin/bash

clear

echo "Introduzca el archivo o directorio que quiera buscar"

read archivo


buscarchivo=$(find / -name $archivo 2>/dev/null) #busco en toda la raiz el archivo. Los errores los suprimo. Me dará la ruta absoluta del archivo

if [[ $buscarchivo ]]; then #si la variable coge un valor da como resultado TRUE y se ejecutan las instrucciones siguientes
	if [[ -d $buscarchivo ]]; then # si es un directorio da como resultado TRUE ejecuta las instrucciones siguientes
		echo  "$archivo es un directorio y se encuntra en la siguiente ruta $buscarchivo"
		contenido=$(ls -l $buscarchivo) #variable que toma como valor el listado de rachivos del directorio
		echo "$archivo contiene los siguientes archivos y directorios: "
		echo "$contenido"
	else
		if [[ -x $buscarchivo ]]; then #si es un archivo ejecutable da como resultado TRUE y  pasa a las instrucciones siguientes
			echo "$archivo es un archivo ejecutable y se encuentra en la siguiente ruta $buscarchivo"
		else
			echo "$archivo es un archivo no ejecutable y se encuentra en la siguiente ruta $buscarchivo"
		fi
	fi	
else #si la variable buscararchivo no coge un valor se ejecuta la siguiente instruccion
	echo "$archivo no existe"
fi

