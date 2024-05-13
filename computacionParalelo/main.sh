#script

echo "Ejecutando script"

#Crea el directorio salida para almacenar los datos 
#Si este directorio ya existe omite su creación.
mkdir salida 2>/dev/null 

echo "Ejecutando algoritmo en serie"
python3 main.py

echo "Ejecutando algoritmo en paralelo"
#Utiliza mpiexec para correr en paralelo el codigo usado. 
#En este caso estamos usando 4 cores para realizar ejecución en paralelo.
mpiexec -n 4 python3 paralell_main.py

echo "Fin del procesamiento"
echo "Almacenando datos en salida"

echo "Graficando datos"

#Ejecuta dos codigo de python para generar los respectivos gráficos
python3 graficador1.py
python3 graficador2.py

echo "Graficado con exito"
echo "Puedes ver las imagenes guardadas como:"
echo "	-salida/grafico1Paralelo.jpg" #Como se almacena el primer gráfico.
echo "	-salida/grafico2Paralelo.jpg" #Como se almacena el segundo gráfico.
echo "Finalizando programa"