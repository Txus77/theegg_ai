# Algoritmos de búsqueda

## ENUNCIADO
EJERCICIO A RESOLVER: Tenemos la siguiente lista de elementos: [3, 56, 21, 33, 874, 123, 66, 1000,23, 45, 65, 56].

1.- Construye tu propio algoritmo para ordenarlo de menor a mayor.

2.-Busca el número 875 utilizando el algoritmo secuencial y el binario. En cada iteración se debe sumar +1
de modo que al final del programa se debe indicar el número de iteraciones realizadas por cada
algoritmo hasta encontrar el elemento.

3.- Realiza el análisis en Notación Big O (visto en la tarea #44) y describe tu conclusiones en un
documento de texto.
Debes subir a tu repositorio GitHub tanto el programa (en el lenguaje de programación que hayas
elegido) y el documento de texto explicativo y razonado sobre el rendimiento y los tiempos de ejecución
de cada algoritmo en notación O Grande.

## SOLUCIÓN

Los algoritmos utilizados han sido los siguientes:

Algoritmo de ordenación: 

**Quicksort**: Este algoritmo utiliza la técnica recursiva Divide y Vencerás. La idea es elegir un elemento como pivote y ordenar el resto de elementos en torno a este
de forma que se divida la lista en 2 sublistas: una de valores menores al pivote y la otra con los valores superiores al pivote. En las sublistas se vuelve a repetir el
proceso hasta que se llega al caso base que en este caso es una lista de un elemento la cual no necesita ser ordenada

Algoritmos de busqueda: 

**Busqueda binaria**: en una lista ordenado, compara el elemento a buscar con el que está en mitad de la lista  y dependiendo de si es menor o mayor va generando sublistas, 
que tienen la mitad de tamaño, en donde se encuentra el elemento buscado. Se repite la operacion  hasta dar con el elemento a buscar

**Busqueda secuencial**: compara uno a uno todos los elementos con el buscado hasta que se encuentra este en el arreglo 



El programa se ha realizado en phyton 3.8. Para ponerlo en funcionamiento basta con abrir el IDLE de phyton, abrir el archivo  y una vez abierto darle a run.




