# Tarea 49: Aprender a pensar como un programador: Introducción a la POO

## Enunciado

1.- Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes
métodos para la clase:

. Un constructor, donde los datos pueden estar vacíos.

. Los setters y getters (métodos set y get) para cada uno de los atributos. Hay que validar las entradas de
datos.

. mostrar(): muestra los datos de la persona.

. esMayorDeEdad(): devuelve un valor lógico indicando si es mayor de edad.

2.- Crea una clase llamada Cuenta que tendrá los siguientes atributos:

. titular (que es una persona)

. cantidad (puede tener decimales).

El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

. Un constructor, donde los datos pueden estar vacíos.

Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo
ingresando o retirando dinero.

. mostrar(): muestra los datos de la cuenta.

. ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se
hará nada.

. retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos

## SOLUCION

Se han realizado 2 programas. El denominado "tarea_49_ejercicio1.py" resuelve el primer ejercicio y el "tarea_49_ejercicio2.py" resuelve el ejercicio 2.
Se ha utilizado phyton 3.8 por lo que para ejecutarlos se puede hacer descargando el archivo y abriendolo con el IDLE de phyton. 

En el ejercicio 1 se ha utilizado como criterios para validar los datos introducidos los sigueintes;
DNI: que tenga 9 elementos de los cuales los 8 primeros serán números y el último letra
Nombre: que sea una cadena de letras
edad: que esté entre 0 y 150 años. En este caso, además, si no se introducen números también obliga a repetir la introduccion de datos
El metodo EsMayorDeEdad () indica True si lo es y False si no lo es

En el ejercicio 2 no se han introducido criterios para validar los datos por lo que si no se introducen correctamente el programa se cae.
Se ha redondeado las cantidades a 3 decimales.
