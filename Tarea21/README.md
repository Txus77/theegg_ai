TAREA 21

Curso inteligencia artificial

ENUNCIADO

Dado un número entre 0.0001 y 0.9999 obtener la fracción equivalente irreducible.
SOLUCIÓN DEL PROBLEMA

Input: número decimal de hasta 4 decimales máximo

Output : Fracción de números enteros irreducible

El primer paso es transformar el número decimal en una fracción de 2 números enteros. En este caso al tener un número decimal que tenga como máximo 4 decimales lo más lógico es multiplicar el número decimal por 10000 y así obtenemos el numerador siendo siempre el denominador 10000. De esta forma tendremos fracciones de 2 números enteros equivalentes a cualquier decimal que se pueda introducir.

El siguiente paso es obtener la fracción irreducible y para ello debemos obtener el máximo común divisor de ambos números y dividir ambos por él. En este caso como el denominador es siempre 10000 y el numerador siempre será menor  que el denominador (ya que el número decimal a introducir siempre es menor que 1)  el máximo común divisor tiene que estar formado por el producto de 1* 2 * 5 elevado cada uno a un exponente que como máximo será 4 y como mínimo 0 ya que 10000=5*5*5*5*2*2*2*2. Entonces divido primero el numerador y al denominador por 2  a la máxima potencia (exponente entre 0 y 4) y si me da un número entero en ambos divido estos a su vez entre 5  a la máxima potencia (exponente entre 0 y 4). El numerador y denominador que obtenga serán los que formes la fracción irreducible

SOLUCIÓN EN LENGUAJE DE PROGRAMACIÓN

El lenguaje de programación que he utilizado es Python ya que parto de cero y parece que es el más sencillo para aprender programación. La versión de Python que he utilizado es la 3.8.

El programa se divide en 3 partes:

En la primera se pide que se introduzca el número decimal en consola y se establece mediante una condicional del tipo "if" que indique que es incorrecto en caso que no se introduzca dentro del rango establecido.

En la segunda parte se establecen las variables numerador y denominador que formarán parte de la fracción inicial equivalente al número introducido, es decir, "numerador= 10000*num" y "denominador=10000". El numerador se redondea con la función round para que no se produzca un error por causa de la coma flotante.

En la tercera parte el programa realiza un ciclo determinado "for" en el que se divide al numerador y denominador entre 2 elevado a i tomando la variable i  valores entre 4 y 0. En el ciclo en el que el numerador y denominador dan como resultado un número entero  ambos cogen ese valor con el cual se pasa al siguiente ciclo. El siguiente ciclo es equivalente al primero pero en vez de dividir entre 2 se divide entre 5 elevado a i tomando la variable i  valores entre 4 y 0. Cuando se obtiene un número entero en ambas divisiones los valores obtenidos para numerador y denominador forman la fracción irreducible.
