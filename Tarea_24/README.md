# CONSTRUYE UN SIMULADOR

## ENUNCIADO

Desarrollar un programa donde una vez enviado un valor decimal a una función este lo convierta a binario y nos lo devuelva. Se trata de construir un simulador de un convertidor analógico digital mediante un programa (software).

## SOLUCIÓN

La transformación de un número en base decimal a otro en base binaria se puede realizar de 2 formas: 

La primera es asignando pesos a los 0 y 1 en función de la posición en la que se encuentren hasta llegar al valor que se quiere obtener en base decimal.  
Los pesos son siempre de base 2 elevado a la posición donde se encuentre el 0 o el 1 empezando por la posición 0 (de derecha a izquierda). 

La segunda forma es dividiendo el número en base decimal entre 2 y, posteriormente, el cociente entero, que vamos obteniendo de las sucesivas divisiones, entre 2, hasta llegar a 0. Los restos que vamor obteniendo en cada una de esas divisiones que sólo pueden ser 0 o 1 los vamos anotando.
El número binario será la sucesión de 0 y 1 que hemos ido obteniendo en los restos de las sucesivas divisiones contando desde  el final (ultima división realizada) hasta el inicio. 

En la solución de la Tarea se ha escogido el segundo método.

## IMPLEMNTACIÓN EN LENGUAJE DE PROGRAMACIÓN

### EJECUCIÓN DEL PROGRAMA

Se ha utilizado como lenguaje de programación Phyron en su versión 3.8. Para ejecutarlo se puede hacer desde la consola de phyton o también desde la consola de windows nos situamos en la ruta en la que se encuentra el archivo y lo ejecutamos escribiendo su nombre.

### IMPLEMENTACIÓN EN PHYTON

Se ha definido una función que convierte el número en base decimal en otro en base binaria. 
En esta función se ha establecido un bucle indeterminado con el objeto que se divida el número dado entre 2 tantas veces como sea necesario. En cada ciclo se obtiene como cociente un número entero, que en el siguiente ciclo será el valor que se vuelva a dividir, y un resto que siempre es 0 o 1. Los 0 y 1 que se van generando se agregan a una lista.
La lista generada estará en orden inverso a la lista que necesitamos por lo que se invierte el orden de los elementos. Los elementos que obtenemos se presentan como una secuencia de números.
EL problema que se plantea es que el número 0 no se representa en la función que se define por lo que para solventarlo se introduce, fuera de la función, una condición para que estén contemplados todos los números.

Otro problema que se presenta es cuando el valor que se introduce por consola no es un número entero en base 10. Para solucionarlo establecemos un ciclo infinito que del que sólo se sale cuando se introduce un número correcto.



