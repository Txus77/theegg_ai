# TAREA 23: Cifrado y descifrado con el solitario
## ENUNCIADO
En la siguiente tarea, el alumno debe construir una comunicación cifrada entre dos funciones utilizando el algoritmo del solitario:

1.- Una primera función a la que enviemos una variable (que será una frase o cadena e texto) para que la función lo cifre mediante el solitario. En programación existen diferentes tipos de variables: strings, enteros, flotantes, booleanos, ... y en este caso la variable o parámetro que se le envía a la función es de tipo String. 

2.- Una segunda función que recoja el mensaje cifrado y lo descifre utilizando este mismo algoritmo

## SOLUCIÓN

La solución se ha realizado para un alfabeto de 26 letras desde la a hasta la z sin tener en cuenta la ñ. Los números tampoco se han tenido en cuenta.

En esta tarea la solución implementada se ha realizado mediante tres funciones principales:

1.- la primera a partir de una clave que es el orden inicial de las cartas genera mediante el algoritmo del solitario una ristra de números que luego se utiliza para cifrar y descifrar el mensaje

2.- la segunda función cifra el mensaje mediante la ristra de números generada en paso anterior aplicando el algoritmo de cifrado. Da como resultado el mensaje cifrado

3.- la tercera función descifra el mensaje cifrado mediante la aplicación del algoritmo de descifrado (opuesto al de cifrado) y la ristra de números generada en la primera función dando como resultado el mensaje descifrado

## IMPLEMENTACIÓN EN CÓDIGO

Se ha utilizado como lenguaje de programación Phyton versión 3.8

La implementación en código está detallada en el archivo .py pero a modo de resumen indican los pasos más importantes:

1.- Se introduce el mensaje a transmitir mediante función "input" que considera las variables por defecto de tipo string.

2.- En una primera función denominada "PrevCodMens" , previa tanto a la generación de la clave, como al cifrado y descifrado, se ha preparado el mensaje para su procesado posterior convirtiendolo en letras minusculas y haciendo que el total de carcateres sea multiplo de 5 (rellenando los caracteres faltantes con x en caso necesario).Con esta función se evita  duplicar codigo en la funcion de generación de claves y en la de cifrado. Se toma como parametro el mensaje original y da como resultado el mensaje preparado para el cifrado.

3.- La segunda función denominada "solitario": es la que genera las claves y se ha realizado de forma que genere una clave por mensaje a cifrar para que ésta no se repita. Aqui se utiliza el resultado de la primera función para conocer el número de caracteres del mensaje y que se generen el mismo número de números. En esta función se asimila la baraja a una lista y se trabaja con ella según el algoritmo del solitario hasta obtener otra lista con los números que se usarán para cifrar y descifrar el mensaje.  

4.- La tercera función denominada "cifrado": Se cifra el mensaje con el algoritmo inidcado. Se utiliza como mensaje el resultado de la primera función reseñada. Da como resultado el mensaje cifrado

5.- La cuarta función denominada "descifrado": toma como parámetro el resultado de la función de cifrado y aplicando el algoritmo opuesto genera nuevamente el mensaje original
