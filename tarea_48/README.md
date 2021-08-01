# Algoritmos de compresión-descompresión

## Enunciado
Ejercicio para esta tarea: De una cadena dada de máximo 30 caracteres debéis construir una función
que comprima la cadena mediante LZ77 y una función que la descomprima. Evidentemente el input y el
output deben coincidir:
1.- Recoger el input de máximo 30 caracteres
2.- Hacer un print que informe sobre el espacio de memoría que ocupa el string introducido.
3.- Comprimir
4.- Hacer un print que informe sobre el espacio de memoría que ocupa el string comprimido.
5.- Descomprimir. El output debe ser igual que el input.
6.- Hacer un print que informe sobre el espacio de memoría que ocupa el string descomprimido. Una vez
descomprimido debería tener el mismo peso que el original.

## Solución
La tarea se ha realizado en phyton 3.7 siguiendo el algoritmo LZ77.

Básicamente, este algoritmo trata de reducir las repeticiones de cadenas de forma que si una cadena se repite  
se codifique de forma que en la salida comprimida esa cadena quede representada por el código. Este algoritmo 
es más efectivo cuantas más repeticiones de cadenas haya. 
Se recorre ordenadamente la cadena que se quiere comprimir desde el primer carácter. La salida comprimida será 
un diccionario donde se representan las cadenas con una codificación
El funcionamiento de algoritmo es el siguiente:

-	El cursor se sitúa en un carácter y se comprueba si en la cadena recorrida hay algún carácter igual. Si no hay un carácter igual se codifica ese carácter. Si hay un carácter igual se corre el cursor un lugar y se vuelve a comprobar si en la cadena recorrida hay una cadena igual (que ahora tendrá 2 caracteres). Si hay una cadena igual se corre el cursor otro carácter y se vuelve a comprobar y así sucesivamente hasta que se llegue a un carácter que haga que las cadenas no coincidan. Cuando ocurre esto se codifica la cadena y se continúa en el siguiente lugar del cursor.

-	Las codificaciones constan de 3 caracteres:

     o	El primer carácter es un número que indica la posición de la cadena repetida respecto a la posición del cursor
  
     o	El segundo carácter es un número que indica el número de caracteres coincidentes entre la cadena que comienza donde se ubica el cursor y la cadena que se ubica en la         cadena recorrida.
  
     o	El tercer carácter es el primer carácter no repetido una vez se comparan las 2 cadenas
  
Por ejemplo, en la cadena: 

abrabra         

la salida será:

(0,0,a),(0,0,b),(0,0,r),(3,4,<eoc>) (<eoc> indica final de frase cuando no hay un carácter)
  
En el programa creado se puede comprobar que para cadenas cortas con pocos o ningún carácter repetido el algoritmo no es eficiente dando cantidades 
de memoria consumidas más grandes en la salda de la compresión que en la cadena original.Además, es importante la estructura de la salida de la 
compresión ya que si la salida es en forma de contenedores (listas, tuplas, diccionarios, etc.) hay que tener en cuenta que  aparte de la memoria 
que ocupa el objeto en sí, es decir, la lista, tupla o diccionario empleado, habría que sumarle la memoria consumida por su contenido. 

El método que se ha utilizado para obtener el tamaño de memoria consumido, tanto por la cadena original como por la salida comprimida, ha sido getsizeof (). Este método 
da valores correctos, pero en el caso de los contenedores (listas, tuplas, diccionarios, etc) el valor obtenido es el de los objetos en sí y sus referencias 
pero no el de su contenido, por lo que al valor obtenido habría que sumarle el del contenido. Si se calcula el tamaño de la salida de este modo, se comprueba 
que, al menos en cadenas de caracteres con un numero pequeño de ellos, el tamaño de memoria utilizado siempre es mayor en el archivo comprimido que en la 
cadena original a comprimir. Este ha sido el motivo por el que se representa la salida comprimida de la cadena como otra cadena. Aún así, teniendo en cuenta 
que para codificar cada parte de cadena repetida o no, se necesitan al menos 3 caracteres (ubicación, longitud cadena, carácter sin repetir) es fácil deducir 
que en cadenas pequeñas la salida que se obtiene comprimida, aún en el caso más favorable, no representará un gran ahorro de memoria.
  
Aparte del programa que está incluido en el archivo “tarea_48.py” se ha creado otro semejante al primero denominado “tarea_48_bis.py” pero procurando que 
fuera más eficiente para cadenas pequeñas (menos de 100 caracteres) formadas sólo por letras. Se consigue una mayor eficiencia que en el programa inicial 
en la compresión ya que se suprime cualquier carácter no necesario como comas, guiones, etc. que en el programa contenido en el archivo “tarea_48.py” sirven 
para delimitar los diferentes componentes de la codificación. En este programa se utilizan las letras como delimitadores de la longitud en caracteres del número 
que agrupa la ubicación y el numero de caracteres de la cadena repetida. Una vez delimitados se obtiene la longitud del número que representa la ubicación teniendo 
en cuenta que este siempre será mayor o igual que el de la longitud de cadena repetida por lo que si la longitud de ambos números es impar, o sea 3 (ya que como 
mucho funciona bien para 100 caracteres) el componente con 2 caracteres será la ubicación y si son 4 caracteres serán 2 caracteres para cada elemento.

