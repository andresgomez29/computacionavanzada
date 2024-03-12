import numpy as np 
import matplotlib.pyplot as plt 
from scipy.special import kn



class Function:
  def __init__(self,Ms_,lash_):
    self.Ms = Ms_
    self.lash = lash_
    self.mh = 125  #GeV  Masa del bosón de Higgs
    self.vev = 246 #GeV Valor esperado del vacío
    self.val_gamma = 0
    self.T = 20 * self.Ms #Colocamos un valor de x = 20

  def rat(self,m):
    return m/self.mh

  def gamma(self,m):
    factor = 0
    if(2*m <= self.mh):
      f1 = (self.lash*self.vev) / (32*np.pi*self.mh)
      f2 = np.sqrt(1 - self.rat(2*m)**2)
      factor = f1 * f2
    else:
      factor = 0
    self.val_gamma = 0.0420 +  factor
    return  self.val_gamma

  def funcD(self,s):
    f1 = (s - self.mh**2)**2
    f2 = self.mh**2 * self.gamma(self.Ms)**2
    return 1 / (f1 + f2)


  def sigma_rel(self,s):
    f1 = (2*(self.lash*self.vev)**2) / (s**0.5)
    f2 = self.funcD(s) * self.gamma(self.Ms)
    return f1*f2

  def funcion_int(self,s):
    cond = s - (2*self.Ms)**2
    '''
    if (cond>=0):
      f1 = s * np.sqrt(cond)
    else:
      f1 = 0
    '''
    f1 = s * np.sqrt(cond)
    fsup = f1 * kn(1,np.sqrt(s)/self.T) * self.sigma_rel(s)
    finf = 16*self.T*(self.Ms**4)*kn(2,self.Ms/self.T)
    return fsup/finf
  
if __name__ == '__main__': 
	ms = 200
	lash = 0.1
	val = Function(ms,lash)
	xMin=4*ms**2
	xMax=xMin*int(1e2)
	
	
	print(xMin,xMax)
	x = np.linspace(xMin,xMax,100000)
	y=val.funcion_int(x)
	plt.figure()
	plt.plot(x,y,'k.')
	plt.xscale('log')
	plt.xlabel('s')
	plt.ylabel('f(s)')
	plt.xlim(int(1e5),int(1e8))
	plt.axvline(int(1e6), color="red", linewidth=1, linestyle="dashed")
	plt.show()