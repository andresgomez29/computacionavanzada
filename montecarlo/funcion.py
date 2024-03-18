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
    self.Mw=80.4
    self.Mz=90.4

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
    self.val_gamma = 0.00407 +  factor
    return  self.val_gamma

  def funcD(self,s):
    f1 = (s - self.mh**2)**2
    f2 = self.mh**2 * self.gamma(self.Ms)**2
    return 1 / (f1 + f2)

  def sigma_rel(self,s):
    f1 = (2*(self.lash*self.vev)**2) / (s**0.5)
    return f1*self.funcD(s) * self.gamma(self.Ms)
  
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
    
    

  def funcion_int(self,s):
    cond = s - (2*self.Ms)**2
    '''
    if (cond>=0):
      f1 = s * np.sqrt(cond)
    else:
      f1 = 0
    '''
    suma = self.sigma_rel(s)+self.sigma_higgs(s) +self.sigma_Bonson_Z(s) +self.sigma_Boson_W(s) 
    f1 = s * np.sqrt(cond)
    fsup = f1 * kn(1,np.sqrt(s)/self.T) * suma
    finf = 16*self.T*(self.Ms**4)*kn(2,self.Ms/self.T)
    return 1e9*(fsup/finf)



if __name__ == '__main__': 
  from scipy.optimize import minimize_scalar
  import matplotlib as mpl
  mpl.rcParams['xtick.major.size'] = 8
  mpl.rcParams['xtick.minor.size'] = 4
  mpl.rcParams['ytick.major.size'] = 8
  mpl.rcParams['ytick.minor.size'] = 4

  #mpl.rcParams['xtick.labelsize'] = 50
  mpl.rc('text', usetex=True)
  #mpl.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
  plt.rcParams['text.latex.preamble'] = r"\usepackage{bm} \usepackage{amsmath}"

  ms = 75
  lash = 0.1
  val = Function(ms,lash)
  fac = int(1e1)
  xMin = 4*ms**2
  xMax = fac*xMin
  res1 = minimize_scalar(lambda x: -val.funcion_int(x), bounds=(xMin,xMax), method='bounded')
  res2 = minimize_scalar(lambda x: abs(val.funcion_int(x) - 10), bounds=(res1.x,xMax), method='bounded')
  res3 = minimize_scalar(lambda x: abs(val.funcion_int(x)),bounds=(xMin,xMax), method='bounded')
  
  x = np.linspace(xMin,xMax,100000)
  #x = np.arange(xMin,xMax,1)
  y = val.funcion_int(x)

  texto = r'f(' + str(ms) + ','+ str(lash) + ')'
  plt.figure(figsize=(9.0,5.5))
  plt.plot(x,y,'ko',label=texto)
  plt.title(r'Comportamiento de la función de interes $f(m_{S},\lambda_{SH}$)',size=25)
  plt.xscale('log')
  plt.xlabel(r'$\boldsymbol{E_{s}}$',size=30)
  plt.ylabel(r'$\boldsymbol{f(' + str(ms) + ','+ str(lash) + ')}$',size=30)
  plt.xticks(fontsize=20)
  plt.yticks(fontsize=20)
  #plt.xlim(int(1e5),int(1e7)+10)
  plt.legend(fontsize=13)
  plt.axvline(res1.x, color="blue", linewidth=1, linestyle="dashed")
  #plt.axvline(res2.x, color="blue", linewidth=1, linestyle="dashed")
  plt.axvline(res3.x, color="blue", linewidth=1, linestyle="dashed")
  plt.tight_layout()
  plt.savefig("Comportamiento de la funcion.png")
  plt.show()