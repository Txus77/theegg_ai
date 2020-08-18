# TAREA 33: EL JUEGO DE PIKACHU

## ENUNCIADO

Entender y dibujar el diagrama de flujo del programa de picachu tal y como
se explica en el vídeo que adjuntamos y posteriormente codificarlo mediante un lenguaje de
programación, es decir, construir el programa tal cual se indica en el diagrama. 

## SOLUCIÓN

El programa se ha realizado en el lenguaje de programación Phyton 3.8.

El codigo se divide en 3 partes. 

En la primera parte se establece tanto la vida como el ataque de los 2 Pokemon definiendo las variables correspondientes. Además, también se dfine la variable Turno 
y se le da el valor por el que se quiere que comience.

En la segunda parte se establece un ciclo en el que se alterna los ataques de ambos Pokemon. Para ello se establece que comience Pikachu a atacar
indicando que se comience por el Turno 1 y cda vez que ataca uno se cambia el valor de esa variable entre 0 (ataca Jigglypuff) y 1 (ataca Pikachu).
El ciclo es indeterminado en el que se pone como condición que la vida de ninguno de los 2 Pokemon baje llegue a 0 o menos. En el momento en que la vida de cualquiera de 
los 2 Pokemon baja de 0 se sale del ciclo.

En la tercera parte se establece el ganador del combate mediante una condición de forma que el Pokemon cuya vida esté por encima del valor 0 sea declarado vencedor.

En el digrama de flujo que se acompaña viene descrito el razonamiento del programa.
