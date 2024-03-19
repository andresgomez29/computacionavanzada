import funcion as func  #Para importar la función de interes 
import montecarlo as m  #Contiene los métodos de integración de Monte Carlo. 
import matplotlib as mpl #Para los graficos
import matplotlib.pyplot as plt
import numpy as np #Para crear el linspace
from scipy.optimize import minimize_scalar #Permite hallar los maximos

#-----------------------------------------------------------------------------------------------------------
#Para generar el gráfico 
mpl.rcParams['xtick.major.size'] = 8
mpl.rcParams['xtick.minor.size'] = 4
mpl.rcParams['ytick.major.size'] = 8
mpl.rcParams['ytick.minor.size'] = 4
mpl.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = r"\usepackage{bm} \usepackage{amsmath}"
#-----------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
	ms = 200 #Valor de la masa 
	lash = 0.1 #Valor de la constante de acoplamiento con el Higgs
	fac = int(3e4) #Factor para hallar el valor del infinito
	xMin = 4*ms**2
	xMax = fac*xMin

	f = func.Function(ms,lash).funcion_int #Función que deseamos integrar

	'''
	------------------------------------------------------------------------------------------------------------
	generar_punto: 
	Debemos ingresarle dos parámetros:
		- La función a calcular el maximo.
		- El factor que deseamos calcular
	Este método permite generar el punto en el eje x donde queremos calcular la mitad, un cuarto o un factor del
	valos maximo. 
	Por ejemplo, si queremos calcular un cuarto del valor maximo, deberemos ingresar fact = 1/4 y la función.
	------------------------------------------------------------------------------------------------------------
	'''
	def generar_punto(f,fact): 
		from scipy.optimize import minimize_scalar
		res1 = minimize_scalar(lambda x: -f(x), bounds=(xMin,xMax), method='bounded')
		valor = -res1.fun * fact 
		resultado_mitad = minimize_scalar(lambda x: 1e7*abs(f(x) - valor), bounds=(xMin,xMax), method='bounded')
		return resultado_mitad.x

	'''
	------------------------------------------------------------------------------------------------------------
	generar_invervalos: 
	Le pasamos la cantidad de puntos donde calculamos los valores de la anterior función y me permite calcular 
	los rangos para integrar la función. 
	------------------------------------------------------------------------------------------------------------
	'''
	def generar_intervalos(vect):
		arreglo = [] 
		for i in range(len(vect)-1):
			arreglo.append((vect[i],vect[i+1])) 
		return arreglo

	#La siguiente parte de graficar la f(x) para corroborar el comportamiento.
	x = np.linspace(xMin+1,xMax,int(1e6))
	y1 = f(x)

	n = 13  #Cantidad de particiones para los intervalos 
	#Me crea un arreglo con los valores que deseo calcular a partir del valor maximo. 
	elemento1 = [(lambda i=i: 1/2**i)() for i in range(n)] 

	plt.figure(figsize=(9.0,5.5))
	plt.plot(x,y1,'ko',label='Comportamiento de la función')
	plt.title(r'Comportamiento de la función de interes $f(m_{S},\lambda_{SH}$)',size=25)

	elementos = [] 

	for i in elemento1:
		p = generar_punto(f,i)
		elementos.append(p)
		texto = r'Valor ' + str(i)
		plt.axvline(p, color="red", linewidth=1, linestyle="dashed",label=texto)
	plt.axvline(xMin,color="red", linewidth=1, linestyle="dashed",label=texto)
	plt.axvline(xMax,color="red", linewidth=1, linestyle="dashed",label=texto)
	I_estratificado = generar_intervalos(elementos)
	plt.xscale('log')
	plt.xlabel(r'$\boldsymbol{E_{s}}$',size=30)
	plt.ylabel(r'$\boldsymbol{f(' + str(ms) + ','+ str(lash) + ')}$',size=30)
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.tight_layout()
	plt.savefig('muestra.png')
	

	
	#-----------------------------------------------------------------------------------------------------------
	#Este apartado usa Integrador, el cual es un método de Monte Carlo normal para integrar la función f
	I_normal = [xMin,xMax] #Intervalos entre los cuales deseo integrar
	N_normal = int(1e6) #Cantidad de puntos para integrar

	s_normal = m.Integrador(f,N_normal,I_normal)
	print("Integral con el método normal")
	print(s_normal) #Imprime el resultado de la integral junto con su varianza y el valor calculado de la cross section
	#-----------------------------------------------------------------------------------------------------------
	#-----------------------------------------------------------------------------------------------------------
	#Este apartado usa IntegradorEstratificado, el cual es un método de Monte Carlo estratificado para integrar 
	#la función f
	N1 = 10000000 #Cantidad de puntos para integrar en el primer intervalos.
	N2 = 10000 #Cantidad de puntos para integrar en el resto de intervalos.
	
	N_estratificado = [int(N1)]
	#Crea un vector de puntos para integrar. 
	for i in range(len(I_estratificado)-1):
		N_estratificado.append(N2)

	s_estratificado = m.IntegradorEstratificado(f,N_estratificado,I_estratificado)
	print("Integral con el método estratificado")
	print(s_estratificado) #Imprime el resultado de la integral junto con su varianza y el valor calculado de la cross section
	#-----------------------------------------------------------------------------------------------------------
	plt.show()