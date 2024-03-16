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

  def funcion_int(self,s):
    cond = s - (2*self.Ms)**2
    #print(cond)
    '''
    def func(s):
      return s - (2*self.Ms)**2

    if (len(cond)!=0):
      f1 = []
      for i in cond:
        if (i>=0):
          f1.append(s * (func(i)**0.5))
        else:
          f1.append(0) 
        print(f1)
      #if (cond>=0):
        
      #else:
        #f1 = 0
    '''
    f1 = s * (np.sqrt(cond))
    #for i in cond: 
      #print(i)
    #print(cond)
    fsup = f1 * kn(1,np.sqrt(s)/self.T) * self.sigma_rel(s)
    finf = 16*self.T*(self.Ms**4)*kn(2,self.Ms/self.T)
    return 1e17*(fsup/finf)



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