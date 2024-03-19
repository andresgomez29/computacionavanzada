import numpy as np
import matplotlib.pyplot as plt


#Define una clase que nos permite integrar mediante el termino de montecarlo "normal", recibe una funcionm el numero de puntos y el intervalo de integracion
class Integrador:
  def __init__(self,f_,N_,inter):
    self.f = f_
    self.N = N_
    self.a = inter[0] #Limite inferior del intervalo
    self.b = inter[1] #Limite superior del intervalo
    self.datos = (self.b - self.a) * np.random.random_sample((self.N)) + self.a #Generacion de un arreglo con N numeros aleatorios en el intervalo [a,b]
    self.F = f_(self.datos) #Genera un arreglo con la funcion evaluada en los N numeros aleatorios generados
    self.div = self.b - self.a #Volumen 
    self.E = self.integral() 
    self.var = self.varianza()
    
  #Integracion por Montecarlo
  def integral(self):
    return self.div*np.sum(self.F) / self.N

  #Caluclo de Varianza
  def varianza(self):
    elementos = self.F**2
    return (self.div**2)*((np.sum(elementos)/self.N) - self.E**2)

  #Imprime los valores de la integral y la varianza
  def __str__(self):
    factor = 1.13e-17
    texto = r"El resultado es " + str(self.integral()) + "\n"
    texto += r"Con error " + str(np.sqrt(abs(self.varianza()))) + "\n"
    texto += r"Cross Section en cm^3/s = " + str(factor*self.E)
    return texto


#Define una clase para el metodo de integracion de motecarlo estratificado
class IntegradorEstratificado:
  def __init__(self,f_,N_,I_):
    self.f = f_ #Funcion a integrar
    self.N = N_ #Numero de puntos aleatorios
    self.I = I_ #Intervalos
    self.E = self.integral()
    self.var = self.varianza()
   
  #Calcula el valor de la integral
  def integral(self):
    suma = [] #Lista donde se almacenan los valores de la integral de cada parametro.
    for i in range(len(self.I)):
      suma.append(Integrador(self.f,self.N[i],inter = self.I[i]).integral()) #Realiza la integral en cada uno de los intervalos
    return np.sum(suma) #Retorna el valor de la integral al sumar cada uno de los valors en cada intervalo

  #Calucla el valor  de la varianza
  def varianza(self):
    suma = []
    for i in range(len(self.I)):
      suma.append(Integrador(self.f,self.N[i],inter = self.I[i]).varianza()) #Suma de las varianzas individuales en cada intervalo
    return np.sum(suma) 
  
  #Funcion que reforma el valor de la integral
  def get_integral(self):
    return self.E
  
  #Funcion que retorna el valor de la varianza
  def get_varianza(self):
    return self.var

  #Funcion que retorna los valores de la integral y la varianza
  def __str__(self):
    factor = 1.17e-17
    texto = r"El resultado es " + str(self.E) + "\n"
    texto += r"Con error " + str(np.sqrt(abs(self.var))) + "\n"
    texto += r"Cross Section en cm^3/s = " + str(factor*self.E)
    return texto
  
