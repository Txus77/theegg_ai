# TAREA 38 RESOLUCIÓN DE MÁS ALGORITMOS

## ENUNCIADO

Resolver los algoritmos siguientes y dibujar diagrama de flujo:

1.- Biologo

Eres un biólogo que examina secuencias de ADN de formas de vida diferentes. Se te darán dos secuencias de ADN, y el objetivo es encontrar el 
conjunto ordenado de bases adyacentes de mayor tamaño que es común en ambos ADNs.
Las secuencias de ADN se darán como conjuntos ordenados de bases de nucleótidos: adenina (abreviado A), citosina (C), guanina (G) y timina (T):

2.- Invertir palabras

Dada una serie de palabras separadas por espacios, escribir la frase formada por las mismas palabras en orden inverso. Cada palabra estará formada exclusivamente por letras, 
y existirá exactamente un espacio entre cada pareja de palabras. La salida debe ser "Case #" seguido del número de caso, de un símbolo de "dos puntos", de un espacio en blanco 
y de la frase invertida.

3.- Palindromo

Un entero se dice que es un palíndromo si es igual al número que se obtiene al invertir el orden de sus cifras. Por ejemplo, 79197 y 324423 son palíndromos. 
En esta tarea se le dará un entero N, 1 <= N <= 1.000.000. Usted debe encontrar el menor entero M tal que M >= N que es primo y M es un palíndromo N.

Por ejemplo, si N es 31, entonces la respuesta es 101.

Formato de entrada:
Un solo entero N, (1 <= N <= 1.000.000), en una sola línea.

Formato de salida:
Su salida debe consistir en un solo número entero, el más pequeño palíndromo primo mayor que o igual a N.

## SOLUCIÓN

Se ha utilizado Phyton 3.8 para la resolución de los difernetes problemas. 

# 1.- Biologo

La solución que se ha adoptado consta de los siguientes pasos:

1.- En el primer paso el objetivo es que las cadenas introducidas sean corrrectas, es decir, que sólo contengan las bases de nucleotidos que se indican. Para ello
se comprueba la cadena introducida descratando las que no se introduzcan de forma correcta obligando al usuario a introducirla de forma correcta

2.- El segundo paso consiste en determinar que cadena es mayor y cual es menor ya que es determinante para que no obtener un error en el paso siguiente

3.- En este paso se comprueba que secuencias de carcateres coinciden entre las 2 cadenas y para ello:

        1.- Se comprueba caracter por caracter si los caracteres de la cadena mayor están en la cadena menor. En caso negativo se añade un espacio a una lista
        vacia creada previamente
        
        2.- En caso de que un caracter de la cadena mayor este en la menor se añade a la lista creada y se comprueba si está el siguiente, en caso afirmativo se añade 
        también a la lista. Se procede de la misma forma hasta  que los caracteres dejan de coincidir o se acaba alguna de las 2 cadenas. Cuando esto ocurre se añade un 
        elemento en blanco a la lista
        
        3.- Tras los pasos anteriores se vuelve a comprobar si el siguiente caracter de la cadena mayor está en la cadena menor y se vuelve a actuar de la misma manera 
        hasta que se acaba de comprobar todos los caracteres de la cadena mayor en la menor
        
        4.- Se transforma los elementos de la lista en secuencias de caracteres de forma que los consecutivos se unen formando las secuencias que se repiten en ambas cadenas
        y los elementos en blanco forman un espacio en blanco. Luego se vuelve a formar una lista donde cada elemento es una de las secuencias obtenidas
        
 4.- Si en el paso anterior no se han obtenido elemento en la lista entonces no hay secuencias repetidas.
 En caso afirmativo se comprueba cual es el elemento con un número mayor de caracteres y se obtienen todos los elementos con ese número de caracteres presentes en la citada
 lista. Se saca de la lista las cadenas resultantes presentandose el resultado en mayúsculas y separadas las secuencias repetidas de mayor número de caracteres por espacios
 en blanco
         
Se aporta un diagrama de flujo para mejor entendimiento del código. 

# 2.- Invertir palabras

La solución que se ha adoptado consta de los siguientes pasos:

1.- Introducir número de casos. Se debe introducir un número entero si no da un error y el programa vuelve a pedir que se introduzca un número.

2.- Introducir tantas variables como números de casos se hayan definido. Cada variable consta de cadenas y espacios. Se comprueba que las variables sólo contengan letras y espacios. Si no da error y hay que volver a introducir el dato. Para la comprobación cada cadena de caracteres se transforma en un elemento de una lista y se comprueba caracter a caracter que no contenga otro tipo de carcater que no sean letras.

3.- Una vez la comprobación anterior se ha realizado, se invierte el orden de los elementos de cada elemento de la lista creada y se imprime de acuerdo a los requerimientos del problema. Para invertir el orden de las secuencias de letras en cada variable lo que se hace es pasar cada secuencia a una lista de forma que cada una sea un elemento. Se invierte el orden de los elementos y se pasa el resultado de la lista a una cadena formada por las secuencias de letras separadas por espacios en orden invertido al que se introdujeron.

Se aporta un diagrama de flujo para mejor entendimiento del código.

# 3.- Palíndromos

La solución que se ha adoptado consta de los siguientes pasos:

1.- Se introduce el número. Se comprueba que cumple con los reuqerimientos del problema y que es un número entero. Si no se introduce correctamente da error y se pide que se vuelva a introducir de forma correcta.

2.- Se van calculando todos los números consecutivamente a partir del introducido y se comprueba que sean primos y palindromos. El primer número que cumple ambas condiciones a la vez es el número buscado.
        1.- para hallar si es primo me he basado en los criterios que se indican aquí:
        https://www.wikiprimes.com/como-saber-si-un-numero-es-primo/#:~:text=Un%20n%C3%BAmero%20es%20primo%20si,divide%2C%20el%20n%C3%BAmero%20ser%C3%A1%20primo.
        la comprobación de si el número es primo se realiza comprobando que cumple con estas 2 condiciones:
                - Que no sea divisible de forma exacta por ningún número entre 2 y la raiz cuadrada del número dado, es decir, que el resto no sea 0.
                - Que no sea 1
        2.- Para comprobar si el número es palíndromo se cambia de tipo de variable de un entero a una cadena y se comprueba si la cadena es igual a su inverso

Se aporta un diagrama de flujo para mejor entendimiento del código.






