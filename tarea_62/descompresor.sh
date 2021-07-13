#!/bin/bash
clear
echo "                     COMPRESOR Y DESCOMPRESOR               "
echo "************************************************************"
echo "Comprime y descomprime archivos con esta sencilla aplicación"
echo " "
echo "OPCIONES"
echo "************************************************************"
echo "OPCION 1 Si quiere comprimir uno o varios archivos pulse 1"
echo "------------------------------------------------------------"
echo "OPCION 2 Si desea descomprimir un archivo pulse 2"
echo "------------------------------------------------------------"

read opcion #comando para leer la opción que introduce el usuario

case $opcion in #comando que  permite establecer diferentes respuestas en función de la opción elegida
	1)
		read -p "Determine directorio de destino: " directorio
		
		directoriodestino=$(find / -name $directorio 2>/dev/null) #defino una variable donde guardo la ruta absoluta del directorio de destino del archivo comprimido resultante		
							  # ls orden 2>/dev/null es para que no me se indiquen por pantalla las rutas que me dan error		
		read -p "Indique el nombre de la carpeta temporal que se creara para el trabajo de compresion. Tenga en cuenta que una vez realizado el trabajo se eliminará: " comptemporal
		mkdir $comptemporal #creo un directorio temporal donde dirijo copias de los archivos que quiero comprimir. El directorio se crea en el directorio en el que estoy trabajando
		
		rutatemporal=$(find / -name $comptemporal 2>/dev/null) # defino una variable para guardar la ruta absoluta de la carpeta temporal creada
		
		read -p "Indique nombre del archivo de destino: " destino
		
		while [ "$parar" != "q" ]; do #establezco un ciclo indeterminado para introducir los nombres de los archivos que quiero comprimir.
					      #Cuando haya acabado de introducir los archivos  salgo del ciclo pulsando q
			read -p "Nombre archivo a comprimir: " archivoacomprimir
			ruta=$(find / -name $archivoacomprimir 2>/dev/null)
			cp $ruta $rutatemporal 2>/dev/null #hago copias de los archivos a comprimir en la carpeta temporal que he creado
			echo "pulse q para terminar de introducir datos o enter para seguir introduciendo datos"
			read parar	
		done
		
		arch=$(ls $rutatemporal) #variable donde tengo  me aparecen los archivos a comprimir
		
		cd $rutatemporal #me sitúo en la carpeta temporal para que el archivo comprimido se cree en esta carpeta
		
		7z a  $destino $arch >/dev/null 2>&1 #comprimo los archivos con el nombre que he establecido anteriormente
		
		comprimido=$(ls | grep ".7z$") #guardo en una variable el nombre del archivo comprimido
		
		if [[ -e "$comprimido" ]]; # condición en la  que se comprueba que el archivo comprimido existe
		then
			echo "el archivo comprimido se ha creado"
			rutafinal=$(find / -name $comprimido 2>/dev/null) #ruta absoluta donde está el archivo comprimido
			mv $rutafinal $directoriodestino # instrucción para mover el archivo comprimido
			rutacomprimido=$(find / -name $comprimido 2>/dev/null)
			echo "La ruta para acceder al archivo comprimido es $rutacomprimido"
		else
			echo "el archivo comprimido no se ha creado"
		fi	
		
		rm -r $rutatemporal #instrucción para eliminar el directorio temporal creado con los archivos que contiene
		
	;;	

	
	2)
		
		read -p "Introduzca el nombre del archivo a descomprimir: " archivodescomp
		rutaorigen=$(find / -name $archivodescomp 2>/dev/null) #localizo el archivo a descomprimir. Me da como resultado su ruta absoluta
		
		read -p "Determine directorio de destino: " directorio                 
                directoriodestino=$(find / -name $directorio 2>/dev/null) #localizo el directorio de destino. Me da como resultado su ruta absoluta

		7z x $rutaorigen -o$directoriodestino #instruccion para descomprimir con el -o inidco la ruta donde quiero que se descomprima
	;;

esac
