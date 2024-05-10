#script

echo "Ejecutando script"

mkdir salida 2>/dev/null

echo "Generando datos"

mpiexec -n 4 python paralell_main.py
echo "Fin de la generación"

echo "Graficando datos"

python graficador1.py
python graficador2.py

echo "Graficado con exito"
echo "Puedes ver las imagenes guardadas como:"
echo "	-salida/grafico1Paralelo.jpg"
echo "	-salida/grafico2Paralelo.jpg"
echo "Finalizando programa"