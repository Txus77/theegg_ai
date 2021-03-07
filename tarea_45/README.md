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

Los algoritmos utilizados han sido los sguientes:

Algoritmo de ordenación: 
Quicksort: Este algoritmo utiliza la técnica recursiva Divide y Vencerás. La idea es elegir un elemento como pivote y ordenar el resto de elementos en torno a este
de forma que se divida la lista en 2 sublistas: una de valores menores al pivote y la otra con los valores superiores al pivote. En las sublistas se vuelve a repetir el
proceso hasta que se llega al caso base que en este caso es una lista de un elemento la cual no necesita ser ordenada
Algoritmos de busqueda: 
Busqueda binaria: en una lista ordenado, compara el elemento a buscar con el que está en mitad de la lista  y dependiendo de si es menor o mayor va generando sublistas, 
que tienen la mitad de tamaño, en donde se encuentra el elemento buscado. Se repite la operacion  hasta dar con el elemento a buscar
Busqueda secuencial: compara uno a uno todos los elementos con el buscado hasta que se encuentra este en el arreglo 

### ANALISIS DE RENDIMIENTO

En el análisis de rendimiento de los algoritmos interesa saber el tiempo de ejecución de los mismos y como este incrementa con el paso del tiempo. Cuando se habla de 
tiempo de ejecución realmente se está hablando del número de operaciones que el algoritmo tiene que realizar y, como éstas se incrementan con el aumento del número de 
datos de entrada. La notación O permite comparar el número de operaciones y ver como estas crecen en función del número de datos de entrada.

Algoritmo Quicksort: El rendimiento de este algoritmo depende de la elección del pivote de forma que en la situación más desfavorable, que es con un arreglo ordenado 
donde escogemos de pivote el primer elemento, el rendimiento será O(n2). Esto se produce porque se generan tantos niveles en la pila de llamadas como elementos tenemos, 
ya que al ir eligiendo siempre de pivote el primer elemento siempre queda un subarreglo vacío a la izquierda y otro con el resto de elementos a la derecha. Además, en 
cada nivel de la pila hay que tocar todos los elementos para ordenarlos de esta forma tenemos O(n) de tamaño de la pila de llamadas y O(n) dentro de los niveles lo que 
da O(n2)

Si, en vez de coger el primer elemento de pivote se coge, en un arreglo ordenado, el elemento del medio el tamaño de la pila de llamadas se reduce a la mitad, es decir, 4. 
Este es el mejor caso, por lo que se tiene O(log n). Sin embargo, dentro de cada nivel hay que tocar todos los elementos para ordenarlos en cada subarreglo así que tenemos O(n).
El rendimiento promedio para este algoritmo es O(n log n). El caso promedio difiere significativamente del caso peor, sobre todo en la forma en la que crece al aumentar
significativamente los datos de entrada

En el caso del algoritmo secuencial  su eficiencia expresada en notación asintótica será O (n) para el caso peor que se daría si el número buscado no está en la lista. 
Si el número buscado fuera el primero de la lista, caso mejor, tendríamos O(1), y el caso promedio se podría establecer como O(n/2) que no difiere mucho del caso peor. 
El crecimiento que experimentan en tiempo de ejecución al aumentar sensiblemente el número de datos de entrada es semejante en ambos casos.
En el algoritmo de búsqueda binaria, el mejor caso también es O(1), si el elemento buscado coincide en la primera operación. Sin embargo, para el caso peor es O(log n) 
ya que en cada operación se divide por la mitad el arreglo por lo que cada vez hay menos elementos en donde buscar.

**Comparación de Algoritmos de búsqueda:**

En el algoritmo secuencial su tiempo de ejecución aumenta proporcionalmente al número de entrada de datos. Sin embargo, en la búsqueda binaria el tiempo de ejecución aumenta 
de forma logarítmica por lo que para grandes cantidades de datos el algoritmo de búsqueda binaria es mucho más eficiente que el de búsqueda secuencial y la diferencia se agranda
a más datos de entrada.

En el programa realizado se puede ver claramente como con el algoritmo de busqueda binaria para el caso más desfavorable, que es cuando el elemnto buscado no está en la lista,
le número de iteracciones realizadas han sido de 5 mientras que en el caso de la busqueda secuencial nos vamos hasta las 12 iteracciones. Como ya se ha indicado, el rendimiento
del algoritmo secuencial expresado en Big-O es O(n) y el del algoritmo de busqueda binaria O (log n).

Sin embargo, el algoritmo de búsqueda binaria necesita de un arreglo previamente ordenado para poder ejecutarse, a diferencia de la búsqueda secuencial, por lo que en caso de
darse un arreglo desordenado habría que sumar a la eficiencia del algoritmo binario la eficiencia del algoritmo de ordenación que se utilice. La eficiencia de los algoritmos 
de ordenación oscilan entre O (n log n) y O(n2). Esto quiere decir que para arreglos desordenados es más eficiente la búsqueda lineal.

El programa se ha realizado en phyton 3.8. Para ponerlo en funcionamiento basta con abrir el IDLE de phyton, abrir el archivo  y una vez abierto darle a run.




