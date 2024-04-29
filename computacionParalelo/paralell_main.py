from mpi4py import MPI 
#import funcion_l as lik
from scipy.optimize import differential_evolution
import numpy as np
import time

world_comm = MPI.COMM_WORLD
world_size = world_comm.Get_size()
my_rank = world_comm.Get_rank()
'''
def diccionario(x_):
	data = {'MAp':3., 'mphi':1,'Mchi1':0.1,'angle':1e-3,'gX':0.1182,'epsilon':0.1,'ff':0.10}
	data['MAp'] = 10**x_[0] #Logaritmico
	data['mphi'] = 10**x_[1] #Logaritmico
	data['Mchi1'] = 10**x_[2] #Logaritmico
	data['gX'] = 10**x_[3] #Logaritmico
	data['epsilon'] = 10**x_[4] #Logaritmico
	data['ff'] = 10**x_[5] #lineal
	return data

def de_scan(bounds,nombre_ = 'datos.csv'):
	global my_rank

	x = [] 
	def objective(x_):
		ob = lik.Likelihood(diccionario(x_))
		datos = ob.get_datos()
		#print(datos)
		x.append(datos)
		#print(x)
		if (len(x)%100 == 0): 
			print(len(x),end='\r')
		return ob.get_gaussian()
	
	print("Mi rank es:",my_rank)

	if my_rank == 0: 
		estrategia = 'best1bin'
	elif my_rank ==1: 
		estrategia = 'rand1bin'
	elif my_rank==2: 
		estrategia = 'randtobest1bin'
	else: 
		estrategia = 'best2bin'

	
	differential_evolution(objective, bounds,
	                           strategy=estrategia, maxiter=None,
	                           popsize=50, tol=0.01, mutation=(0.7, 1.99999), recombination=0.15,
	                           polish=False, seed=seed)


	np.save(nombre_,np.array(x))
	print("El tamaño de los datos es:",len(datos))
	print("Datos almacenados con exito")
	return np.array(x),len(x)


def ejecutable(nombre):
	#Rango espacio de parámetros
	gX_min = 1.12
	gX_max = 1.12
	epsilon_min = -4
	epsilon_max = -4
	Mchi1_min = -3
	Mchi1_max = 1
	MAp_min = -4
	MAp_max = 2
	Mphi_min = -4
	Mphi_max = 2
	ff_min = -2
	ff_max = -2
	bounds = [(MAp_min,MAp_max),(Mphi_min,Mphi_max),(Mchi1_min,Mchi1_max),(gX_min,gX_max),(epsilon_min,epsilon_max),(ff_min,ff_max)]
	np.random.seed(seed)
	print("Running de_scan") 
	tO = time.time()
	x,call = de_scan(bounds,nombre_=nombre)
	de_time = time.time() - tO 
	de_time = de_time/60
	print("Tiempo de ejecución: ", de_time, " minutos")
	print("Cantidad de datos generados: ", call)
	print("Finalizado")

'''


min_ = -5
max_ = 5 
dim = 4
bounds = [(min_,max_)] *(dim)
seed = 127

#print(critical_chi_sq)
min_chi_sq = 0. 

# Color style for output sample points
de_pts = "#91bfdb" # Diver scan
rn_pts = "#fc8d59" # Random scan
gd_pts = "#ffffbf" # Grid scan

def rosenbrock(x,y): 
    a = 1. 
    b = 100.
    return (a-x)**2 + b * (y - x**2)**2
def rosenbrock_general(x): 
    n = len(x) 
    return sum(rosenbrock(x[i],x[i+1]) for i in range(n-1))
def loglike(x): 
    return - rosenbrock_general(x)

def de_scan(dim,round_to_nearest=None,nombre_ = 'datos'): 

    x = [] 
    chi_sq = [] 
    x_chi = [] 
    #dim nos dice de cuantos puntos sumo 
    #Activamos la función de Rosenbrock y 
    #guardamos los datos en x y chi_sq 
    def objective(x_): 
        x_chi_ = [0]*5
        x_chi_[0] = x_[0]
        x_chi_[1] = x_[1]
        x_chi_[2] = x_[2] 
        x_chi_[3] = x_[3]
        chi_sq_ = -2.*loglike(x_) 
        x_chi_[4] = chi_sq_
        chi_sq.append(chi_sq_) #Guarda los datos desde que se ejecuta differential_evolution
        x.append(x_) 
        x_chi.append(x_chi_)
        #print(x_chi_)
        return chi_sq_

    
    if my_rank == 0:
    	#print("Ejecutando 0")
    	estrategia = 'best1bin'
    elif my_rank == 1: 
    	#print("Ejecutando 1")
    	estrategia = 'rand1bin'
    elif my_rank == 2:
    	#print("Ejecutando 2")
    	estrategia = 'randtobest1bin'
    else: 
    	#print("Ejecutando default")
    	estrategia='best2bin'
    print("Mi rank es "+str(my_rank) + ", mi estrategia es "+str(estrategia))
    
    differential_evolution(objective, bounds,
	                           strategy=estrategia, maxiter=None,
	                           popsize=50, tol=0.01, mutation=(0.7, 1.99999), recombination=0.15,
	                           polish=False, seed=seed)

    print(nombre_)
    np.save(nombre_,x)
    print("Almacenado " + str(nombre_))
    return np.array(x),len(x)

if __name__ == '__main__':
	tO = time.time()
	seed = 16
	nombre = 'datos_DE' + str(my_rank)
	#ejecutable(nombre)
	de_scan(4,nombre_ = nombre)
	de_time = time.time() - tO 
	de_time = de_time/60
	print("Tiempo de ejecución: ", de_time, " minutos") 
