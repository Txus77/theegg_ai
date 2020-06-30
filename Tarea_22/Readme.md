PROBLEMA

Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la
Plaza del pueblo. Como es una persona muy prudente, desea que la leche que venderá sea
perfectamente natural y fresca, y por esa razón, va a traer unas sanísimas vacas de desde Tolosa.
Dispone de un camión con un cierto límite de peso, y un grupo de vacas disponibles para la venta. Cada
vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día.
Debes elegir qué vacas comprar y llevar en su camión, de modo que pueda maximizar la producción de
leche, observando el límite de peso del camión.

1.- Para este propósito tienes que definir las siguientes entradas:

Entrada: Número total de vacas en la zona de Tolosa que están a la venta.

Entrada: Peso total que el camión puede llevar.

Entrada: Lista de pesos de las vacas.

Entrada: Lista de la producción de leche por vaca, en litros por día.

2.- El algoritmo que programes tiene que calcular la siguiente salida:

Salida: Cantidad máxima de producción de leche se puede obtener

SOLUCION

He utilizado Phyton 3.8 como lenguaje de programación

La solucion más evidente es la de una vez introducidos los datos de entrada seguir los pasos que siguen:

1- Establecer una relación entre el peso y la producción de cada vaca, es decir, que cada peso se corresponda sólo con un peso (según se han ido introduciendo)

2- Calcular todas las posibles combinaciones de las sumas de peso de las vacas.

2- Discriminar las vacas cuya combinación de pesos está por encima del peso del remolque a utilizar 

2- Calcular todas las posibles sumas de las producciones de las vacas que hayan entrado en el remolque

3- Hallar el máximo de todas las posibles sumas de producción de las vacas que entren en el remolque que será la producción máxima


IMPLEMENTACIÓN EN PHYTON


Divido la solución en varias partes:

1- Introducción de los datos de entrada: 
    Mediante la función input introduzco el peso del remolque, el número de vacas y el peso y producción de cada vaca.
    Para introducir el peso y producción de cada vaca utilizo un bucle indeterminado que está acotado por el número de vacas que ya he introducido previamente.
    
2- Relaciono pesos y producción:
    Junto ambas variables en una lista (funicon zip) formada por tuplas de 2 elementos, primer elemento la producción y segundo el peso y los ordeno de mayor a menor producción.
3- De la lista anterior saco 2 listas una de producción y otra de pesos con el orden anterior (bucle determinado "for")

4- combino los pesos, por un lado, y los volumenes, por otro, de todas las formas posibles y sumo las listas que genero lo que me genra sublistas con las posibles combinaciones
dentro de la lista (funciones "combination" (para combinar)de itertools y "map"(aplicar a cada elemnto de la lista)desde el elemnto 0 al nº de vacas)

5- Mediante un bucle "for" sumo los elementos de las sublistas generadas durante la combinación en cada índice y:
    con un condicional "if" sólo me quedo con las que son menores que el peso del remolque haciendo que salte "continue" las que den un resultado más alto
    
6- En el mismo bucle que la anterior instrucción constituyo otra condicional de forma q que para los casos en los que el peso sea menor que el peso del remolque me de el 
resultado de producción máximo
