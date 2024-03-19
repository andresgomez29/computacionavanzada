import numpy as np 
import matplotlib.pyplot as plt 
from scipy.special import kn

'''
------------------------------------------------------------------------------------------------------------
Crea una clase llamada Function, tiene las siguientes caracteristicas:
Parametros: 
  -Ms_ : Valor de la masa de la materia oscura. 
  -lash_ : Valor de la constante de acoplamiento con el Higgs. 

Metodos:
  -rat(m) : Calcula el ratio de la masa m con respecto a la masa del Higgs. 
  -gamma(m) : Calcula el acho del decaimiento del Higgs dependiendo de la masa de la materia oscura. 
  -funcD(s) : Define el propagador de la interacción que estamos considerando. 
  -sigma_rel(s) : Define la cross section del proceso de aniquilacion.
  -sigma_higgs(s) : Define la cross section del proceso de 4 puntos entre la materia oscrua y el boson de higgs.
  -sigma_Boson_W(s) : Define la contribucion al decaimiento del higgs a los boson W+-.
  -sigma_Bonson_Z(s) : Define la contribucion al decaimiento del higgs a el boson Z.
  -sigma_fermions_quarks(s,m) : Define la contribucion al decaimiento del higgs a los quarks.
  -funcion_int(s) : Define la cross section promediada termicamente, esta es la funcion a integrar.
  
------------------------------------------------------------------------------------------------------------
'''
#Esta clase define la funcion que debemos integrar la cross section promediada termicamente
class Function:
  def __init__(self,Ms_,lash_):
    self.Ms = Ms_ #Masa de la amteria oscura
    self.lash = lash_ #Parametro de acoplamiento entre el Higgs y la materia oscura
    self.mh = 125  #GeV  Masa del bosón de Higgs
    self.vev = 246 #GeV Valor esperado del vacío
    self.val_gamma = 0 
    self.T = 25.9 * self.Ms #Colocamos un valor de x = 20
    self.Mw=80.4 #Masa del boson W
    self.Mz=90.4 #Masa del boson Z
    self.Mt=173.34 #Masa del quark top
    self.Mb=4.19 #Masa del quark Bottom
    self.Mst=140e-3 #Masa Quark Strange
    self.Mch=1350e-3 #Masa del Quark charm

  def rat(self,m):
    return m/self.mh

  def gamma(self,m):
    factor = 0
    if(2*m <= self.mh): #Condicion para considerar el proceso del decaimiento del higgs a materia oscura
      f1 = (self.lash*self.vev) / (32*np.pi*self.mh)
      f2 = np.sqrt(1 - self.rat(2*m)**2)
      factor = f1 * f2
    else:
      factor = 0
    self.val_gamma = 0.00407 +  factor
    return  self.val_gamma

  def funcD(self,s):
    f1 = (s - self.mh**2)**2
    f2 = self.mh**2 * self.gamma(self.Ms)**2
    return 1 / (f1 + f2)
  
  def sigma_rel(self,s):
    f1 = (2*(self.lash*self.vev)**2) / (s**0.5)
    f2 = self.funcD(s) * self.gamma(self.Ms)
    return f1*f2

  def sigma_higgs(self,s):
    
    vs=(1- (4*(self.Ms)**2)/s)**0.5
    vh=(1- (4*(self.mh)**2)/s)**0.5
    
    t_plus=self.Ms**2 +self.mh**2 -0.5*s*(1-vs*vh)
    t_minus=self.Ms**2 +self.mh**2 -0.5*s*(1+vs*vh)
    
    aR=1+ 3*(self.mh**2) * (s-self.mh**2)*self.funcD(s)
    aI=3*(self.mh**2)*((s)**0.5) *self.gamma(self.Ms)*self.funcD(s)
    
    f=self.lash**2 /(16*np.pi*s**2 *vs)
    
    f1=(aR**2 +aI**2)*s*vs*vh
    f2=4*self.lash*self.vev**2 *(aR-(self.lash* self.vev**2)/(s-2*self.mh**2))*np.log(abs((self.Ms**2-t_plus)/(self.Ms**2-t_minus)))
    f3=(2*self.lash**2*self.vev**4 *s*vs*vh)/((self.Ms**2-t_minus)*(self.Ms**2-t_plus))
    
    return f*(f1+f2+f3)
  
  
  def sigma_Boson_W(self,s):
    x=self.Mw**2 /s
    vW=(1-4*x)**0.5
    
    f=vW*self.lash**2 *s/(8*np.pi)
    f1=self.funcD(s)*(1-4*x+12*x**2)
    
    return f*f1
  
  
  def sigma_Bonson_Z(self,s):
      x=self.Mz**2 /s
      vW=(1-4*x)**0.5 
    
      f=0.5*vW*self.lash**2 *s/(8*np.pi)
      f1=self.funcD(s)*(1-4*x+12*x**2)
    
      return f*f1
    
  def sigma_fermions_quarks(self,s,m):
    Xq=3*(1 + (4*0.12)/(3*np.pi) *((3/2)*np.log(m**2/s) +9/4)) #Enhancment de los quarks
    vf=(1-4*m**2 /s)**0.5
    f=(self.lash**2 *m**2) /(4*np.pi)
    f1=Xq*vf**3 *self.funcD(s)
    
    return f*f1
  
  def funcion_int(self,s):
    cond = s - (2*self.Ms)**2
    #Suma de los terminos que contribuyen a la seccion termica promediada termicamente
    suma = (self.sigma_rel(s)+self.sigma_higgs(s) +self.sigma_Bonson_Z(s) +self.sigma_Boson_W(s) + self.sigma_fermions_quarks(s,self.Mt)+  self.sigma_fermions_quarks(s,self.Mb) +self.sigma_fermions_quarks(s,self.Mch)+ self.sigma_fermions_quarks(s,self.Mst))
    #Terminos individuales que componen la funcion
    f1 = s * np.sqrt(cond)
    fsup = f1 * kn(1,np.sqrt(s)/self.T) * suma
    finf = 16*self.T*(self.Ms**4)*kn(2,self.Ms/self.T)
    return (fsup/finf)