import numpy as np 
import matplotlib.pyplot as plt 
from scipy.special import kn



class Funcion: 
	#---------------------------------------------------------------------------
	# A la clase Funcion se le ingresan dos parámetros. 
	# El primero está relacionado a la masa de la materia oscura. 
	# El segundo está relacionado al valor de la constante de acoplamiento lambda
	#---------------------------------------------------------------------------
	def __init__(self,Ms_,lambd_): 
		self.Ms = Ms_ 
		self.lambd = lambd_
		self.val_gamma = 0 #Almacena el valor de gamma calculado. 
		#Parametros de masa 
		self.mh = 125 #GeV Masa del bosón de Higgs
		self.mz = 91.2 #GeV Masa del bosón Z
		self.mw = 80.4 #GeV Masa del bosón W
		self.vew = 246 #Valor esperado del vacío electroweak
		self.x = 10 #Valor relacionado con la temperatura y la masa de DM
		self.sigma1 = 0 #Sigma de interacción con fermiones.
		self.sigma2 = 0 #Sigma de interacción con el bosón Z. 
		self.sigma3 = 0 #Sigma de interacción con el bosón W.
		self.sigma4 = 0 #Sigma de interacción con el bosón de Higgs.
		self.s = 0 #Definir el valor de s #Sigma del valor total

	#---------------------------------------------------------------------------
	# Una función para calcular el ratio entre la masa y la masa de Higgs
	#---------------------------------------------------------------------------
	def rat(self,m):
		return m/self.mh

	#---------------------------------------------------------------------------
	# Aca se define el gamma para el boson de Higgs
	#---------------------------------------------------------------------------
	def gamma(self): 
		f1 = self.mh**3/(np.pi*self.vew**2) 
		#s1 = #Falta el primer termino de gamma
		s2 = (f1/32)*((1 - self.rat(2*self.mz)**2)**0.5)*(1 - self.rat(2*self.mz)**2 + self.rat(np.sqrt(12)*self.mz)**4)
		s3 = (f1/16)*((1 - self.rat(2*self.mw)**2)**0.5)*(1 - self.rat(2*self.mw)**2 + self.rat(np.sqrt(12)*self.mw)**4)
		s4 = ((self.lambd*self.vew)**2)/(8*np.pi)*((1-self.rat(2*self.Ms))**0.5)/self.mh
		#self.val_gamma =  s1 +s2 + s3 +s4
		self.val_gamma = s2 + s3 + s4 
		return self.val_gamma

	#---------------------------------------------------------------------------
	#En este apartado definimos todos los valores de las sigma
	#---------------------------------------------------------------------------
	def sigmaff(self):
		self.sigma1 = 0 
		return self.sigma1 

	def sigmazz(self):
		self.sigma2 = 0
		return self.sigma2

	def sigmaww(self): 
		self.sigma3 = 0
		return self.sigma3

	def sigmahh(self): 
		self.sigma4 = 0
		return self.sigma4
	#---------------------------------------------------------------------------
	#Aca definimos el sigma total que es la suma de todas las sigma
	#---------------------------------------------------------------------------
	def sigma(self): 
		return self.sigmaff() + self.sigmazz() + self.sigmaww() + self.sigmahh()
	#---------------------------------------------------------------------------
	#Aca se define la función a integrar
	#---------------------------------------------------------------------------
	def funcion(self):
		sigmabarra = 1 
		return sigmabarra*np.sqrt(self.s)*kn(1,(self.x*np.sqrt(self.s))/self.Ms)

	def __str__(self): 
		return "El valor de gamma es: " + str(self.gamma())

if __name__ == '__main__': 
	#print(gamma(100,0.1))
	val = Funcion(100,0.1)
	print(val)