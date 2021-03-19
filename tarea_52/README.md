# TAREA 52: Estructura de datos

## Enunciado

EJERCICIO 1.

Desarrolla un programa que sirva para:
- Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el
número 0, el cual no debe guardarse.
- A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su
primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
- Recorrer la lista para imprimir la sumatoria de todos los elementos.
- Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores
que el número dado. Imprimir esta nueva lista, iterando por ella.
- Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una
compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si
la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

EJERCICIO 2.

Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela,
finalizando al ingresar ?x?. A continuación, solicitar que ingrese los nombres de los alumnos de nivel
secundario, finalizando al ingresar ?x?.
- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
- Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

## Solución

Ambos ejercicios se han realizado en el lenguaje de programación PHYTON version 3.8. Para ejecutarlos se deben descargar 
los archivos y desde el IDLE de phyton se abre el archivo que corresponda. Una vez abierto se clicka en RUN y el programa empieza a correr

EJERCICIO 1

Este ejercicio se ha realizado empleando listas para su resolución en todos los apartados menos en el último donde
también se ha empleado un diccionario.
La resolución se ha ha hecho empleando los métodos típicos de listas para eliminar (**remove ()**)o agregar elementos (**append ()**)
En el último apartado se ha utilizado un diccionario en cual se emplea de clave los elementos de la lista y como valor las veces que ese elemento se repite.
Una vez creado el diccionario se pasa tupla con el metodo **item ()** donde el primer elemento es la clave y el segundo el número de repeticiones
Además, este último apartado también se ha resulto de 2 formas más que están comentadas:
En la primera de estas formas lo que se hace es obtener primero
una lista sin elementos repetidos y luego iterando esta lista se crea una lista de tuplas donde el primer elemnto de cada tupla es un elemento de esta lista creada
y el segundo elemento es el número de repeticiones que se obtiene aplicando el metodo **count ()** a la lista de referencia.
En la segunda forma se obtiene la lista con la funcion **set ()** que da como resultado una lista donde sólo aparece cada elemnto una vez, es decir, las
repeticiones no aparecen. Luego se genera una lista de tuplas igual que en el caso anterior

EJERCICIO 2

En este ejercicio se han implemntado una serie de funciones que permiten, por un lado, que el programa no se caiga si los datos no se introducen de forma correcta
y, por otro lado, que los datos, una vez introducidos tengan una estructura homogenea que permita su comparación.
Por último, se han definido una serie de funciones que generan listas que dan solución a los diferentes apartados del ejercicio, utilizando metodos típicos de listas como los
indicados en el ejercicio anterior, y ciclos para comparar-buscar elementos y, otras, que imprimen en pantalla las diferentes soluciones pedidas



