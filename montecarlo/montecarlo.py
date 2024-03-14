import numpy as np
import matplotlib.pyplot as plt

class Integrador:
  def __init__(self,f_,N_,inter = [0,1]):
    self.f = f_
    self.N = N_
    self.a = inter[0]
    self.b = inter[1]
    self.datos = (self.b - self.a) * np.random.random_sample((self.N)) + self.a
    #print(self.datos)
    self.F = f_(self.datos)
    self.E = 0
    self.var = 0
    self.div = self.b - self.a

  def integral(self):
    self.E = self.div*np.sum(self.F) / self.N
    return self.E

  def varianza(self):
    elementos = self.F**2
    self.var = (self.div**2)*((np.sum(elementos)/self.N) - self.E**2)
    return self.var

  def __str__(self):
    texto = r"El valor de la integral es " + str(self.integral()) + " y su error es: " + str(np.sqrt(abs(self.varianza())))
    return texto


class IntegradorEstratificado:
  def __init__(self,f_,N_,I_):
    self.f = f_
    self.N = N_
    self.I = I_
    self.E = 0
    self.var = 0

  def integral(self):
    sum = []
    for i in range(len(self.I)):
      sum.append(Integrador(self.f,self.N[i],inter = self.I[i]).integral())
    self.E = np.sum(sum)
    return self.E

  def varianza(self):
    sum = []
    for i in range(len(self.I)):
      sum.append(Integrador(self.f,self.N[i],inter = self.I[i]).varianza())
    self.var = np.sum(sum)
    return self.var

  def get_integral(self):
    return self.E
  
  def get_varianza(self):
    return self.var

  def __str__(self):
    texto = r'El valor de la integral es: '+ str(self.integral()) + " y su error  es: " + str(self.varianza())
    #texto = r'El valor de la integral es: '+ str(self.integral())
    return texto


if __name__ == '__main__': 
  f2 = lambda x: np.sin(x) / x
  x2 = np.linspace(0.1,8*np.pi,1000)
  y2 = f2(x2)
  plt.figure(figsize=(7.2,5.5))
  plt.plot(x2,y2,'b')
  plt.title("$f(x) = sin(x)/x$",size=25)
  plt.ylabel("f(x)",size=30)
  plt.xlabel('x',size=30)
  plt.ylim(-0.3, 1)
  LINEA1 = 5
  LINEA2 = 15
  plt.axvline(LINEA1, color="red", linewidth=1, linestyle="dashed",ymin=-0.3,ymax=0.1)
  plt.axvline(LINEA2, color="cyan", linewidth=1, linestyle="dashed",ymin=-0.3,ymax=0.27)
  
  n1 = 1e6
  n2 = 1e4
  n3 = 1e3
  I = [(0,5),(5,15),(15,8*np.pi)]
  N = [int(n1),int(n2),int(n3)]
  s2 = IntegradorEstratificado(f2,N,I)
  print(s2)
  plt.show()