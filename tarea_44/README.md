# Análisis del rendimiento de las aplicaciones de IA

## Enunciado

Se trata de analizar la eficiencia de los algoritmos medinte la Notación asintótica

## Solución

La notación asintótica se desarrolla para analizar la eficiencia de los algoritmos con independencia del hardware, lenguaje de programación o compilador utilizado para su ejecución.

Si representamos la eficiencia de un algoritmo por medio de una función donde en el eje de accisas se indica el número de datos de entrada y en el de ordenadas el tiempo de ejecución, 
la Notación asintótica sirve para analizar dicha eficiencia en función de las funciones resultantes teniendo en cuenta una serie de criterios:
  
  •	Asumimos que las entradas son muy grandes
  
  •	Nos interesa el “orden de crecimiento”
  
  •	Las constantes y términos de orden inferior no son relevantes, al ser dominados por un término de orden superior
  
Hay diferentes tipos de notación en función del caso qque se utilice de comparación:

- Notación O (Omicrón, cota superior): O(g(n)) = {f (n) : ∃ c > 0 y n0 > 0 / 0 ≤ f (n) ≤ c · g(n), ∀n ≥ n0}, es decir, a partir de n0, c · g(n) siempre supera (o iguala) a f (n)

La jerarquía de complejidad será: O(1) (constante) ⊂ O(log n) (logaritmico) ⊂ O(n) (lineal) ⊂ O(n log n) (Quasilineal): ⊂ O(n²) (cuadrática) ⊂ O(n³) (cúbico) ⊂ O(2ⁿ) (Exponencial)

- Notación Ω (Omega, cota inferior): Ω(g(n)) = {f (n) : ∃ c > 0 y n0 > 0 / 0 ≤ c · g(n) ≤ f (n), ∀n ≥ n0}, es decir, a partir de n0, f (n) siempre supera (o iguala) a c · g(n)

- Notación Θ (Theta, cota ajusta): Θ(g(n)) = {f (n) : ∃ c1 > 0, c2 > 0 y n0 > 0 / 0 ≤ c1g(n) ≤ f (n) ≤ c2g(n), ∀n ≥ n0}, es decir,a partir de n0, f (n) siempre queda en medio de c1g(n)
y c2g(n)

En el programa que acompaña a esta explicación se puede observar claramente la diferencia de rendimiento que hay de resolver la tarea de una forma o de otra.

En el primer caso el algoritmo es de complejidad lineal por lo que el tiempo de ejcución aumenta de forma proporcional al número de datos que se añadan. Sin embargo en el 
segundo caso, el tiempo de ejcución del programa es independiente del número de datos que introduzcamos ya que el tiempo de ejecución es constante y, por tanto, más eficiente que 
el caso de complejidad lineal.

El programa se ha realizado con phyton 3.8. Su ejecución se puede realizar a través de la consola de phyton.


Respecto de 
