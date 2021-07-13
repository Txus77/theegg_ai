# Convertir una computadora tonta en algo más inteligente: bash scriptin

Para la realización de esta tarea he hecho los 3 programas siguientes:
-	Un buscador de archivos
-	Un  compresor y descompresor de archivos
-	Una agenda de teléfonos y email

Para la ejecución de los programas se tienen que descargar los archivos en un sistema operativo LINUX y ejecutar por terminal.

## Buscador de archivos:

Se denomina **buscador.sh**. Permite encontrar un archivo en el sistema operativo en caso de existir. Si no existe el programa lo indicará. También nos dice si el archivo es un directorio o un archivo. Además, si es un archivo nos indicará si es ejecutable o no. Una vez encontrado nos da la ruta absoluta del archivo o directorio buscado.

Para ejecutarlo hay que abrir la terminal en Linux y, si estamos en el directorio donde está el ejecutable, escribir:

./buscador.sh     

o poner su ruta absoluta si no estamos en el mismo directorio que el ejecutable

## Compresor y descompresor de archivos:

Se denomina **descompresor.sh**. Este programa permite tanto comprimir como descomprimir archivos. 

Para comprimir archivos el programa pedirá: 
- Un directorio de destino que tiene que ser existente. 
- El nombre de una carpeta temporal donde ejecutará las tareas de compresión y que posteriormente eliminará. Esta carpeta temporal la crea el programa, por lo que hay que tener cuidado de no elegir un nombre de una carpeta existente ya que si no el programa la eliminará al finalizar la compresión.
- El nombre del archivo destino, es decir, el archivo resultante de la compresión de archivos
- Nombre de los archivos a comprimir 

En el proceso de compresión el programa localiza los archivos a comprimir, crea una copia de ellos en la carpeta temporal, que ha creado el programa, y genera un archivo comprimido que envía al directorio de destino, que hayamos elegido, y nos indica la ruta del archivo comprimido. Finalmente, elimina la carpeta temporal con los archivos que tenga.

Para descomprimir archivos el programa también pedirá un directorio de destino que tiene que ser existente. En la descompresión el programa pide:
- Nombre del archivo a descomprimir
- Directorio de destino, que tiene que existir

el programa localiza el archivo a descomprimir y los descomprime en el directorio de destino que indiquemos.

Usa el compresor y descompresor 7z que es gratuito por lo que antes de utilizarlo es necesario instalar este paquete. El paquete 7z en Linux se instala escribiendo en la terminal 
sudo apt install p7zip-full

Para ejecutarlo hay que abrir la terminal en Linux y, si estamos en el directorio donde está el ejecutable, escribir:

./descompresor.sh         

o poner su ruta absoluta si no estamos en el mismo directorio que el ejecutable

## Agenda de teléfonos y email:

Se denomina **agenda.sh**. Este programa genera un archivo de texto donde se van guardando nombre, apellidos, teléfono y email de cuantas personas queramos. Además de introducir datos permite modificarlos, eliminarlos, ver la agenda por orden alfabético y buscar registros. El archivo de texto que genera el programa se denomina agenda.txt. 

Para ejecutarlo hay que abrir la terminal en Linux y, si estamos en el directorio donde está el ejecutable, escribir:

./agenda.sh     

o poner su ruta absoluta si no estamos en el mismo directorio que el ejecutable


