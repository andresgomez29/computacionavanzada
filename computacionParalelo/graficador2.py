import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Lectura de los archivos generados en paralelo
dat1 = np.load('salida/datos_DE0.npy')
dat2 = np.load('salida/datos_DE1.npy')
dat3 = np.load('salida/datos_DE2.npy')
dat4 = np.load('salida/datos_DE3.npy')

#DataFrames de los datos en paralelo
names = ['x1','x2','x3','x4','loglikelihood']
df1 = pd.DataFrame(dat1,columns=names)
df2 = pd.DataFrame(dat2,columns=names)
df3 = pd.DataFrame(dat3,columns=names)
df4 = pd.DataFrame(dat4,columns=names)

#Se genera una máscara para filtrar nuestros datos de interés. 
datos1 = df1[df1['loglikelihood']<5.56]
datos2 = df2[df2['loglikelihood']<5.56]
datos3 = df3[df3['loglikelihood']<5.56]
datos4 = df4[df4['loglikelihood']<5.56]

best_index = df1["loglikelihood"].idxmin()  # Obtiene el índice del valor mínimo en la columna "loglikelihood"
best_point = df1.loc[best_index]  # Selecciona la fila correspondiente al índice del valor mínimo

print("Generando grafico")

fig, ax = plt.subplots(figsize=(14, 10))  

ax.plot(datos1['x1'], datos1['x2'], '.',color='red')
ax.plot(datos2['x1'], datos2['x2'], '.',color='red')
ax.plot(datos3['x1'], datos3['x2'], '.',color='red')
ax.plot(datos4['x1'], datos4['x2'], '.',color='red')
ax.plot(best_point["x1"],best_point["x2"],"o",color="white",label="Bestpoint")
ax.legend()
ax.set_title('Espacio de parámetros Total',size=25)
ax.set_xlabel('$x_{1}$', size=25)
ax.set_ylabel('$x_{2}$', size=25)
ax.tick_params(axis='x', labelsize=17)
ax.tick_params(axis='y', labelsize=20)
plt.savefig('salida/grafico2Paralelo.jpg')