import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Lectura de los archivos generados en paralelo
dat1 = np.load('datos_DE0.npy')
dat2 = np.load('datos_DE1.npy')
dat3 = np.load('datos_DE2.npy')
dat4 = np.load('datos_DE3.npy')

#Lectura de los archivos generado en serie
dat1S = np.load('datos_DE0_Serie.npy')
dat2S = np.load('datos_DE1_Serie.npy')
dat3S = np.load('datos_DE2_Serie.npy')
dat4S = np.load('datos_DE3_Serie.npy')


names = ['x1','x2','x3','x4','loglikelihood']

df1 = pd.DataFrame(dat1,columns=names)
df2 = pd.DataFrame(dat2,columns=names)
df3 = pd.DataFrame(dat3,columns=names)
df4 = pd.DataFrame(dat4,columns=names)



datos1 = df1[df1['loglikelihood']<5.56]
datos2 = df2[df2['loglikelihood']<5.56]
datos3 = df3[df3['loglikelihood']<5.56]
datos4 = df4[df4['loglikelihood']<5.56]


df1S = pd.DataFrame(dat1S,columns=names)
df2S = pd.DataFrame(dat2S,columns=names)
df3S = pd.DataFrame(dat3S,columns=names)
df4S = pd.DataFrame(dat4S,columns=names)

datos1S = df1S[df1S['loglikelihood']<5.56]
datos2S = df2S[df2S['loglikelihood']<5.56]
datos3S = df3S[df3S['loglikelihood']<5.56]
datos4S = df4S[df4S['loglikelihood']<5.56]


print("Generando grafico")

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

axs[0, 0].plot(datos1['x1'],datos1['x2'],'k.',label='Cantida de datos: '+str(len(datos1)))
axs[0, 0].set_title('best1bin',size=25)

axs[1, 1].plot(datos2['x1'],datos2['x2'],'c.',label='Cantida de datos: '+str(len(datos2)))
axs[1, 1].set_title('rand1bin',size=25)

axs[1, 0].plot(datos3['x1'],datos3['x2'],'r.',label='Cantida de datos: '+str(len(datos3)))
axs[1, 0].set_title('randtobest1bin',size=25)

axs[0, 1].plot(datos4['x1'],datos4['x2'],'b.',label='Cantida de datos: '+str(len(datos4)))
axs[0, 1].set_title('best2bin',size=25)



for ax in axs.flatten():
    ax.set_xlabel('$x_{1}$',size = 25)
    ax.set_ylabel('$x_{2}$',size = 25)
    ax.tick_params(axis='x', labelsize=17)
    ax.tick_params(axis='y', labelsize=17)
    ax.legend(fontsize=13)
fig.subplots_adjust(hspace=0.5, wspace=0.3)
plt.savefig('grafico1Paralelo.jpg')
#plt.show()

#Grafico en serie.

figS, axsS = plt.subplots(2, 2, figsize=(14, 10))

axsS[0, 0].plot(datos1S['x1'],datos1S['x2'],'k.',label='Cantida de datos: '+str(len(datos1)))
axsS[0, 0].set_title('best1bin',size=25)

axsS[1, 1].plot(datos2S['x1'],datos2S['x2'],'c.',label='Cantida de datos: '+str(len(datos2)))
axsS[1, 1].set_title('rand1bin',size=25)

axsS[1, 0].plot(datos3S['x1'],datos3S['x2'],'r.',label='Cantida de datos: '+str(len(datos3)))
axsS[1, 0].set_title('randtobest1bin',size=25)

axsS[0, 1].plot(datos4S['x1'],datos4S['x2'],'b.',label='Cantida de datos: '+str(len(datos4)))
axsS[0, 1].set_title('best2bin',size=25)



for ax in axsS.flatten():
    ax.set_xlabel('$x_{1}$',size = 25)
    ax.set_ylabel('$x_{2}$',size = 25)
    ax.tick_params(axis='x', labelsize=17)
    ax.tick_params(axis='y', labelsize=17)
    ax.legend(fontsize=13)
figS.subplots_adjust(hspace=0.5, wspace=0.3)
plt.savefig('grafico1Serie.jpg')
#plt.show()


