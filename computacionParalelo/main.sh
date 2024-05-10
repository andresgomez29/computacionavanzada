#script



echo "Ejecutando script"

echo "Generando datos"
mpiexec -n 4 python paralell_main.py
echo "Fin de la generación"

echo "Graficando datos"

python graficador1.py
python graficador2.py

echo "Graficado con exito"
echo "Puedes ver las imagenes guardadas como:"
echo "	-grafico1Paralelo.jpg"
echo "	-grafico2Paralelo.jpg"
echo "Finalizando programa"