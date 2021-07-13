#!/bin/bash
clear
echo "AGENDA DE TELEFONO Y CORREO ELECTRONICO"
echo "**********************************************"
echo "Si quiere introducir un nuevo registro pulse 1"
echo "--------------------------------------------------"
echo "Si quiere modificar un registro existente pulse 2"
echo "--------------------------------------------------"
echo "Si quiere eliminar un registro pulse 3"
echo "--------------------------------------------------"
echo "si quiere ver todos los registros ordenados por orden alfabético pulse 4"
echo "--------------------------------------------------"
echo "Si quiere consultar algún registro pulse 5"
echo "--------------------------------------------------"
# Las primeras lineas imprimen en pantalla las opciones que tiene el usuario 
read opcion #se guarda en la variable  opcion lo que elige el usuario

case $opcion in #comando que nos permite definir las instrucciones que se jecutaran en función de la eleccion del usuario
	1)	
		while [ "$parar" != "q" ]; do #bucle indeterminado para introducir datos hasta que cumplamos la condicion puesta
			read -p "Nombre: " nombre #se crea una variable nombre con lo que introduzca el usuario

			read -p "Primer Apellido: " primerapellido

			read -p "Segundo Apellido: " segundoapellido

			read -p "telefono: " telefono

			read -p "e-mail: " email
			echo "$nombre $primerapellido $segundoapellido $telefono $email">> agenda.txt #se imprime los datos que se van introduciendo en el archivo agenda.txt 
			echo "pulse q para terminar de introducir datos o enter para introducir otro registro"
			read parar
			
		done
	;;

	2)
		echo "Introduzca nombre, apellido u otro parametro de busqueda del registro a modificar"
		read busqueda
		grep -in "$busqueda" agenda.txt #comando que busca la fila donde se encuntra el patron establecido, que en este caso es el valor de la variable busqueda, en el archivo agenda.txt
		if [[ $(grep -in "$busqueda" agenda.txt) ]]; then #condicional  para que el programa sepa que hacer en caso que se encuentre algun resultado o ningun resultado
			echo "El número que esta en primer lugar es el id del registro"
			echo "Introduzca el id del registro que quiera modificar"
			read id
			echo "Introduzca 1 para modificar Nombre"
			echo "Introduzca 2 para modificar Apellidos"
			echo "Introduzca 3 para modificar telefono"
			echo "Introduzca 4 para modificar e-mail"
			read modificar
			case $modificar in #se establecen las instrucciones en funcion de lo que queramos modificar 
				1)
					read -p "intrduzca nuevo nombre " nuevonombre
					nombreagenda=$(awk 'NR=='$id'' agenda.txt | awk '{print$1}') #con el comando awk se localiza el valor que queremos sustituir.
					# con NR nos situamos en la línea y  con el print$1 establecemos que  es el primer valor de esa línea.
					sed -i ''$id's/'$nombreagenda'/'$nuevonombre'/' agenda.txt #con el comando sed sustituimos el valor antiguo por el nuevo
					echo "El registro modificado es: $(awk 'NR=='$id'' agenda.txt)" #se imprime pòr pantalla el resultado
				;;
			
				2)
					read -p "introduzca nuevo primer apellido " nuevoprimerapellido
                                	read -p "introduzca nuevo segundo apellido " nuevosegundoapellido
					primerapellidoagenda=$(awk 'NR=='$id'' agenda.txt | awk '{print$2}')
					segundoapellidoagenda=$(awk 'NR=='$id'' agenda.txt | awk '{print$3}')
					sed -i ''$id's/'$primerapellidoagenda'/'$nuevoprimerapellido'/' agenda.txt  
					sed -i ''$id's/'$segundoapellidoagenda'/'$nuevosegundoapellido'/' agenda.txt 
					echo "El registro modificado es: $(awk 'NR=='$id'' agenda.txt)"
				;;

				3)
					read -p "introduzca nuevo telefono " nuevotelefono
					telefonoagenda=$(awk 'NR=='$id'' agenda.txt | awk '{print$4}')
                                	sed -i ''$id's/'$telefonoagenda'/'$nuevotelefono'/' agenda.txt
					echo "El registro modificado es: $(awk 'NR=='$id'' agenda.txt)"
				;;
			
				4)	
					read -p "introduzca  nuevo email " nuevoemail
					emailagenda=$(awk 'NR=='$id'' agenda.txt | awk '{print$5}')
                                	sed -i ''$id's/'$emailagenda'/'$nuevoemail'/' agenda.txt
					echo "El registro modificado es: $(awk 'NR=='$id'' agenda.txt)"
				;;
			esac
		else
			echo "El parametro introducido no se corresponde con ningún registro. Vuelva a Incializar el programa"
		fi
	;;
	3)
		
		read -p "introduce parametro de busqueda del resgistro a eliminar: " parametro
		grep -in "$parametro" agenda.txt #encuentra en el archivo agenda.txt todas las líneas que tengan el patron establecido en este caso el valor de la variable parametro		
		if [[ $(grep -in "$parametro" agenda.txt) ]]; then
			echo "El número que esta en primer lugar es el id del resgistro"
			read -p "Introduce id: " id
			sed -i ''$id'd' agenda.txt
		else
                        echo "El parametro introducido no se corresponde con ningún registro. Vuelva a Incializar el programa"
                fi	
	;;	

	4)
		agendaordenada=$(sort agenda.txt | grep -n $) #creo una variable con el valor de la agenda ordenada alfabéticamente con el grep hago que aparezca el número al inicio.
		echo "$agendaordenada" | more #se imprime la agenda ordenada por pantalla y con el comando more hacemos que aparezca paginada una vez se llena la pantalla de registros de uno en uno
	;;

	5)	
		echo "Introduzca nombre, apellidos u otro parametro para iniciar la busqueda"
		read datoconsulta
		grep -in "$datoconsulta" agenda.txt
		if [[ $(grep -in "$datoconsulta" agenda.txt) ]]; then
			echo "El número que está al principio de cada línea es el id"
			read -p "Introduzca id para obtener los datos: " id
			datosfinales=$(awk 'NR=='$id'' agenda.txt)
			echo $datosfinales
		else
			echo "El parametro introducido no se corresponde con ningún registro. Vuelva a Incializar el programa"
                fi      
	;;
esac

