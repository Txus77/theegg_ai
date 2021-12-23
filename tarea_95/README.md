# Tarea - Media docena de ejercicios en Python

## Enunciados

### 1.- Realiza un programa que lea 2 números por teclado y determine:

  - Si los dos números son iguales
  - Si los dos números son diferentes
  - Si el primero es mayor que el segundo
  - Si el segundo es mayor o igual que el primero

### 2.- Determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual a 5 y a su vez es menor que 10.

### 3.- Realiza un programa que haga la tabla de multiplicación de un número introducido de valor entre 0 y 99:
  - Guarda en una variable el número introducido por el usuario
  - Añade un filtro que asegure que el número sea entre 0 y 99
  - Escribe la tabla multiplicando el valor introducido por valores entre 1 y 10

### 4.- El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?

  numero_1 = 9

  numero_2 = 3

  numero_3 = 6

  media=numero_1 + numero_2 + numero_3 / 3

código en enlace siguiente

https://docs.hektorprofe.net/python/introduccion-informal/ejercicios/

### 5.- Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar el proceso debe repetirse hasta que lo introduzca correctamente.

### 6.- Realiza un programa que sume todos los números enteros impares desde el 0 hasta el 115.

## Soluciones

Todos los ejercicios se han realizado con phyton 3.8. Antes de ejecutarlos se deben descargar los archivos al equipo.
Para ejecutarlo abrir cada ejercicio en IDLE de phyton, para ello seguir los pasos siguientes:
 - Abrir IDLE
 - clickar pestaña "File"
 - clickar en Open y buscar el archivo que se quiera ejecutar donde lo hayas descargado
 - Una vez abierto el archivo clickar la pestaña Run y dentro de ésta Run module

En cada ejercicio se han  introducido comentarios que explican los pasos dados por lo que se pasa a explicar las soluciones de forma conceptual:

### ejercicio 1

En este ejercicio, y en otros, para la validación de los datos introducidos se ha utilizado un ciclo indeterminado infinito que sólo se rompe cuando los
datos que se introducen son los que se piden, en este caso que sean números reales. Se ha utilizado la formula de la gestion de excepciones ya que
que obliga al que el dato que se introduzca sea valido ya que si no generaría una excepción y el bucle no concluiría por lo que hasta que no se introduzca
el dato correcto el programa no prosigue.

Para cumplir con lo que indica el enunciado se han definido sendas fuciones para tener el código estructurado, de forma que podamos llamar a la que nos interese
según necesidad

### ejercicio 2

En este ejercicio he cambiado el método de validación de los datos introducidos. En este caso he utilizado un condicional y un metodo de la librería estandar de phyton 
de forma que si la cadena no está formada únicamente de números y letras el programa se va al else y sale un mensaje para que reinicie el programa e introduzca los datos 
correctos.

En caso que introduzca bien la cadena realiza las acciones de indicar si la cadena está en un intervalo concreto de longitud de caracteres, es mayor o menor.

### ejercicio 3

En este ejercicio la forma de validar los datos introducidos es la misma que en el ejercicio 1 pero con el añadido que además de obligar a que no se genere la excepción,
es decir, se tiene que introducir un número entero, se ha añadido un filtro que si no se cumple no se rompe el bucle, que el número que se introduzca esté entre el 1 y el 99, 
y sigue pidiendo al usuario que intoduzca un dato correcto. El filtro se ha establecido mediante un condicional de forma que si se cumple la condición se sale del bucle y si
no sale un mensaje para que se introduzca el dato correcto y no se sale del bucle.

Para generar la tabla de multiplicación, primero con un ciclo determinado y la funcion range() he generado los números del 1 al 10 y en cada vuelta de ciclo calculo 
el producto del número escogido por el número que se geenra en cada vuelta de ciclo (empieza en el 1 y en cada vuelta se genera el siguiente hasta el 10). 
Imprimo cada vuelta de ciclo y obtengo la tabla de multiplicar

### ejercicio 4

En este ejercicio la solución se basa en que en matemáticas y,en phyton también, si tengo varias operaciones y ningún parentesis primero se ejecutan las multiplicaciones y 
divisiones y luego las sumas y restas. En este caso primero se ejecuta la división de los dos números que se dividen y luego se hace la suma de ese resultado con los otos dos
números. Para corregirlo y obtener la media de los 3 números hay que forzar a que se realice primero la suma de los 3 números mediante un parentesis que englobe a los 3. Una vez
hecho esto el resultado obtenido se dividirá entre 3

### ejercicio 5

La resolución de este ejercicio es muy similar al proceso utilizado para validar los datos introducidos en el ejercicio 3 pero en este caso como filtro se indica que el modulo del
número que se introduzca dividido entre 2 (el modulo es el resto obtenido de la división de  2 números) sea diferente de 0 (condición para que sea impar).
Hasta que no se produzca que el número sea entero y, a la vez, su modulo al dividirlo entre 2 diferente de 0 no se romperá el bucle y obligará a introducir un nuevo dato.

### ejercicio 6

Este ejercicio se resuelve generando primero todos los impares desde 0 hasta 115, inclusive, mediante la combinación de un bucle determiando y una función range() donde 
se estable el inicio de la serie que se quiere generar, en este caso 1, el final, en este caso 116 (ya que se quiere incluir el 115), y como tercer argumento de cuanto en cuanto
queremos que aumente, en este caso, de 2 en 2.
En cada vuelta de ciclo hacemos que se sume el impar que se genere a la suma que se va generando de los anteriores. Esta suma se va almacemando en una variable que hemos creado 
antes de iniciar el ciclo y cuyo valor va cambiando a cada vuelta del ciclo. Tras la última vuelta tendremos la suma de todos los impares entre 0 y 115, ambos inclusive




 

