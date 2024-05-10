import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

dat1 = np.load('datos_DE0.npy')
dat2 = np.load('datos_DE1.npy')
dat3 = np.load('datos_DE2.npy')
dat4 = np.load('datos_DE3.npy')

names = ['x1','x2','x3','x4','loglikelihood']
df1 = pd.DataFrame(dat1,columns=names)
df2 = pd.DataFrame(dat2,columns=names)
df3 = pd.DataFrame(dat3,columns=names)
df4 = pd.DataFrame(dat4,columns=names)

datos1 = df1[df1['loglikelihood']<5.56]
datos2 = df2[df2['loglikelihood']<5.56]
datos3 = df3[df3['loglikelihood']<5.56]
datos4 = df4[df4['loglikelihood']<5.56]

print("Generando grafico")

fig, ax = plt.subplots(figsize=(14, 10))  

ax.plot(datos1['x1'], datos1['x2'], '.',color='red')
ax.plot(datos2['x1'], datos2['x2'], '.',color='red')
ax.plot(datos3['x1'], datos3['x2'], '.',color='red')
ax.plot(datos4['x1'], datos4['x2'], '.',color='red')
ax.set_title('Espacio de parámetros total',size=25)
ax.set_xlabel('$x_{1}$', size=25)
ax.set_ylabel('$x_{2}$', size=25)
ax.tick_params(axis='x', labelsize=17)
ax.tick_params(axis='y', labelsize=20)
#ax.legend(fontsize=13)
plt.savefig('grafico2Paralelo.jpg')
#plt.show()