from scipy.optimize import differential_evolution
import numpy as np
import time

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

def de_scan(dim,my_rank,round_to_nearest=None,nombre_ = 'datos'): 

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
	for i in range(4):
		my_rank = i
		nombre = 'datos_DE' + str(my_rank)
		de_scan(4,my_rank,nombre_ = nombre)
	de_time = time.time() - tO 
	de_time = de_time/60
	print("Tiempo de ejecución: ", de_time, " minutos") 
