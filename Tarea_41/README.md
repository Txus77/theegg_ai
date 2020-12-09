# TAREA 41: EXPRESIONES REGULARES

## Enunciado

Mediante técnicas de Regex se debe calcular el número de caracteres, el número palabras y ranking de palabras por frecuencia de uso
del siguiente texto:

"En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como
referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?
Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas
olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por
hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo,
ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.
Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta
increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando
quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no
porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me
solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso
yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.
El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios
congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando
semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.
Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar
hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que
se encarga de pensar, y hasta cantamos juntos la canción de Annie.
Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de
Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."

Ref: https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/

## Solución

La elaboración del programa se ha realizado en Phyton 3.8.

La solución de este ejercicio la he planteado en varias partes:

En la **primera parte**, ya que se daba la página web de donde se ha cogido el texto he extraido el mismo de la página web meiante scraping.
Para ello he importado la biblioteca requests para realizar una petición a la web  y mediante la biblioteca BeautifulSoup y los diferntes he extraído el texto que me interesaba.
Para ello he tenido que utilizar expresiones regulares que me han permitido localizar el inicio y el final del texto una vez extraída la información de la web. Una vez extraido 
el texto lo he almacenado en una variable (en caso de no querer realizarlo así bastaría con asignar el texto a la variable).

La **segunda parte**, una vez conseguido el texto ha sido definir una serie de funciones con diferentes cometidos:

  -  buscar_num_caracteres (): Cuenta los caracteres. Se ha utilizado de patrón  la expresión regular 'r"\S"' de forma que  coja todos los carcateres que no sean espacio en 
     blanco.
  
  - palabras(): Busca las palabras. En este caso como patron de la expreión regular se ha excogido 'r"[a-zA-ZñÑáÁéÉíÍóÓúÚüÜ]+". Se ha optado por este patron para que sólo tenga 
    en cuenta las letras, las letras con acento, la ñ y las letras con dieresis que son las más comunes en la lengua española. En esta función se pasan todas las palabras a 
    minúsculas para que el programa no considere palabras diferentes a la misma palabra con alguna letra en mayúscula o todas en minúsculas. Esta función retorna una lista con 
    todas las palabras
    
  - ordenar_palabras(): En esta función primero se establece el número de veces que se repite cada palabra en el texto y para ello se coge la lista de palabras que se ha obtenido
    de la anterior función y se pasa a conjunto con el objetivo que queden las palabras sin ninguna repetición. Se pasa este conjunto por un bucle for para que me diga cuntas veces
    aparece cada palabra en la lista obtenida en en la función palabras(). con los resultados se crea un diccionario con las palabras como vlaves y el número de repeticiones 
    como valor.
    
    Finalmente, se ordena el diccionario de mayor a menor por el número de veces que se repite cada palabra. Las palabras que se repiten un mismo número de veces se ordenan alfabéticamente
    de la A a la Z. Para ordenar correctamente se ha tenido de definir otra función denominada normalizar() con el objeto de quitar todos los acentos a las palabras ya que si no las 
    palabras acentuadas o que comiencen por algún caracter no habitual como la ñ se sitúan al final. Para no complicarlo demasiado en la función normalizar se han sustituido los caracteres 
    acentuados y la ñ mediante el método translate despúes de haber creado un tabla de equivalencias de los cracteres que me interesaban con el método maketrans(). La normalización
    de las palabras con estos caracteres se ha realizado después de haber asigando la frecuencia de cada palabra debido a que una palabra con acento y la misma palabra sin acento tienen dos
    significados diferentes y he considerado que, por lo tanto son palabras diferentes. Por otro lado, a pesar de lo anterior he considerado oportuno que en el listado donde se ven
    las palabras oredenadas figure una nota indicando si la palabra tiene alguno de los caracteres referidos.
 
 NOTA: En el programa he indicaod una serie de coentarios para su mejor compresión. Soy consciente que no se cumplen varios de las normas de estilo indicadas en las guías de phyton
 pero están realziados desde un punto de vista didáctico tanto para mí cuando lovea en un futuro como para otra gente que vea el programa.
    
