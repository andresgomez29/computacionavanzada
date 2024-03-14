import funcion as f 
import montecarlo as m 
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar



if __name__ == '__main__':
	ms = 200 
	lash = 0.1
	fac = int(1e7)
	xMin = 4*ms**2
	xMax = fac*xMin
	f = f.Function(ms,lash).funcion_int

	res1 = minimize_scalar(lambda x: f(x), bounds=(xMin,xMax), method='bounded')

	I = [xMin,xMax]
	#N = int(1e8)
	N = int(1e6)
	s1 = m.Integrador(f,N,I)
	print("Integral con el método normal")
	print(s1)
	N1 = 1e7
	N2 = 1e7
	I = [(xMin,res1.x),(res1.x,xMax)]
	N = [int(N1),int(N2)]
	s2 = m.IntegradorEstratificado(f,N,I)
	print("Integral con el método estratificado")
	print(s2)
	res_integral = s2.get_integral()
	res_varianza = s2.get_varianza()
	print(res_integral)
	print(res_varianza)
