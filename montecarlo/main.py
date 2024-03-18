import funcion as func 
import montecarlo as m 
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from scipy.optimize import root_scalar
import numpy as np 
import matplotlib as mpl
import pandas as pd
mpl.rcParams['xtick.major.size'] = 8
mpl.rcParams['xtick.minor.size'] = 4
mpl.rcParams['ytick.major.size'] = 8
mpl.rcParams['ytick.minor.size'] = 4

#mpl.rcParams['xtick.labelsize'] = 50
mpl.rc('text', usetex=True)
#mpl.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
plt.rcParams['text.latex.preamble'] = r"\usepackage{bm} \usepackage{amsmath}"


if __name__ == '__main__':
	ms = 200 
	lash = 0.1
	fac = int(1e4)
	xMin = 4*ms**2
	xMax = fac*xMin
	f = func.Function(ms,lash).funcion_int

	def generar_punto(f,fact): 
		from scipy.optimize import minimize_scalar
		res1 = minimize_scalar(lambda x: -f(x), bounds=(xMin,xMax), method='bounded')
		#val_x = res1.x #Calculo del punto medio
		valor = -res1.fun * fact 
		resultado_mitad = minimize_scalar(lambda x: 1e7*abs(f(x) - valor), bounds=(xMin,xMax), method='bounded')
		return resultado_mitad.x

	def generar_intervalos(vect):
		arreglo = [] 
		for i in range(len(vect)-1):
			arreglo.append((vect[i],vect[i+1])) 
		return arreglo


	#x = np.linspace(xMin+1,xMax,int(1e6))
	#y1 = f(x)

	n = 9  # Número de elementos en la secuencia
	elemento1 = [(lambda i=i: 1/2**i)() for i in range(n)]

	plt.figure(figsize=(9.0,5.5))
	#plt.plot(x,y1,'ko',label='Comportamiento de la función')
	plt.title(r'Comportamiento de la función de interes $f(m_{S},\lambda_{SH}$)',size=25)

	I_estratificado = [] 
	elementos = [] 
	for i in elemento1:
		p = generar_punto(f,i)
		elementos.append(p)
		texto = r'Valor ' + str(i)
		plt.axvline(p, color="red", linewidth=1, linestyle="dashed",label=texto)

	
	I_estratificado = generar_intervalos(elementos)
	plt.xscale('log')
	plt.xlabel(r'$\boldsymbol{E_{s}}$',size=30)
	plt.ylabel(r'$\boldsymbol{f(' + str(ms) + ','+ str(lash) + ')}$',size=30)
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.legend(fontsize=13)
	plt.tight_layout()
	plt.savefig('muestra.png')

	I_t = [xMin,xMax]
	N = int(1e6)
	#s1 = m.Integrador(f,N,I_t)
	print("Integral con el método normal")
	#print(s1)
	N1 = 1000000
	N2 = 10000
	
	N_estratificado = [int(N1)]

	for i in range(len(I_estratificado)-1):
		N_estratificado.append(N2)

	
	#s2 = m.IntegradorEstratificado(f,N_estratificado,I_estratificado)
	print("Integral con el método estratificado")
	#print(s2)
	#plt.show()
	df = pd.read_csv('InteraccionDM-P.csv')
	#print(df)

	df = df[df['Mass DM'] >= 65]
	#print(df)
	datos = [] 
	datos.append(df['Mass DM'])
	datos.append(df['SSHH'])
	datos = np.array(datos).T
	print(datos[0][0])