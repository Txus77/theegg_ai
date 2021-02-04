# HTML5, la revolución de los navegadores

## Enunciado

El alumno para superar esta tarea debe:

1.- Diseñar una estructura básica de HTML y verla en el navegador.

2.- Introducir algo de color a la página apoyándose en CSS.

3.- Añádir un video gracias a la nueva etiqueta video de html5.

4.- Serías capaz de darle al play y al pause del video mediante instrucciones por voz (hablando a la
computadora) utilizando javascript? (no obligatorio).

## Solución

Para la solución de la tarea he creado un sitio web con varios archivos. He creado un archivo index con una estructura básica
consitente en los siguientes elementos: head, body y dentro del body los elementos header, nav, section, aside y footer. Dentro de estos he utilizado otros elementos típicos de Html5.
Además, he creado otros archivos Html para poder navegar entre ellos. 
Dentro del sitio web lo he estructurado con un directorio **imagenes**, donde he guardado todas las imagenes y videos que se utilizan en el sitio web y otro directorio denominado recursos donde he guardado 
la hoja de estilos que se aplica.

En el archivo **fotos_animales**, además de lincarlo a la hoja de estilos, he introducido en el elemento Head otros estilos para no limitarme a realizarlo sólo con una hoja de estilos.

Se puede interactuar con los videos con comandos de voz aunque sólo si se utiliza el navegador de google y se instala un servidor en el ordenador personal. Yo he utilizado 
MAMP que se puede descargar desde www.mamp.info. Es un paquete gratuito. Este paquete incluye un servidor Apache, un servidor PHP y un servidor MySQL.
Una vez descargado e instalado solo hace falta abrirlo para comenzar a usar el servidor.
MAMP crea un directorio dentro del propio directorio llamado htdocs donde se supone que se debe almacenar los archivos de nuestro sitio web, pero también se puede asignar un directorio en la opción **Preferences**
Esta opción abre una nueva ventana con varias pestañas para su configuración. La pestaña **Web Server** muestra el directorio actual que usa el servidor Apache y ofrece un botón para seleccionar
uno diferente.
Después de seleccionar el directorio en el que se encuentran los archivos de nuestro sitio web, podemos acceder a ellos desde el servidor. Apache crea un dominio especial llamado **localhost**
para referenciar al servidor y, por tanto, se puede acceder a nuestro sitio web desde la URL http://localhost/. Si se quiere acceder a un archivo específico sólo hay que añadir
el nombre del archivo al final de la URL.

Para interactuar con los videos con comandos de voz se puede hacer ocn las palabras **reproducir** para que se ponga en marcha el video y **pausar** para detener el video. para
comprobar si el microfono funciona cunado estamos en la pagina del video si se dice **hola** tiene que saltar una ventana emergente respondiendo **hola**.



