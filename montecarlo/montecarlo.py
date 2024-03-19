import numpy as np
import matplotlib.pyplot as plt

'''
------------------------------------------------------------------------------------------------------------
Crea una clase llamada integrador, tiene las siguientes caracteristicas:
Parametros: 
  -f_ : Función a integrar. 
  -N_ : Cantidad de puntos para intergrar. 
  -inter : Intervalo a integrar la función f.

Metodos:
  -integral() : Calcula la integral por medio del método de monte carlo. 
  -varianza() : Calcula la varianza del método usado. 
  -__str__()  : Me imprime un mensaje con los calculos de la integral, varianza y sección tranvesarl.
------------------------------------------------------------------------------------------------------------
'''
class Integrador:
  def __init__(self,f_,N_,inter):
    self.f = f_
    self.N = N_
    self.a = inter[0] #Limite inferior del intervalo
    self.b = inter[1] #Limite superior del intervalo
    self.datos = (self.b - self.a) * np.random.random_sample((self.N)) + self.a #Generacion de un arreglo con N numeros aleatorios en el intervalo [a,b]
    self.F = f_(self.datos) #Genera un arreglo con la funcion evaluada en los N numeros aleatorios generados
    self.div = self.b - self.a #Volumen 
    self.E = self.integral() #Almacena el valor de la integral
    self.var = self.varianza() #Almacena el valor de la varianza
      
  def integral(self):
    return self.div*np.sum(self.F) / self.N

  def varianza(self):
    elementos = self.F**2
    return (self.div**2)*((np.sum(elementos)/self.N) - self.E**2)

  def __str__(self):
    factor = 1.13e-17 #Factor para conversión de unidades.
    texto = r"El resultado es " + str(self.integral()) + "\n"
    texto += r"Con error " + str(np.sqrt(abs(self.varianza()))) + "\n"
    texto += r"Cross Section en cm^3/s = " + str(factor*self.E)
    return texto

'''
------------------------------------------------------------------------------------------------------------
Crea una clase llamada IntegradorEstratificado, tiene las siguientes caracteristicas:
Parametros: 
  -f_ : Función a integrar. 
  -N_ : Vector con la cantidad de puntos para intergrar. 
  -inter : Vector con los intervalo a integrar la función f.

Metodos:
  -integral() : Calcula la integral, esta se hace haciendo uso de la clase Integral.  
  -varianza() : Calcula la varianza, por medio de los hecho en la clase Integral.
  -__str__()  : Me imprime un mensaje con los calculos de la integral, varianza y sección tranvesarl.
  -get_integral() : Me permite obtener el valor de la integral. 
  -get_varianza() : Me permite obtener el valor de la varianza. 
------------------------------------------------------------------------------------------------------------
'''
#Define una clase para el metodo de integracion de motecarlo estratificado
class IntegradorEstratificado:
  def __init__(self,f_,N_,I_):
    self.f = f_ #Funcion a integrar
    self.N = N_ #Numero de puntos aleatorios
    self.I = I_ #Intervalos
    self.E = self.integral()
    self.var = self.varianza()
   
  def integral(self):
    suma = [] #Lista donde se almacenan los valores de la integral de cada parametro.
    for i in range(len(self.I)):
      suma.append(Integrador(self.f,self.N[i],inter = self.I[i]).integral()) #Realiza la integral en cada uno de los intervalos
    return np.sum(suma) #Retorna el valor de la integral al sumar cada uno de los valors en cada intervalo

  
  def varianza(self):
    suma = []
    for i in range(len(self.I)):
      suma.append(Integrador(self.f,self.N[i],inter = self.I[i]).varianza()) #Suma de las varianzas individuales en cada intervalo
    return np.sum(suma) 
  
  def get_integral(self):
    return self.E
  
  def get_varianza(self):
    return self.var

  def __str__(self):
    factor = 1.13e-17 #Factor para conversión de unidades.
    texto = r"El resultado es " + str(self.E) + "\n"
    texto += r"Con error " + str(np.sqrt(abs(self.var))) + "\n"
    texto += r"Cross Section en cm^3/s = " + str(factor*self.E)
    return texto