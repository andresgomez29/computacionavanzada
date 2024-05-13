from mpi4py import MPI #Importamos la libreria para ejecutar el codigo en paralelo.
from scipy.optimize import differential_evolution
import numpy as np
import time

world_comm = MPI.COMM_WORLD
world_size = world_comm.Get_size()
my_rank = world_comm.Get_rank() #Da un indicador especial para detectar que clase de proceso se esta ejecutando


'''
Para estudiar el espacio de parámetros de cualquier función debemos restringirla, para esto establecemos un intervalo de
estudio, en este caso nuestro intervalo estará entre -5 y 5 para todo el conjunto de parámetros que deseamos calcular.
'''
min_ = -5 
max_ = 5 
dim = 4 #Grados de libertad (cantidad de parámetros libres)
bounds = [(min_,max_)] *(dim) #Creamos un vector donde estamos estableciendo las ligaduras de nuestro problemas
seed = 127 #Establecemos una semilla con el fin de poder replicar los datos.

#Definimos la función de Rosenbrock
def rosenbrock(x,y): 
    a = 1. 
    b = 100.
    return (a-x)**2 + b * (y - x**2)**2

def rosenbrock_general(x): #Construcción de la likelihood
    n = len(x) 
    return sum(rosenbrock(x[i],x[i+1]) for i in range(n-1))

def loglike(x): #Caculo el logaritmo de la likelihood planteada
    return - rosenbrock_general(x)

def de_scan(dim,round_to_nearest=None,nombre_ = 'datos'): 
    x_chi = [] 
    #dim nos dice los grados de libertad de mi modelo.  
    #Activamos la función de Rosenbrock y 
    #guardamos los datos en x y chi_sq 
    def objective(x_): 
        x_chi_ = [0]*4
        x_chi_[0:3] = x_ 
        x_chi_[4] = -2.*loglike(x_) #Calcula el chi cuadrado a partir del teorema de Will's 
        x_chi.append(x_chi_) #Guarda los datos desde que se ejecuta differential_evolution
        return x_chi_[4]

    '''
    En función de una estrategia en especifico es posible calcular de forma más rapida, general o especifica 
    un sector del espacio de parámetros a estudiar. Por ende, para estudiar a más detalle el uso de la computación 
    en paralelo, ejecutamos diferentes estrategias esto en función del rank determinado por MPI. 
    '''
    if my_rank==0:
        estrategia="best1bin"
    elif my_rank==1:
        estrategia="rand1bin"
    elif my_rank==2:
        estrategia='randtobest1bin'
    else:
        estrategia='best2bin'
    	
    print("Mi rank es "+str(my_rank) + ", mi estrategia es "+str(estrategia))
    
    differential_evolution(objective, bounds,
	                           strategy=estrategia, maxiter=None,
	                           popsize=50, tol=0.01, mutation=(0.7, 1.99999), recombination=0.15,
	                           polish=False, seed=seed)

    np.save(nombre_,x_chi)
    print("salida/Almacenado en " + str(nombre_)) #Almacenamos los datos en función de my_rank generado por MPI
    return np.array(x_chi),len(x_chi)

if __name__=="__main__":
     t0=time.time()
     nombre= 'salida/datos_DE' + str(my_rank)
     de_scan(4,my_rank,nombre_=nombre)
     de_time=time.time() -t0
     print("Tiempo de ejecuion en serie: ", de_time, " segundos")
     np.savetxt("salida/TiempoParalelo.txt", [de_time], fmt='%s segundos') #Almacenamos el tiempo transcurrido