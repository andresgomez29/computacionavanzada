# Integración por medio de métodos de monte carlo 

Este apartado del proyecto contiene código relacionado a usar métodos de monte carlo para solucionar problemas en el cálculo de integrales de materia oscura, en este caso estamos considerando un el modelo del singlete escalar, en consideración de los siguientes artículos: 

- https://arxiv.org/pdf/1006.2518.pdf
	
La idea principal es usar métodos de monte carlo para calcular calcular secciones transversales térmicas usando métodos normales de montecarlo y estratificados. 

## Relevancia: 

Este repositorio toma relevancia a la hora del cálculo de las densidades reliquia en materia oscura, este enfoque radica es que existen modelos para los cuales micrOmegas no puede ser usado, por ejemplo modelos de materia oscura tensorial, por lo tanto, se vuelve necesario considerar nuevos métodos o estrategias para integral las secciones transversales y calcular la densidad reliquia de diversos modelos. Por tanto, partimos de un modelo básico o de juguete como lo es el singlete escalar, para corroborar nuestros resultados con el mismo y lograr plantear una nueva alternativa de integración para estos modelos con los métodos de monte carlo. 

## Archivos: 
El presente apartado está compuesto de 3 archivos de interés. 

### Funcion.py: 
Este contiene una clase de python creada a partir de los archivos considerados anteriormente, donde los parámetros de la clase están relacionados a los parámetros libres del modelo, estos son: la masa de la partícula de materia oscura y la constante de acoplamiento con el bosón de Higgs. La clase en términos generales, generará un valor numérico en función de la energía s suministrada a la función. 

### montecarlo.py: 
Este archivo contiene los métodos computacionales usados para integrar, estos son: Integrador e Integrado Estratificado. Estos métodos se encargan de aplicar los métodos de Montecarlo normal y estratificado respectivamente. 
### Main.py: 
Es un método main, usado con el fin de aplicar los métodos de montecarlo y funcion, este únicamente se encarga de ejecutar estos dos métodos debidamente para calcular la integral de interés y realizar los respectivos gráficos. 


## Contribuidores: 

- Gustavo Adolfo Castrillon : gadolfo.castrillon@udea.edu.co

- Andres Gomez: andres.gomez29@udea.edu.co

