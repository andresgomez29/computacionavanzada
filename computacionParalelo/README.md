# Estudio del espacio de parámetros usando algoritmos genéticos y computación en paralelo. 

Este apartado del proyecto contiene código relacionado al uso de algoritmos genéticos para el estudio del espacio de parámetros, ademas de ello se aplica un apartado de paralelización para verificar si este método de la computación es más eficiente en terminos de tiempo que la programación en forma serializada.

- S. Das and P. Suganthan, Differential evolution: A surveyof the state-of-the-art, IEEE Transactions on Evolutionary Computation , 4 (2011).
- R. Storn and K. Price, Differential evolution—a simple and efficient heuristic for global optimization over continuous spaces, J. Global Optimiz., vol. 11, pp. 341–359 (1997).
- J. Brest, S. Greiner, B. Boskovic, M. Mernik, and V. Zumer, Self-adapting control parameters in differential evolution: A comparative study on numerical benchmark problems, Evolutionary Computation, IEEE Transactions , 646–657 (2006).
- SciPy Contributors, scipy.optimize.differential evolution, https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential\_evolution.html.
- P. Rodriguez Mier, A tutorial on differential evolution with python (2017), consultado en Octubre 31, 2023.
- J. Qiang, A unified differential evolution algorithm for global optimization, (2014).
- S. S. AbdusSalam, F. J. Agocs, B. C. Allanach, P. Athron, C. Bal´azs, E. Bagnaschi, P. Bechtle, O. Buchmueller, A. Beniwal, J. Bhom, et al., Simple and statistically sound recommendations for analysing physical theories, Reports on Progress in Physics 85, 052201 (2022)
 
	
La idea principal es estudiar la función de rosenbrock con 4 parámetros diferentes. Este espacio de parámetros será calculado por un algoritmo conocido como differential_evolution. El codigo aquí presente hace uso de varías estrategias para el estudio más general de la función a interés. 

## Relevancia: 

Este repositorio se plantea con el fin de corroborar que tanto se puede ver modificado el tiempo de calculo de los aloritmos genéticos al considerar o no la paralelización. En base a esto es posible observar en los tiempos de computo resultantes como en realidad la computación en paralelo si afecta el tiempo de calculo, permitiendo generar más puntos en menor cantidad de tiempo.

## Archivos: 
El presente apartado está compuesto de 5 archivos de interés. 

### main.py: 
Este contiene todo el algoritmo principal que se usaria sin necesidad de tener una paralelización. Este por medio de calculos en serie determina todo el espacio de parámetros de forma general. 

### paralell_main.py: 
Este apartado contiene casi exactamente lo mismo que main.py, pero esta diseñado para ser ejecutado en paralelo en función de las indicaciones necesarias para el uso de mpiexec.


### graficador1.py y graficado2.py: 
Estos dos métodos se encargan de usar los datos generados por el algoritmo genético y realizar ciertos gráficos de interés para nuestros resultados.

### main.sh:
Es un ejecutable creado para hacer todo de forma más fluida. El main.sh se encarga de crear la carpeta salida y ejecuta tanto main.py y paralell_main.py para crear los datos y los valores de los tiempos de ejecución. Por último, ejecuta graficador1.py y graficador2.py para generar los respectivos gráficos. Todos estos calculos siempre estarán almacenados en la carpeta salida. 

NOTA: En caso tal de presentar error al ejecutar el main.sh se debe tener presente que este ejecuta python3, asi que será necesario verificar que posees instalado python3. 

## Contribuidores: 

- Gustavo Adolfo Castrillon : gadolfo.castrillon@udea.edu.co

- Andres Gomez: andres.gomez29@udea.edu.co